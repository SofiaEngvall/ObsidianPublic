
# Access Tokens

each user has an access token containing security info
executed processes get a copy
contains:
- groups
- priveledges
- SID (sec id)

###### user example
```sh
C:\Users\sofia>whoami /all

USER INFORMATION
----------------

User Name       SID
=============== ============================================
main-i732\sofia S-1-5-21-1191888695-326032422-535987215-1001


GROUP INFORMATION
-----------------

Group Name                                                    Type             SID                                                                                                       Attributes                           
==================================================================================================================================================
Mandatory Label\Medium Mandatory Level                        Label            S-1-16-8192                                                           Everyone                                                      Well-known group S-1-1-0          Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114        Group used for deny only             
MAIN-I732\docker-users                                        Alias            S-1-5-21-1191888695-326032422-535987215-1002                                                                                                                          Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                                        Alias            S-1-5-32-544     Group used for deny only             
BUILTIN\Hyper-V Administrators                                Alias            S-1-5-32-578     Mandatory group, Enabled by default, Enabled group
BUILTIN\Performance Log Users                                 Alias            S-1-5-32-559     Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                                                 Alias            S-1-5-32-545     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE                                      Well-known group S-1-5-4          Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                                                 Well-known group S-1-2-1          Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11         Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization                                Well-known group S-1-5-15         Mandatory group, Enabled by default, Enabled group
	MicrosoftAccount\sofia@babythings.se                          User             S-1-11-96-3623454863-58364-18864-2661722203-1597581903-1553819501-3367357022-47032614-747335975-949769753                                                         Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account                                    Well-known group S-1-5-113        Mandatory group, Enabled by default, Enabled group
LOCAL                                                         Well-known group S-1-2-0          Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Cloud Account Authentication                     Well-known group S-1-5-64-36      Mandatory group, Enabled by default, Enabled group


PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                          State
============================= ==================================== ========
SeLockMemoryPrivilege         Lock pages in memory                 Disabled
SeShutdownPrivilege           Shut down the system                 Disabled
SeChangeNotifyPrivilege       Bypass traverse checking             Enabled
SeUndockPrivilege             Remove computer from docking station Disabled
SeIncreaseWorkingSetPrivilege Increase a process working set       Disabled
```


## Admin tokens

a user thats a local admin gets two access tokens, one used when running stuff as admin

admin example
```sh
C:\WINDOWS\system32>whoami /all

USER INFORMATION
----------------

User Name       SID
=============== ============================================
main-i732\sofia S-1-5-21-1191888695-326032422-535987215-1001


GROUP INFORMATION
-----------------

Group Name                                                    Type             SID                                                                                                       Attributes                           
====================================================================================================================================================
Mandatory Label\High Mandatory Level                          Label            S-1-16-12288     
Everyone                                                      Well-known group S-1-1-0          Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114        Mandatory group, Enabled by default, Enabled group
MAIN-I732\docker-users                                        Alias            S-1-5-21-1191888695-326032422-535987215-1002                                                                                                                          Mandatory group, Enabled by default, Enabled group
BUILTIN\Administrators                                        Alias            S-1-5-32-544     Mandatory group, Enabled by default, Enabled group, Group owner
BUILTIN\Hyper-V Administrators                                Alias            S-1-5-32-578     Mandatory group, Enabled by default, Enabled group
BUILTIN\Performance Log Users                                 Alias            S-1-5-32-559     Mandatory group, Enabled by default, Enabled group
BUILTIN\Users                                                 Alias            S-1-5-32-545     Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\INTERACTIVE                                      Well-known group S-1-5-4          Mandatory group, Enabled by default, Enabled group
CONSOLE LOGON                                                 Well-known group S-1-2-1          Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11         Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\This Organization                                Well-known group S-1-5-15         Mandatory group, Enabled by default, Enabled group
MicrosoftAccount\sofia@babythings.se                          User             S-1-11-96-3623454863-58364-18864-2661722203-1597581903-1553819501-3367357022-47032614-747335975-949769753                                                         Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Local account                                    Well-known group S-1-5-113        Mandatory group, Enabled by default, Enabled group
LOCAL                                                         Well-known group S-1-2-0          Mandatory group, Enabled by default, Enabled group
NT AUTHORITY\Cloud Account Authentication                     Well-known group S-1-5-64-36      Mandatory group, Enabled by default, Enabled group


PRIVILEGES INFORMATION
----------------------

Privilege Name                            Description                                                        State
========================================= ================================================================== ========
SeLockMemoryPrivilege                     Lock pages in memory                                               Disabled
SeIncreaseQuotaPrivilege                  Adjust memory quotas for a process                                 Disabled
SeSecurityPrivilege                       Manage auditing and security log                                   Disabled
SeTakeOwnershipPrivilege                  Take ownership of files or other objects                           Disabled
SeLoadDriverPrivilege                     Load and unload device drivers                                     Disabled
SeSystemProfilePrivilege                  Profile system performance                                         Disabled
SeSystemtimePrivilege                     Change the system time                                             Disabled
SeProfileSingleProcessPrivilege           Profile single process                                             Disabled
SeIncreaseBasePriorityPrivilege           Increase scheduling priority                                       Disabled
SeCreatePagefilePrivilege                 Create a pagefile                                                  Disabled
SeBackupPrivilege                         Back up files and directories                                      Disabled
SeRestorePrivilege                        Restore files and directories                                      Disabled
SeShutdownPrivilege                       Shut down the system                                               Disabled
SeDebugPrivilege                          Debug programs                                                     Disabled
SeSystemEnvironmentPrivilege              Modify firmware environment values                                 Disabled
SeChangeNotifyPrivilege                   Bypass traverse checking                                           Enabled
SeRemoteShutdownPrivilege                 Force shutdown from a remote system                                Disabled
SeUndockPrivilege                         Remove computer from docking station                               Disabled
SeManageVolumePrivilege                   Perform volume maintenance tasks                                   Disabled
SeImpersonatePrivilege                    Impersonate a client after authentication                          Enabled
SeCreateGlobalPrivilege                   Create global objects                                              Enabled
SeIncreaseWorkingSetPrivilege             Increase a process working set                                     Disabled
SeTimeZonePrivilege                       Change the time zone                                               Disabled
SeCreateSymbolicLinkPrivilege             Create symbolic links                                              Disabled
SeDelegateSessionUserImpersonatePrivilege Obtain an impersonation token for another user in the same session Disabled
```


