
## What is Buffer Overflow?

Buffer overflow is when vulnerable code allows us to write over a bigger section of memory than it should.
The C functions gets(), strcopy(), sprintf, scanf and strcat() are examples of functions that doesn't check the available space before writing.

Example
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int variable = 0;
  char buffer[14];

  gets(buffer);

  if(variable != 0) {
      printf("You have changed the value of the variable\n");
  } else {
      printf("Try again?\n");
  }
}
```
<font size=2>We have to do 15 chars though 14 actually overwrites the int variable but with the string terminating null, meaning the value doesn't change and we'd get "Try again?".</font>


#### Tips to check out
Al tips:
"Hacking: The Art of Exploitation" book to check out
tool bofuzz


#### Real world buffer overflow examples:
https://www.bleepingcomputer.com/news/security/you-can-bypass-authentication-on-hpe-ilo4-servers-with-29-a-characters/
https://blog.qualys.com/vulnerabilities-threat-research/2021/01/26/cve-2021-3156-heap-based-buffer-overflow-in-sudo-baron-samedit

