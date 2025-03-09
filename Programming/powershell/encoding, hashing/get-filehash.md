
```powershell
PS C:\Users\Administrator> get-filehash 'C:\Program Files\interesting-file.txt.txt' -Algorithm md5

Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
MD5             49A586A2A9456226F8A1B4CEC6FAB329                                       C:\Program Files\interesting-file.txt.txt
```


Help
```powershell
PS C:\Users\Administrator> get-help Get-FileHash

NAME
    Get-FileHash

SYNOPSIS
    Computes the hash value for a file by using a specified hash algorithm.


SYNTAX
    Get-FileHash [-Algorithm {SHA1 | SHA256 | SHA384 | SHA512 | MACTripleDES | MD5 | RIPEMD160}] -InputStream <Stream> [<CommonParameters>]

    Get-FileHash [-Algorithm {SHA1 | SHA256 | SHA384 | SHA512 | MACTripleDES | MD5 | RIPEMD160}] -LiteralPath <String[]> [<CommonParameters>]

    Get-FileHash [-Path] <String[]> [-Algorithm {SHA1 | SHA256 | SHA384 | SHA512 | MACTripleDES | MD5 | RIPEMD160}] [<CommonParameters>]


DESCRIPTION
    The Get-FileHash cmdlet computes the hash value for a file by using a specified hash algorithm. A hash value is a unique value that corresponds to the content of the
    file. Rather than identifying the contents of a file by its file name, extension, or other designation, a hash assigns a unique value to the contents of a file. File
    names and extensions can be changed without altering the content of the file, and without changing the hash value. Similarly, the file's content can be changed
    without changing the name or extension. However, changing even a single character in the contents of a file changes the hash value of the file.

    The purpose of hash values is to provide a cryptographically-secure way to verify that the contents of a file have not been changed. While some hash algorithms,
    including MD5 and SHA1, are no longer considered secure against attack, the goal of a secure hash algorithm is to render it impossible to change the contents of a
    file-either by accident, or by malicious or unauthorized attempt-and maintain the same hash value. You can also use hash values to determine if two different files
    have exactly the same content. If the hash values of two files are identical, the contents of the files are also identical.

    By default, the Get-FileHash cmdlet uses the SHA256 algorithm, although any hash algorithm that is supported by the target operating system can be used.


RELATED LINKS
    Online Version: http://go.microsoft.com/fwlink/?LinkId=822413
    Format-List

REMARKS
    To see the examples, type: "get-help Get-FileHash -examples".
    For more information, type: "get-help Get-FileHash -detailed".
    For technical information, type: "get-help Get-FileHash -full".
    For online help, type: "get-help Get-FileHash -online"
```

