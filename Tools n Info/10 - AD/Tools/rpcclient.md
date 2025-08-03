
`rpcclient -U '' -N 10.129.170.211`
gives a prompt `rpcclient $>`

enumerate domain users
`rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211 -c 'enumdomusers'`

show info on one user
`rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211 -c 'queryuser svc-printer'`
`rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211 -c 'queryuser 0x44f'`

enumerate printers
`rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211 -c 'enumprinters'`



TODO! sniff traffic - default port? protocol really rpc?
```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient -U '' -N 10.129.170.211 -p 135
Cannot connect to server.  Error was NT_STATUS_IO_TIMEOUT

┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient -U '' -N 10.129.170.211 -p 139
Cannot connect to server.  Error was NT_STATUS_RESOURCE_NAME_NOT_FOUND

┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient -U '' -N 10.129.170.211 -p 445
rpcclient $>
```


### Examples

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211 -c 'enumdomusers'
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[svc-printer] rid:[0x44f]
```

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211 -c 'queryuser svc-printer'
        User Name   :   svc-printer
        Full Name   :   SVCPrinter
...
		Description :   Service Account for Printer
...
```

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211 -c 'enumprinters'         
        flags:[0x800000]
        name:[\\10.129.170.211\Microsoft XPS Document Writer]
        description:[\\10.129.170.211\Microsoft XPS Document Writer,Microsoft XPS Document Writer v4,]
        comment:[]

        flags:[0x800000]
        name:[\\10.129.170.211\Microsoft Print to PDF]
        description:[\\10.129.170.211\Microsoft Print to PDF,Microsoft Print To PDF,]
        comment:[]
```

### Help

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient --help
Usage: rpcclient [OPTION...] BINDING-STRING|HOST
Options:
  -c, --command=COMMANDS                       Execute semicolon separated cmds
  -I, --dest-ip=IP                             Specify destination IP address
  -p, --port=PORT                              Specify port number

Help options:
  -?, --help                                   Show this help message
      --usage                                  Display brief usage message

Common Samba options:
  -d, --debuglevel=DEBUGLEVEL                  Set debug level
      --debug-stdout                           Send debug output to standard output
  -s, --configfile=CONFIGFILE                  Use alternative configuration file
      --option=name=value                      Set smb.conf option from command line
  -l, --log-basename=LOGFILEBASE               Basename for log/debug files
      --leak-report                            enable talloc leak reporting on exit
      --leak-report-full                       enable full talloc leak reporting on exit

Connection options:
  -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution services only
  -O, --socket-options=SOCKETOPTIONS           socket options to use
  -m, --max-protocol=MAXPROTOCOL               Set max protocol level
  -n, --netbiosname=NETBIOSNAME                Primary netbios name
      --netbios-scope=SCOPE                    Use this Netbios scope
  -W, --workgroup=WORKGROUP                    Set the workgroup name
      --realm=REALM                            Set the realm name

Credential options:
  -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
  -N, --no-pass                                Don´t ask for a password
      --password=STRING                        Password
      --pw-nt-hash                             The supplied password is the NT hash
  -A, --authentication-file=FILE               Get the credentials from a file
  -P, --machine-pass                           Use stored machine account password
      --simple-bind-dn=DN                      DN to use for a simple bind
      --use-kerberos=desired|required|off      Use Kerberos authentication
      --use-krb5-ccache=CCACHE                 Credentials cache location for Kerberos
      --use-winbind-ccache                     Use the winbind ccache for authentication
      --client-protection=sign|encrypt|off     Configure used protection for client connections

Deprecated legacy options:
  -k, --kerberos                               DEPRECATED: Migrate to --use-kerberos

Version options:
  -V, --version                                Print version
```

```sh
┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient -U '' -N 10.129.170.211                                                                    
rpcclient $> help
---------------         ----------------------
       UNIXINFO
       getpwuid         Get shell and homedir
       uidtosid         Convert uid to sid
---------------         ----------------------
         MDSSVC
fetch_properties                Fetch connection properties
fetch_attributes                Fetch attributes for a CNID
---------------         ----------------------
        CLUSAPI
clusapi_open_cluster            Open cluster
clusapi_get_cluster_name                Get cluster name
clusapi_get_cluster_version             Get cluster version
clusapi_get_quorum_resource             Get quorum resource
clusapi_create_enum             Create enum query
clusapi_create_enumex           Create enumex query
clusapi_open_resource           Open cluster resource
clusapi_online_resource         Set cluster resource online
clusapi_offline_resource                Set cluster resource offline
clusapi_get_resource_state              Get cluster resource state
clusapi_get_cluster_version2            Get cluster version2
clusapi_pause_node              Pause cluster node
clusapi_resume_node             Resume cluster node
---------------         ----------------------
        WITNESS
GetInterfaceList                List the interfaces to which witness client connections can be made
       Register         Register for resource state change notifications of a NetName and IPAddress
     UnRegister         Unregister for notifications from the server</para></listitem></varlistentry>
    AsyncNotify         Request notification of registered resource changes from the server
     RegisterEx         Register for resource state change notifications of a NetName, ShareName and multiple IPAddresses
---------------         ----------------------
          FSRVP
fss_is_path_sup         Check whether a share supports shadow-copy requests
fss_get_sup_version             Get supported FSRVP version from server
fss_create_expose               Request shadow-copy creation and exposure
     fss_delete         Request shadow-copy share deletion
fss_has_shadow_copy             Check for an associated share shadow-copy
fss_get_mapping         Get shadow-copy share mapping information
fss_recovery_complete           Flag read-write snapshot as recovery complete, allowing further shadow-copy requests
---------------         ----------------------
         WINREG
 winreg_enumkey         Enumerate Keys
querymultiplevalues             Query multiple values
querymultiplevalues2            Query multiple values
 winreg_enumval         Enumerate Values
---------------         ----------------------
       EVENTLOG
eventlog_readlog                Read Eventlog
eventlog_numrecord              Get number of records
eventlog_oldestrecord           Get oldest record
eventlog_reportevent            Report event
eventlog_reporteventsource              Report event and source
eventlog_registerevsource               Register event source
eventlog_backuplog              Backup Eventlog File
eventlog_loginfo                Get Eventlog Information
---------------         ----------------------
        DRSUAPI
   dscracknames         Crack Name
    dsgetdcinfo         Get Domain Controller Info
 dsgetncchanges         Get NC Changes
dswriteaccountspn               Write Account SPN
---------------         ----------------------
         NTSVCS
ntsvcs_getversion               Query NTSVCS version
ntsvcs_validatedevinst          Query NTSVCS device instance
ntsvcs_hwprofflags              Query NTSVCS HW prof flags
ntsvcs_hwprofinfo               Query NTSVCS HW prof info
ntsvcs_getdevregprop            Query NTSVCS device registry property
ntsvcs_getdevlistsize           Query NTSVCS device list size
ntsvcs_getdevlist               Query NTSVCS device list
---------------         ----------------------
         WKSSVC
wkssvc_wkstagetinfo             Query WKSSVC Workstation Information
wkssvc_getjoininformation               Query WKSSVC Join Information
wkssvc_messagebuffersend                Send WKSSVC message
wkssvc_enumeratecomputernames           Enumerate WKSSVC computer names
wkssvc_enumerateusers           Enumerate WKSSVC users
---------------         ----------------------
       SHUTDOWN
---------------         ----------------------
       EPMAPPER
         epmmap         Map a binding
      epmlookup         Lookup bindings
---------------         ----------------------
           ECHO
     echoaddone         Add one to a number
       echodata         Echo data
       sinkdata         Sink data
     sourcedata         Source data
---------------         ----------------------
            DFS
     dfsversion         Query DFS support
         dfsadd         Add a DFS share
      dfsremove         Remove a DFS share
     dfsgetinfo         Query DFS share info
        dfsenum         Enumerate dfs shares
      dfsenumex         Enumerate dfs shares
---------------         ----------------------
         SRVSVC
        srvinfo         Server query info
   netshareenum         Enumerate shares
netshareenumall         Enumerate all shares
netsharegetinfo         Get Share Info
netsharesetinfo         Set Share Info
netsharesetdfsflags             Set DFS flags
    netfileenum         Enumerate open files
   netremotetod         Fetch remote time of day
netnamevalidate         Validate sharename
  netfilegetsec         Get File security
     netsessdel         Delete Session
    netsessenum         Enumerate Sessions
    netdiskenum         Enumerate Disks
    netconnenum         Enumerate Connections
    netshareadd         Add share
    netsharedel         Delete share
---------------         ----------------------
       NETLOGON
     logonctrl2         Logon Control 2
   getanydcname         Get trusted DC name
      getdcname         Get trusted PDC name
  dsr_getdcname         Get trusted DC name
dsr_getdcnameex         Get trusted DC name
dsr_getdcnameex2                Get trusted DC name
dsr_getsitename         Get sitename
dsr_getforesttrustinfo          Get Forest Trust Info
      logonctrl         Logon Control
       samlogon         Sam Logon
change_trust_pw         Change Trust Account Password
    gettrustrid         Get trust rid
dsr_enumtrustdom                Enumerate trusted domains
dsenumdomtrusts         Enumerate all trusted domains in an AD forest
deregisterdnsrecords            Deregister DNS records
netrenumtrusteddomains          Enumerate trusted domains
netrenumtrusteddomainsex                Enumerate trusted domains
getdcsitecoverage               Get the Site-Coverage from a DC
   capabilities         Return Capabilities
logongetdomaininfo              Return LogonGetDomainInfo
---------------         ----------------------
IRemoteWinspool
winspool_AsyncOpenPrinter               Open printer handle
winspool_AsyncCorePrinterDriverInstalled                Query Core Printer Driver Installed
---------------         ----------------------
        SPOOLSS
      adddriver         Add a print driver
     addprinter         Add a printer
      deldriver         Delete a printer driver
    deldriverex         Delete a printer driver with files
       enumdata         Enumerate printer data
     enumdataex         Enumerate printer data for a key
        enumkey         Enumerate printer keys
       enumjobs         Enumerate print jobs
         getjob         Get print job
         setjob         Set print job
      enumports         Enumerate printer ports
    enumdrivers         Enumerate installed printer drivers
   enumprinters         Enumerate printers
        getdata         Get print driver data
      getdataex         Get printer driver data with keyname
      getdriver         Get print driver information
   getdriverdir         Get print driver upload directory
getdriverpackagepath            Get print driver package download directory
     getprinter         Get printer info
    openprinter         Open printer handle
 openprinter_ex         Open printer handle
      setdriver         Set printer driver
getprintprocdir         Get print processor directory
        addform         Add form
        setform         Set form
        getform         Get form
     deleteform         Delete form
      enumforms         Enumerate forms
     setprinter         Set printer comment
 setprintername         Set printername
 setprinterdata         Set REG_SZ printer data
       rffpcnex         Rffpcnex test
     printercmp         Printer comparison test
      enumprocs         Enumerate Print Processors
enumprocdatatypes               Enumerate Print Processor Data Types
   enummonitors         Enumerate Print Monitors
createprinteric         Create Printer IC
playgdiscriptonprinteric                Create Printer IC
getcoreprinterdrivers           Get CorePrinterDriver
enumpermachineconnections               Enumerate Per Machine Connections
addpermachineconnection         Add Per Machine Connection
delpermachineconnection         Delete Per Machine Connection
---------------         ----------------------
           SAMR
      queryuser         Query user info
     querygroup         Query group info
queryusergroups         Query user groups
queryuseraliases                Query user aliases
  querygroupmem         Query group membership
  queryaliasmem         Query alias membership
 queryaliasinfo         Query alias info
    deletealias         Delete an alias
  querydispinfo         Query display info
 querydispinfo2         Query display info
 querydispinfo3         Query display info
   querydominfo         Query domain info
   enumdomusers         Enumerate domain users
  enumdomgroups         Enumerate domain groups
  enumalsgroups         Enumerate alias groups
    enumdomains         Enumerate domains
  createdomuser         Create domain user
 createdomgroup         Create domain group
 createdomalias         Create domain alias
 samlookupnames         Look up names
  samlookuprids         Look up names
 deletedomgroup         Delete domain group
  deletedomuser         Delete domain user
 samquerysecobj         Query SAMR security object
   getdompwinfo         Retrieve domain password info
getusrdompwinfo         Retrieve user domain password info
   lookupdomain         Lookup Domain Name
      chgpasswd         Change user password
     chgpasswd2         Change user password
     chgpasswd3         Change user password
     chgpasswd4         Change user password
 getdispinfoidx         Get Display Information Index
    setuserinfo         Set user info
   setuserinfo2         Set user info2
---------------         ----------------------
      LSARPC-DS
  dsroledominfo         Get Primary Domain Information
---------------         ----------------------
         LSARPC
       lsaquery         Query info policy
     lookupsids         Convert SIDs to names
    lookupsids3         Convert SIDs to names
lookupsids_level                Convert SIDs to names
    lookupnames         Convert names to SIDs
   lookupnames4         Convert names to SIDs
lookupnames_level               Convert names to SIDs
      enumtrust         Enumerate trusted domains
      enumprivs         Enumerate privileges
    getdispname         Get the privilege name
     lsaenumsid         Enumerate the LSA SIDS
lsacreateaccount                Create a new lsa account
lsaenumprivsaccount             Enumerate the privileges of an SID
lsaenumacctrights               Enumerate the rights of an SID
     lsaaddpriv         Assign a privilege to a SID
     lsadelpriv         Revoke a privilege from a SID
lsaaddacctrights                Add rights to an account
lsaremoveacctrights             Remove rights from an account
lsalookupprivvalue              Get a privilege value given its name
 lsaquerysecobj         Query LSA security object
lsaquerytrustdominfo            Query LSA trusted domains info (given a SID)
lsaquerytrustdominfobyname              Query LSA trusted domains info (given a name), only works for Windows > 2k
lsaquerytrustdominfobysid               Query LSA trusted domains info (given a SID)
lsasettrustdominfo              Set LSA trusted domain info
    getusername         Get username
   createsecret         Create Secret
   deletesecret         Delete Secret
    querysecret         Query Secret
      setsecret         Set Secret
retrieveprivatedata             Retrieve Private Data
storeprivatedata                Store Private Data
 createtrustdom         Create Trusted Domain
createtrustdomex2               Create Trusted Domain (Ex2 Variant)
createtrustdomex3               Create Trusted Domain (Ex3 Variant)
 deletetrustdom         Delete Trusted Domain
---------------         ----------------------
GENERAL OPTIONS
           help         Get help on commands
              ?         Get help on commands
     debuglevel         Set debug level
          debug         Set debug level
           list         List available commands on <pipe>
           exit         Exit program
           quit         Exit program
           sign         Force RPC pipe connections to be signed
           seal         Force RPC pipe connections to be sealed
         packet         Force RPC pipe connections with packet authentication level
       schannel         Force RPC pipe connections to be sealed with 'schannel'. Assumes valid machine account to this domain controller.
   schannelsign         Force RPC pipe connections to be signed (not sealed) with 'schannel'.  Assumes valid machine account to this domain controller.
        timeout         Set timeout (in milliseconds) for RPC operations
      transport         Choose ncacn transport for RPC operations
           none         Force RPC pipe connections to have no special properties
rpcclient $> fss_is_path_sup
do_cmd: Could not initialise FileServerVssAgent. Error was NT_STATUS_ACCESS_DENIED
rpcclient $> exit
                                                                                                                              
┌──(fixit42㉿kali)-[~/shells]
└─$ rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211                  
rpcclient $> fss_is_path_sup
do_cmd: Could not initialise FileServerVssAgent. Error was NT_STATUS_OBJECT_NAME_NOT_FOUND
rpcclient $> 

```

TODO! test this later on htb return (we replaced the vss service, oupsie!)
`rpcclient -U 'return\svc-printer' --password '1edFg43012!!' 10.129.170.211 -c 'fss_is_path_sup'`

