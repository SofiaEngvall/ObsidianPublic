
/var/lib/sss/db serves as the Linux equivalent of Windows DCC2 hashes (cached AD logons). It enables users to log in when the KDC or AD server is unreachable, as long as their credentials were previously cached during a successful login. This ensures offline authentication for AD-joined Linux systems.


