
```sh
┌──(fixit42㉿kali)-[~/Downloads/Logs]
└─$ /opt/analyzeMFT/analyzeMFT.py -f '$MFT' -o mft.csv
Python version: 3.13.9 (main, Oct 15 2025, 14:56:22) [GCC 15.2.0]
Current working directory: /home/fixit42/Downloads/Logs
sys.path (first 5): ['/opt/analyzeMFT/src', '/opt/analyzeMFT', '/usr/lib/python313.zip', '/usr/lib/python3.13', '/usr/lib/python3.13/lib-dynload']
Contents of current directory: ['Windows', '$MFT', 'Users', 'body.txt', 'ProgramData', '$LogFile', '$Extend', 'Program Files (x86)', '$Boot', '$Secure_$SDS']
2025-12-06 00:55:29 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=688, record_size=1024
2025-12-06 00:55:29 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 42: Attribute length 2228296 exceeds record size 1024
2025-12-06 00:55:29 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 42: Attribute length 131072 exceeds record size 1024
2025-12-06 00:55:29 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=608, record_size=1024
2025-12-06 00:55:29 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=656, record_size=1024
2025-12-06 00:55:29 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=552, record_size=1024
```

...

```
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20580: Attribute length 1397042757 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20580: Attribute length 503334216 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20580: Attribute length 3322282496 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20580: Attribute length 2147603678 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20580: Attribute length 33674099 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20581: Attribute length 983192 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20581: Attribute length 393216 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20581: Attribute length 1397042757 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20581: Attribute length 503334216 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20581: Attribute length 3322282496 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20581: Attribute length 2147603678 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20581: Attribute length 33674099 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20604: Attribute length 393368 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20604: Attribute length 393216 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20604: Attribute length 1397042757 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20604: Attribute length 503334216 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20604: Attribute length 3322282496 exceeds record size 1024
2025-12-06 00:55:31 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 20604: Attribute length 2147603678 exceeds record size 1024

```

...

```
2025-12-06 00:55:56 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=544, record_size=1024
2025-12-06 00:55:56 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=544, record_size=1024
2025-12-06 00:55:56 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=528, record_size=1024
2025-12-06 00:55:56 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=544, record_size=1024
2025-12-06 00:55:56 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=664, record_size=1024
2025-12-06 00:55:56 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=544, record_size=1024
2025-12-06 00:55:56 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 155061: Attribute length 131144 exceeds record size 1024
2025-12-06 00:55:56 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 155061: Attribute length 65536 exceeds record size 1024
2025-12-06 00:55:56 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 155062: Attribute length 131144 exceeds record size 1024
2025-12-06 00:55:56 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 155062: Attribute length 65536 exceeds record size 1024
2025-12-06 00:55:56 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 155064: Attribute length 131144 exceeds record size 1024
2025-12-06 00:55:56 - analyzeMFT.analyzer - ERROR - Attribute validation failed at record 155064: Attribute length 65536 exceeds record size 1024
2025-12-06 00:55:56 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=712, record_size=1024
2025-12-06 00:55:56 - analyzeMFT.validators - WARNING - Large attribute detected: type=144, length=616, record_size=1024
2025-12-06 00:56:00 - analyzeMFT.cli - WARNING - Analysis complete. Results written to /home/fixit42/Downloads/Logs/mft.csv
```

