
runs in the background - exits with script
```python
import subprocess

subprocess.Popen([OLLAMA_PATH, "serve"])
```

runs in the foreground - need's to be closed
```python
import subprocess

process = subprocess.run([OLLAMA_PATH, "serve"])

...

if ollama_process is not None:
    ollama_process.terminate()
    ollama_process.wait()
```

