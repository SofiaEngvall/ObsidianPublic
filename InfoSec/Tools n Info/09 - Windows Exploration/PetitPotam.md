
start listener responder




Uses Encrypting File System Remote (EFSRPC) Protocol



Uses "Windows LSA Spoofing Vulnerability" CVE-2021-36942 (from Microsoft)

An unauthenticated attacker could call a method on the LSARPC interface and coerce the domain controller to authenticate against another server using NTLM. This security update blocks the affected API calls OpenEncryptedFileRawA and OpenEncryptedFileRawW through LSARPC interface.

Can be chained with the noted NTLM Relay Attacks on Active Directory Certificate Services (AD CS).


Full article https://pentestlab.blog/2021/09/14/petitpotam-ntlm-relay-to-ad-cs/