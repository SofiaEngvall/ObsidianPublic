
```sh
┌──(kali㉿proxli)-[/opt]
└─$ sudo git clone https://github.com/rhasspy/piper
Cloning into 'piper'...
remote: Enumerating objects: 2005, done.
remote: Counting objects: 100% (143/143), done.
remote: Compressing objects: 100% (27/27), done.
remote: Total 2005 (delta 123), reused 116 (delta 116), pack-reused 1862 (from 2)
Receiving objects: 100% (2005/2005), 213.32 MiB | 11.82 MiB/s, done.
Resolving deltas: 100% (1114/1114), done.
```


```sh
┌──(kali㉿proxli)-[/opt/piper/src/python_run]
└─$ sudo python3 -m venv .
[sudo] password for kali: 

┌──(kali㉿proxli)-[/opt/piper/src/python_run]
└─$ source bin/activate 
```

```sh
┌──(python_run)─(kali㉿proxli)-[/opt/piper/src/python_run]
└─$ python3 -m pip install -r requirements.txt 
ERROR: Could not find a version that satisfies the requirement piper-phonemize~=1.1.0 (from versions: none)
ERROR: No matching distribution found for piper-phonemize~=1.1.0  
```

```sh
┌──(python_run)─(kali㉿proxli)-[/opt/piper/src/python_run]
└─$ cat requirements.txt 
piper-phonemize~=1.1.0
onnxruntime>=1.11.0,<2
```

```sh
┌──(python_run)─(kali㉿proxli)-[/opt/piper/src/python_run]
└─$ deactivate
```

```sh
┌──(kali㉿proxli)-[/opt/piper/src/python]
└─$ cat requirements.txt
cython>=0.29.0,<1
piper-phonemize~=1.1.0
librosa>=0.9.2,<1
numpy>=1.19.0
onnxruntime>=1.11.0
pytorch-lightning~=1.7.0
torch>=1.11.0,<2
```

```sh
┌──(kali㉿proxli)-[/opt]
└─$ sudo rm -rf piper
[sudo] password for kali: 
```

---

```sh
┌──(kali㉿proxli)-[~/py-piper-test]
└─$ sudo python3 -m venv .

┌──(kali㉿proxli)-[~/py-piper-test]
└─$ source bin/activate   
```

```sh
┌──(py-piper-test)─(kali㉿proxli)-[~/py-piper-test]
└─$ pip3 install piper-tts
Collecting piper-tts
  Downloading piper_tts-1.2.0-py3-none-any.whl.metadata (776 bytes)
INFO: pip is looking at multiple versions of piper-tts to determine which version is compatible with other requirements. This could take a while.
  Downloading piper_tts-1.1.0-py3-none-any.whl.metadata (776 bytes)
ERROR: Cannot install piper-tts==1.1.0 and piper-tts==1.2.0 because these package versions have conflicting dependencies.                                                                       

The conflict is caused by:
    piper-tts 1.2.0 depends on piper-phonemize~=1.1.0
    piper-tts 1.1.0 depends on piper-phonemize~=1.0.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts 
```

`sudo apt install espeak-ng libsndfile1`

---

Testing following a guide: https://www.youtube.com/watch?v=pLR5AsbCMHs

updating pip
```sh
┌──(py-piper-test)─(kali㉿proxli)-[~/py-piper-test]
└─$ pip install pip setuptools wheel -U
Requirement already satisfied: pip in ./lib/python3.13/site-packages (25.1.1)
Collecting setuptools
  Downloading setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Downloading setuptools-80.9.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 5.3 MB/s eta 0:00:00
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: '/home/kali/py-piper-test/lib/python3.13/site-packages/wheel'                                                                              
Check the permissions. 
```

```sh
┌──(py-piper-test)─(kali㉿proxli)-[~/py-piper-test]
└─$ sudo bin/pip install pip setuptools wheel -U
Requirement already satisfied: pip in ./lib/python3.13/site-packages (25.1.1)
Collecting setuptools
  Downloading setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting wheel
  Downloading wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Downloading setuptools-80.9.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 4.6 MB/s eta 0:00:00
Downloading wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools
Successfully installed setuptools-80.9.0 wheel-0.45.1
```

```sh
┌──(py-piper-test)─(kali㉿proxli)-[~/py-piper-test]
└─$ pip list                           
Package    Version
---------- -------
pip        25.1.1
setuptools 80.9.0
wheel      0.45.1
```

```sh
┌──(py-piper-test)─(kali㉿proxli)-[~/py-piper-test]
└─$ git clone https://github.com/rhasspy/piper.git
Cloning into 'piper'...
remote: Enumerating objects: 2005, done.
remote: Counting objects: 100% (143/143), done.
remote: Compressing objects: 100% (27/27), done.
remote: Total 2005 (delta 123), reused 116 (delta 116), pack-reused 1862 (from 2)
Receiving objects: 100% (2005/2005), 213.32 MiB | 11.45 MiB/s, done.
Resolving deltas: 100% (1114/1114), done.
```

it fails here:
```sh
┌──(py-piper-test)─(kali㉿proxli)-[~/py-piper-test/piper/src/python_run]
└─$ pip install -e .  
Obtaining file:///home/kali/py-piper-test/piper/src/python_run
  Preparing metadata (setup.py) ... done
INFO: pip is looking at multiple versions of piper-tts to determine which version is compatible with other requirements. This could take a while.
ERROR: Could not find a version that satisfies the requirement piper-phonemize~=1.1.0 (from piper-tts) (from versions: none)                                                                                                  
ERROR: No matching distribution found for piper-phonemize~=1.1.0 
```

let's run sudo apt update & upgrade so at least that's not the problem
I'll also reboot and try this again

