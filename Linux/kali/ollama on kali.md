
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

new version

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
CHAT_MODEL = "qwen2.5:1.5b"

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
        
        # Clean old records before saving new/modified ones
        delete_file_from_db(collection, relative_path)
        
        chunks = split_text(content)
        for i, chunk in enumerate(chunks):
            response = ollama.embeddings(model=EMBED_MODEL, prompt=chunk)
            embedding = response['embedding']
            
            collection.add(
                embeddings=[embedding],
                documents=[chunk],
                metadatas=[{"source": relative_path}, {"mtime": os.path.getmtime(file_path)}],
                ids=[f"id_{relative_path}_{counter_start + i}"]
            )
        return counter_start + len(chunks)
    except Exception as e:
        print(f"[!] Encoding/Read error in: {file_path} -> {e}")
        return counter_start

def index_notes(force_full=False):
    collection = chroma_client.get_or_create_collection(name="cyber_notes")
    
    all_files = glob.glob(os.path.join(NOTES_DIR, "**/*"), recursive=True)
    valid_files = [f for f in all_files if not os.path.isdir(f) and os.path.splitext(f).lower() in TARGET_EXTENSIONS]
    
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

    # Filter out files that haven't changed since the last fully successful sync
    modified_files = []
    for f_path in valid_files:
        try:
            rel_path = os.path.relpath(f_path, NOTES_DIR)
            # 1. Quick check: If the file hasn't changed since the last known global sync, skip it entirely
            if os.path.getmtime(f_path) <= last_sync:
                continue
                
            # 2. Crash Protection Check: If the global sync file doesn't exist (like after a crash),
            # check ChromaDB directly to see if this specific file already has indexed records.
            if last_sync == 0.0:
                existing = collection.get(where={"source": rel_path}, limit=1)
                if existing and existing['ids']:
                    continue # Already parsed before the crash! Skip it.
                    
            modified_files.append(f_path)
        except Exception:
            pass

    if not modified_files:
        print("[+] No new or updated files found. Database is up to date!")
        # If we skipped everything because it was already inside the DB after a crash recovery,
        # let's set the global timestamp now to seal it.
        update_sync_time(current_run_time)
        return collection

    print(f"[*] Syncing {len(modified_files)} files into the database...")
    
    chunk_id_counter = 0
    for i, file_path in enumerate(modified_files):
        chunk_id_counter = process_single_file(file_path, collection, chunk_id_counter)
        # Visual progress tracker for large datasets
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
    if results and results['documents'] and results['documents']:
        for doc, meta in zip(results['documents'], results['metadatas']):
            context_list.append(f"Source [{meta['source']}]:\n{doc}")
            
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