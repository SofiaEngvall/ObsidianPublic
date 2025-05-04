
I just need to make sure I can retrieve the article links from python. that is the text let ollama summarize and tts read, not just the text within the rss feed.

maybe you could run through and check some links within each rss feed? is that possible?

I run something similar to this but with much more details and safety checks
feed = feedparser.parse(rss_feed)
for entry in entries:
    response = requests.get(entry.link, headers=headers, allow_redirects=True)
    summary = Document(response.content.decode('utf-8').summary()
    ...

---

I already have fallbacks in my code using summary, description.. and also an option to open the link if all else fails

adding support for other types of data like pdf would be something that we possible could add later but for not we would just add pdf content to the status if several links have that format. I also ended up on a github issue page, which readability-lxml's Document could not handle and some web pages where a side description was returned instead of the main article. I think that we might make special case exceptions in some cases later but for now, as long as not all articles from a site get problems but just a few, it's quite ok. but to add to the status string and fix later if possible is the plan.

but please list as much useable information as possible in the status fleld

even though I mainly want the link and to test it for access and format problems, please also test other useful fields for useable contents

we will not add content type for now

---

Please incorporate the updated status fields into the previous list (headers and order). Don't sort according to how well they work.
Please give me the full list.
Thank you! <3

```python
rss_feeds = [
    # =====================
    # 🚨 Time-Critical Alerts
    # =====================
    ("CISA Alerts", "Government vulnerability alerts", "alerts", "https://www.cisa.gov/news-events/cybersecurity-advisories/rss.xml", "https://www.cisa.gov", "ok | link=direct | content=full_html | desc=partial", 10),
    ("Krebs on Security", "Investigative security journalism", "alerts", "https://krebsonsecurity.com/feed/", "https://krebsonsecurity.com", "ok | link=direct | content=full_html | desc=partial", 10),
    ("SANS Internet Storm Center", "Daily threat intelligence", "alerts", "https://isc.sans.edu/rssfeed_full.xml", "https://isc.sans.edu", "ok | link=direct | content=rss_only | desc=full", 9),
    ("The Hacker News", "Breaking cybersecurity news", "alerts", "https://feeds.feedburner.com/TheHackersNews?format=xml", "https://thehackernews.com", "ok | link=redirects | content=full_html | desc=partial", 9),
    ("Dark Reading", "Urgent security news", "alerts", "https://www.darkreading.com/rss.xml", "https://www.darkreading.com", "ok | link=direct | content=full_html | desc=partial", 9),
    ("BleepingComputer", "Ransomware tracking", "alerts", "https://www.bleepingcomputer.com/feed/", "https://www.bleepingcomputer.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("Threatpost", "Vulnerability disclosures", "alerts", "https://threatpost.com/feed/", "https://threatpost.com", "ok | link=direct | content=full_html | desc=partial", 8),
    ("CyberScoop", "Policy and breach alerts", "alerts", "https://www.cyberscoop.com/feed/", "https://www.cyberscoop.com", "ok | link=direct | content=full_html | desc=partial", 7),
    ("NCSC News", "UK National Cyber Security Centre alerts", "alerts", "https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml", "https://www.ncsc.gov.uk/news", "need_java | link=direct | content=js_required | desc=full", 5),

    # =====================
    # 🔥 Advanced Threat Intel
    # =====================
    ("Citizen Lab", "Spyware and disinformation research", "threat_intel", "https://citizenlab.ca/feed/", "https://citizenlab.ca", "ok | link=direct | content=full_html | desc=full", 10),
    ("Project Zero", "Zero-day vulnerability research", "threat_intel", "http://googleprojectzero.blogspot.com/feeds/posts/default", "https://googleprojectzero.blogspot.com", "ok | link=direct | content=full_html | desc=full", 10),
    ("Mandiant Blog", "APT group analysis", "threat_intel", "https://www.mandiant.com/resources/blog/rss.xml", "https://www.mandiant.com/resources/blog", "ok | link=direct | content=full_html | desc=full", 9),
    ("Talos Intel", "Threat reports from Cisco", "threat_intel", "https://blog.talosintelligence.com/feeds/posts/default", "https://blog.talosintelligence.com", "ok | link=direct | content=full_html | desc=full", 9),
    ("Kaspersky Securelist", "Malware deep dives", "threat_intel", "https://securelist.com/feed/", "https://securelist.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("Unit42 (Palo Alto)", "Threat intelligence", "threat_intel", "https://unit42.paloaltonetworks.com/feed/", "https://unit42.paloaltonetworks.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("WeLiveSecurity", "Malware trends from ESET", "threat_intel", "https://feeds.feedburner.com/eset/blog", "https://www.welivesecurity.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("FireEye Threat Research", "APT analysis", "threat_intel", "https://www.fireeye.com/blog/threat-research/_jcr_content.feed", "https://www.fireeye.com/blog/threat-research", "ok | link=direct | content=full_html | desc=full", 8),
    ("Check Point Research", "Emerging threats", "threat_intel", "https://research.checkpoint.com/feed/", "https://research.checkpoint.com/", "ok | link=direct | content=full_html | desc=full", 8),
    ("Recorded Future", "Threat intelligence platform", "threat_intel", "https://www.recordedfuture.com/feed", "https://www.recordedfuture.com", "ok | link=direct | content=full_html | desc=partial", 7),
    ("PT SWARM", "APT research", "threat_intel", "https://swarm.ptsecurity.com/feed/", "https://swarm.ptsecurity.com", "ok | link=direct | content=full_html | desc=full", 7),
    ("Keen Security Lab (Tencent)", "Advanced vulnerability research", "threat_intel", "https://little-canada.org/feeds/output/tencent-keenlabs.rss", "https://keenlab.tencent.com/en/", "ok | link=direct | content=full_html | desc=full", 7),

    # =====================
    # 🛠️ Exploit Development
    # =====================
    ("PortSwigger Research", "Web application exploits", "exploit_dev", "https://portswigger.net/research/rss", "https://portswigger.net/research", "ok | link=direct | content=full_html | desc=full", 9),
    ("Project Zero Bug Tracker", "Zero-day exploit database", "exploit_dev", "https://little-canada.org/feeds/output/projectzero-bugs.rss", "https://bugs.chromium.org/p/project-zero", "ok | link=direct | content=full_html | desc=none", 9),
    ("STÖK's Blog", "Bug bounty techniques", "exploit_dev", "https://stokfredrik.com/rss.xml", "https://stokfredrik.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("Diary of a Reverse-Engineer", "Reverse engineering techniques", "exploit_dev", "https://doar-e.github.io/feeds/rss.xml", "https://doar-e.github.io/", "ok | link=direct | content=full_html | desc=full", 8),
    ("GRIMM Blog", "Exploit development", "exploit_dev", "https://blog.grimm-co.com/feeds/posts/default", "https://blog.grimm-co.com/", "ok | link=direct | content=full_html | desc=full", 8),
    ("Hexacorn", "Malware analysis tricks", "exploit_dev", "https://www.hexacorn.com/blog/feed/", "https://www.hexacorn.com", "ok | link=direct | content=full_html | desc=full", 7),
    ("Doyensec's Blog", "Application security", "exploit_dev", "https://blog.doyensec.com/atom.xml", "https://blog.doyensec.com/", "ok | link=direct | content=full_html | desc=full", 7),
    ("Access Vector", "Vulnerability research", "exploit_dev", "https://accessvector.net/rss.xml", "https://accessvector.net/", "ok | link=direct | content=full_html | desc=full", 7),
    ("RET2 Systems Blog", "Exploit development", "exploit_dev", "https://blog.ret2.io/feed.xml", "https://blog.ret2.io/", "ok | link=direct | content=full_html | desc=full", 7),
    ("Gamozo Labs Blog", "Low-level exploitation", "exploit_dev", "https://gamozolabs.github.io/feed.xml", "https://gamozolabs.github.io/", "ok | link=direct | content=full_html | desc=full", 7),

    # =====================
    # 🔴 Red Team & Offensive
    # =====================
    ("SpecterOps Blog", "Active Directory security", "red_team", "https://posts.specterops.io/feed", "https://posts.specterops.io", "ok | link=direct | content=full_html | desc=full", 9),
    ("MDSec ActiveBreach", "Red team tradecraft", "red_team", "https://www.mdsec.co.uk/feed/", "https://www.mdsec.co.uk", "ok | link=direct | content=full_html | desc=full", 9),
    ("Rasta Mouse's Blog", "C2 framework development", "red_team", "https://rastamouse.me/rss.xml", "https://rastamouse.me", "ok | link=direct | content=full_html | desc=full", 8),
    ("Airbus CERT Blog", "ICS/OT security", "red_team", "https://blog.airbus-cyber-security.com/rss/", "https://blog.airbus-cyber-security.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("Synacktiv | Publications", "Advanced exploitation", "red_team", "https://little-canada.org/feeds/output/synacktiv-publications.rss", "https://www.synacktiv.com/en/publications", "ok | link=direct | content=full_html | desc=full", 8),
    ("Rhino Security Labs", "Cloud red teaming", "red_team", "https://rhinosecuritylabs.com/feed/", "https://rhinosecuritylabs.com/", "ok | link=direct | content=full_html | desc=full", 7),
    ("Elttam", "Red team research", "red_team", "https://little-canada.org/feeds/output/elttam.rss", "https://www.elttam.com/blog/", "ok | link=direct | content=full_html | desc=full", 7),

    # =====================
    # 📰 General News
    # =====================
    ("Schneier on Security", "Security policy analysis", "news", "https://www.schneier.com/feed/atom/", "https://www.schneier.com", "ok | link=direct | content=full_html | desc=partial", 9),
    ("Risky Business Podcast", "Weekly news roundup", "news", "https://risky.biz/feeds/risky-business/", "https://risky.biz", "ok | link=audio | content=episode_page | desc=full", 9),
    ("SecurityWeek", "Enterprise security news", "news", "https://www.securityweek.com/rss", "https://www.securityweek.com", "ok | link=direct | content=full_html | desc=partial", 7),
    ("CSO Online", "Enterprise security", "news", "https://www.csoonline.com/index.rss", "https://www.csoonline.com", "ok | link=direct | content=full_html | desc=partial", 7),
    ("ZDNet Security", "Technology security news", "news", "https://www.zdnet.com/topic/security/rss.xml", "https://www.zdnet.com/security/", "ok | link=direct | content=full_html | desc=partial", 7),
    ("Infosecurity Magazine", "Cybersecurity news", "news", "https://www.infosecurity-magazine.com/rss/news/", "https://www.infosecurity-magazine.com", "ok | link=direct | content=full_html | desc=partial", 7),
    ("Help Net Security", "Security news", "news", "https://www.helpnetsecurity.com/feed/", "https://www.helpnetsecurity.com", "ok | link=direct | content=full_html | desc=partial", 7),
    ("SC Magazine", "Security news", "news", "https://www.scmagazine.com/home/feed/", "https://www.scmagazine.com", "warn | link=paywall | content=truncated | desc=partial", 4),

    # =====================
    # 🎙️ Podcasts
    # =====================
    ("Security Now (TWIT)", "Deep-dive security podcast", "podcast", "https://feeds.twit.tv/sn.xml", "https://twit.tv/shows/security-now", "ok | link=audio | content=episode_page | desc=full", 8),
    ("Darknet Diaries", "True cybercrime stories", "podcast", "https://feeds.megaphone.fm/darknetdiaries", "https://darknetdiaries.com", "ok | link=audio | content=episode_page | desc=full", 9),
    ("Graham Cluley", "Security podcast", "podcast", "https://grahamcluley.com/feed/", "https://grahamcluley.com", "ok | link=direct | content=full_html | desc=full", 7),

    # =====================
    # 🧠 Deep Dives & Education
    # =====================
    ("The DFIR Report", "Incident response case studies", "education", "https://thedfirreport.com/feed/", "https://thedfirreport.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("SANS Digital Forensics", "Forensics techniques", "education", "https://digital-forensics.sans.org/blog/rss.xml", "https://digital-forensics.sans.org", "ok | link=direct | content=full_html | desc=full", 7),
    ("Lenny Zeltser's Blog", "Malware analysis guides", "education", "https://zeltser.com/feed/", "https://zeltser.com", "ok | link=direct | content=full_html | desc=full", 7),
    ("NCC Group Research", "Technical whitepapers", "education", "https://research.nccgroup.com/feed/", "https://research.nccgroup.com", "ok | link=direct | content=full_html | desc=full", 7),
    ("Windows Internals Blog", "OS security deep dives", "education", "https://windows-internals.com/feed/", "https://windows-internals.com", "ok | link=direct | content=full_html | desc=full", 7),
    ("Troy Hunt", "Security tutorials", "education", "https://www.troyhunt.com/rss/", "https://www.troyhunt.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("Trenchant", "Advanced research", "education", "http://little-canada.org/feeds/output/trenchant.rss", "https://trenchant.io/", "ok | link=direct | content=full_html | desc=full", 7)
]
```

```python
# Example: Skip paywalled content
if "link=paywall" in feed[5]:
    continue
```

