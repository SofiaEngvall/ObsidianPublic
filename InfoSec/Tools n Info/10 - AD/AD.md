
## Active Directory Domain Service (AD DS)


#### Security Principals
an object that can act upon resources in the network
##### Users
usually people or services
##### Machines
machines joined to the domain
a machine named `DC01` will have a machine account called `DC01$`
local admin on the computer
##### Security Groups

| **Security Group** | **Description**                                                                                  |
| ------------------ | ------------------------------------------------------------------------------------------------ |
| Domain Admins      | Admin privileges over the entire domain. Control over any computer on the domain, including DCs. |
| Server Operators   | Can administer DCs. Can't change any administrative group memberships.                           |
| Backup Operators   | Allowed to access any file, ignoring their permissions. Used to do backups.                      |
| Account Operators  | Can create or modify other accounts in the domain.                                               |
| Domain Users       | All existing user accounts in the domain.                                                        |
| Domain Computers   | All existing computers in the domain.                                                            |
| Domain Controllers | All existing DCs on the domain.                                                                  |

### Active Directory Users and Computers

##### Organizational Units (OUs)
A Security Principal can only be in one OU
##### Default OUs
- **Builtin:** Contains default groups available to any Windows host.
- **Computers:** Machines are put here by default when joining the domain.
- **Domain Controllers:** DCs in your network.
- **Users:** The default place for users and groups.
- **Managed Service Accounts:** Holds accounts used by services.

To delete protected OUs, activate Advanced options in the View menu. You can then go to the Object tab in the OUs properties and remove the checkmark by Protect object from accidental deletion.

### Delegation

Common use id to grant support the privileges to reset user passwords.

To delegate control, right click the item you want to grant privileges on and follow the Delegate Control guide.

This will not give access to AD U&C but commands can be run from the command line: `Set-ADAccountPassword <username> -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose`

### Command line control

Reset user password:
```powershell
Set-ADAccountPassword <username> -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose
```

Force password reset:
```powershell
Set-ADUser -ChangePasswordAtLogon $true -Identity sophie -Verbose
```


