
```powershell
PS C:\Users\Administrator> get-command | Measure-Object
Count    : 7935
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

```powershell
get-command | where-object -Property CommandType -eq Cmdlet | Measure-Object
Count    : 6638
Average  :
Sum      :
Maximum  :
Minimum  :
Property :
```

