
in one dedicated terminal, run `ollama serve` to start the service


example first run:
```sh
D:\ollama>ollama serve
Couldn`t find 'C:\Users\sofia\.ollama\id_ed25519'. Generating new private key.
Your new public key is:

ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPjxX4fX+I1sdW65mokoS25tPEfkIPRR3q6KDo6xmYDj

2025/04/25 23:51:31 routes.go:1232: INFO server config env="map[CUDA_VISIBLE_DEVICES: GPU_DEVICE_ORDINAL: HIP_VISIBLE_DEVICES: HSA_OVERRIDE_GFX_VERSION: HTTPS_PROXY: HTTP_PROXY: NO_PROXY: OLLAMA_CONTEXT_LENGTH:2048 OLLAMA_DEBUG:false OLLAMA_FLASH_ATTENTION:false OLLAMA_GPU_OVERHEAD:0 OLLAMA_HOST:http://127.0.0.1:11434 OLLAMA_INTEL_GPU:false OLLAMA_KEEP_ALIVE:5m0s OLLAMA_KV_CACHE_TYPE: OLLAMA_LLM_LIBRARY: OLLAMA_LOAD_TIMEOUT:5m0s OLLAMA_MAX_LOADED_MODELS:0 OLLAMA_MAX_QUEUE:512 OLLAMA_MODELS:C:\\Users\\sofia\\.ollama\\models OLLAMA_MULTIUSER_CACHE:false OLLAMA_NEW_ENGINE:false OLLAMA_NOHISTORY:false OLLAMA_NOPRUNE:false OLLAMA_NUM_PARALLEL:0 OLLAMA_ORIGINS:[http://localhost https://localhost http://localhost:* https://localhost:* http://127.0.0.1 https://127.0.0.1 http://127.0.0.1:* https://127.0.0.1:* http://0.0.0.0 https://0.0.0.0 http://0.0.0.0:* https://0.0.0.0:* app://* file://* tauri://* vscode-webview://* vscode-file://*] OLLAMA_SCHED_SPREAD:false ROCR_VISIBLE_DEVICES:]"
time=2025-04-25T23:51:31.875+02:00 level=INFO source=images.go:458 msg="total blobs: 0"
time=2025-04-25T23:51:31.875+02:00 level=INFO source=images.go:465 msg="total unused blobs removed: 0"
time=2025-04-25T23:51:31.875+02:00 level=INFO source=routes.go:1299 msg="Listening on 127.0.0.1:11434 (version 0.6.6)"
time=2025-04-25T23:51:31.875+02:00 level=INFO source=gpu.go:217 msg="looking for compatible GPUs"
time=2025-04-25T23:51:31.875+02:00 level=INFO source=gpu_windows.go:167 msg=packages count=1
time=2025-04-25T23:51:31.875+02:00 level=INFO source=gpu_windows.go:214 msg="" package=0 cores=4 efficiency=0 threads=8
time=2025-04-25T23:51:32.013+02:00 level=INFO source=types.go:130 msg="inference compute" id=GPU-83ebfc30-941f-123e-120a-cb1f4bed593e library=cuda variant=v12 compute=6.1 driver=12.8 name="NVIDIA GeForce GTX 1080" total="8.0 GiB" available="7.0 GiB"
```