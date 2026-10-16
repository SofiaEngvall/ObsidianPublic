
download and install ollama (tool to run models)
`curl -fsSL https://ollama.com/install.sh | sh`

run a model that matches your hardware (I have 8 GB ram on this old laptop)
`ollama run qwen2.5:1.5b`

let's make a dir for our stuff
`mkdir ollama`
`cd ollama`

make and activate a python environment
`python3 -m venv .`
`source bin/activate`

for rag stuff
`pip install chromadb ollama`

add model to 
`ollama pull nomic-embed-text`


`nano brain.py`

```python
import os
import glob
import chromadb
from chromadb.config import Settings
import ollama

# 1. Define paths and model
NOTES_DIR = os.path.expanduser("~/notes")
DB_DIR = os.path.expanduser("~/ollama/chroma_db")
MODEL_NAME = "qwen2.5:1.5b"

# Initialize local persistent database
chroma_client = chromadb.PersistentClient(path=DB_DIR)

# Helper function to split text into small chunks
def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    words = text.split()
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

def index_notes():
    print(f"[*] Scanning and indexing markdown notes from {NOTES_DIR}...")
    
    # Get or create the vector collection
    try:
        chroma_client.delete_collection(name="cyber_notes")
    except Exception:
        pass
    collection = chroma_client.create_collection(name="cyber_notes")
    
    # Walk through your git repo and find all markdown files
    search_path = os.path.join(NOTES_DIR, "**/*.md")
    md_files = glob.glob(search_path, recursive=True)
    
    if not md_files:
        print(f"[!] Warning: No markdown files found in {NOTES_DIR}")
        return collection

    chunk_id_counter = 0
    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if not content.strip():
                continue
                
            # Break down your notes into digestible pieces
            chunks = split_text(content)
            relative_path = os.path.relpath(file_path, NOTES_DIR)
            
            for chunk in chunks:
                # Generate embedding using your local 1.5b model
                response = ollama.embeddings(model=MODEL_NAME, prompt=chunk)
                embedding = response['embedding']
                
                # Store text, vector, and reference metadata
                collection.add(
                    embeddings=[embedding],
                    documents=[chunk],
                    metadatas=[{"source": relative_path}],
                    ids=[f"id_{chunk_id_counter}"]
                )
                chunk_id_counter += 1
        except Exception as e:
            print(f"[!] Failed to read {file_path}: {e}")
            
    print(f"[+] Successfully indexed {chunk_id_counter} chunks of notes.")
    return collection

def query_brain(query_text, collection):
    # Turn your question into a vector embedding
    response = ollama.embeddings(model=MODEL_NAME, prompt=query_text)
    query_embedding = response['embedding']
    
    # Grab the top 3 closest matching snippets from your notes
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    
    # Combine the source contexts cleanly
    context_list = []
    if results and results['documents'] and results['documents'][0]:
        for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
            context_list.append(f"Source [{meta['source']}]:\n{doc}")
            
    context = "\n---\n".join(context_list)
    
    # Structure the prompt injecting your data
    prompt = f"""You are a security assistant with access to the user's private cyber notes.
Use the following context from their files to accurately answer the question.
If the notes do not contain the answer, rely on your default training data but clearly state that the answer wasn't explicitly found in their notes.

CONTEXT:
{context}

QUESTION: {query_text}
ANSWER:"""
    
    print("\n[Thinking...]")
    
    # Generate response string via stream so you can watch it type in real time
    stream = ollama.generate(model=MODEL_NAME, prompt=prompt, stream=True)
    for chunk in stream:
        print(chunk['response'], end='', flush=True)
    print("\n")

if __name__ == "__main__":
    # Fetch existing collection or build a new one
    try:
        db_collection = chroma_client.get_collection(name="cyber_notes")
        print("[+] Loaded existing notes database.")
    except Exception:
        db_collection = index_notes()
        
    while True:
        try:
            user_query = input("brain-cli >>> ").strip()
            if not user_query:
                continue
            if user_query.lower() in ['exit', 'quit']:
                break
            if user_query.lower() == 'refresh':
                db_collection = index_notes()
                continue
            query_brain(user_query, db_collection)
        except KeyboardInterrupt:
            break
```


find extensions in the data (so we can select which ones to index)

`find ~/notes -type f | grep -E '\.[a-zA-Z0-9]+$' | awk -F. '{print $NF}' | sort -u`

```
┌──(fixit42㉿x1)-[~/ollama]
└─$ find ~/notes -type f | grep -E '\.[a-zA-Z0-9]+$' | awk -F. '{print $NF}' | sort -u
avif
bin
cpp
cs
css
csv
enc
exe
gif
gitignore
go
h
html
idx
inf
ini
ino
java
jpeg
jpg
JPG
js
json
jsp
lnk
log
md
old1
old2
pack
pdf
pdn
php
png
ps1
py
rev
sample
st
svg
txt
url
URL
war
wav
webp
```

middle version output

```sh
┌──(ollama)─(fixit42㉿x1)-[~/ollama]
└─$ python brain.py
[*] Syncing 4 files into the database...
[!] Encoding/Read error in: /home/fixit42/notes/Programming/go/output.txt -> Unequal lengths for fields: ids: 1, metadatas: 2, embeddings: 1, documents: 1 in add.
[!] Encoding/Read error in: /home/fixit42/notes/Programming/go/output3.txt -> Unequal lengths for fields: ids: 1, metadatas: 2, embeddings: 1, documents: 1 in add.
[!] Encoding/Read error in: /home/fixit42/notes/Programming/go/output2.txt -> Unequal lengths for fields: ids: 1, metadatas: 2, embeddings: 1, documents: 1 in add.
[!] Encoding/Read error in: /home/fixit42/notes/Linux/kali/ollama on kali.md -> Unequal lengths for fields: ids: 1, metadatas: 2, embeddings: 1, documents: 1 in add.
    [4/4] Files synced...
[+] Sync complete. Database updated successfully.
brain-cli >>> hello there! can you get me my notes on kali as a daily driver, why I will try it?
```

more of the output but as it's in markdown it is as is:

[Thinking...]
Yes, I can help you with that. Here are the notes on Kali Linux as a daily driver:

### Why?

I'm going to try running Kali as a dual-boot daily driver because:

- Win10 is dying and my computer is too old for Win11 (I could bypass but I don't want Win11!)
- I've run Kali on so many VMs and laptops and I'm very comfy with it. I run Debian for servers.
- I want the Kali tools and a Debian base, so why not try it?

### What do I need?

- Firefox, Thunderbird, LibreOffice, VLC
- OBS (optional, can be installed from source)
- Streamer.bot, Wine
- Speaker.bot, Wine
- SAMMI, Wine
- Iriun, can be installed via flatpak or source

### Tools for streaming

- OBS, can be installed via flatpak or source
- Streamer.bot, Wine
- Speaker.bot, Wine
- SAMMI, Wine
- Iriun, can be installed via source

### Additional tools

- Chrome, can be installed from Google Chrome store
- Balena Etcher, can be used to flash Kali images

### Pre-installed Tools

- Kali tools (preinstalled)
- SQLmap, can be used for SQL injection testing

### Examples

- `sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs`
- `sqlmap -r request.txt --technique=B --level=5 --risk=3 --dbms=mysql --dbs`

### Help

```sh
sqlmap ~/request.txt -h
```

This should help you get started with Kali Linux as your daily driver. If you have any more questions, feel free to ask!

brain-cli >>> now, tell me arguments for and against running kali as my daily driver

[Thinking...]
### Arguments for Running Kali Linux as Your Daily Driver

**Pros:**
1. **Dual-Boot Option:** If you're already using Windows 10, having a dual-boot solution means you don't need to reformat your hard drive, saving you time and money.
2. **Customization and Flexibility:** Kali Linux is a lightweight Linux distribution that is specifically tailored for security and penetration testing. If you're looking for a secure operating environment, Kali fits that perfectly. It's also flexible enough to be used for server environments.
3. **Extremely Secure:** Kali Linux is known for its security features, which is perfect if you're looking for a secure operating environment.
4. **Community Support:** Kali Linux has a large community, which means you have access to forums, tutorials, and bug reports, making it easier to troubleshoot and find solutions to problems.
5. **Ease of Use:** Kali Linux is designed to be easy to use, making it a pleasant choice for everyday use. It has a simple interface and a straightforward installation process.
6. **Debian Base:** Kali Linux is built on top of a Debian base, which means that everything you need for a Debian-based system is already included, reducing the amount of software you have to install and maintain.

### Arguments Against Running Kali Linux as Your Daily Driver

**Cons:**
1. **Performance Issues:** While Kali Linux is designed to be lightweight, it can sometimes perform slower than other Linux distributions, especially if you're running a dual-boot setup with a less powerful CPU.
2. **Resource Intensive:** Kali Linux uses a lot of system resources, including CPU, RAM, and disk space, which could cause issues if you're on a laptop or a system with limited resources.
3. **Security Risks:** If your computer is already compromised, running Kali Linux could potentially help the attacker by giving them more tools and resources to exploit your system.
4. **Security Concerns:** Since Kali Linux is designed for security and penetration testing, it could potentially be used for malicious activities if it's left unmonitored.
5. **Limited Tools:** While Kali Linux is a great choice for security and penetration testing, it doesn't come with all the tools you might need for everyday use, such as word processors or media players.
6. **Customization Challenges:** Customizing Kali Linux to your exact needs can be a bit of a challenge, especially if you're not familiar with Linux or don't have access to a Linux system.

brain-cli >>> exit

end of output

after a lot of back n forth we have a new version that works

```python
import os
import glob
import time
import chromadb
import ollama

# 1. Configuration
NOTES_DIR = os.path.expanduser("~/notes")
DB_DIR = os.path.expanduser("~/ollama/chroma_db")
SYNC_TIME_FILE = os.path.expanduser("~/ollama/last_sync.txt")

TARGET_EXTENSIONS = [
    ".md", ".py", ".c", ".cpp", ".go", ".php", 
    ".js", ".ps1", ".txt", ".json", ".html", ".css", ".java"
]

EMBED_MODEL = "nomic-embed-text"

# --- MODEL SELECTION CONFIGURATION ---
# Simply uncomment the model you want to active test run:
CHAT_MODEL = "qwen2.5:1.5b"  # Fast, lightweight default (Sweet spot for 8GB RAM)
# CHAT_MODEL = "qwen2.5:3b"    # Smarter reasoning, medium execution speed
# CHAT_MODEL = "phi4-mini"     # Best logic/reasoning, pushes 8GB RAM to limit
# -------------------------------------

chroma_client = chromadb.PersistentClient(path=DB_DIR)

def split_text(text, chunk_size=1500, overlap=150):
    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def get_last_sync_time():
    if os.path.exists(SYNC_TIME_FILE):
        try:
            with open(SYNC_TIME_FILE, "r") as f:
                return float(f.read().strip())
        except Exception:
            pass
    return 0.0

def update_sync_time(current_timestamp):
    try:
        with open(SYNC_TIME_FILE, "w") as f:
            f.write(str(current_timestamp))
    except Exception as e:
        print(f"[!] Warning: Failed to save sync timestamp: {e}")

def delete_file_from_db(collection, relative_path):
    try:
        collection.delete(where={"source": relative_path})
    except Exception:
        pass

def process_single_file(file_path, collection, counter_start):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if not content.strip():
            return counter_start

        relative_path = os.path.relpath(file_path, NOTES_DIR)
        
        delete_file_from_db(collection, relative_path)
        
        chunks = split_text(content)
        for i, chunk in enumerate(chunks):
            response = ollama.embeddings(model=EMBED_MODEL, prompt=chunk)
            embedding = response['embedding']
            
            # FIXED STRUCTURAL METADATA LINE
            collection.add(
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{"source": relative_path, "mtime": os.path.getmtime(file_path)}],
                ids=[f"id_{relative_path}_{counter_start + i}"]
            )
        return counter_start + len(chunks)
    except Exception as e:
        print(f"[!] Encoding/Read error in: {file_path} -> {e}")
        return counter_start

def index_notes(force_full=False):
    collection = chroma_client.get_or_create_collection(name="cyber_notes")
    all_files = glob.glob(os.path.join(NOTES_DIR, "**/*"), recursive=True)
    
    valid_files = [
        f for f in all_files 
        if not os.path.isdir(f) and os.path.splitext(f)[1].lower() in TARGET_EXTENSIONS
    ]
    
    last_sync = 0.0 if force_full else get_last_sync_time()
    current_run_time = time.time()
    
    if force_full:
        print("[*] Wiping database for forced full re-index...")
        try:
            chroma_client.delete_collection(name="cyber_notes")
        except Exception:
            pass
        collection = chroma_client.create_collection(name="cyber_notes")
        last_sync = 0.0

    modified_files = []
    for f_path in valid_files:
        try:
            rel_path = os.path.relpath(f_path, NOTES_DIR)
            if os.path.getmtime(f_path) <= last_sync:
                continue
                
            if last_sync == 0.0:
                existing = collection.get(where={"source": rel_path}, limit=1)
                if existing and existing['ids']:
                    continue
                    
            modified_files.append(f_path)
        except Exception:
            pass

    if not modified_files:
        print("[+] No new or updated files found. Database is up to date!")
        update_sync_time(current_run_time)
        return collection

    print(f"[*] Syncing {len(modified_files)} files into the database...")
    
    chunk_id_counter = 0
    for i, file_path in enumerate(modified_files):
        chunk_id_counter = process_single_file(file_path, collection, chunk_id_counter)
        if (i + 1) % 50 == 0 or (i + 1) == len(modified_files):
            print(f"    [{i + 1}/{len(modified_files)}] Files synced...")
            
    update_sync_time(current_run_time)
    print(f"[+] Sync complete. Database updated successfully.")
    return collection

def query_brain(query_text, collection):
    response = ollama.embeddings(model=EMBED_MODEL, prompt=query_text)
    query_embedding = response['embedding']
    
    results = collection.query(query_embeddings=[query_embedding], n_results=4)
    
    context_list = []
    if results and 'documents' in results and results['documents'] and results['documents']:
        inner_docs = results['documents']
        inner_metas = results['metadatas'] if 'metadatas' in results and results['metadatas'] else []
        
        for doc, meta in zip(inner_docs, inner_metas):
            source_file = meta.get('source', 'Unknown Document') if isinstance(meta, dict) else 'Unknown Document'
            context_list.append(f"Source [{source_file}]:\n{doc}")
            
    context = "\n---\n".join(context_list)
    prompt = f"""You are a security assistant with access to the user's private notes.
Use the context to accurately answer the question. If missing, use general context but declare it.

CONTEXT:
{context}

QUESTION: {query_text}
ANSWER:"""
    
    print("\n[Thinking...]")
    stream = ollama.generate(model=CHAT_MODEL, prompt=prompt, stream=True)
    for chunk in stream:
        print(chunk['response'], end='', flush=True)
    print("\n")

if __name__ == "__main__":
    db_collection = index_notes(force_full=False)
        
    while True:
        try:
            user_query = input("brain-cli >>> ").strip()
            if not user_query:
                continue
            if user_query.lower() in ['exit', 'quit']:
                break
            if user_query.lower() == 'refresh':
                db_collection = index_notes(force_full=False)
                continue
            if user_query.lower() == 'force-wipe':
                db_collection = index_notes(force_full=True)
                continue
            query_brain(user_query, db_collection)
        except KeyboardInterrupt:
            break
```

which also means we have added two alternative models as the first one was hallucinating

`pip install prompt_toolkit`




