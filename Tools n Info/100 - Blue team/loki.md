
https://github.com/Neo23x0/Loki

`python loki.py -h`
`python loki.py --update` to get and generate the signature-base directory

### Examples

```sh
cmnatic@thm-yara:~/suspicious-files/file1$ python ../../tools/Loki/loki.py -p .

	  __   ____  __ ______                                                                                    
     / /  / __ \/ //_/  _/                                                                                    
    / /__/ /_/ / ,< _/ /                                                                                      
   /____/\____/_/|_/___/                                                                                      
      ________  _____  ____                                                                                   
     /  _/ __ \/ ___/ / __/______ ____  ___  ___ ____                                                         
    _/ // /_/ / /__  _\ \/ __/ _ `/ _ \/ _ \/ -_) __/                                                         
   /___/\____/\___/ /___/\__/\_,_/_//_/_//_/\__/_/                                                            

   Copyright by Florian Roth, Released under the GNU General Public License                                   
   Version 0.32.1                                                                                             

   DISCLAIMER - USE AT YOUR OWN RISK                                                                          
   Please report false positives via https://github.com/Neo23x0/Loki/issues                                   


[NOTICE] Starting Loki Scan VERSION: 0.32.1 SYSTEM: thm-yara TIME: 20250410T12:04:28Z PLATFORM:     PROC: x86_64 ARCH: 64bit                                                                                                
[NOTICE] Registered plugin PluginWMI                                                                          
[NOTICE] Loaded plugin /home/cmnatic/tools/Loki/plugins/loki-plugin-wmi.py                                    
[NOTICE] PE-Sieve successfully initialized BINARY: /home/cmnatic/tools/Loki/tools/pe-sieve64.exe SOURCE: https://github.com/hasherezade/pe-sieve                                                                            
[INFO] File Name Characteristics initialized with 2841 regex patterns                                         
[INFO] C2 server indicators initialized with 1541 elements                                                    
[INFO] Malicious MD5 Hashes initialized with 19034 hashes                                                     
[INFO] Malicious SHA1 Hashes initialized with 7159 hashes                                                     
[INFO] Malicious SHA256 Hashes initialized with 22841 hashes                                                  
[INFO] False Positive Hashes initialized with 30 hashes                                                       
[INFO] Processing YARA rules folder /home/cmnatic/tools/Loki/signature-base/yara                              
[INFO] Initializing all YARA rules at once (composed string of all rule files)                                
[INFO] Initialized 653 Yara rules                                                                             
[INFO] Reading private rules from binary ...                                                                  
[NOTICE] Program should be run as 'root' to ensure all access rights to process memory and file objects.      
[NOTICE] Running plugin PluginWMI                                                                             
[NOTICE] Finished running plugin PluginWMI                                                                    
[INFO] Scanning . ...                                                                                         
[WARNING]                                                                                                     
FILE: ./ind3x.php SCORE: 70 TYPE: PHP SIZE: 80992                                                             
FIRST_BYTES: 3c3f7068700a2f2a0a09623337346b20322e320a / <?php/*b374k 2.2                                      
MD5: 1606bdac2cb613bf0b8a22690364fbc5                                                                         
SHA1: 9383ed4ee7df17193f7a034c3190ecabc9000f9f                                                                
SHA256: 5479f8cd1375364770df36e5a18262480a8f9d311e8eedb2c2390ecb233852ad CREATED: Mon Nov  9 15:15:32 2020 MODIFIED: Mon Nov  9 13:06:56 2020 ACCESSED: Thu Apr 10 12:04:32 2025                                            
REASON_1: Yara Rule MATCH: webshell_metaslsoft SUBSCORE: 70                                                   
DESCRIPTION: Web Shell - file metaslsoft.php REF: -                                                           
MATCHES: Str1: $buff .= "<tr><td><a href=\\"?d=".$pwd."\\">[ $folder ]</a></td><td>LINK</t                    "
[NOTICE] Results: 0 alerts, 1 warnings, 7 notices                                                             
[RESULT] Suspicious objects detected!                                                                         
[RESULT] Loki recommends a deeper analysis of the suspicious objects.                                         
[INFO] Please report false positives via https://github.com/Neo23x0/signature-base                            
[NOTICE] Finished LOKI Scan SYSTEM: thm-yara TIME: 20250410T12:04:32Z                                         

Press Enter to exit ... 
```
### Help

```sh
cmnatic@thm-yara:~/tools/Loki$ python loki.py -h
usage: loki.py [-h] [-p path] [-s kilobyte] [-l log-file] [-r remote-loghost]
               [-t remote-syslog-port] [-a alert-level] [-w warning-level]
               [-n notice-level] [--printall] [--allreasons] [--noprocscan]
               [--nofilescan] [--nolevcheck] [--scriptanalysis] [--rootkit]
               [--noindicator] [--reginfs] [--dontwait] [--intense] [--csv]
               [--onlyrelevant] [--nolog] [--update] [--debug]
               [--maxworkingset MAXWORKINGSET] [--syslogtcp]
               [--logfolder log-folder] [--nopesieve] [--pesieveshellc]
               [--nolisten] [--excludeprocess EXCLUDEPROCESS]

Loki - Simple IOC Scanner

optional arguments:
  -h, --help            show this help message and exit
  -p path               Path to scan
  -s kilobyte           Maximum file size to check in KB (default 5000 KB)
  -l log-file           Log file
  -r remote-loghost     Remote syslog system
  -t remote-syslog-port
                        Remote syslog port
  -a alert-level        Alert score
  -w warning-level      Warning score
  -n notice-level       Notice score
  --printall            Print all files that are scanned
  --allreasons          Print all reasons that caused the score
  --noprocscan          Skip the process scan
  --nofilescan          Skip the file scan
  --nolevcheck          Skip the Levenshtein distance check
  --scriptanalysis      Activate script analysis (beta)
  --rootkit             Skip the rootkit check
  --noindicator         Do not show a progress indicator
  --reginfs             Do check for Regin virtual file system
  --dontwait            Do not wait on exit
  --intense             Intense scan mode (also scan unknown file types and
                        all extensions)
  --csv                 Write CSV log format to STDOUT (machine processing)
  --onlyrelevant        Only print warnings or alerts
  --nolog               Don´t write a local log file
  --update              Update the signatures from the "signature-base" sub
                        repository
  --debug               Debug output
  --maxworkingset MAXWORKINGSET
                        Maximum working set size of processes to scan (in MB,
                        default 100 MB)
  --syslogtcp           Use TCP instead of UDP for syslog logging
  --logfolder log-folder
                        Folder to use for logging when log file is not
                        specified
  --nopesieve           Do not perform pe-sieve scans
  --pesieveshellc       Perform pe-sieve shellcode scan
  --nolisten            Dot not show listening connections
  --excludeprocess EXCLUDEPROCESS
                        Specify an executable name to exclude from scans, can
                        be used multiple times
```

