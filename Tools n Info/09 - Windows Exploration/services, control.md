
### Powershell
*Note: `sc.exe` can be used in ps too (`sc` is an alias to `Set-Content`)*

List all services with status
```powershell
Get-Service
```

Stop service
```powershell
Stop-Service -Name "SERVICE-NAME"
Stop-Service -Name "SERVICE-NAME" -Force
```

Start service
```powershell
Start-Service -Name "SERVICE-NAME"
```

Restart service
```powershell
Restart-Service -Name "SERVICE-NAME"
Restart-Service -Name "SERVICE-NAME" -Force
```

Starting by setting the status
```powershell
Set-Service -Name "SERVICE-NAME" -Status running
```

Disable service (and stop)
```powershell
Set-Service -Name "SERVICE-NAME" -Status stopped -StartupType disabled
```

Set to automatic (and start)
```powershell
Set-Service -Name "SERVICE-NAME" -Status running -StartupType automatic
```


### Command line

List all services with status
```sh
sc queryex state=all type=service
```

Get info on specific service
```sh
sc qc [service name]
```

Stop service
```sh
net stop "SERVICE-NAME"
sc stop "SERVICE-NAME"
```

Start service
```sh
net start "SERVICE-NAME"
sc start "SERVICE-NAME"
```

Restart - to test
```sh
net stop "SERVICE-NAME" && net start "SERVICE-NAME"
```
*net stop and start are blocking, sc stop and start are not*

Set disabled
```sh
sc config "SERVICE-NAME" start=disabled
```

Set auto
```sh
sc config "SERVICE-NAME" start=auto
```

Manual
```
sc config "SERVICE-NAME" start=demand
```

Automatic Delayed
```
sc config "SERVICE-NAME" start=delayed-auto
```


### Info

`net` can only start, stop and pause services.
`sc` has more advanced controls, can query state, create and delete services, change their configuration and security: `sc config beep start= demand`

`net` only works locally.
`sc` can be used over the network: `sc \\snow start rpcapd`

`net` accepts display names: `net start "Windows Firewall"`
`sc` always requires a service name: `sc start SharedAccess`

`net` stop and start are blocking, `sc` stop and start are not
meaning we can't get an accurate reply from sc if it was successful

### Help

```sh
C:\Users\sofia>sc -h

ERROR:  Unrecognized command

DESCRIPTION:
        SC is a command line program used for communicating with the
        Service Control Manager and services.
USAGE:
        sc <server> [command] [service name] <option1> <option2>...


        The option <server> has the form "\\ServerName"
        Further help on commands can be obtained by typing: "sc [command]"
        Commands:
          query-----------Queries the status for a service, or
                          enumerates the status for types of services.
          queryex---------Queries the extended status for a service, or
                          enumerates the status for types of services.
          start-----------Starts a service.
          pause-----------Sends a PAUSE control request to a service.
          interrogate-----Sends an INTERROGATE control request to a service.
          continue--------Sends a CONTINUE control request to a service.
          stop------------Sends a STOP request to a service.
          config----------Changes the configuration of a service (persistent).
          description-----Changes the description of a service.
          failure---------Changes the actions taken by a service upon failure.
          failureflag-----Changes the failure actions flag of a service.
          sidtype---------Changes the service SID type of a service.
          privs-----------Changes the required privileges of a service.
          managedaccount--Changes the service to mark the service account
                          password as managed by LSA.
          qc--------------Queries the configuration information for a service.
          qdescription----Queries the description for a service.
          qfailure--------Queries the actions taken by a service upon failure.
          qfailureflag----Queries the failure actions flag of a service.
          qsidtype--------Queries the service SID type of a service.
          qprivs----------Queries the required privileges of a service.
          qtriggerinfo----Queries the trigger parameters of a service.
          qpreferrednode--Queries the preferred NUMA node of a service.
          qmanagedaccount-Queries whether a services uses an account with a
                          password managed by LSA.
          qprotection-----Queries the process protection level of a service.
          quserservice----Queries for a local instance of a user service template.
          delete----------Deletes a service (from the registry).
          create----------Creates a service. (adds it to the registry).
          control---------Sends a control to a service.
          sdshow----------Displays a service`s security descriptor.
          sdset-----------Sets a service`s security descriptor.
          showsid---------Displays the service SID string corresponding to an arbitrary name.
          triggerinfo-----Configures the trigger parameters of a service.
          preferrednode---Sets the preferred NUMA node of a service.
          GetDisplayName--Gets the DisplayName for a service.
          GetKeyName------Gets the ServiceKeyName for a service.
          EnumDepend------Enumerates Service Dependencies.

        The following commands don`t require a service name:
        sc <server> <command> <option>
          boot------------(ok | bad) Indicates whether the last boot should
                          be saved as the last-known-good boot configuration
          Lock------------Locks the Service Database
          QueryLock-------Queries the LockStatus for the SCManager Database
EXAMPLE:
        sc start MyService


QUERY and QUERYEX OPTIONS:
        If the query command is followed by a service name, the status
        for that service is returned.  Further options do not apply in
        this case.  If the query command is followed by nothing or one of
        the options listed below, the services are enumerated.
    type=    Type of services to enumerate (driver, service, userservice, all)
             (default = service)
    state=   State of services to enumerate (inactive, all)
             (default = active)
    bufsize= The size (in bytes) of the enumeration buffer
             (default = 4096)
    ri=      The resume index number at which to begin the enumeration
             (default = 0)
    group=   Service group to enumerate
             (default = all groups)

SYNTAX EXAMPLES
sc query                - Enumerates status for active services & drivers
sc query eventlog       - Displays status for the eventlog service
sc queryex eventlog     - Displays extended status for the eventlog service
sc query type= driver   - Enumerates only active drivers
sc query type= service  - Enumerates only Win32 services
sc query state= all     - Enumerates all services & drivers
sc query bufsize= 50    - Enumerates with a 50 byte buffer
sc query ri= 14         - Enumerates with resume index = 14
sc queryex group= ""    - Enumerates active services not in a group
sc query type= interact - Enumerates all interactive services
sc query type= driver group= NDIS     - Enumerates all NDIS drivers
```

```sh
*Evil-WinRM* PS C:\users\svc-printer\desktop> sc.exe config
DESCRIPTION:
        Modifies a service entry in the registry and Service Database.
USAGE:
        sc <server> config [service name] <option1> <option2>...

OPTIONS:
NOTE: The option name includes the equal sign.
      A space is required between the equal sign and the value.
      To remove the dependency, use a single / as dependency value.
 type= <own|share|interact|kernel|filesys|rec|adapt|userown|usershare>
 start= <boot|system|auto|demand|disabled|delayed-auto>
 error= <normal|severe|critical|ignore>
 binPath= <BinaryPathName to the .exe file>
 group= <LoadOrderGroup>
 tag= <yes|no>
 depend= <Dependencies(separated by / (forward slash))>
 obj= <AccountName|ObjectName>
 DisplayName= <display name>
 password= <password>
```

