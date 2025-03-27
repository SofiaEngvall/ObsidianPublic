
10.10.114.253
10.10.175.80

```sh
Some AutoLogon credentials were found
DefaultUserName               :  bill
DefaultPassword               :  PMBAf5KhZAxVhvqb

����������͹ Checking Credential manager
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-manager-windows-vault
    [!] Warning: if password contains non-printable characters, it will be printed as unicode base64 encoded string


Username:              STEELMOUNTAIN\bill
Password:               PMBAf5KhZAxVhvqb
Target:                STEELMOUNTAIN\bill
PersistenceType:       Enterprise
LastWriteTime:         9/27/2019 5:22:42 AM

����������͹ Interesting Services -non Microsoft-
� Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                                                        
    AdvancedSystemCareService9(IObit - Advanced SystemCare Service 9)[C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe] - Auto - Running - No quotes and Space detected                                                                      
    File Permissions: bill [WriteData/CreateFiles]
    Possible DLL Hijacking in binary folder: C:\Program Files (x86)\IObit\Advanced SystemCare (bill [WriteData/CreateFiles])
    Advanced SystemCare Service

```