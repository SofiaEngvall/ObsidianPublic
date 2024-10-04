
```c
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  modified = 0;
  gets(buffer);

  if(modified != 0) {
      printf("you have changed the 'modified' variable\n");
  } else {
      printf("Try again?\n");
  }
}
```

This is the first test of buffer overflow. The gets function is unsafe since it doesn't check the buffer size but just puts whatever the user input is on the stack. This means we can overwrite the int variable by just typing a string longer than 63 characters (since a null will be added at the end as a terminator).

For example like this:
```sh
┌──(kali㉿kali)-[~/vulnhub/protostar-2/bin]
└─$ ./stack0
12345678901234567890123456789012345678901234567890123456789012345
you have changed the 'modified' variable
```

(Since the check is for 0 we won't get the assumed "modified" there as we overwrite the 0 with 0 (the null).)

