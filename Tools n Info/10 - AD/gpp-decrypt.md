
https://www.mindpointgroup.com/blog/privilege-escalation-via-group-policy-preferences-gpp

dumped group policy file
```xml
<Groups clsid="{3125E937-EB16-4b4c-9934-544FC6D24D26}">
<User clsid="{DF5F1855-51E5-4d24-8B1A-D9BDE98BA1D1}" name="ladmin_gpo" image="0" changed="2012-02-03 07:10:48" uid="{FE47E73C-7525-46CD-B2E0-F68D3022EDCE}">
<Properties action="C" fullName="Local admin created by GPO" description="" cpassword="9QHhFTUdm6rDgu30J7ShZfqt07T6vOUGkyAFG3G7M+5AotJjkOva7E9KSAcamdrruTgly0O/uVTB/UUdLNU4775b5381hyuUzkd4lJW+llcNNNrQlYu7zqH3/i+8jfjhUq9lqPn8VjCtb9iaEqWbKQ" changeLogon="0" noChange="0" neverExpires="0" acctDisabled="0" userName="ladmin_gpo"/>
</User>
<Group clsid="{6D4A79E4-529C-4481-ABD0-F5BD7EA93BA7}" name="Administrators (built-in)" image="2" changed="2012-02-06 10:45:50" uid="{4D0CE71D-D2E4-42B1-9BF3-147C910A15F1}">
<Properties action="U" newName="" description="" deleteAllUsers="0" userAction="ADD" deleteAllGroups="0" removeAccounts="0" groupSid="S-1-5-32-544" groupName="Administrators (built-in)">
<Members>
<Member name="ladmin_gpo" action="ADD" sid=""/>
</Members>
</Properties>
</Group>
</Groups>
```

we decrypt the cpassword
```sh
┌──(kali㉿kali)-[~/Downloads/_sleeping_monster.jpg.extracted/hide]
└─$ gpp-decrypt 9QHhFTUdm6rDgu30J7ShZfqt07T6vOUGkyAFG3G7M+5AotJjkOva7E9KSAcamdrruTgly0O/uVTB/UUdLNU4775b5381hyuUzkd4lJW+llcNNNrQlYu7zqH3/i+8jfjhUq9lqPn8VjCtb9iaEqWbKQ
Th1s-P@$$w0rd-ShOud-B3-SaFe_@cc0rding-to-XKCD.com!:-)
```

