
```powershell
PS C:\Users\Administrator> get-localuser

Name           Enabled Description
----           ------- -----------
Administrator  True    Built-in account for administering the computer/domain
DefaultAccount False   A user account managed by the system.
duck           True
duck2          True
Guest          False   Built-in account for guest access to the computer/domain
```

```powershell
PS C:\Users\Administrator> get-localuser | select-Object -Property name, sid

Name           SID
----           ---
Administrator  S-1-5-21-1394777289-3961777894-1791813945-500
DefaultAccount S-1-5-21-1394777289-3961777894-1791813945-503
duck           S-1-5-21-1394777289-3961777894-1791813945-1008
duck2          S-1-5-21-1394777289-3961777894-1791813945-1009
Guest          S-1-5-21-1394777289-3961777894-1791813945-501
```

```powershell
PS C:\Users\Administrator> get-localuser | get-member

   TypeName: Microsoft.PowerShell.Commands.LocalUser

Name                   MemberType Definition
----                   ---------- ----------
Clone                  Method     Microsoft.PowerShell.Commands.LocalUser Clone()
Equals                 Method     bool Equals(System.Object obj)
GetHashCode            Method     int GetHashCode()
GetType                Method     type GetType()
ToString               Method     string ToString()
AccountExpires         Property   System.Nullable[datetime] AccountExpires {get;set;}
Description            Property   string Description {get;set;}
Enabled                Property   bool Enabled {get;set;}
FullName               Property   string FullName {get;set;}
LastLogon              Property   System.Nullable[datetime] LastLogon {get;set;}
Name                   Property   string Name {get;set;}
ObjectClass            Property   string ObjectClass {get;set;}
PasswordChangeableDate Property   System.Nullable[datetime] PasswordChangeableDate {get;set;}
PasswordExpires        Property   System.Nullable[datetime] PasswordExpires {get;set;}
PasswordLastSet        Property   System.Nullable[datetime] PasswordLastSet {get;set;}
PasswordRequired       Property   bool PasswordRequired {get;set;}
PrincipalSource        Property   System.Nullable[Microsoft.PowerShell.Commands.PrincipalSource] PrincipalSource {get;set;}
SID                    Property   System.Security.Principal.SecurityIdentifier SID {get;set;}
UserMayChangePassword  Property   bool UserMayChangePassword {get;set;}
```

