
`/usr/local/bin/validate`

Ghidra disassembled code:
```c
int main(int argc,char **argv)
{
  char *pcVar1;
  char *s;
  
  if (argc < 2) {
    printf("usage %s <input>\n",*argv);
  }
  else {
    printf("validating input...");
    pcVar1 = validate(argv[1]);
    if (pcVar1 != (char *)0x0) {
      puts("passed.");
    }
  }
  return 0;
}
```

```c
char * validate(char *s)
{
  size_t sVar1;
  char buf [100];
  int i;
  
  i = 0;
  while( true ) {
    sVar1 = strlen(s);
    if (sVar1 <= (uint)i) {
      strcpy(buf,s);
      return buf;
    }
    if (s[i] == 'F') break;
    i = i + 1;
  }
  printf("failed: %x\n",(int)s[i]);
                    /* WARNING: Subroutine does not return */
  exit(1);
}
```

We can see that is the input string at any position contains an "F" then the loop will exit (meaning this is a bad char!).
If we reach the end of the string, going one character at a time, the full string will be copied using the vulnable strcpy() and the function returns.
The buffer we copy into is 100 characters.

I tested to send an argument with 120 characters and got a segmentation fault as expected. time for edb and python
