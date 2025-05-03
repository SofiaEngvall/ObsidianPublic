import feedparser
import requests
from bs4 import BeautifulSoup


rss_url = 'https://www.mmafighting.com/rss/current'
feed = feedparser.parse(rss_url)

if feed.status == 200:
    for entry in feed.entries:
        print(entry.title)
        print(entry.link)

        x = requests.get(entry.link)
        print(x.status_code)

        soup = BeautifulSoup(x.text, 'html')
        print(soup.get_text())

        print("\n")

else:
    print("Failed to get RSS feed. Status code:", feed.status)


