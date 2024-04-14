
cut -d " " -f1,3,6 access.log | nl | tail

cut -d '"' -f2 access.log | tail

nl access.log | tail

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f1,3,6 access.log | nl | tail
 49072	[2023/10/25:16:17:13] ocsp.globalsign.com:80 301
 49073	[2023/10/25:16:17:13] www.globalsign.com:443 200
 49074	[2023/10/25:16:17:13] www.globalsign.com:443 302
 49075	[2023/10/25:16:17:13] www.globalsign.com:443 301
 49076	[2023/10/25:16:17:13] www.globalsign.com:443 200
 49077	[2023/10/25:16:17:13] passwordreset.microsoftonline.com:443 200
 49078	[2023/10/25:16:17:13] passwordreset.microsoftonline.com:443 200
 49079	[2023/10/25:16:17:14] ocsp.digicert.com:80 200
 49080	[2023/10/25:16:17:14] storage.live.com:443 200
 49081	[2023/10/25:16:17:14] storage.live.com:443 400
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d '"' -f2 access.log | tail
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
-
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
-
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
-
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
ubuntu@tryhackme:~/Desktop/artefacts$ nl access.log | tail
 49072	[2023/10/25:16:17:13] 10.10.140.96 ocsp.globalsign.com:80 GET / 301 640 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
 49073	[2023/10/25:16:17:13] 10.10.140.96 www.globalsign.com:443 CONNECT - 200 0 "-"
 49074	[2023/10/25:16:17:13] 10.10.140.96 www.globalsign.com:443 GET / 302 730 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
 49075	[2023/10/25:16:17:13] 10.10.140.96 www.globalsign.com:443 GET /en/ 301 868 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
 49076	[2023/10/25:16:17:13] 10.10.140.96 www.globalsign.com:443 GET /en 200 15003 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
 49077	[2023/10/25:16:17:13] 10.10.75.132 passwordreset.microsoftonline.com:443 CONNECT - 200 0 "-"
 49078	[2023/10/25:16:17:13] 10.10.75.132 passwordreset.microsoftonline.com:443 GET / 200 53070 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
 49079	[2023/10/25:16:17:14] 10.10.140.96 ocsp.digicert.com:80 GET / 200 913 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
 49080	[2023/10/25:16:17:14] 10.10.140.96 storage.live.com:443 CONNECT - 200 0 "-"
 49081	[2023/10/25:16:17:14] 10.10.140.96 storage.live.com:443 GET / 400 630 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
ubuntu@tryhackme:~/Desktop/artefacts$ grep 10.10.140.96 | cut -d " " -f1,3,6 access.log | head -n 5
[2023/10/25:15:42:02] sway.com:443 200
[2023/10/25:15:42:02] sway.com:443 301
[2023/10/25:15:42:02] sway.office.com:443 200
[2023/10/25:15:42:02] sway.office.com:443 200
[2023/10/25:15:42:02] protection.office.com:443 200
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f3 access.log | cut -d ":" -f1 | sort | uniq | tail
www.google.com
www.microsoft365.com
www.msn.com
www.office.com
www.onenote.com
www.skype.com
www.sway.com
www.verisign.com
www.yammer.com
yammer.com
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f3 access.log | cut -d ":" -f1 | sort | uniq | wc -l
111
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f3 access.log | cut -d ":" -f1 | sort | uniq -c
    423 account.activedirectory.windowsazure.com
    184 activity.windows.com
    680 admin.microsoft.com
    272 admin.onedrive.com
    304 adminwebservice.microsoftonline.com
    300 ajax.aspnetcdn.com
    282 api.passwordreset.microsoftonline.com
    316 appex.bing.com
    288 appsforoffice.microsoft.com
    272 autologon.microsoftazuread-sso.com
    274 becws.microsoftonline.com
    850 c.bing.com
    327 c.live.com
    456 c1.microsoft.com
    278 cacerts.digicert.com
    258 ccs.login.microsoftonline.com
    292 cdn.odc.officeapps.live.com
    240 cdn.uci.officeapps.live.com
    266 companymanager.microsoftonline.com
    306 compass-ssl.microsoft.com
    256 compliance.microsoft.com
    304 crl.globalsign.com
    308 dc.services.visualstudio.com
    300 defender.microsoft.com
    390 developer.microsoft.com
    232 device.login.microsoftonline.com
    274 dgps.support.microsoft.com
    606 docs.microsoft.com
    260 eus-www.sway-cdn.com
    306 eus-www.sway-extensions.com
    572 flow.microsoft.com
   1581 frostlings.bigbadstash.thm
    268 g.live.com
    265 geotrust.com
    462 github.com
    131 google.com
    260 graph.microsoft.com
   1554 learn.microsoft.com
    286 login-us.microsoftonline.com
    484 login.live.com
    300 login.microsoft.com
    278 login.microsoftonline-p.com
   4695 login.microsoftonline.com
    262 logincert.microsoftonline.com
    250 loginex.microsoftonline.com
    572 make.powerautomate.com
    113 mcgreedysecretc2.thm
    244 mscrl.microsoft.com
    310 msdn.microsoft.com
    238 nexus.microsoftonline-p.com
    278 o15.officeredir.microsoft.com
    118 ocsp.digicert.com
    141 ocsp.globalsign.com
    147 ocsp.msocsp.com
    134 ocsp2.globalsign.com
    128 ocspx.digicert.com
    316 office.com
    381 office.live.com
    274 office15client.microsoft.com
    238 officeapps.live.com
    270 officecdn.microsoft.com
    123 officeclient.microsoft.com
    276 officepreviewredir.microsoft.com
    242 officeredir.microsoft.com
    228 officespeech.platform.bing.com
    262 onenote.com
    520 outlook.office.com
    878 outlook.office365.com
     78 partnerservices.getmicrosoftkey.com
    290 passwordreset.microsoftonline.com
    288 platform.linkedin.com
    278 portal.cloudappsecurity.com
    264 powerapps.com
    396 powerapps.microsoft.com
    292 powerautomate.com
    333 prod.msocdn.com
    286 protection.office.com
    290 provisioningapi.microsoftonline.com
    266 r.office.microsoft.com
    284 secure.globalsign.com
    576 security.microsoft.com
    148 shellprod.msocdn.com
    390 signup.live.com
    282 skype.com
    622 smtp.office365.com
    282 ssw.live.com
    402 stackoverflow.com
    318 storage.live.com
    492 support.microsoft.com
    580 sway.com
    580 sway.office.com
    300 teams.microsoft.com
    220 technet.microsoft.com
    290 verisign.com
    306 wus-www.sway-cdn.com
    260 wus-www.sway-extensions.com
    300 www.asp.net
    578 www.bing.com
    302 www.digicert.com
    264 www.geotrust.com
   1860 www.globalsign.com
    393 www.google.com
    284 www.microsoft365.com
    536 www.msn.com
   4992 www.office.com
    393 www.onenote.com
    423 www.skype.com
    322 www.sway.com
    290 www.verisign.com
    284 www.yammer.com
    284 yammer.com
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ grep frostlings.bigbadstash.thm access.log | head -n 5
[2023/10/25:15:56:29] 10.10.185.225 frostlings.bigbadstash.thm:80 GET /storage.php?goodies=aWQscmVjaXBpZW50LGdp 200 362 "Go-http-client/1.1"
[2023/10/25:15:56:29] 10.10.185.225 frostlings.bigbadstash.thm:80 GET /storage.php?goodies=ZnQKZGRiZTlmMDI1OGE4 200 362 "Go-http-client/1.1"
[2023/10/25:15:56:29] 10.10.185.225 frostlings.bigbadstash.thm:80 GET /storage.php?goodies=MDRjOGExNWNmNTI0ZTMy 200 362 "Go-http-client/1.1"
[2023/10/25:15:56:30] 10.10.185.225 frostlings.bigbadstash.thm:80 GET /storage.php?goodies=ZTE3ODUsTm9haCxQbGF5 200 362 "Go-http-client/1.1"
[2023/10/25:15:56:30] 10.10.185.225 frostlings.bigbadstash.thm:80 GET /storage.php?goodies=IENhc2ggUmVnaXN0ZXIK 200 362 "Go-http-client/1.1"
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ grep frostlings.bigbadstash.thm access.log | cut -d ' ' -f5 | cut -d '=' -f2 | head -n 5
aWQscmVjaXBpZW50LGdp
ZnQKZGRiZTlmMDI1OGE4
MDRjOGExNWNmNTI0ZTMy
ZTE3ODUsTm9haCxQbGF5
IENhc2ggUmVnaXN0ZXIK
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ grep frostlings.bigbadstash.thm access.log | cut -d ' ' -f5 | cut -d '=' -f2 | base64 -d | head -n 5
id,recipient,gift
ddbe9f0258a804c8a15cf524e32e1785,Noah,Play Cash Register
cb597d69d83f24c75b2a2d7298705ed7,William,Toy Pirate Hat
4824fb68fe63146aabc3587f8e12fb90,Charlotte,Play-Doh Bakery Set
f619a90e1fdedc23e515c7d6804a0811,Benjamin,Soccer Ball
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f2 access.log | sort | uniq -c       
   5711 10.10.116.67
   4974 10.10.120.75
   5495 10.10.132.238
   5750 10.10.140.96
   5564 10.10.161.168
   4994 10.10.185.225
   5802 10.10.46.50
   5140 10.10.75.132
   5651 10.10.89.232
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f2 access.log | sort | uniq | wc -l  
9
```

unique domains:
```sh
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f3 access.log | cut -d ":" -f1 | sort | uniq -c | wc -l
111
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ grep frostlings.bigbadstash.thm access.log | cut -d ' ' -f5 | cut -d '=' -f2 | wc -l    
1581
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ grep frostlings.bigbadstash.thm access.log | cut -d ' ' -f5 | cut -d '=' -f2 | base64 -d | grep THM
72703959c91cb18edbefedc692c45204,SOC Analyst,THM{a_gift_for_you_awesome_analyst!}
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f3 access.log | cut -d ":" -f1 | sort | uniq -c | sort | head -5
     78 partnerservices.getmicrosoftkey.com
    113 mcgreedysecretc2.thm
    118 ocsp.digicert.com
    123 officeclient.microsoft.com
    128 ocspx.digicert.com
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ grep partnerservices.getmicrosoftkey.com access.log | cut -d ' ' -f6 | sort | uniq
503
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f3 access.log | cut -d ":" -f1 | sort | uniq -c | sort | head -1 | xargs | cut -d ' ' -f 2 | xargs -I {} grep {} access.log | cut -d ' ' -f6 | sort | uniq
503
```

```sh
ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f3 access.log | cut -d ":" -f1 | sort | uniq -c | sort | head -5 | tr -s '[:blank:]' | cut -d ' ' -f 3
partnerservices.getmicrosoftkey.com
mcgreedysecretc2.thm
ocsp.digicert.com
officeclient.microsoft.com
ocspx.digicert.com

ubuntu@tryhackme:~/Desktop/artefacts$ cut -d " " -f3 access.log | cut -d ":" -f1 | sort | uniq -c | sort | head -5 | tr -s '[:blank:]' | cut -d ' ' -f 3 | xargs -I {} grep {} access.log | cut -d ' ' -f6 | sort | uniq
200
404
503

```