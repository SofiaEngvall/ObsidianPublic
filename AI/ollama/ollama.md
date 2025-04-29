
https://github.com/ollama/ollama
https://ollama.com/search - model search


`ollama serve` in one dedicated terminal to start the background service


`ollama list`  lists installed models
`ollama pull <model>` downloads and installs model
`ollama run <model>` (downloads, installs and) runs model

`>>>` the input prompt of ollama - ask questions
`/?` lists commands


##### good and safe models to start with
llama3.2 - Following instructions, Summarization, Prompt rewriting, Tool use - multilingual (8 languages?)
mistral - function calling, 
phi4 - microsoft

##### other llms to test
gemma3:4b (1b, 4b, 12b) - question answering, summarization, and reasoning - 140 languages - runs on resource-limited devices
deepseek-r1:8b (7b, 8b) - ## reasoning model - 

##### embedding model for data
mxbai-embed-large

### Model files

combine with model - instructions of different complexity

`ollama create newname -f -/model-file-name`

temperature 1 is the most creative 0 the least

Example
```sh
FROM deepseek-r1

PARAMETER temperature 0.8

SYSTEM """
you are a cyber security expert, answer in a teaching way, give short answers when possible
"""
```

`ollama create cyber-teacker -f cyber-teacher-modelfile`
