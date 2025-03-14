#!/usr/bin/env python3
 
import requests

#url = 'https://assets.tryhackme.com/img/THMlogo.png'
url = 'https://download.sysinternals.com/files/PSTools.zip' #psexec

r = requests.get(url, allow_redirects=True)
open('THMlogo.png', 'wb').write(r.content)
