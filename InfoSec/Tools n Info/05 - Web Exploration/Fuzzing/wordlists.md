
```sh
┌──(kali㉿kali)-[/usr/share/wordlists]
└─$ ls -la     
total 136672
drwxr-xr-x   2 root root      4096 Apr 28 12:22 .
drwxr-xr-x 442 root root     20480 May  3 15:01 ..
lrwxrwxrwx   1 root root        26 Apr 28 12:22 amass -> /usr/share/amass/wordlists
lrwxrwxrwx   1 root root        25 Apr 28 12:22 dirb -> /usr/share/dirb/wordlists
lrwxrwxrwx   1 root root        30 Apr 28 12:22 dirbuster -> /usr/share/dirbuster/wordlists
lrwxrwxrwx   1 root root        35 Apr 28 12:22 dnsmap.txt -> /usr/share/dnsmap/wordlist_TLAs.txt
lrwxrwxrwx   1 root root        41 Apr 28 12:22 fasttrack.txt -> /usr/share/set/src/fasttrack/wordlist.txt
lrwxrwxrwx   1 root root        45 Apr 28 12:22 fern-wifi -> /usr/share/fern-wifi-cracker/extras/wordlists
lrwxrwxrwx   1 root root        28 Apr 28 12:22 john.lst -> /usr/share/john/password.lst
lrwxrwxrwx   1 root root        27 Apr 28 12:22 legion -> /usr/share/legion/wordlists
lrwxrwxrwx   1 root root        46 Apr 28 12:22 metasploit -> /usr/share/metasploit-framework/data/wordlists
lrwxrwxrwx   1 root root        41 Apr 28 12:22 nmap.lst -> /usr/share/nmap/nselib/data/passwords.lst
-rw-r--r--   1 root root 139921507 May 12  2023 rockyou.txt
lrwxrwxrwx   1 root root        19 Apr 28 12:22 seclists -> /usr/share/seclists
lrwxrwxrwx   1 root root        39 Apr 28 12:22 sqlmap.txt -> /usr/share/sqlmap/data/txt/wordlist.txt
lrwxrwxrwx   1 root root        25 Apr 28 12:22 wfuzz -> /usr/share/wfuzz/wordlist
lrwxrwxrwx   1 root root        37 Apr 28 12:22 wifite.txt -> /usr/share/dict/wordlist-probable.txt
```

/usr/share/wordlists/seclists/Discovery/Web-Content


```sh
┌──(kali㉿kali)-[/usr/share/wordlists/dirbuster]
└─$ ls -la
total 7592
drwxr-xr-x 2 root root    4096 Sep 25  2023 .
drwxr-xr-x 4 root root    4096 Sep 25  2023 ..
-rw-r--r-- 1 root root   71638 Feb 27  2009 apache-user-enum-1.0.txt
-rw-r--r-- 1 root root   90418 Feb 27  2009 apache-user-enum-2.0.txt
-rw-r--r-- 1 root root  546618 Feb 27  2009 directories.jbrofuzz
-rw-r--r-- 1 root root 1802668 Feb 27  2009 directory-list-1.0.txt
-rw-r--r-- 1 root root 1980043 Feb 27  2009 directory-list-2.3-medium.txt
-rw-r--r-- 1 root root  725439 Feb 27  2009 directory-list-2.3-small.txt
-rw-r--r-- 1 root root 1849676 Feb 27  2009 directory-list-lowercase-2.3-medium.txt
-rw-r--r-- 1 root root  676768 Feb 27  2009 directory-list-lowercase-2.3-small.txt
```

```sh
┌──(kali㉿kali)-[/usr/share/wordlists/seclists]
└─$ ls -la
total 80
drwxr-xr-x  11 root root  4096 Feb 25 15:21 .
drwxr-xr-x 442 root root 20480 May  3 15:01 ..
drwxr-xr-x   9 root root  4096 Sep 25  2023 Discovery
drwxr-xr-x  10 root root 12288 Feb 25 15:21 Fuzzing
drwxr-xr-x   2 root root  4096 Feb 25 15:21 IOCs
drwxr-xr-x   9 root root  4096 Feb 25 15:21 Miscellaneous
drwxr-xr-x  16 root root 12288 Feb 25 15:21 Passwords
drwxr-xr-x   3 root root  4096 Feb 25 15:21 Pattern-Matching
drwxr-xr-x   8 root root  4096 Feb 25 15:21 Payloads
-rw-r--r--   1 root root  2425 Feb 16 16:55 README.md
drwxr-xr-x   4 root root  4096 Feb 25 15:21 Usernames
drwxr-xr-x  10 root root  4096 Feb 25 15:21 Web-Shells
```

```sh
┌──(kali㉿kali)-[/usr/share/wordlists/seclists/Discovery]
└─$ ls -la
total 60
drwxr-xr-x  9 root root  4096 Sep 25  2023 .
drwxr-xr-x 11 root root  4096 Feb 25 15:21 ..
drwxr-xr-x  2 root root  4096 Feb 25 15:21 DNS
drwxr-xr-x  2 root root  4096 Feb 25 15:21 File-System
drwxr-xr-x  2 root root  4096 Feb 25 15:21 Infrastructure
drwxr-xr-x  2 root root  4096 Feb 25 15:21 Mainframe
drwxr-xr-x  2 root root  4096 Feb 25 15:21 SNMP
drwxr-xr-x  2 root root  4096 Feb 25 15:21 Variables
drwxr-xr-x 11 root root 24576 Feb 25 15:21 Web-Content
```

```sh
┌──(kali㉿kali)-[/usr/…/wordlists/seclists/Discovery/Web-Content]
└─$ ls -la
total 64724
drwxr-xr-x 11 root root    24576 Feb 25 15:21 .
drwxr-xr-x  9 root root     4096 Sep 25  2023 ..
-rw-r--r--  1 root root     7882 Feb 16 16:55 AdobeCQ-AEM.txt
-rw-r--r--  1 root root      412 Feb 16 16:55 AdobeXML.fuzz.txt
-rw-r--r--  1 root root    68629 Feb 16 16:55 Apache.fuzz.txt
-rw-r--r--  1 root root     1983 Feb 16 16:55 ApacheTomcat.fuzz.txt
drwxr-xr-x  2 root root     4096 Feb 25 15:21 BurpSuite-ParamMiner
-rw-r--r--  1 root root      689 Feb 16 16:55 CGI-HTTP-POST-Windows.fuzz.txt
-rw-r--r--  1 root root      310 Feb 16 16:55 CGI-HTTP-POST.fuzz.txt
-rw-r--r--  1 root root     2074 Feb 16 16:55 CGI-Microsoft.fuzz.txt
-rw-r--r--  1 root root   140024 Feb 16 16:55 CGI-XPlatform.fuzz.txt
-rw-r--r--  1 root root   120751 Feb 16 16:55 CGIs.txt
drwxr-xr-x  3 root root     4096 Feb 25 15:21 CMS
-rw-r--r--  1 root root     4590 Feb 16 16:55 Common-DB-Backups.txt
-rw-r--r--  1 root root    75713 Feb 16 16:55 Common-PHP-Filenames.txt
-rw-r--r--  1 root root      272 Feb 16 16:55 CommonBackdoors-ASP.fuzz.txt
-rw-r--r--  1 root root      106 Feb 16 16:55 CommonBackdoors-JSP.fuzz.txt
-rw-r--r--  1 root root     7875 Feb 16 16:55 CommonBackdoors-PHP.fuzz.txt
-rw-r--r--  1 root root       87 Feb 16 16:55 CommonBackdoors-PL.fuzz.txt
drwxr-xr-x  2 root root     4096 Feb 25 15:21 Domino-Hunter
-rw-r--r--  1 root root    16595 Feb 16 16:55 FatwireCMS.fuzz.txt
-rw-r--r--  1 root root      360 Feb 16 16:55 Frontpage.fuzz.txt
-rw-r--r--  1 root root      143 Feb 16 16:55 HTTP-POST-Microsoft.fuzz.txt
-rw-r--r--  1 root root    20710 Feb 16 16:55 Hyperion.fuzz.txt
-rw-r--r--  1 root root     4924 Feb 16 16:55 IIS.fuzz.txt
-rw-r--r--  1 root root      306 Feb 16 16:55 JRun.fuzz.txt
-rw-r--r--  1 root root      746 Feb 16 16:55 JavaScript-Miners.txt
-rw-r--r--  1 root root       56 Feb 16 16:55 JavaServlets-Common.fuzz.txt
-rw-r--r--  1 root root      526 Feb 16 16:55 Jenkins-Hudson.txt
-rw-r--r--  1 root root    18914 Feb 16 16:55 KitchensinkDirectories.fuzz.txt
-rw-r--r--  1 root root  2664080 Feb 16 16:55 LinuxFileList.txt
-rw-r--r--  1 root root     1078 Feb 16 16:55 Logins.fuzz.txt
-rw-r--r--  1 root root     2810 Feb 16 16:55 LotusNotes.fuzz.txt
-rw-r--r--  1 root root    28518 Feb 16 16:55 Oracle-EBS-wordlist.txt
-rw-r--r--  1 root root      507 Feb 16 16:55 Oracle9i.fuzz.txt
-rw-r--r--  1 root root     2053 Feb 16 16:55 OracleAppServer.fuzz.txt
-rw-r--r--  1 root root     1623 Feb 16 16:55 PHP.fuzz.txt
-rw-r--r--  1 root root      527 Feb 16 16:55 Passwords.fuzz.txt
-rw-r--r--  1 root root    15285 Feb 16 16:55 Public-Source-Repo-Issues.json
-rw-r--r--  1 root root     1983 Feb 16 16:55 README.md
-rw-r--r--  1 root root      269 Feb 16 16:55 Randomfiles.fuzz.txt
-rw-r--r--  1 root root    99819 Feb 16 16:55 Roundcube-123.txt
drwxr-xr-x  4 root root     4096 Feb 25 15:21 SVNDigger
-rw-r--r--  1 root root      917 Feb 16 16:55 SunAppServerGlassfish.fuzz.txt
-rw-r--r--  1 root root      362 Feb 16 16:55 SuniPlanet.fuzz.txt
drwxr-xr-x  2 root root     4096 Feb 25 15:21 URLs
-rw-r--r--  1 root root      686 Feb 16 16:55 UnixDotfiles.fuzz.txt
-rw-r--r--  1 root root      549 Feb 16 16:55 Vignette.fuzz.txt
drwxr-xr-x  2 root root     4096 Feb 25 15:21 Web-Services
-rw-r--r--  1 root root    36246 Feb 16 16:55 aem2.txt
-rw-r--r--  1 root root      275 Feb 16 16:55 apache.txt
drwxr-xr-x  2 root root     4096 Feb 25 15:21 api
-rw-r--r--  1 root root      223 Feb 16 16:55 axis.txt
-rw-r--r--  1 root root   166371 Feb 16 16:55 big.txt
-rw-r--r--  1 root root    54157 Feb 16 16:55 burp-parameter-names.txt
-rw-r--r--  1 root root      686 Feb 16 16:55 coldfusion.txt
-rw-r--r--  1 root root 16205722 Feb 16 16:55 combined_directories.txt
-rw-r--r--  1 root root  1147407 Feb 16 16:55 combined_words.txt
-rw-r--r--  1 root root    36116 Feb 16 16:55 common-and-dutch.txt
-rw-r--r--  1 root root    38434 Feb 16 16:55 common-and-french.txt
-rw-r--r--  1 root root    40318 Feb 16 16:55 common-and-italian.txt
-rw-r--r--  1 root root    38653 Feb 16 16:55 common-and-portuguese.txt
-rw-r--r--  1 root root    39018 Feb 16 16:55 common-and-spanish.txt
-rw-r--r--  1 root root     1164 Feb 16 16:55 common-api-endpoints-mazen160.txt
-rw-r--r--  1 root root    38138 Feb 16 16:55 common.txt
-rw-r--r--  1 root root      968 Feb 16 16:55 confluence-administration.txt
-rw-r--r--  1 root root      197 Feb 16 16:55 default-web-root-directory-linux.txt
-rw-r--r--  1 root root       49 Feb 16 16:55 default-web-root-directory-windows.txt
-rw-r--r--  1 root root  1802665 Feb 16 16:55 directory-list-1.0.txt
-rw-r--r--  1 root root 14802863 Feb 16 16:55 directory-list-2.3-big.txt
-rw-r--r--  1 root root  1980035 Feb 16 16:55 directory-list-2.3-medium.txt
-rw-r--r--  1 root root   725434 Feb 16 16:55 directory-list-2.3-small.txt
-rw-r--r--  1 root root 13192445 Feb 16 16:55 directory-list-lowercase-2.3-big.txt
-rw-r--r--  1 root root  1849665 Feb 16 16:55 directory-list-lowercase-2.3-medium.txt
-rw-r--r--  1 root root   676761 Feb 16 16:55 directory-list-lowercase-2.3-small.txt
-rw-r--r--  1 root root   146080 Feb 16 16:55 dirsearch.txt
-rw-r--r--  1 root root     1234 Feb 16 16:55 domino-dirs-coldfusion39.txt
-rw-r--r--  1 root root     7395 Feb 16 16:55 domino-endpoints-coldfusion39.txt
-rw-r--r--  1 root root    17378 Feb 16 16:55 dsstorewordlist.txt
drwxr-xr-x  3 root root     4096 Feb 25 15:21 dutch
-rwxr-xr-x  1 root root       94 Feb 16 16:55 elmah.txt
-rw-r--r--  1 root root      633 Feb 16 16:55 fnf-fuzz.txt
-rw-r--r--  1 root root    18410 Feb 16 16:55 forefront-identity-management.txt
-rw-r--r--  1 root root      522 Feb 16 16:55 frontpage.txt
-rw-r--r--  1 root root     2225 Feb 16 16:55 golang.txt
-rw-r--r--  1 root root     1602 Feb 16 16:55 graphql.txt
-rw-r--r--  1 root root      871 Feb 16 16:55 hashicorp-consul-api.txt
-rw-r--r--  1 root root     1355 Feb 16 16:55 hashicorp-vault.txt
-rw-r--r--  1 root root     3658 Feb 16 16:55 hpsmh.txt
-rw-r--r--  1 root root    20643 Feb 16 16:55 hyperion.txt
-rw-r--r--  1 root root      849 Feb 16 16:55 iis-systemweb.txt
-rw-r--r--  1 root root      362 Feb 16 16:55 iplanet.txt
-rw-r--r--  1 root root      365 Feb 16 16:55 jboss.txt
-rw-r--r--  1 root root      306 Feb 16 16:55 jrun.txt
-rw-r--r--  1 root root     1110 Feb 16 16:55 keycloak.txt
-rw-r--r--  1 root root  1037454 Feb 16 16:55 local-ports.txt
-rw-r--r--  1 root root      465 Feb 16 16:55 netware.txt
-rw-r--r--  1 root root      570 Feb 16 16:55 nginx.txt
-rw-r--r--  1 root root     9327 Feb 16 16:55 oauth-oidc-scopes.txt
-rw-r--r--  1 root root    26862 Feb 16 16:55 oracle.txt
-rw-r--r--  1 root root      368 Feb 16 16:55 proxy-conf.fuzz.txt
-rw-r--r--  1 root root     6304 Feb 16 16:55 pulsesecure.txt
-rw-r--r--  1 root root    40117 Feb 16 16:55 quickhits.txt
-rw-r--r--  1 root root   494077 Feb 16 16:55 raft-large-directories-lowercase.txt
-rw-r--r--  1 root root   542009 Feb 16 16:55 raft-large-directories.txt
-rw-r--r--  1 root root    20247 Feb 16 16:55 raft-large-extensions-lowercase.txt
-rw-r--r--  1 root root    20692 Feb 16 16:55 raft-large-extensions.txt
-rw-r--r--  1 root root   470356 Feb 16 16:55 raft-large-files-lowercase.txt
-rw-r--r--  1 root root   493618 Feb 16 16:55 raft-large-files.txt
-rw-r--r--  1 root root   959425 Feb 16 16:55 raft-large-words-lowercase.txt
-rw-r--r--  1 root root  1053888 Feb 16 16:55 raft-large-words.txt
-rw-r--r--  1 root root   224501 Feb 16 16:55 raft-medium-directories-lowercase.txt
-rw-r--r--  1 root root   250429 Feb 16 16:55 raft-medium-directories.txt
-rw-r--r--  1 root root     9591 Feb 16 16:55 raft-medium-extensions-lowercase.txt
-rw-r--r--  1 root root     9890 Feb 16 16:55 raft-medium-extensions.txt
-rw-r--r--  1 root root   212598 Feb 16 16:55 raft-medium-files-lowercase.txt
-rw-r--r--  1 root root   224381 Feb 16 16:55 raft-medium-files.txt
-rw-r--r--  1 root root   471037 Feb 16 16:55 raft-medium-words-lowercase.txt
-rw-r--r--  1 root root   524649 Feb 16 16:55 raft-medium-words.txt
-rw-r--r--  1 root root   145744 Feb 16 16:55 raft-small-directories-lowercase.txt
-rw-r--r--  1 root root   163211 Feb 16 16:55 raft-small-directories.txt
-rw-r--r--  1 root root     7055 Feb 16 16:55 raft-small-extensions-lowercase.txt
-rw-r--r--  1 root root     7317 Feb 16 16:55 raft-small-extensions.txt
-rw-r--r--  1 root root   140712 Feb 16 16:55 raft-small-files-lowercase.txt
-rw-r--r--  1 root root   148390 Feb 16 16:55 raft-small-files.txt
-rw-r--r--  1 root root   311826 Feb 16 16:55 raft-small-words-lowercase.txt
-rw-r--r--  1 root root   348619 Feb 16 16:55 raft-small-words.txt
-rw-r--r--  1 root root      401 Feb 16 16:55 reverse-proxy-inconsistencies.txt
-rw-r--r--  1 root root     2716 Feb 16 16:55 ror.txt
-rw-r--r--  1 root root     1480 Feb 16 16:55 sap-analytics-cloud.txt
-rw-r--r--  1 root root    31437 Feb 16 16:55 sap.txt
-rw-r--r--  1 root root    25504 Feb 16 16:55 sharepoint-ennumeration.txt
-rw-r--r--  1 root root     1890 Feb 16 16:55 spring-boot.txt
-rw-r--r--  1 root root      917 Feb 16 16:55 sunas.txt
-rw-r--r--  1 root root      778 Feb 16 16:55 swagger.txt
-rw-r--r--  1 root root      219 Feb 16 16:55 tests.txt
-rw-r--r--  1 root root     1326 Feb 16 16:55 tftp.fuzz.txt
-rw-r--r--  1 root root     2474 Feb 16 16:55 tomcat.txt
drwxr-xr-x  2 root root     4096 Feb 25 15:21 trickest-robots-disallowed-wordlists
-rw-r--r--  1 root root    67618 Feb 16 16:55 uri-from-top-55-most-popular-apps.txt
-rw-r--r--  1 root root     1583 Feb 16 16:55 url-params_from-top-55-most-popular-apps.txt
-rw-r--r--  1 root root     1788 Feb 16 16:55 versioning_metafiles.txt
-rw-r--r--  1 root root     5259 Feb 16 16:55 vulnerability-scan_j2ee-websites_WEB-INF.txt
-rw-r--r--  1 root root    58204 Feb 16 16:55 web-all-content-types.txt
-rw-r--r--  1 root root   828660 Feb 16 16:55 web-extensions-big.txt
-rw-r--r--  1 root root      217 Feb 16 16:55 web-extensions.txt
-rw-r--r--  1 root root      250 Feb 16 16:55 web-mutations.txt
-rw-r--r--  1 root root     7407 Feb 16 16:55 weblogic.txt
-rw-r--r--  1 root root    10893 Feb 16 16:55 websphere.txt
-rw-r--r--  1 root root     4477 Feb 16 16:55 wso2-enterprise-integrator.txt
```
