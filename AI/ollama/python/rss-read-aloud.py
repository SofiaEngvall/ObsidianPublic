#!/usr/bin/env python3

# rss-read-aloud.py - RSS feed reader with AI summarization
# by Sofia Engvall - FixIt42, 2025-05-03
# https://github.com/SofiaEngvall/RSS-Read-Aloud-Cyber-News-Reader.git

# This script fetches articles from a list of RSS feeds, summarizes them using AI (Ollama), and reads them aloud.
# 
# It uses these libraries:
# 
# - `os` to get terminal size
# - `subprocess` to start Ollama
# 
# - `time` and `datetime` to manage time and timezones
# - `dateutil.parser` to parse dates
# 
# - `feedparser` to parse RSS feeds
# - `requests` to download articles
# - `playwright` to bypass restrictions on some webpages - TODO!
# - `webbrowser` to open links in a browser
# - `readability-lxml` (and `lxml_html_clean`) to extract the main content from webpages
# - `BeautifulSoup` to convert HTML to plain text
# 
# - `ollama` for AI summarization
# 
# - `speaker` and `listener` modules for text-to-speech and speech recognition
#   (These modules will be available in the same directory as this script.)
# 
# The script is designed to be run in a terminal but as most output is spoken, it should work in a GUI as well.


### Import libraries
import os
import subprocess

import time
from datetime import datetime, timezone
from dateutil import parser

import feedparser
import requests
#from playwright.sync_api import sync_playwright
from webbrowser import open_new_tab #for opening odd pages in a browser
from readability import Document
from bs4 import BeautifulSoup

import ollama

import speaker
import listener


# TODO!
# - Add functionality to save and load (file? registry?) information, for example:
#   - Read articles - to remember what you already read/heard
#   - RSS feed list
#   - Ollama path
#   - Article length
#   - Article days
# - Possible add command line options to set these values, overriding both the defaults in the script and the saved options
# - Make a database of articles
# - Make a database for the RSS feeds, or just add more fields to the list
# - Add feedback on the feeds - Maybe at the end of the reading of a feed - connect to db on the web server?
#   - Then maybe host a db for feeds there too - then just sync at start


### Settings
use_ollama = True #If True, use Ollama for summarization. If False, just read the full articles, even if they are thousands of words long.
START_OLLAMA = True #If True, start Ollama if it is not running. If False, ask the user if they want to start it.
OLLAMA_PATH = "D:/ollama/ollama.exe" #The full path to the ollama executable file. Use double backslashes or single forward slashes.
DEFAULT_TTS_SPEED = 4 #The default speed of the text-to-speech voice. -10 to 10, where 0 is normal speed.
DEFAULT_STT_RETRIES = 0 # -1 = no question asked, 0 = ask once, 1 = retry once, 2 = retry twice, etc.
DEFAULT_ARTICLE_DAYS = 20 #How old articles to read, older ones are skipped
DEFAULT_ARTICLE_LENGTH = 200 #Default length of the long article summary. Articles 100 words longer are read in full.
ALWAYS_READ_LONG = True # if True, always read the long summary and will skip making a short summary


### RSS feeds - Please tell me if you have more feeds to add something is incorrect or missing so I can fix it!
### The list was refined and formatted with the help of AI so please tell me errors I missed, like a bad description.
### Format: (name, description, category, feed_url, site_url, status, rating)
### Status: "{overall_status} | link={link_quality} | content={content_type} | desc={desc_quality}"

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
    # 🧠 Deep Dives & Education
    # =====================
    ("The DFIR Report", "Incident response case studies", "education", "https://thedfirreport.com/feed/", "https://thedfirreport.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("SANS Digital Forensics", "Forensics techniques", "education", "https://digital-forensics.sans.org/blog/rss.xml", "https://digital-forensics.sans.org", "ok | link=direct | content=full_html | desc=full", 7),
    ("Lenny Zeltser's Blog", "Malware analysis guides", "education", "https://zeltser.com/feed/", "https://zeltser.com", "ok | link=direct | content=full_html | desc=full", 7),
    ("NCC Group Research", "Technical whitepapers", "education", "https://research.nccgroup.com/feed/", "https://research.nccgroup.com", "ok | link=direct | content=full_html | desc=full", 7),
    ("Windows Internals Blog", "OS security deep dives", "education", "https://windows-internals.com/feed/", "https://windows-internals.com", "ok | link=direct | content=full_html | desc=full", 7),
    ("Troy Hunt", "Security tutorials", "education", "https://www.troyhunt.com/rss/", "https://www.troyhunt.com", "ok | link=direct | content=full_html | desc=full", 8),
    ("Trenchant", "Advanced research", "education", "http://little-canada.org/feeds/output/trenchant.rss", "https://trenchant.io/", "ok | link=direct | content=full_html | desc=full", 7),

    # =====================
    # 🎙️ Podcasts
    # =====================
    ("Security Now (TWIT)", "Deep-dive security podcast", "podcast", "https://feeds.twit.tv/sn.xml", "https://twit.tv/shows/security-now", "ok | link=audio | content=episode_page | desc=full", 8),
    ("Darknet Diaries", "True cybercrime stories", "podcast", "https://feeds.megaphone.fm/darknetdiaries", "https://darknetdiaries.com", "ok | link=audio | content=episode_page | desc=full", 9),
    ("Risky Business Podcast", "Weekly news analysis", "podcast", "https://risky.biz/feeds/risky-business/", "https://risky.biz", "ok | link=episode_page | content=show_notes | desc=full", 9),
    ("Graham Cluley", "Security podcast", "podcast", "https://grahamcluley.com/feed/", "https://grahamcluley.com", "ok | link=direct | content=full_html | desc=full", 7),
]


### Headers for the requests - Used to mimic a real browser request and avoid being blocked
headers = {
    #"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    #'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
    'Te': 'trailers',
    'Connection': 'keep-alive',
}

### Function to print a dashed line
def dash_line():
    print("-" * max(0, (os.get_terminal_size().columns-1))) #------------------------------------------

### Function to print the keys of the first entry in the feed
def print_key_names(feed):
    if feed.entries:
        entry = feed.entries[0]
        for key in entry.keys():
            print(f"{key}, ", end="")

### Function to get the feed entries from a given RSS feed
def get_feed_entries(rss_feed):
    feed = feedparser.parse(rss_feed)
    dash_line() #------------------------------------------
    if feed.entries:
        if "title" in feed.feed:
            s.speak(f"\nFetched {len(feed.entries)} articles from {feed.feed.title}.\n")
        else:
            s.speak(f"\nFetched {len(feed.entries)} articles from {rss_feed}.\n")
    else:
        s.speak(f"\nNo articles found in {rss_feed}\n")
    return feed.entries

### Function to get a yes or no answer from the user
def get_yes_no(prompt, default="yes"):
    if DEFAULT_STT_RETRIES == -1:
        print()
        return default
    else:
        s.speak(prompt)
    retiry_no = 0
    answer = ""
    while answer == "":
        user_response = l.listen()
        print(f"You: {user_response}\n")
        if user_response.lower() in ["yes", "sure", "ok", "read it", "yes please", "yup"]:
            answer = "yes"
        elif user_response.lower() in ["no", "nope", "not now", "skip", "no thanks", "no please"]:
            answer = "no"
        elif retiry_no != DEFAULT_STT_RETRIES:
            s.speak("I didn't understand that. Please answer with yes or no.")
            retiry_no += 1
        else:
            answer = default
    return answer

### Function to inform the user how to install Ollama
def how_to_install_ollama():
    dash_line() #------------------------------------------
    s.speak("The easiest way to install ollama is to download the zip-file matching your setup from https://github.com/ollama/ollama/releases. Then you just unzip to your choosen directory and enter the ollama executable path and filename at the top of this script. Done! :)")
    dash_line() #------------------------------------------

### Function to check if Ollama is running
def check_for_ollama():
    try:
        ollama.chat(model='llama3.2', messages=[{"role": "user", "content": "Hello"}])
    except Exception as e:
        return False
    return True

### Function to ask the user if they want to start ollama if it is not running and inform them how to install it if it is not found
def start_ollama():
    dash_line() #------------------------------------------
    if START_OLLAMA or get_yes_no("\nOllama is not running. Do you want to start it?", "yes") == "yes":
        s.speak("Starting Ollama...")
        if os.path.isfile(OLLAMA_PATH):
            subprocess.Popen([OLLAMA_PATH, "serve"]) #), shell=True)
            time.sleep(7)

        if check_for_ollama():
            s.speak("Successfully started Ollama.")
            return
        else:
            s.speak("Could not start Ollama. Please double check your path and installation.\n")
    else:
        s.speak("There is an option, use_ollama, at the top of the script to start it without using ollama.")

    how_to_install_ollama()

    if get_yes_no("\nDo you still want news, without using AI summarization?", "yes") == "yes":
        s.speak("Starting news without AI summarization.\n")
        global use_ollama
        use_ollama = False
    else:
        s.speak("Stopping news script.\n")
        print()
        exit(0) #replace with 1 if you want, 1 makes my debugger stop :D


### Function to check if an article is old or already read, also prints the title and published date if available
def print_info_n_check_if_old_or_read():
    if "title" in entry and "published" not in entry:
        s.speak(f"Title: {entry.title}")
        return False

    if "published" in entry:
        published_date = parser.parse(entry.published) #fix date format
        days =(datetime.now(timezone.utc) - published_date).days #how old is the article
        if days <= DEFAULT_ARTICLE_DAYS: # The article is new enough
            if "title" in entry:
                s.speak(f"Title: {entry.title}")
            s.speak(f"Published: {published_date.strftime('%Y-%m-%d')}")
            return False
        else: #old article - just print the info
            if "title" in entry:
                print(f"Title: {entry.title}")
            print(f"Published: {published_date.strftime('%Y-%m-%d')}")
            print(f"Article is older than {DEFAULT_ARTICLE_DAYS} days. Skipping.")
            print()
            time.sleep(1)
            return True

### Function to download an article from a given URL
def download_article(url):
    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        response.raise_for_status()
    except Exception as e:
        print(f"Error: {e}")
        s.speak("An error occurred while processing the article.")
        return None
    return response.content #text

### Function to download an article from a given URL, using Playwright to bypass restrictions
# TODO! continue debugging the url's where we only get odd byte data
# def get_full_article(url):
#     with sync_playwright() as p:
#         browser = p.firefox.launch(headless=True)
#         page = browser.new_page()
#         page.goto(url, timeout=60000)
#         html = page.content()
#         browser.close()
#         return html

### Function to get the encoding and string content from a response
def get_format_n_string(content): #
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

### Function to extract the title and content from a webpage using Readability
def extract_article_from_webpage(html):
    doc = Document(html)
    title = doc.short_title()
    content = doc.summary()
    return title, content

### Function to convert HTML content to plain text using BeautifulSoup
def convert_html_to_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.text
                    
### Function to generate a summary of an article using Ollama
def generate_article_summary(article_html, lenth):
    summary = ollama.chat(model='llama3.2', messages=[
        {"role": "system", "content": f"Summarize the following article in approximately {lenth} words. Answer only with the summary."},
        {"role": "user", "content": article_html}
    ])
    return summary.message.content

### Function to get the content/summary/description of a feed entry
def get_feed_entry_content(entry):
    if 'content' in entry:
        return entry.content[0].value
    elif 'summary' in entry and entry.summary != entry.title:
        return entry.summary
    elif 'description' in entry and entry.description != entry.title:
        return entry.description
    else:
        return None

### Main function to run the script
if __name__ == "__main__":

    s = speaker.Speaker(also_print=True, speed=DEFAULT_TTS_SPEED)
    l = listener.Listener()

    ollama_process = None

    if use_ollama and not check_for_ollama():
        ollama_process = start_ollama()

    s.speak("\nHere are the latest articles from your RSS feeds.")

    for rss_feed in rss_feeds:

        entries = get_feed_entries(rss_feed[3]) #feed_url
        if not entries:
            continue

        #print("This feed has the following keys:")
        #print_key_names(feed)

        for entry in entries:

            dash_line() #------------------------------------------

            skip_article = print_info_n_check_if_old_or_read()
            if skip_article:
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
                    if get_yes_no("The article has zero length. Do you want to open the link in a browser?", "no") == "yes":
                        open_new_tab(entry.link)
                    link_fail = True

                elif article_format == "latin1" and average_word_length > 20: #lower? one had 10 and was binary data
                    if get_yes_no("The article appears to have longer words than normal. This is probably binary data. Do you want to open the link in a browser?", "no") == "yes":
                        open_new_tab(entry.link)
                    #if get_yes_no(f"The average word length is {average_word_length:.2f}. Do you still want me to read this?", "no") == "no":
                    article_text = ""
                    link_fail = True

            else: #"link" not in entry
                s.speak("No link found in entry.")
                article_text = ""
                link_fail = True

            if link_fail:

                # If we didn't get the article text from the link, try to get as much as we can from the feed entry
                text = get_feed_entry_content(entry)
                if text is not None:
                    article_text = convert_html_to_text(text)
                else:
                    article_text = ""
                    if get_yes_no("Can't read the article. Do you want to open the link in a browser?", "no") == "yes":
                        open_new_tab(entry.link)

            if article_text != "":

                # For very short articles, read the article text directly
                if word_count > 0 and word_count < 100:
                    if link_fail:
                        s.speak("Reading summary, content or description:")
                    else:
                        s.speak("Reading article:")
                    s.speak(article_text)

                else:
                    # Read summary
                    if not ALWAYS_READ_LONG:
                        if use_ollama:
                            print("Generating short summary...")
                            s.speak(f"\n{generate_article_summary(article_text, 50)}\n")
                        elif 'summary' in entry and entry.summary != entry.title:
                            print("Reading RSS feed summary:")
                            s.speak(entry.summary)
                        else:
                            print("No summary for this article.")

                    # Read full article
                    if ALWAYS_READ_LONG or get_yes_no("Do you want me to read the article?", "yes") == "yes":

                        if use_ollama and word_count > (DEFAULT_ARTICLE_LENGTH + 100):
                            print(f"Generating summary (approximate length {DEFAULT_ARTICLE_LENGTH})...")
                            summary_long = generate_article_summary(article_text, DEFAULT_ARTICLE_LENGTH)
                            #print(f"Summary word count: {len(summary_long.split())} (Original: {word_count})")
                            s.speak(f"\n{summary_long}\n")
                        else:
                            print("Reading full article:")
                            s.speak(article_text)

            print()
            time.sleep(1)
    
    if ollama_process is not None:
        s.speak("Stopping Ollama.")
        ollama_process.terminate()
        ollama_process.wait()

    s.speak("Finished reading articles.")
    print()
