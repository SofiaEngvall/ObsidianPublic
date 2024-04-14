# Sofia 2023-10-01

import requests
import os
import sys

# url = "http://checkip.amazonaws.com/"
url = "https://www.fixitnow.se/nothing"


def print_file(url):
    response = requests.get(url)
    if response.status_code in range(200, 230):
        print(response.status_code)
        print(response.content)
    else:
        print(f"Error: {response.status_code}", file=sys.stderr)


def download_file(url, localname):
    response = requests.get(url)
    if response.status_code in range(200, 230):
        file = None
        if not os.path.exists(localname):
            try:
                # binary, could add if for text/bin
                file = open(localname, "wb")
                file.write(response.content)
                print(f"File saved: {localname}")
            finally:
                if file != None:
                    file.close
        else:
            print("File exists", file=sys.stderr)
    else:
        print(f"Error: {response.status_code}", file=sys.stderr)


def cookie():
    pass


if __name__ == "__main__":
    print_file(url)
    download_file(url, "C:/Obsidian/InfoSec/Making/testfile.txt")
