import os #for terminal size

import time
from datetime import datetime, timezone
from dateutil import parser

import feedparser
import requests
#from playwright.sync_api import sync_playwright
from readability import Document #readability-lxml
from bs4 import BeautifulSoup

import ollama #for summarization

import speaker
import listener


DEFAULT_ARTICLE_LENGTH = 400
DEFAULT_ARTICLE_DAYS = 7

rss_feeds = [
    #reccomended in reddit and other places
    #"https://podcast.darknetdiaries.com/", #Darknet Diaries RSS, ok & summary of longer articles
    #"https://grahamcluley.com/feed/", #Graham Cluley RSS, bad data
    #"https://krebsonsecurity.com/feed/", #Krebs on Security RSS, ok & news
    #"https://isc.sans.edu/rssfeed_full.xml", #SANS Internet Storm Center RSS, ok
    #"https://www.schneier.com/feed/atom/", #Schneier on Security RSS, ok
    "https://securelist.com/feed/", #Securelist RSS
    "https://news.sophos.com/en-us/category/security-operations/feed/", #Security Operations – Sophos News RSS
    "https://feeds.feedburner.com/TheHackersNews?format=xml", #The Hacker News RSS
    "https://news.sophos.com/en-us/category/threat-research/feed/", #Threat Research – Sophos News RSS
    "https://www.troyhunt.com/rss/", #Troy Hunt RSS
    "https://www.usom.gov.tr/rss/tehdit.rss", #USOM RSS
    "https://www.usom.gov.tr/rss/duyuru.rss", #USOM RSS
    "https://feeds.feedburner.com/eset/blog", #WeLiveSecurity RSS

# 0dayfans RSS: https://0dayfans.com/feed.rss 
# the above https://0dayfans.com/feeds.txt

# https://cyberalerts.io/rss/latest-public

# https://www.ncsc.gov.uk/api/1/services/v1/report-rss-feed.xml
# https://www.ncsc.gov.uk/api/1/services/v1/news-rss-feed.xml
# https://www.ncsc.gov.uk/api/1/services/v1/blog-post-rss-feed.xml
# https://www.ncsc.gov.uk/api/1/services/v1/guidance-rss-feed.xml



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

    # to check:
    # "https://www.fireeye.com/blog/threat-research/_jcr_content.feed", #ok
    # "https://www.recordedfuture.com/feed",
    # "https://unit42.paloaltonetworks.com/feed/",
    # "https://blog.talosintelligence.com/feeds/posts/default",
    # "https://www.malwarebytes.com/blog/feed",
    # "https://www.crowdstrike.com/blog/feed/",
    # "https://www.trendmicro.com/rss/enterprise-security.xml",
    # "https://www.fortinet.com/blog/threat-research/_jcr_content.feed",
    # "https://www.mcafee.com/blogs/feed/",
    # "https://www.sophos.com/en-us/rss.aspx",
    # "https://www.avast.com/en-us/rss",
    # "https://securelist.com/feed/",
    # "https://www.eset.com/int/about/newsroom/rss/",
    # "https://www.cybersecurity-insiders.com/feed/",
    # "https://www.nakedsecurity.sophos.com/feed/",
    # "https://www.thehackernews.com/feeds/posts/default",
    # "https://www.cyberark.com/resources/blog/feed/",
    # "https://www.imperva.com/blog/feed/",
    # "https://www.varonis.com/blog/rss.xml",
    # "https://www.exabeam.com/feed/"
]

headers = {
    #"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
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

def print_key_names(feed):
    if feed.entries:
        entry = feed.entries[0]
        for key in entry.keys():
            print(f"{key}, ", end="")

def download_article(url):
    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()
    except Exception as e:
        print(f"Error: {e}")
        s.speak("An error occurred while processing the article.")
        return None
    return response.content #text

def generate_short_summary(article_html):
    summary = ollama.chat(model='llama3.2', messages=[
        {"role": "system", "content": f"Summarize the following article in approximately 30 words. Answer only with the summary"},
        {"role": "user", "content": article_html}
    ])
    return summary.message.content

def generate_article_summary(article_html, lenth):
    summary = ollama.chat(model='llama3.2', messages=[
        {"role": "system", "content": f"Summarize the following article in approximately {lenth} words."},
        {"role": "user", "content": article_html}
    ])
    return summary.message.content

def get_yes_no(prompt):
    answer = ""
    s.speak(prompt)
    while answer == "":
        user_response = l.listen()
        print(f"You: {user_response}\n")
        if user_response.lower() in ["yes", "sure", "ok", "read it", "yes please", "yup"]:
            answer = "yes"
        elif user_response.lower() in ["no", "nope", "not now", "skip", "no thanks", "no please"]:
            answer = "no"
        else:
            s.speak("I didn't understand that. Please answer with yes or no.")
    return answer

def extract_article_from_webpage(html):
    doc = Document(html)
    title = doc.short_title()
    content = doc.summary()
    return title, content

def convert_html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text

def get_feed_entry_content(entry):
    if 'content' in entry:
        return entry.content[0].value
    elif 'summary' in entry and entry.summary != entry.title:
        return entry.summary
    elif 'description' in entry and entry.description != entry.title:
        return entry.description
    else:
        return None

#continue to debug the url's where we only get add byte data
# def get_full_article(url):
#     with sync_playwright() as p:
#         browser = p.firefox.launch(headless=True)
#         page = browser.new_page()
#         page.goto(url, timeout=60000)
#         html = page.content()
#         browser.close()
#         return html


def get_format_n_string(content): #responce.content in
    try:
        return "utf-8", content.decode('utf-8')
    except UnicodeDecodeError:
        try:
            return "windows-1252", content.decode('windows-1252')
        except UnicodeDecodeError:
            try:
                return "latin1", content.decode('latin1')
            except UnicodeDecodeError:
                try:
                    return "ISO-8859-1", content.decode('ISO-8859-1')
                except UnicodeDecodeError:
                    try:
                        return "ascii", content.decode('ascii')
                    except UnicodeDecodeError:
                        return "unredable", content


if __name__ == "__main__":

    s = speaker.Speaker(also_print=True)
    l = listener.Listener()

    #s.speak("Here are the latest articles from your RSS feeds.")

    for rss_feed in rss_feeds:

        feed = feedparser.parse(rss_feed)

        if not feed.entries:
            continue

        if "title" in feed.feed:
            s.speak(f"Fetched {len(feed.entries)} articles from {feed.feed.title}.\n")
        else:
            s.speak(f"Fetched {len(feed.entries)} articles from {rss_feed}.\n")

        #print("This feed has the following keys:")
        #print_key_names(feed)

        for entry in feed.entries:

            #only print anything if the date is newer than the limit

            print("-" * max(0, os.get_terminal_size().columns)) #------------------------------------------

            if "title" in entry:
                s.speak(f"Title: {entry.title}")

            if "published" in entry:
                published_date = parser.parse(entry.published)
                print(f"Published: {published_date.strftime('%Y-%m-%d')}")

                days =(datetime.now(timezone.utc) - published_date).days
                if days > DEFAULT_ARTICLE_DAYS:
                    s.speak(f"Article is older than {DEFAULT_ARTICLE_DAYS} days. Skipping.")
                    print()
                    time.sleep(1)
                    continue

            link_fail = False
            if "link" in entry:
                print(f"Link: {entry.link}")

                article_html = download_article(entry.link)
                if article_html is None:
                    article_html = ""
                else:
                    article_format, article_string = get_format_n_string(article_html)

                    if article_format == "unredable":
                        s.speak("Error decoding response:")
                        print(article_string[:100])
                        article_html = ""
                    else:
                        print(f"Format: {article_format}")
                        article_html = article_string

                title, article_html_fixed = extract_article_from_webpage(article_html)
                article_text = convert_html_to_text(article_html_fixed)

                word_count = len(article_text.split())
                print(f"Word count: {word_count}")
                average_word_length = len(article_text) / word_count if word_count > 0 else 0

                if word_count == 0:
                    link_fail = True
                elif article_format == "latin1" and average_word_length > 20:
                    #if get_yes_no(f"The average word length is {average_word_length:.2f}. Do you still want me to read this?") == "no":
                    article_text = ""
                    link_fail = True
            else: #"link" not in entry
                article_text = ""
                link_fail = True

            if link_fail:
                text = get_feed_entry_content(entry)
                if text is not None:
                    article_text = convert_html_to_text(text)
                    print("Failed to download article. Using summary/content.")
                else:
                    article_text = ""
                    s.speak("Can't read article contents. Please check the link.")

            if article_text != "":

                if word_count > 0 and word_count < 50:
                    s.speak("Reding full article:")
                    s.speak(article_text)

                else:
                    s.speak("Generating short summary...")
                    s.speak(generate_short_summary(article_text))

                    if get_yes_no("Do you want me to read more?") == "yes":

                        if word_count > (DEFAULT_ARTICLE_LENGTH+100):
                            s.speak(f"Generating summary (length approx {DEFAULT_ARTICLE_LENGTH})...")
                            s.speak(generate_article_summary(article_text, DEFAULT_ARTICLE_LENGTH))
                        else:
                            s.speak("Reding full article:")
                            s.speak(article_text)

            print()
            time.sleep(1)
