
Get info on specific event
````powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} | Format-List
````

List with only time and username
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} | Select-Object @{Name="TimeCreated";Expression={$_.TimeCreated}}, @{Name="UserName";Expression={$_.Properties[5].Value}} | Format-Table -AutoSize
```

alternative
```powershell
Get-WinEvent -MaxEvents 10 -FilterHashTable @{LogName="Security"; ID=4625} | Select-Object TimeCreated, @{name='AccountName'; expression={$_.Properties[5].Value}}
```

