
[[permissions ACL DACL]]

`accesschk64.exe -qlc thmservice` using sysinternals tool to get human readable output, needs to be DLed
```sh
thmservice
  DESCRIPTOR FLAGS:
      [SE_DACL_PRESENT]
      [SE_SACL_PRESENT]
      [SE_SELF_RELATIVE]
...
  [4] ACCESS_ALLOWED_ACE_TYPE: BUILTIN\Users
        SERVICE_ALL_ACCESS
```

`sc sdshow thmservice`
```sh
D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BU)
```

To understand the output of sc we can list the "rights":
`sc sdshow scmanager showrights`
```sh
C:\tools\AccessChk>sc sdshow scmanager showrights

D:(A;;CC;;;AU)(A;;CCLCRPRC;;;IU)(A;;CCLCRPRC;;;SU)(A;;CCLCRPWPRC;;;SY)(A;;KA;;;BA)(A;;CC;;;AC)(A;;CC;;;S-1-15-3-1024-528118966-3876874398-709513571-1907873084-3598227634-3698730060-278077788-3990600205)

SDDL right       Right value
----------       -----------
   GA        -   GENERIC_ALL
   KA        -   GENERIC_ALL
   GR        -   GENERIC_READ
   GW        -   GENERIC_WRITE
   GX        -   GENERIC_EXECUTE
   RC        -   READ_CONTROL
   SD        -   DELETE
   WD        -   WRITE_DAC
   WO        -   WRITE_OWNER
   RP        -   SC_MANAGER_QUERY_LOCK_STATUS
   WP        -   SC_MANAGER_MODIFY_BOOT_CONFIG
   CC        -   SC_MANAGER_CONNECT
   DC        -   SC_MANAGER_CREATE_SERVICE
   LC        -   SC_MANAGER_ENUMERATE_SERVICE
   SW        -   SC_MANAGER_LOCK
```

### The SDDL Format

Example:
```
D:(A;;CCLCSWRPWPDTLOCRRC;;;SY)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BA)(A;;CCLCSWLOCRRC;;;IU)(A;;CCLCSWLOCRRC;;;SU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;BU)
```

- **D:** comes from **_discretionary access control list_** (**_DACL_**)
- **S:** comes from **_system access control list_** (**_SACL_**)

https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control-lists

  
The next string represents the assignable permissions on that specific service.  

- **CC** — SERVICE_QUERY_CONFIG (request service settings)
- **LC** — SERVICE_QUERY_STATUS (service status polling)
- **SW** — SERVICE_ENUMERATE_DEPENDENTS
- **LO** — SERVICE_INTERROGATE
- **CR** — SERVICE_USER_DEFINED_CONTROL
- **RC** — READ_CONTROL
- **RP** — SERVICE_START
- **WP** — SERVICE_STOP
- **DT** — SERVICE_PAUSE_CONTINUE

The last two characters represent the objects (user, group or SID) that are granted permissions. Please find below a list of the predefined groups:  

- AU --> Authenticated Users
- AO --> Account operators
- AN --> Anonymous logon
- AU --> Authenticated users
- BA --> Built-in administrators
- BG --> Built-in guests
- BO --> Backup operators
- BU --> Built-in users
- CA --> Certificate server administrators
- CG --> Creator group
- CO --> Creator owner
- DA --> Domain administrators
- DC --> Domain computers
- DD --> Domain controllers
- DG --> Domain guests
- DU --> Domain users
- EA --> Enterprise administrators
- ED --> Enterprise domain controllers
- WD --> Everyone
- PA --> Group Policy administrators
- IU --> Interactively logged-on user
- LA --> Local administrator
- LG --> Local guest
- LS --> Local service account
- SY --> Local system
- NU --> Network logon user
- NO --> Network configuration operators
- NS --> Network service account
- PO --> Printer operators
- PS --> Personal self
- PU --> Power users
- RS --> RAS servers group
- RD --> Terminal server users
- SA --> Schema administrators
- SU --> Service logon user
