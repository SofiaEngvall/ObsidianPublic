
```python
### Security related RSS feeds to fetch articles from
rss_feeds = [
    # Alerts

    # News
    ("Krebs on Security", "News", "https://krebsonsecurity.com/feed/", None),
    ("SANS Internet Storm Center", "News", "https://isc.sans.edu/rssfeed_full.xml", None),
    ("Kaspersky Securelist", "News", "https://securelist.com/feed/", None),
    ("The Hacker News", "News", "https://feeds.feedburner.com/TheHackersNews?format=xml", None),
    ("Cyber Alerts", "News", "https://cyberalerts.io/rss/latest-public", None),  # some links broken

    # Longer news
    ("Sophos Security Operations", "Long News", "https://news.sophos.com/en-us/category/security-operations/feed/", None),

    # Security blogs
    ("Schneier on Security", "Blog", "https://www.schneier.com/feed/atom/", None),

    # Podcasts
    ("Darknet Diaries", "Podcast", "https://podcast.darknetdiaries.com/", None),
    ("Graham Cluley", "Podcast", "https://grahamcluley.com/feed/", None),

    # Research
    ("WeLiveSecurity", "Research", "https://feeds.feedburner.com/eset/blog", None),
    ("Sophos Threat Research", "Research", "https://news.sophos.com/en-us/category/threat-research/feed/", None),

    # Personal blogs
    ("Troy Hunt", "Personal Blog", "https://www.troyhunt.com/rss/", None),


    #Requires javascript to run - TODO! - use playwright to bypass this
    #"https://www.ncsc.gov.uk/api/1/services/v1/report-rss-feed.xml",
    #"https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml",
    #"https://www.ncsc.gov.uk/api/1/services/v1/blog-post-rss-feed.xml",
    #"https://www.ncsc.gov.uk/api/1/services/v1/guidance-rss-feed.xml",


    #the first few from googling, the rest from ai
    "https://www.reddit.com/r/netsec/.rss",
    "https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml",
    "https://www.cshub.com/rss/articles", 
    "https://www.cshub.com/rss/news-trends"
    "https://threatpost.com/feed/", # news from 2022
    "https://www.darkreading.com/rss.xml",
    "https://krebsonsecurity.com/feed/",
    "https://www.securityweek.com/rss",
    "https://www.scmagazine.com/home/feed/",
    "https://www.cyberscoop.com/feed/",
    "https://www.zdnet.com/topic/security/rss.xml",
    "https://www.wired.com/category/security/feed/",
    "https://www.csoonline.com/index.rss",
    "https://www.infosecurity-magazine.com/rss/news/",
    "https://www.helpnetsecurity.com/feed/",
    "https://www.hackread.com/feed/",
    "https://portswigger.net/daily-swig/rss",
    "https://www.tripwire.com/state-of-security/feed/",
    "https://www.schneier.com/blog/atom.xml",
    "https://securityaffairs.co/wordpress/feed",
    "https://www.fireeye.com/blog/threat-research/_jcr_content.feed",
    "https://www.recordedfuture.com/feed",
    "https://unit42.paloaltonetworks.com/feed/",
    "https://blog.talosintelligence.com/feeds/posts/default",
    "https://www.malwarebytes.com/blog/feed",
    "https://www.crowdstrike.com/blog/feed/",
    "https://www.trendmicro.com/rss/enterprise-security.xml",
    "https://www.fortinet.com/blog/threat-research/_jcr_content.feed",
    "https://www.mcafee.com/blogs/feed/",
    "https://www.sophos.com/en-us/rss.aspx",
    "https://www.avast.com/en-us/rss",
    "https://securelist.com/feed/",
    "https://www.eset.com/int/about/newsroom/rss/",
    "https://www.cybersecurity-insiders.com/feed/",
    "https://www.nakedsecurity.sophos.com/feed/",
    "https://www.thehackernews.com/feeds/posts/default",
    "https://www.cyberark.com/resources/blog/feed/",
    "https://www.imperva.com/blog/feed/",
    "https://www.varonis.com/blog/rss.xml",
    "https://www.exabeam.com/feed/"

    #Sourses
    #Long list of RSS feeds - https://0dayfans.com/feeds.txt
]
```
