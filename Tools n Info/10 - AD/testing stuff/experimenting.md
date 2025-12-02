powershell - working example
```powershell
$guid = [Guid]"89e95b76-444d-4c62-991a-0facbeda640c"  # GetChangesInFilteredSet GUID
$root = Get-ADObject "DC=administrator,DC=htb"
(Get-Acl "AD:$($root.DistinguishedName)").Access | Where-Object { $_.ObjectType -eq $guid }
```

```powershell
*Evil-WinRM* PS C:\Users\emily\Documents> $guid = [Guid]"89e95b76-444d-4c62-991a-0facbeda640c"  # GetChangesInFilteredSet GUID 
$root = Get-ADObject "DC=administrator,DC=htb"
(Get-Acl "AD:$($root.DistinguishedName)").Access | Where-Object { $_.ObjectType -eq $guid }


ActiveDirectoryRights : ExtendedRight
InheritanceType       : None
ObjectType            : 89e95b76-444d-4c62-991a-0facbeda640c
InheritedObjectType   : 00000000-0000-0000-0000-000000000000
ObjectFlags           : ObjectAceTypePresent
AccessControlType     : Allow
IdentityReference     : NT AUTHORITY\ENTERPRISE DOMAIN CONTROLLERS
IsInherited           : False
InheritanceFlags      : None
PropagationFlags      : None

ActiveDirectoryRights : ExtendedRight
InheritanceType       : None
ObjectType            : 89e95b76-444d-4c62-991a-0facbeda640c
InheritedObjectType   : 00000000-0000-0000-0000-000000000000
ObjectFlags           : ObjectAceTypePresent
AccessControlType     : Allow
IdentityReference     : BUILTIN\Administrators
IsInherited           : False
InheritanceFlags      : None
PropagationFlags      : None

ActiveDirectoryRights : ExtendedRight
InheritanceType       : None
ObjectType            : 89e95b76-444d-4c62-991a-0facbeda640c
InheritedObjectType   : 00000000-0000-0000-0000-000000000000
ObjectFlags           : ObjectAceTypePresent
AccessControlType     : Allow
IdentityReference     : ADMINISTRATOR\ethan
IsInherited           : False
InheritanceFlags      : None
PropagationFlags      : None

```

GetChanges → 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2
GetChangesAll → 1131f6ad-9c07-11d1-f79f-00c04fc2dcd2
GetChangesInFilteredSet → 89e95b76-444d-4c62-991a-0facbeda640c

`impacket.ldap.ldap` or `impacket.ldap.ldaptypes`

`ldaptypes.SR_SECURITY_DESCRIPTOR` to parse `nTSecurityDescriptor`

```powershell

attributes=['nTSecurityDescriptor']

```


https://github.com/fortra/impacket/blob/9282c9bb120793013cb0493f984c7d96ca74cf85/impacket/ldap/ldapasn1.py#L252


## **Interesting AD Rights & How to Retrieve Them**
chat gpt data - not tested!


| Right Name                               | How to get the data (attribute / GUID / access mask)                                                          | Description                                                                                           |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **GenericAll**                           | **Standard Access Mask:** `ADS_RIGHT_GENERIC_ALL` (`0x10000000`) in `ActiveDirectoryRights`                   | Full control over the object, can modify any setting, reset passwords, change group memberships, etc. |
| **GenericWrite**                         | **Standard Access Mask:** `ADS_RIGHT_GENERIC_WRITE` (`0x40000000`)                                            | Can write all writable properties (not protected ones like owner/DACL).                               |
| **WriteOwner**                           | **Standard Access Mask:** `WRITE_OWNER` (`0x00080000`)                                                        | Can take ownership of the object.                                                                     |
| **WriteDACL**                            | **Standard Access Mask:** `WRITE_DAC` (`0x00040000`)                                                          | Can modify the object’s ACL, granting new rights.                                                     |
| **AllExtendedRights**                    | **Standard Access Mask:** `ADS_RIGHT_DS_CONTROL_ACCESS` (`0x00000100`) with empty `ObjectType` GUID           | Implies all extended rights available on the object.                                                  |
| **Self**                                 | **Standard Access Mask:** `ADS_RIGHT_SELF` (`0x00000008`)                                                     | Self-membership modification or control of attributes with Self permission.                           |
| **ResetPassword / ForceChangePassword**  | **Extended Right GUID:** `00299570-246d-11d0-a768-00aa006e0529`                                               | Reset a user’s password without knowing the old one. Often set on OUs or the domain root.             |
| **ReadLAPSPassword**                     | **Extended Right GUID:** `c7407360-20bf-11d0-a768-00aa006e0529`                                               | Read the `ms-Mcs-AdmPwd` LAPS attribute.                                                              |
| **WriteLAPSPassword**                    | **Extended Right GUID:** `c7407360-20bf-11d0-a768-00aa006e0529` with `ADS_RIGHT_DS_WRITE_PROP` (`0x00000020`) | Modify the LAPS password attribute.                                                                   |
| **GetChanges**                           | **Extended Right GUID:** `1131f6aa-9c07-11d1-f79f-00c04fc2dcd2`                                               | First part of DCSync — replicate directory changes.                                                   |
| **GetChangesAll**                        | **Extended Right GUID:** `1131f6ad-9c07-11d1-f79f-00c04fc2dcd2`                                               | Second part of DCSync — replicate secrets like password hashes.                                       |
| **GetChangesInFilteredSet**              | **Extended Right GUID:** `89e95b76-444d-4c62-991a-0facbeda640c`                                               | Allows replication of confidential attributes.                                                        |
| **AddMember**                            | **Extended Right GUID:** `bf9679c0-0de6-11d0-a285-00aa003049e2`                                               | Add members to a group.                                                                               |
| **RemoveMember**                         | **Extended Right GUID:** `bf9679c0-0de6-11d0-a285-00aa003049e2` with `ADS_RIGHT_DS_WRITE_PROP`                | Remove members from a group.                                                                          |
| **WriteSPN / WriteServicePrincipalName** | **Property Set GUID:** `28630eb0-41d5-11d1-a9c1-0000f80367c1` with `ADS_RIGHT_DS_WRITE_PROP`                  | Modify Service Principal Name attribute — useful for Kerberoasting.                                   |
| **WriteUserAccountControl**              | **Property Set:** attribute `userAccountControl` with `ADS_RIGHT_DS_WRITE_PROP`                               | Change account flags (enable, disable, require smart card, etc.).                                     |
| **WritePrimaryGroupID**                  | **Property Set:** attribute `primaryGroupID` with `ADS_RIGHT_DS_WRITE_PROP`                                   | Change primary group (could give Domain Admin privileges indirectly).                                 |
| **WriteLogonScript**                     | **Property Set:** attribute `scriptPath` with `ADS_RIGHT_DS_WRITE_PROP`                                       | Change logon script executed at logon.                                                                |
| **WriteHomeDirectory**                   | **Property Set:** attribute `homeDirectory` with `ADS_RIGHT_DS_WRITE_PROP`                                    | Change home directory path (potential for UNC path abuse).                                            |

| Right Name                               | How to get the data (attribute / GUID / access mask)                                          | Retrieval Type       | Description                                                                            |
| ---------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------- |
| **GenericAll**                           | **Mask:** `0x10000000` (`ADS_RIGHT_GENERIC_ALL`) in `Ace['Ace']['Mask']['Mask']`              | Standard Access Mask | Full control over the object — can change anything, including DACL, owner, attributes. |
| **GenericWrite**                         | **Mask:** `0x40000000` (`ADS_RIGHT_GENERIC_WRITE`)                                            | Standard Access Mask | Can write all writable attributes (except protected).                                  |
| **WriteOwner**                           | **Mask:** `0x00080000` (`WRITE_OWNER`)                                                        | Standard Access Mask | Can take ownership of the object.                                                      |
| **WriteDACL**                            | **Mask:** `0x00040000` (`WRITE_DAC`)                                                          | Standard Access Mask | Can modify the ACL, grant themselves extra rights.                                     |
| **AllExtendedRights**                    | **Mask:** `0x00000100` (`ADS_RIGHT_DS_CONTROL_ACCESS`) with **empty `ObjectType` GUID**       | Standard Access Mask | Grants all extended rights on the object.                                              |
| **Self**                                 | **Mask:** `0x00000008` (`ADS_RIGHT_SELF`)                                                     | Standard Access Mask | Special “self” permissions, often for modifying own attributes (like phone number).    |
| **ResetPassword / ForceChangePassword**  | **Extended Right GUID:** `00299570-246d-11d0-a768-00aa006e0529` in `Ace['Ace']['ObjectType']` | Extended Right       | Reset a user’s password without knowing the old one.                                   |
| **ReadLAPSPassword**                     | **Extended Right GUID:** `c7407360-20bf-11d0-a768-00aa006e0529`                               | Extended Right       | Read `ms-Mcs-AdmPwd` attribute (LAPS local admin password).                            |
| **WriteLAPSPassword**                    | **GUID:** `c7407360-20bf-11d0-a768-00aa006e0529` with **Mask:** `0x00000020` (`WRITE_PROP`)   | Attribute Right      | Modify the LAPS password attribute.                                                    |
| **GetChanges**                           | **Extended Right GUID:** `1131f6aa-9c07-11d1-f79f-00c04fc2dcd2`                               | Extended Right       | Needed for DCSync.                                                                     |
| **GetChangesAll**                        | **Extended Right GUID:** `1131f6ad-9c07-11d1-f79f-00c04fc2dcd2`                               | Extended Right       | Needed for DCSync (hash replication).                                                  |
| **GetChangesInFilteredSet**              | **Extended Right GUID:** `89e95b76-444d-4c62-991a-0facbeda640c`                               | Extended Right       | Needed for replication of confidential attributes.                                     |
| **AddMember**                            | **Extended Right GUID:** `bf9679c0-0de6-11d0-a285-00aa003049e2`                               | Extended Right       | Add members to a group.                                                                |
| **RemoveMember**                         | Same GUID as AddMember (`bf9679c0-0de6-11d0-a285-00aa003049e2`) + `WRITE_PROP`                | Attribute Right      | Remove members from a group.                                                           |
| **WriteSPN / WriteServicePrincipalName** | **Property GUID:** `28630eb0-41d5-11d1-a9c1-0000f80367c1` + `WRITE_PROP`                      | Attribute Right      | Modify SPN attribute — Kerberoasting vector.                                           |
| **WriteUserAccountControl**              | **Property GUID:** `bf967a68-0de6-11d0-a285-00aa003049e2` + `WRITE_PROP`                      | Attribute Right      | Change account flags (enable, disable, password never expires, etc.).                  |
| **WritePrimaryGroupID**                  | **Property GUID:** `bf967a0c-0de6-11d0-a285-00aa003049e2` + `WRITE_PROP`                      | Attribute Right      | Change primary group (can escalate privileges).                                        |
| **WriteLogonScript**                     | **Property GUID:** `bf9679d0-0de6-11d0-a285-00aa003049e2` + `WRITE_PROP`                      | Attribute Right      | Set logon script (can run attacker code).                                              |
| **WriteHomeDirectory**                   | **Property GUID:** `bf967a03-0de6-11d0-a285-00aa003049e2` + `WRITE_PROP`                      | Attribute Right      | Set home directory path (can be used for UNC path abuse).                              |