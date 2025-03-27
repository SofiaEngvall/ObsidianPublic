
The files:
```sh
[user1@ip-10-10-128-37 overflow-1]$ ls -la
total 16
drwxrwxr-x 2 user1 user1   48 Sep  2  2019 .
drwx------ 7 user1 user1  169 Nov 27  2019 ..
-rwxrwxr-x 1 user1 user1 8224 Sep  2  2019 int-overflow
-rw-rw-r-- 1 user1 user1  291 Sep  2  2019 int-overflow.c
```

The code:
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

Running it and getting buffer overflow:
```sh
[user1@ip-10-10-128-37 overflow-1]$ ./int-overflow 
1
Try again?

[user1@ip-10-10-128-37 overflow-1]$ ./int-overflow 
123456789012345
You have changed the value of the variable
```

We have to do 15 chars though 14 actually overwrites the int variable but with the string terminating null, meaning the value doesn't change and we'd get "Try again?".
