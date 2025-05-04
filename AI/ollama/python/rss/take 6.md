
Thank you!

I love security now, but it's a podcast. I'm curious on what the feed could contain. I guess I'll look :)

I believe you might have made a mistake in the code though, looking for "EXPLOIT DEVELOPMENT" in the fees when it's in the comment. do you think we should add another field for the cathegory? In that cane, not in all upper case :)

```python
rss_feeds = [
    # =====================
    # 🚨 Time-Critical Alerts
    # =====================
    ("CISA Alerts", "Government vulnerability alerts", "alerts", "https://www.cisa.gov/news-events/cybersecurity-advisories/rss.xml", "https://www.cisa.gov", "active", 10),
    ("Krebs on Security", "Investigative security journalism", "alerts", "https://krebsonsecurity.com/feed/", "https://krebsonsecurity.com", "ok", 10),
    ("SANS Internet Storm Center", "Daily threat intelligence", "alerts", "https://isc.sans.edu/rssfeed_full.xml", "https://isc.sans.edu", "ok", 9),
    ("The Hacker News", "Breaking cybersecurity news", "alerts", "https://feeds.feedburner.com/TheHackersNews?format=xml", "https://thehackernews.com", "ok", 9),
    ("Dark Reading", "Urgent security news", "alerts", "https://www.darkreading.com/rss.xml", "https://www.darkreading.com", "unknown", 9),
    ("BleepingComputer", "Ransomware tracking", "alerts", "https://www.bleepingcomputer.com/feed/", "https://www.bleepingcomputer.com", "active", 8),
    ("Threatpost", "Vulnerability disclosures", "alerts", "https://threatpost.com/feed/", "https://threatpost.com", "unknown", 8),
    ("CyberScoop", "Policy and breach alerts", "alerts", "https://www.cyberscoop.com/feed/", "https://www.cyberscoop.com", "unknown", 7),
    ("NCSC News", "UK National Cyber Security Centre alerts", "alerts", "https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml", "https://www.ncsc.gov.uk/news", "need java", 5),

    # =====================
    # 🔥 Advanced Threat Intel
    # =====================
    ("Citizen Lab", "Spyware and disinformation research", "threat_intel", "https://citizenlab.ca/feed/", "https://citizenlab.ca", "active", 10),
    ("Project Zero", "Zero-day vulnerability research", "threat_intel", "http://googleprojectzero.blogspot.com/feeds/posts/default", "https://googleprojectzero.blogspot.com", "unknown", 10),
    ("Mandiant Blog", "APT group analysis", "threat_intel", "https://www.mandiant.com/resources/blog/rss.xml", "https://www.mandiant.com/resources/blog", "active", 9),
    ("Talos Intel", "Threat reports from Cisco", "threat_intel", "https://blog.talosintelligence.com/feeds/posts/default", "https://blog.talosintelligence.com", "unknown", 9),
    ("Kaspersky Securelist", "Malware deep dives", "threat_intel", "https://securelist.com/feed/", "https://securelist.com", "ok", 8),
    ("Unit42 (Palo Alto)", "Threat intelligence", "threat_intel", "https://unit42.paloaltonetworks.com/feed/", "https://unit42.paloaltonetworks.com", "unknown", 8),
    ("WeLiveSecurity", "Malware trends from ESET", "threat_intel", "https://feeds.feedburner.com/eset/blog", "https://www.welivesecurity.com", "ok", 8),
    ("FireEye Threat Research", "APT analysis", "threat_intel", "https://www.fireeye.com/blog/threat-research/_jcr_content.feed", "https://www.fireeye.com/blog/threat-research", "unknown", 8),
    ("Check Point Research", "Emerging threats", "threat_intel", "https://research.checkpoint.com/feed/", "https://research.checkpoint.com/", "unknown", 8),
    ("Recorded Future", "Threat intelligence platform", "threat_intel", "https://www.recordedfuture.com/feed", "https://www.recordedfuture.com", "unknown", 7),
    ("PT SWARM", "APT research", "threat_intel", "https://swarm.ptsecurity.com/feed/", "https://swarm.ptsecurity.com", "unknown", 7),
    ("Keen Security Lab (Tencent)", "Advanced vulnerability research", "threat_intel", "https://little-canada.org/feeds/output/tencent-keenlabs.rss", "https://keenlab.tencent.com/en/", "unknown", 7),

    # =====================
    # 🛠️ Exploit Development
    # =====================
    ("PortSwigger Research", "Web application exploits", "exploit_dev", "https://portswigger.net/research/rss", "https://portswigger.net/research", "unknown", 9),
    ("Project Zero Bug Tracker", "Zero-day exploit database", "exploit_dev", "https://little-canada.org/feeds/output/projectzero-bugs.rss", "https://bugs.chromium.org/p/project-zero", "unknown", 9),
    ("STÖK's Blog", "Bug bounty techniques", "exploit_dev", "https://stokfredrik.com/rss.xml", "https://stokfredrik.com", "active", 8),
    ("Diary of a Reverse-Engineer", "Reverse engineering techniques", "exploit_dev", "https://doar-e.github.io/feeds/rss.xml", "https://doar-e.github.io/", "unknown", 8),
    ("GRIMM Blog", "Exploit development", "exploit_dev", "https://blog.grimm-co.com/feeds/posts/default", "https://blog.grimm-co.com/", "unknown", 8),
    ("Hexacorn", "Malware analysis tricks", "exploit_dev", "https://www.hexacorn.com/blog/feed/", "https://www.hexacorn.com", "active", 7),
    ("Doyensec's Blog", "Application security", "exploit_dev", "https://blog.doyensec.com/atom.xml", "https://blog.doyensec.com/", "unknown", 7),
    ("Access Vector", "Vulnerability research", "exploit_dev", "https://accessvector.net/rss.xml", "https://accessvector.net/", "unknown", 7),
    ("RET2 Systems Blog", "Exploit development", "exploit_dev", "https://blog.ret2.io/feed.xml", "https://blog.ret2.io/", "unknown", 7),
    ("Gamozo Labs Blog", "Low-level exploitation", "exploit_dev", "https://gamozolabs.github.io/feed.xml", "https://gamozolabs.github.io/", "unknown", 7),

    # =====================
    # 🔴 Red Team & Offensive
    # =====================
    ("SpecterOps Blog", "Active Directory security", "red_team", "https://posts.specterops.io/feed", "https://posts.specterops.io", "active", 9),
    ("MDSec ActiveBreach", "Red team tradecraft", "red_team", "https://www.mdsec.co.uk/feed/", "https://www.mdsec.co.uk", "active", 9),
    ("Rasta Mouse's Blog", "C2 framework development", "red_team", "https://rastamouse.me/rss.xml", "https://rastamouse.me", "active", 8),
    ("Airbus CERT Blog", "ICS/OT security", "red_team", "https://blog.airbus-cyber-security.com/rss/", "https://blog.airbus-cyber-security.com", "active", 8),
    ("Synacktiv | Publications", "Advanced exploitation", "red_team", "https://little-canada.org/feeds/output/synacktiv-publications.rss", "https://www.synacktiv.com/en/publications", "unknown", 8),
    ("Rhino Security Labs", "Cloud red teaming", "red_team", "https://rhinosecuritylabs.com/feed/", "https://rhinosecuritylabs.com/", "unknown", 7),
    ("Elttam", "Red team research", "red_team", "https://little-canada.org/feeds/output/elttam.rss", "https://www.elttam.com/blog/", "unknown", 7),

    # =====================
    # 📰 General News
    # =====================
    ("Schneier on Security", "Security policy analysis", "news", "https://www.schneier.com/feed/atom/", "https://www.schneier.com", "ok", 9),
    ("Risky Business Podcast", "Weekly news roundup", "news", "https://risky.biz/feeds/risky-business/", "https://risky.biz", "active", 9),
    ("SecurityWeek", "Enterprise security news", "news", "https://www.securityweek.com/rss", "https://www.securityweek.com", "unknown", 7),
    ("CSO Online", "Enterprise security", "news", "https://www.csoonline.com/index.rss", "https://www.csoonline.com", "unknown", 7),
    ("ZDNet Security", "Technology security news", "news", "https://www.zdnet.com/topic/security/rss.xml", "https://www.zdnet.com/security/", "unknown", 7),
    ("Infosecurity Magazine", "Cybersecurity news", "news", "https://www.infosecurity-magazine.com/rss/news/", "https://www.infosecurity-magazine.com", "unknown", 7),
    ("Help Net Security", "Security news", "news", "https://www.helpnetsecurity.com/feed/", "https://www.helpnetsecurity.com", "unknown", 7),
    ("SC Magazine", "Security news", "news", "https://www.scmagazine.com/home/feed/", "https://www.scmagazine.com", "unknown", 6),

    # =====================
    # 🎙️ Podcasts
    # =====================
    ("Security Now (TWIT)", "Deep-dive security podcast", "podcast", "https://feeds.twit.tv/sn.xml", "https://twit.tv/shows/security-now", "active", 8),
    ("Darknet Diaries", "True cybercrime stories", "podcast", "https://feeds.megaphone.fm/darknetdiaries", "https://darknetdiaries.com", "ok", 9),
    ("Risky Business Podcast", "News and analysis", "podcast", "https://risky.biz/feeds/risky-business/", "https://risky.biz", "active", 9),
    ("Graham Cluley", "Security podcast", "podcast", "https://grahamcluley.com/feed/", "https://grahamcluley.com", "ok", 7),

    # =====================
    # 🧠 Deep Dives & Education
    # =====================
    ("The DFIR Report", "Incident response case studies", "education", "https://thedfirreport.com/feed/", "https://thedfirreport.com", "active", 8),
    ("SANS Digital Forensics", "Forensics techniques", "education", "https://digital-forensics.sans.org/blog/rss.xml", "https://digital-forensics.sans.org", "active", 7),
    ("Lenny Zeltser's Blog", "Malware analysis guides", "education", "https://zeltser.com/feed/", "https://zeltser.com", "active", 7),
    ("NCC Group Research", "Technical whitepapers", "education", "https://research.nccgroup.com/feed/", "https://research.nccgroup.com", "active", 7),
    ("Windows Internals Blog", "OS security deep dives", "education", "https://windows-internals.com/feed/", "https://windows-internals.com", "unknown", 7),
    ("Troy Hunt", "Security tutorials", "education", "https://www.troyhunt.com/rss/", "https://www.troyhunt.com", "ok", 8),
    ("Trenchant", "Advanced research", "education", "http://little-canada.org/feeds/output/trenchant.rss", "https://trenchant.io/", "unknown", 7)
]
```

Suggested code

```python
# Get all exploit development feeds:
exploit_feeds = [feed for feed in rss_feeds if feed[2] == "exploit_dev"]

# Get all 9+/10 feeds:
top_tier = [feed for feed in rss_feeds if feed[6] >= 9]
```
