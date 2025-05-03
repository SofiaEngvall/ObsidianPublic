
### Generate a response

```sh
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt":"Why is the sky blue?"
}'
```

```powershell
Invoke-RestMethod -Uri "http://localhost:11434/api/generate" -Method Post -Body '{"model":"llama3.2","prompt":"Why is the sky blue?"}' -ContentType "application/json"
```

### Chat

```sh
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}'
```

```powershell
Invoke-WebRequest -Uri "http://localhost:11434/api/chat" -Method Post -Body '{"model": "llama3.2", "messages": [{"role": "user", "content": "why is the sky blue?"}]}' -ContentType "application/json"
```

```powershell
$response = Invoke-WebRequest -Uri "http://localhost:11434/api/chat" `
  -Method Post `
  -Body '{"model": "llama3.2", "messages": [{"role": "user", "content": "why is the sky blue?"}]}' `
  -ContentType "application/json"

# Convert RawContent from bytes to string
$text = [System.Text.Encoding]::UTF8.GetString($response.RawContentStream.ToArray())

# Split the NDJSON by newline and parse each JSON object
$text -split "`n" | ForEach-Object { 
    if ($_ -ne "") { $_ | ConvertFrom-Json } 
}
```