import requests
import os

# Base URL for the files
base_url = "https://twit.cachefly.net/audio/sn/sn"
file_path = "E:\Security Now" #os.path.dirname(__file__)

# Range of files to download
start = 101
end = 1001

for i in range(start, end + 1):
    file_number = f"{i:04d}"  # Format number as 4 digits (e.g., 0001)
    file_url = f"{base_url}{file_number}/sn{file_number}.mp3"
    file_name = os.path.join(file_path, f"sn{file_number}.mp3")
    
    print(f"Downloading {file_url}...")
    response = requests.get(file_url, stream=True)
    
    if response.status_code == 200:
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        print(f"Saved as {file_name}")
    else:
        print(f"Failed to download {file_url} (Status code: {response.status_code})")
