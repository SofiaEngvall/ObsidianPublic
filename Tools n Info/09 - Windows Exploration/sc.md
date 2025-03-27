
ServiceControl
https://ss64.com/nt/sc.html
https://www.advancedinstaller.com/forums/viewtopic.php?t=49990

`sc [\\server] [command] [service_name] [Options]`

`sc GetKeyName DisplayName` find the `service_name`

`sc <ServerName> sdshow <ServiceName>`

`sc <ServerName> sdshow <ServiceName> showrights` Shows all the service dacls in SDDL format



#### commands

`query [qryOpt]`   Show status.
`queryEx [qryOpt]`  Show extended info - pid, flags.
GetDisplayName    Show the DisplayName.
GetKeyName        Show the Service KeyName.
EnumDepend        Show Dependencies.
qc                Show config - dependencies, full path etc.
**start**          START a service.
**stop**           STOP a service
pause          PAUSE a service.
continue       CONTINUE a service.
create         Create a service. (add it to the registry).
**config**         permanently change the service configuration.
delete         Delete a service (from the registry).
control        Send a control to a service.
interrogate    Send an INTERROGATE control request to a service.
Qdescription   Query the description of a service.
description    Change the description of a service.
Qfailure       Query the actions taken by a service upon failure.
failure        Change the actions taken by a service upon failure.
sdShow         Display a service’s security descriptor using SDDL.
SdSet          Sets a service’s security descriptor using SDDL.

