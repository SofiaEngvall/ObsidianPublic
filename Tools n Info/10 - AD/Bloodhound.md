
### Gathering data using Sharphound

run on windows machine

https://bloodhound.readthedocs.io/en/latest/data-collection/sharphound-all-flags.html old?
https://support.bloodhoundenterprise.io/hc/en-us/sections/17274904083483
https://github.com/SpecterOps/SharpHound/releases
https://github.com/SpecterOps/AzureHound/releases

`Sharphound.exe --CollectionMethods All --Domain za.tryhackme.com --ExcludeDCs`

OBS! Sharphound is very noicy!

Execute Sharphound with the "All" collection method once at the start of your assessment
Then execute Sharphound at least twice a day using the "Session" collection method (coffee break time?)
(Click "Clear Session Information" in Bloodhound before importing the data from the Session runs.)

Stealthier option:
`SharpHound.exe -c Session,LocalAdmin,Trusts,ACL `

### Gathering from Kali

`bloodhound-python -u svc-admin -p 'management2005' -d spookysec.local -dc AttacktiveDirectory.spookysec.local -ns 10.10.229.142 -c all`
-c works the same as with sharphound

### Gather offline data

- the NTDS.dit
- registry hives
- group membership dumps

can we do this? if so, how to import?

### Running Bloodhound

##### Starting Bloodhound

`bloodhound --no-sandbox`

opens http://127.0.0.1:8080

neo4j available at http://localhost:7474

##### Clearing old data

- Go to neo4j at http://localhost:7474
- In the field containing `neo4j$`, enter `MATCH (n) DETACH DELETE n;`

##### Ingesting data

- Go to `Administration`, `File Ingest` and click `Upload File(s)`
- Drag files in or select in file browser
- Click `Upload`, `Upload` and `Close`
- Wait until the `Status Message` is `Complete`

##### Look at data

###### Example to see who has permissions for the domain
- Go to `Explore` `Search` and click the search field
- Type `.`
- Click something and remove everything but the domain name
- Double click the domain name
- Click the domain in the graph
- Click Controllers on the left side

![[Images/Pasted image 20250705020519.png]]
##### Pathfinding from user to a admin
![[Images/Pasted image 20250313232837.png]]

###### Example exploitation of this path
1. Use our AD credentials to RDP into **THMJMP1**.
2. Look for a privilege escalation vector on the host that would provide us with Administrative access.
3. Using Administrative access, we can use credential harvesting techniques and tools such as Mimikatz.
4. Since the T1 Admin has an active session on **THMJMP1**, our credential harvesting would provide us with the NTLM hash of the associated account.

https://bloodhound.readthedocs.io/en/latest/data-analysis/edges.html

Check the Analysis tab!
- List all Kerberoastable Accounts

##### Key shortcuts

Left Ctrl - Toggle Labels


### Examples

Sharphound:
```powershell
PS C:\Users\graeme.williams\Documents> ./Sharphound.exe --CollectionMethods All --Domain za.tryhackme.com --ExcludeDCs        
2025-03-13T19:42:16.6434417+00:00|INFORMATION|Resolved Collection Methods: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn
, Trusts, ACL, Container, RDP, ObjectProps, DCOM, SPNTargets, PSRemote
2025-03-13T19:42:16.6434417+00:00|INFORMATION|Initializing SharpHound at 7:42 PM on 3/13/2025
2025-03-13T19:42:17.1902965+00:00|INFORMATION|Flags: Group, LocalAdmin, GPOLocalGroup, Session, LoggedOn, Trusts, ACL, Contain
er, RDP, ObjectProps, DCOM, SPNTargets, PSRemote
2025-03-13T19:42:17.3638575+00:00|INFORMATION|Beginning LDAP search for za.tryhackme.com
2025-03-13T19:42:47.9373979+00:00|INFORMATION|Status: 0 objects finished (+0 0)/s -- Using 50 MB RAM
2025-03-13T19:43:02.9456587+00:00|INFORMATION|Producer has finished, closing LDAP channel
2025-03-13T19:43:03.3310968+00:00|INFORMATION|LDAP channel closed, waiting for consumers
2025-03-13T19:43:03.5185992+00:00|INFORMATION|Consumers finished, closing output channel
2025-03-13T19:43:03.5810959+00:00|INFORMATION|Output channel closed, waiting for output task to complete
Closing writers
2025-03-13T19:43:04.0342287+00:00|INFORMATION|Status: 2159 objects finished (+2159 46.93478)/s -- Using 88 MB RAM
2025-03-13T19:43:04.0342287+00:00|INFORMATION|Enumeration finished in 00:00:46.6887506
2025-03-13T19:43:04.3500417+00:00|INFORMATION|SharpHound Enumeration Completed at 7:43 PM on 3/13/2025! Happy Graphing!
```


### Problemsolving

##### Error - Outdated Postgres

###### error when trying to run bloodhound

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ bloodhound --no-sandbox
[sudo] password for kali: 

 It seems it's the first time you run bloodhound

 Please run bloodhound-setup first

Do you want to run bloodhound-setup now? [Y/n] y

 [*] Starting PostgreSQL service

 [*] Creating Database
WARNING:  database "postgres" has a collation version mismatch
DETAIL:  The database was created using collation version 2.40, but the operating system provides version 2.41.
HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE postgres REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.

 Creating database user
WARNING:  database "postgres" has a collation version mismatch
DETAIL:  The database was created using collation version 2.40, but the operating system provides version 2.41.
HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE postgres REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
WARNING:  database "postgres" has a collation version mismatch
DETAIL:  The database was created using collation version 2.40, but the operating system provides version 2.41.
HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE postgres REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.

 Creating database
WARNING:  database "postgres" has a collation version mismatch
DETAIL:  The database was created using collation version 2.40, but the operating system provides version 2.41.
HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE postgres REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
createdb: error: database creation failed: ERROR:  template database "template1" has a collation version mismatch
DETAIL:  The template database was created using collation version 2.40, but the operating system provides version 2.41.
HINT:  Rebuild all objects in the template database that use the default collation and run ALTER DATABASE template1 REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: FATAL:  database "bloodhound" does not exist
```
###### steps to take

```sh
┌──(kali㉿proxli)-[~/boxes/thm/attacktive]
└─$ sudo -u postgres psql                                                                               
WARNING:  database "postgres" has a collation version mismatch
DETAIL:  The database was created using collation version 2.40, but the operating system provides version 2.41.
HINT:  Rebuild all objects in this database that use the default collation and run ALTER DATABASE postgres REFRESH COLLATION VERSION, or build PostgreSQL with the right library version.
psql (17.5 (Debian 17.5-1))
Type "help" for help.

postgres=# ALTER DATABASE postgres REFRESH COLLATION VERSION;
NOTICE:  changing version from 2.40 to 2.41
ALTER DATABASE
```


##### Error - Data is not uploaded as is should

###### Check Neo4j Directly
Open the Neo4j browser: [`http://localhost:7474`](http://localhost:7474) (default credentials: `neo4j:neo4j`).
- To check if there's data - Run `MATCH (n) RETURN count(n);`
  If this returns `0`, the data wasn’t imported.
- To delete all data and start over - Run `MATCH (n) DETACH DELETE n;`
  and Re-import the JSON files

### Installation

`sudo apt install bloodhound neo4j`
`sudo neo4j console`

continue: https://www.kali.org/tools/bloodhound/

```sh
┌──(kali㉿kali)-[~/ad-temp]
└─$ neo4j console start                                                  
Command 'neo4j' not found, but can be installed with:
sudo apt install neo4j
Do you want to install it? (N/y)y
sudo apt install neo4j
[sudo] password for kali: 
Installing:                     
  neo4j

Installing dependencies:
  binfmt-support  fastjar  jarwrapper

Summary:
  Upgrading: 0, Installing: 4, Removing: 0, Not Upgrading: 1267
  Download size: 99.6 MB
  Space needed: 112 MB / 2173 MB available

Continue? [Y/n] y
Get:1 http://mirror.accum.se/mirror/kali.org/kali kali-rolling/main amd64 binfmt-support amd64 2.2.2-7 [64.3 kB]
Get:2 http://kali.download/kali kali-rolling/main amd64 fastjar amd64 2:0.98-7 [80.1 kB]
Get:3 http://kali.download/kali kali-rolling/main amd64 jarwrapper all 0.80 [9692 B]
Get:4 http://http.kali.org/kali kali-rolling/main amd64 neo4j all 5.2.0+really4.4.26-0kali1 [99.4 MB]
Fetched 99.6 MB in 32s (3103 kB/s)                                                                                           
Selecting previously unselected package binfmt-support.
(Reading database ... 510332 files and directories currently installed.)
Preparing to unpack .../binfmt-support_2.2.2-7_amd64.deb ...
Unpacking binfmt-support (2.2.2-7) ...
Selecting previously unselected package fastjar.
Preparing to unpack .../fastjar_2%3a0.98-7_amd64.deb ...
Unpacking fastjar (2:0.98-7) ...
Selecting previously unselected package jarwrapper.
Preparing to unpack .../jarwrapper_0.80_all.deb ...
Unpacking jarwrapper (0.80) ...
Selecting previously unselected package neo4j.
Preparing to unpack .../neo4j_5.2.0+really4.4.26-0kali1_all.deb ...
Unpacking neo4j (5.2.0+really4.4.26-0kali1) ...
Setting up fastjar (2:0.98-7) ...
Setting up binfmt-support (2.2.2-7) ...
update-binfmts: warning: llvm-17-runtime.binfmt already enabled in kernel.
update-binfmts: warning: llvm-19-runtime.binfmt already enabled in kernel.
update-binfmts: warning: llvm-14-runtime.binfmt already enabled in kernel.
update-binfmts: warning: python3.12 already enabled in kernel.
update-binfmts: warning: llvm-15-runtime.binfmt already enabled in kernel.
update-binfmts: warning: python3.13 already enabled in kernel.
update-binfmts: warning: llvm-16-runtime.binfmt already enabled in kernel.
Created symlink '/etc/systemd/system/multi-user.target.wants/binfmt-support.service' → '/usr/lib/systemd/system/binfmt-support.service'.
Setting up jarwrapper (0.80) ...
Setting up neo4j (5.2.0+really4.4.26-0kali1) ...
Processing triggers for man-db (2.13.0-1) ...
Processing triggers for kali-menu (2025.1.1) ...

┌──(kali㉿kali)-[~/ad-temp]
└─$ sudo neo4j console      
Directories in use:
home:         /usr/share/neo4j
config:       /usr/share/neo4j/conf
logs:         /etc/neo4j/logs
plugins:      /usr/share/neo4j/plugins
import:       /usr/share/neo4j/import
data:         /etc/neo4j/data
certificates: /usr/share/neo4j/certificates
licenses:     /usr/share/neo4j/licenses
run:          /var/lib/neo4j/run
Starting Neo4j.
2025-03-13 20:06:22.980+0000 INFO  Starting...
2025-03-13 20:06:23.724+0000 INFO  This instance is ServerId{65f88a1b} (65f88a1b-db42-4c06-a236-67ec95f9ed6a)
2025-03-13 20:06:24.967+0000 INFO  ======== Neo4j 4.4.26 ========
2025-03-13 20:06:30.338+0000 INFO  Initializing system graph model for component 'security-users' with version -1 and status UNINITIALIZED
2025-03-13 20:06:30.345+0000 INFO  Setting up initial user from defaults: neo4j
2025-03-13 20:06:30.345+0000 INFO  Creating new user 'neo4j' (passwordChangeRequired=true, suspended=false)
2025-03-13 20:06:30.404+0000 INFO  Setting version for 'security-users' to 3
2025-03-13 20:06:30.415+0000 INFO  After initialization of system graph model component 'security-users' have version 3 and status CURRENT
2025-03-13 20:06:30.427+0000 INFO  Performing postInitialization step for component 'security-users' with version 3 and status CURRENT
2025-03-13 20:06:33.686+0000 INFO  Bolt enabled on localhost:7687.
2025-03-13 20:06:34.841+0000 INFO  Remote interface available at http://localhost:7474/
2025-03-13 20:06:34.844+0000 INFO  id: F6F11E44891CA38104F6E51B8AE7ACDA66CF5E12832B5D97F343E7D2BE37048F
2025-03-13 20:06:34.845+0000 INFO  name: system
2025-03-13 20:06:34.845+0000 INFO  creationDate: 2025-03-13T20:06:27.355Z
2025-03-13 20:06:34.845+0000 INFO  Started.

```

Password set to: monster-chaos-mike-distant-action-9068
bloodhound: *:hi7hdka&~.$ZH

```sh
┌──(kali㉿kali)-[~/ad-temp]
└─$ bloodhound --no-sandbox
Command 'bloodhound' not found, but can be installed with:
sudo apt install bloodhound
Do you want to install it? (N/y)y
sudo apt install bloodhound
[sudo] password for kali: 
Installing:                     
  bloodhound

Summary:
  Upgrading: 0, Installing: 1, Removing: 0, Not Upgrading: 1267
  Download size: 69.3 MB
  Space needed: 274 MB / 1534 MB available

Get:1 http://kali.download/kali kali-rolling/main amd64 bloodhound amd64 4.3.1-0kali2 [69.3 MB]
Fetched 69.3 MB in 28s (2459 kB/s)                                                                                           
Selecting previously unselected package bloodhound.
(Reading database ... 510561 files and directories currently installed.)
Preparing to unpack .../bloodhound_4.3.1-0kali2_amd64.deb ...
Unpacking bloodhound (4.3.1-0kali2) ...
Setting up bloodhound (4.3.1-0kali2) ...
Processing triggers for kali-menu (2025.1.1) ...
```

