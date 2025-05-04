
Do you have and suggestions for cyber security rss feeds that I have missed? The better they are, the more grateful I am

Please make a full list of these in the same format. but double check that they are not on the old list first, thank you again! <3

```python
rss_feeds.extend([
    # --- Advanced Threat Research & Zero-Days ---
    ("Mandiant Blog", "APT Research", "https://www.mandiant.com/resources/blog/rss.xml", "https://www.mandiant.com/resources/blog", "active", 9),
    ("Google Threat Analysis Group (TAG)", "APT Research", "https://blog.google/threat-analysis-group/rss/", "https://blog.google/threat-analysis-group/", "active", 9),
    ("Citizen Lab", "Spyware Research", "https://citizenlab.ca/feed/", "https://citizenlab.ca", "active", 10),
    ("NCC Group Research", "Exploits", "https://research.nccgroup.com/feed/", "https://research.nccgroup.com", "active", 8),
    
    # --- Exploit Development & Malware ---
    ("STÖK’s Blog", "Bug Bounty", "https://stokfredrik.com/rss.xml", "https://stokfredrik.com", "active", 8),
    ("Hexacorn", "Malware Analysis", "https://www.hexacorn.com/blog/feed/", "https://www.hexacorn.com", "active", 7),
    ("Airbus CERT Blog", "Industrial Security", "https://blog.airbus-cyber-security.com/rss/", "https://blog.airbus-cyber-security.com", "active", 8),
    
    # --- Underrated High-Signal Feeds ---
    ("Risky Business Podcast", "News", "https://risky.biz/feeds/risky-business/", "https://risky.biz", "active", 9),
    ("BleepingComputer", "Ransomware", "https://www.bleepingcomputer.com/feed/", "https://www.bleepingcomputer.com", "active", 8),
    ("Lenny Zeltser’s Blog", "Malware", "https://zeltser.com/feed/", "https://zeltser.com", "active", 7),
    
    # --- Government & Policy ---
    ("CISA Alerts", "Vulnerabilities", "https://www.cisa.gov/news-events/cybersecurity-advisories/rss.xml", "https://www.cisa.gov", "active", 8),
    ("Europol EC3", "Cybercrime", "https://www.europol.europa.eu/rss/news-events", "https://www.europol.europa.eu", "active", 7),
    
    # --- Offensive Security (Red Team) ---
    ("SpecterOps Blog", "Red Team", "https://posts.specterops.io/feed", "https://posts.specterops.io", "active", 9),
    ("MDSec ActiveBreach", "Red Team", "https://www.mdsec.co.uk/feed/", "https://www.mdsec.co.uk", "active", 9),
    ("Rasta Mouse’s Blog", "C2 & Evasion", "https://rastamouse.me/rss.xml", "https://rastamouse.me", "active", 8),
    
    # --- Bonus: Lesser-Known but Valuable ---
    ("Securelist (Kaspersky)", "Threat Intel", "https://securelist.com/feed/", "https://securelist.com", "active", 8),  # Note: Different from "Kaspersky Securelist" in your list
    ("The DFIR Report", "Incident Response", "https://thedfirreport.com/feed/", "https://thedfirreport.com", "active", 8),
    ("SANS Digital Forensics", "Forensics", "https://digital-forensics.sans.org/blog/rss.xml", "https://digital-forensics.sans.org", "active", 7)
])
```