import time
import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import win32com.client
import httpx
from playwright.sync_api import sync_playwright
import shutil
import os

SPEAKING_SPEED = 4  # -10 to 10

rss_urls = [
    #reccomended in reddit and other places
    https://podcast.darknetdiaries.com/ #Darknet Diaries RSS
    https://grahamcluley.com/feed/ #Graham Cluley RSS
    https://krebsonsecurity.com/feed/ #Krebs on Security RSS
SANS Internet Storm Center RSS: https://isc.sans.edu/rssfeed_full.xml
Schneier on Security RSS: https://www.schneier.com/feed/atom/
Securelist RSS: https://securelist.com/feed/
Security Operations – Sophos News RSS: https://news.sophos.com/en-us/category/security-operations/feed/
The Hacker News RSS: https://feeds.feedburner.com/TheHackersNews?format=xml
Threat Research – Sophos News RSS: https://news.sophos.com/en-us/category/threat-research/feed/
Troy Hunt RSS: https://www.troyhunt.com/rss/
USOM RSS: https://www.usom.gov.tr/rss/tehdit.rss
USOM RSS: https://www.usom.gov.tr/rss/duyuru.rss
WeLiveSecurity RSS: https://feeds.feedburner.com/eset/blog

0dayfans RSS: https://0dayfans.com/feed.rss 
the above https://0dayfans.com/feeds.txt

https://cyberalerts.io/rss/latest-public

https://www.ncsc.gov.uk/api/1/services/v1/report-rss-feed.xml
https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml
https://www.ncsc.gov.uk/api/1/services/v1/blog-post-rss-feed.xml
https://www.ncsc.gov.uk/api/1/services/v1/guidance-rss-feed.xml



    #the first dew from googling, the rest from ai
    #"https://www.reddit.com/r/netsec/.rss",  # authors, author_detail, href, author, tags, content, summary, id, guidislink, link, links, updated, updated_parsed, published, published_parsed, title, title_detail
    #"https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml",  # title, title_detail, links, link, summary, summary_detail, published, published_parsed, id, guidislink
    #"https://www.cshub.com/rss/articles",  # title, title_detail, links, link, summary, summary_detail, authors, author, author_detail, id, guidislink, published, published_parsed
    #"https://www.cshub.com/rss/news-trends"  # empty now
    #"https://threatpost.com/feed/", # news from 2022
    #"https://www.darkreading.com/rss.xml", #403 #title, title_detail, links, link, summary, summary_detail, published, published_parsed, authors, author, author_detail, id, guidislink, media_thumbnail, href, media_content
    #"https://krebsonsecurity.com/feed/", #ok
    #"https://www.securityweek.com/rss", #403
    #"https://www.scmagazine.com/home/feed/", #b'' odd data
    #"https://www.cyberscoop.com/feed/", #b'' odd data
    #"https://www.zdnet.com/topic/security/rss.xml", #ok
    #"https://www.wired.com/category/security/feed/", #ok
    #"https://www.csoonline.com/index.rss", # byte data and no title
    #"https://www.infosecurity-magazine.com/rss/news/", #odd data
    #"https://www.helpnetsecurity.com/feed/", #ok
    #"https://www.hackread.com/feed/", #odd data
    #"https://portswigger.net/daily-swig/rss", #ok
    #"https://www.tripwire.com/state-of-security/feed/", #ok
    #"https://www.schneier.com/blog/atom.xml", #byte data
    #"https://securityaffairs.co/wordpress/feed", #byte data
    "https://www.fireeye.com/blog/threat-research/_jcr_content.feed", #ok
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
]

class Speaker():
    def __init__(self):
        self.tts = win32com.client.Dispatch('SAPI.Spvoice')

        # self.print_voices()
        self.set_voice(2)
        self.set_speed(SPEAKING_SPEED)
        # self.tell_speed()

    def set_voice(self, voice_number):
        voices = self.tts.GetVoices()
        self.tts.Voice = voices.Item(voice_number)

    def print_voices(self):
        voices = self.tts.GetVoices()
        for voice in voices:
            print(voice.GetDescription())
        print(f"Current voice: {self.tts.Voice.GetDescription()}")

    def set_speed(self, speed):
        self.tts.Rate = speed

    def tell_speed(self):
        self.speak(f"My speaking rate is set to {self.tts.Rate}.")

    def speak(self, text):
        print(text)
        self.tts.Speak(text)

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join(p.get_text() for p in paragraphs)
    return text

def print_key_names(feed):
    if feed.entries:
        entry = feed.entries[0]
        for key in entry.keys():
            print(f"{key}, ", end="")


def read_full_article(url):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        html = page.content()
        browser.close()
        return html


def read_full_article(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
            #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Priority': 'u=0, i',
            'Te': 'trailers',
            'Connection': 'keep-alive',
        }

        #response = requests.get(url=url, headers=headers, follow_redirects=True)
        response = client.get(url, headers=headers, follow_redirects=True)





        response.raise_for_status()

        # print(f"DEBUG\n-----\n")
        # print(f"soup.title.string: {soup.title.string}\n")
        # print(f"soup.contents: {soup.contents}\n\n")
        # print(f"soup.head: {soup.head}\n\n")
        # print(f"soup.body: {soup.body}\n\n")

    except Exception as e:
        print(f"Error: {e}")
        speaker.speak("An error occurred while processing the article.")








    print(response.content)

    if "text/html" in response.headers.get('Content-Type', ''):

        #response.encoding = response.apparent_encoding
        #html = response.text
        #soup = BeautifulSoup(html, 'html.parser')

        #html = response.content.decode('utf-8', errors='replace')


        #html = response.content.decode('utf-8')
        #html = response.content.decode('latin-1')
        #html = response.content.decode('windows-1252')
        #soup = BeautifulSoup(html, 'html.parser')



        #base one
        soup = BeautifulSoup(response.text, 'html.parser')



        paragraphs = soup.find_all('p')
        article_content = ' '.join(p.get_text() for p in paragraphs)
        speaker.speak(f"{article_content}")
    else:
        speaker.speak("The article content is byte data.")



if __name__ == "__main__":

    client = httpx.Client(http2=True)

    speaker = Speaker()

    speaker.speak("Here are the latest articles from the RSS feed.")

    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)
        if not feed.entries:
            continue

        if "title" in feed.feed:
            speaker.speak(f"Fetched {len(feed.entries)} articles from {feed.feed.title}.\n")
        else:
            speaker.speak(f"Fetched {len(feed.entries)} articles from {rss_url}.\n")

        #print_key_names(feed)

        for entry in feed.entries:

            print("-" * max(0, os.get_terminal_size().columns))

            if "title" in entry:
                speaker.speak(f"Title: {entry.title}")

            if "published" in entry:
                try:
                    published_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
                except ValueError:
                    try:
                        published_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
                    except ValueError:
                        published_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S GMT")
                print(f"Published: {published_date.strftime('%Y-%m-%d')}")




            if "link" in entry:
                print(f"Link: {entry.link}")

            # if 'content' in entry:
            #     speaker.speak(f"Content: {extract_text_from_html(entry.content[0].value)}")
            # elif 'summary' in entry and entry.summary != entry.title:
            #     if "<" in entry.summary:
            #         speaker.speak(f"Summary: {extract_text_from_html(entry.summary)}")
            #     else:
            #         speaker.speak(f"Summary: {entry.summary}")

            #add voice question to read full article - TODO! when the mic works
            # speaker.speak("Do you want to read the full article?")

            if 'link' in entry:
                read_full_article(entry.link)

            print()
            time.sleep(1)

    client.close()
