
could you please re-evaluate the type for the feeds in the old list and then integrate both lists using headers as you have done here

the first header should be the one with the most time critical type, maybe alerts or hot news.
my script uses ollama to summarize the articles so article length is not a problem.
and then end with the least time sensitive ones like maybe teaching or detailed explanations.

under each header, order the feeds according to your grading

and return the results in the same python-compatible format please

Thanks a million! <3

```python
rss_feeds = [
    # =====================
    # 🚨 BREAKING ALERTS & TIME-CRITICAL NEWS
    # =====================
    ("CISA Alerts", "Gov Alerts", "https://www.cisa.gov/news-events/cybersecurity-advisories/rss.xml", "https://www.cisa.gov", "active", 10),
    ("Krebs on Security", "Breach Alerts", "https://krebsonsecurity.com/feed/", "https://krebsonsecurity.com", "ok", 10),
    ("SANS Internet Storm Center", "Threat Alerts", "https://isc.sans.edu/rssfeed_full.xml", "https://isc.sans.edu", "ok", 9),
    ("The Hacker News", "Breaking News", "https://feeds.feedburner.com/TheHackersNews?format=xml", "https://thehackernews.com", "ok", 9),
    ("Dark Reading", "Urgent News", "https://www.darkreading.com/rss.xml", "https://www.darkreading.com", "unknown", 9),
    ("BleepingComputer", "Ransomware Alerts", "https://www.bleepingcomputer.com/feed/", "https://www.bleepingcomputer.com", "active", 8),
    ("Threatpost", "Vulnerability Alerts", "https://threatpost.com/feed/", "https://threatpost.com", "unknown", 8),
    ("CyberScoop", "Policy Alerts", "https://www.cyberscoop.com/feed/", "https://www.cyberscoop.com", "unknown", 7),

    # =====================
    # 🔥 HOT THREAT INTELLIGENCE (APT/Malware)
    # =====================
    ("Citizen Lab", "Spyware Research", "https://citizenlab.ca/feed/", "https://citizenlab.ca", "active", 10),
    ("Project Zero", "Zero-Day Research", "http://googleprojectzero.blogspot.com/feeds/posts/default", "https://googleprojectzero.blogspot.com", "unknown", 10),
    ("Mandiant Blog", "APT Reports", "https://www.mandiant.com/resources/blog/rss.xml", "https://www.mandiant.com/resources/blog", "active", 9),
    ("Talos Intel", "Threat Reports", "https://blog.talosintelligence.com/feeds/posts/default", "https://blog.talosintelligence.com", "unknown", 9),
    ("Kaspersky Securelist", "Malware Analysis", "https://securelist.com/feed/", "https://securelist.com", "ok", 8),
    ("Unit42 (Palo Alto)", "Threat Intel", "https://unit42.paloaltonetworks.com/feed/", "https://unit42.paloaltonetworks.com", "unknown", 8),
    ("WeLiveSecurity", "Malware Trends", "https://feeds.feedburner.com/eset/blog", "https://www.welivesecurity.com", "ok", 8),
    ("FireEye Threat Research", "APT Analysis", "https://www.fireeye.com/blog/threat-research/_jcr_content.feed", "https://www.fireeye.com/blog/threat-research", "unknown", 8),
    ("Check Point Research", "Threat Intel", "https://research.checkpoint.com/feed/", "https://research.checkpoint.com/", "unknown", 8),

    # =====================
    # 🛠️ TOOLS & EXPLOIT DEVELOPMENT
    # =====================
    ("PortSwigger Research", "Web Exploits", "https://portswigger.net/research/rss", "https://portswigger.net/research", "unknown", 9),
    ("Project Zero Bug Tracker", "Exploit DB", "https://little-canada.org/feeds/output/projectzero-bugs.rss", "https://bugs.chromium.org/p/project-zero", "unknown", 9),
    ("STÖK's Blog", "Bug Bounty Tech", "https://stokfredrik.com/rss.xml", "https://stokfredrik.com", "active", 8),
    ("Diary of a Reverse-Engineer", "RE Techniques", "https://doar-e.github.io/feeds/rss.xml", "https://doar-e.github.io/", "unknown", 8),
    ("GRIMM Blog", "Exploit Dev", "https://blog.grimm-co.com/feeds/posts/default", "https://blog.grimm-co.com/", "unknown", 8),
    ("Hexacorn", "Malware Tricks", "https://www.hexacorn.com/blog/feed/", "https://www.hexacorn.com", "active", 7),

    # =====================
    # 🔴 RED TEAM & OFFENSIVE SECURITY
    # =====================
    ("SpecterOps Blog", "AD Security", "https://posts.specterops.io/feed", "https://posts.specterops.io", "active", 9),
    ("MDSec ActiveBreach", "Red Team", "https://www.mdsec.co.uk/feed/", "https://www.mdsec.co.uk", "active", 9),
    ("Rasta Mouse's Blog", "C2 Frameworks", "https://rastamouse.me/rss.xml", "https://rastamouse.me", "active", 8),
    ("Airbus CERT Blog", "ICS Attacks", "https://blog.airbus-cyber-security.com/rss/", "https://blog.airbus-cyber-security.com", "active", 8),

    # =====================
    # 📰 GENERAL NEWS & ANALYSIS
    # =====================
    ("Schneier on Security", "Security Policy", "https://www.schneier.com/feed/atom/", "https://www.schneier.com", "ok", 9),
    ("Risky Business Podcast", "News Roundup", "https://risky.biz/feeds/risky-business/", "https://risky.biz", "active", 9),
    ("SecurityWeek", "Enterprise News", "https://www.securityweek.com/rss", "https://www.securityweek.com", "unknown", 7),
    ("CSO Online", "Enterprise Security", "https://www.csoonline.com/index.rss", "https://www.csoonline.com", "unknown", 7),
    ("ZDNet Security", "Tech News", "https://www.zdnet.com/topic/security/rss.xml", "https://www.zdnet.com/security/", "unknown", 7),

    # =====================
    # 🧠 DEEP DIVES & EDUCATION
    # =====================
    ("The DFIR Report", "Incident Case Studies", "https://thedfirreport.com/feed/", "https://thedfirreport.com", "active", 8),
    ("SANS Digital Forensics", "Forensics", "https://digital-forensics.sans.org/blog/rss.xml", "https://digital-forensics.sans.org", "active", 7),
    ("Lenny Zeltser's Blog", "Malware Analysis", "https://zeltser.com/feed/", "https://zeltser.com", "active", 7),
    ("NCC Group Research", "Technical Papers", "https://research.nccgroup.com/feed/", "https://research.nccgroup.com", "active", 7),
    ("Google Security Research", "Advisories", "https://little-canada.org/feeds/output/google-research-advisories.rss", "https://github.com/google/security-research", "unknown", 7)
]
```

suggested code:
```python
# Get all 9+/10 feeds for critical monitoring:
critical_feeds = [feed for feed in rss_feeds if feed[5] >= 9]

# Get educational content only:
education_feeds = [feed for feed in rss_feeds if "DEEP DIVES" in str(feed)]

# Get only exploit development feeds:
exploit_dev = [feed for feed in rss_feeds if "EXPLOIT DEVELOPMENT" in str(feed)]
```
