
```powershell
[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String((Get-Content -Raw ".\desktop\b64.txt")))
```

```powershell
[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String("dGhpcyBpcyB0aGUgZmxhZyAtIGl="))
```

```powershell
PS C:\Users\Administrator> get-content ./desktop/b64.txt
dGhpcyBpcyB0aGUgZmxhZyAtIGlob3BleW91ZGlkdGhpc29ud2luZG93cwp0aGUgcmVzdCBpcyBnYXJiYWdlCnRoZSByZXN0IGlzIGdhcmJhZ2UKdGhlIHJlc3QgaXMgZ2FyYmFnZQp0aGUgcmVzdCBpcyBnYXJiYWdlCnRoZSB
yZXN0IGlzIGdhcmJhZ2UKdGhlIHJlc3QgaXMgZ2FyYmFnZQp0aGUgcmVzdCBpcyBnYXJiYWdlCnRoZSByZXN0IGlzIGdhcmJhZ2UKdGhlIHJlc3QgaXMgZ2FyYmFnZQp0aGUgcmVzdCBpcyBnYXJiYWdlCnRoZSByZXN0IGlzIG
dhcmJhZ2UKdGhlIHJlc3QgaXMgZ2FyYmFnZQp0aGUgcmVzdCBpcyBnYXJiYWdlCnRoZSByZXN0IGlzIGdhcmJhZ2U=

PS C:\Users\Administrator> [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String((Get-Content -Raw ".\desktop\b64.txt")))
this is the flag - ihopeyoudidthisonwindows
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
the rest is garbage
```

