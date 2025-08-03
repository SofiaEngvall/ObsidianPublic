
Example to add our sid to SeRemoteInteractiveLogonRight

`secedit /export /cfg policy.inf`

`(Get-Content policy.inf).replace("SeRemoteInteractiveLogonRight = *S-1-5-32-544", "SeRemoteInteractiveLogonRight = *S-1-5-32-544,*S-1-5-21-...-500") | Set-Content policy.inf`

`secedit /configure /db secedit.sdb /cfg policy.inf /overwrite`


### MS info

"Configures and analyzes system security by comparing your current security configuration against specified security templates."

| Parameter                                                                                                                              | Description                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [secedit /analyze](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit-analyze)                   | Allows you to analyze current systems settings against baseline settings that are stored in a database. The analysis results are stored in a separate area of the database and can be viewed in the Security Configuration and Analysis snap-in. |
| [secedit /configure](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit-configure)               | Allows you to configure a system with security settings stored in a database.                                                                                                                                                                    |
| [secedit /export](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit-export)                     | Allows you to export security settings stored in a database.                                                                                                                                                                                     |
| [secedit /generaterollback](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit-generaterollback) | Allows you to generate a rollback template with respect to a configuration template.                                                                                                                                                             |
| [secedit /import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit-import)                     | Allows you to import a security template into a database so that the settings specified in the template can be applied to a system or analyzed against a system.                                                                                 |
| [secedit /validate](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit-validate)                 | Allows you to validate the syntax of a security template.                                                                                                                                                                                        |
from: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/secedit

### Help

```sh
*Evil-WinRM* PS V:\> secedit -h

The syntax of this command is:

secedit [/configure | /analyze | /import | /export | /validate | /generaterollback]
```

##### /configure

```sh
*Evil-WinRM* PS V:\> secedit /configure -h

Allows you to configure a system with security settings stored in a database.

The syntax of this command is:

secedit /configure /db filename [/cfg filename] [/overwrite][/areas area1 area2...] [/log filename] [/quiet]

            /db filename - Specifies the database used to perform the security configuration.

            /cfg filename - Specifies a security template to import into the database prior to configuring the computer. Security templates are created using the Security Templates snap-in.

            /overwrite - Specifies that the database should be emptied prior to importing the security template. If this parameter is not specified, the settings in the security template are accumulated into the database.  If this parameter is not specified and there are conflicting settings in the database and the template being imported, the template settings win.

            /areas - Specifies the security areas to be applied to the system. If this parameter is not specified, all security settings defined in the database are applied to the system. To configure multiple areas, separate each area by a space.  The following security areas are supported:

                        SECURITYPOLICY - Includes Account Policies, Audit Policies, Event Log Settings and Security Options.
                        GROUP_MGMT - Includes Restricted Group settings
                        USER_RIGHTS - Includes User Rights Assignment
                        REGKEYS - Includes Registry Permissions
                        FILESTORE - Includes File System permissions
                        SERVICES - Includes System Service settings

            /log filename - Specifies a file in which to log the status of the configuration process.  If not specified, configuration processing information is logged in the scesrv.log file which is located in the %windir%\security\logs directory.

            /quiet - Specifies that the configuration process should take place without prompting the user for any confirmation.

Example:

secedit /configure /db hisecws.sdb /cfg hisecws.inf /overwrite /log hisecws.log

For all filenames, the current directory is used if no path is specified.
```

##### /analyze

```sh
*Evil-WinRM* PS V:\> secedit /analyze -h

Allows you to analyze current systems settings against baseline settings that are stored in a database.  The analysis results are stored in a separate area of the database and can be viewed in the Security Configuration and Analysis snap-in.

The syntax of this command is:

secedit /analyze /db filename [/cfg filename ] [/overwrite] [/log filename] [/quiet]

            /db filename - Specifies the database used to perform the analysis.

            /cfg filename - Specifies a security template to import into the database prior to performing the analysis. Security templates are created using the Security Templates snap-in.

            /log filename - Specifies a file in which to log the status of the configuration process.  If not specified, configuration processing information is logged in the scesrv.log file which is located in the s%windir%\security\logs directory.

            /quiet - Specifies that the analysis process should take place without prompting the user for any confirmation.

Example:

secedit /analyze /db hisecws.sdb

For all filenames, the current directory is used if no path is specified.
```

##### /import

```sh
*Evil-WinRM* PS V:\> secedit /import -h

Allows you to import a security template into a database so that the settings specified in the template can be applied to a system or analyzed against a system.

The syntax of this command is:

secedit /import  /db filename /cfg filename [/overwrite][/areas area1 area2...] [/log filename] [/quiet]

            /db filename - Specifies the database that the security template settings will be imported into.

            /cfg filename - Specifies a security template to import into the database. Security templates are created using the Security Templates snap-in.

            /overwrite - Specifies that the database should be emptied prior to importing the security template. If this parameter is not specified, the settings in the security template are accumulated into the database.  If this parameter is not specified and there are conflicting settings in the database and the template being imported, the template settings win.

            /areas - Specifies the security areas to export. If this parameter is not specified, all security settings defined in the database are exported. To export specific areas, separate each area by a space.  The following security areas are exported:

                        SECURITYPOLICY - Includes Account Policies, Audit Policies, Event Log Settings and Security Options.
                        GROUP_MGMT - Includes Restricted Group settings
                        USER_RIGHTS - Includes User Rights Assignment
                        REGKEYS - Includes Registry Permissions
                        FILESTORE - Includes File System permissions
                        SERVICES - Includes System Service settings

            /log filename - Specifies a file in which to log the status of the import process.  If not specified, import processing information is logged in the scesrv.log file which is located in the %windir%\security\logs directory.

            /quiet - Specifies that the import process should take place without prompting the user for any confirmation.

Example:

secedit /import /db hisecws.sdb /cfg hisecws.inf /overwrite

For all filenames, the current directory is used if no path is specified.
```

##### /export

```sh
Evil-WinRM* PS V:\> secedit /export -h

Allows you to export security settings stored in a database.

The syntax of this command is:

secedit /export [/db filename] [/mergedpolicy] /cfg filename [/areas area1 area2...] [/log filename]

            /db filename - Specifies the database to export data from. If not specified, system security database will be used.

            /cfg filename - Specifies a security template to export the database contents to.

            /mergedpolicy - Merges and exports domain and local policy security settings.

            /areas - Specifies the security areas to export. If this parameter is not specified, all security settings defined in the database are exported. To export specific areas, separate each area by a space.  The following security areas are exported:

                        SECURITYPOLICY - Includes Account Policies, Audit Policies, Event Log Settings and Security Options.
                        GROUP_MGMT - Includes Restricted Group settings
                        USER_RIGHTS - Includes User Rights Assignment
                        REGKEYS - Includes Registry Permissions
                        FILESTORE - Includes File System permissions
                        SERVICES - Includes System Service settings

            /log filename - Specifies a file in which to log the status of the export process.  If not specified, export processing information is logged in the scesrv.log file which is located in the %windir%\security\logs directory.

Example:

secedit /export /db hisecws.sdb /cfg hisecws.inf /log hisecws.log

For all filenames, the current directory is used if no path is specified.
```

##### /validate

```sh
*Evil-WinRM* PS V:\> secedit /validate -h
The system cannot find the file specified.

 Can't open the template.
```

##### /generaterollback

```sh
*Evil-WinRM* PS V:\> secedit /generaterollback -h

Allows you to generate a rollback template with respect to a configuration template.

The syntax of this command is:

secedit /generaterollback /cfg filename /rbk filename [/log filename] [/quiet]

            /db filename - Specifies the database used to perform the rollback.

            /cfg filename - Specifies a security template with respect to which a rollback template is generated. Security templates are created using the Security Templates snap-in.

            /rbk filename - Specifies a security template into which the rollback information is written. Security templates are created using the Security Templates snap-in.

            /log filename - Specifies a file in which to log the status of the rollback process.  If not specified, rollback processing information is logged in the scesrv.log file which is located in the %windir%\security\logs directory.

            /quiet - Specifies that the rollback process should take place without prompting the user for any confirmation.

Example:

secedit /generaterollback /db hisecws.sdb /cfg hisecws.inf /rbk hisecwsrollback.inf /log hisecws.log

For all filenames, the current directory is used if no path is specified.
```


