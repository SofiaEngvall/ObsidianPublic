

https://github.com/p0dalirius/Coercer

make machine accounts (elevated privileges) authenticate to us

### Print Spooler service

### PetitPotam - NTLM relay attack

Exploits the Encrypting File System Remote Protocol (EFSRPC) EfsRpcOpenFileRaw method.
EFSRPC is used to remotely manage encrypted files and folders.

Trick a machine to to authenticate by making it think it needs to access a remote resource
`rpcclient -U "" --command="efsinfo` \\\\TARGET_IP\\share" TARGET_IP`
	`rpcclient` is a tool in the samba suite
	`-U ""` intentionally left blank to force anonymous authentication
	`--command="efsinfo` 
	
make windows servers auth to a relay
capture the NTLM auth and repay it to another service that accepts NTLM auth, as a DC

https://pentestlab.blog/2021/09/14/petitpotam-ntlm-relay-to-ad-cs/

### Windows lock screen


### Webclient

https://pentestlab.blog/2021/10/20/lateral-movement-webclient/
https://www.thehacker.recipes/ad/movement/mitm-and-coerced-authentications/webclient
