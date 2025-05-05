# RSS Read Aloud for Cyber Security News


rss-read-aloud.py - RSS feed reader with AI summarization
version 1.0
by Sofia Engvall - FixIt42, 2025-05-04

This script fetches articles from a list of RSS feeds, summarizes them using AI (Ollama), and reads them aloud.

It uses these libraries:

- `os` to get terminal size
- `subprocess` to start Ollama
- `sys` to find the python executable running this script to use when installing ms playwright

- `time` and `datetime` to manage time and timezones
- `dateutil.parser` to parse dates

- `feedparser` to parse RSS feeds
- `requests` to download articles
- `playwright` to bypass restrictions on some webpages
- `webbrowser` to open links in a browser
- `readability-lxml` (and `lxml_html_clean`) to extract the main content from webpages
- `BeautifulSoup` to convert HTML to plain text
 
- `ollama` for AI summarization
 
- `speaker` and `listener` modules for text-to-speech and speech recognition
  (These modules will be available in the same directory as this script.)

The script is designed to be run in a terminal but as most output is spoken, it should work in a GUI as well.


### Installation

```sh
git clone https://github.com/SofiaEngvall/RSS-Read-Aloud-Cyber-News-Reader.git
```

```sh
pip install -r requirements.txt
```


### Settings
use_ollama = True #If True, use Ollama for summarization. If False, just read the full articles, even if they are thousands of words long.
START_OLLAMA = True #If True, start Ollama if it is not running. If False, ask the user if they want to start it.
OLLAMA_PATH = "D:/ollama/ollama.exe" #The full path to the ollama executable file. Use double backslashes or single forward slashes.
DEFAULT_TTS_SPEED = 4 #The default speed of the text-to-speech voice. -10 to 10, where 0 is normal speed.
DEFAULT_STT_RETRIES = 0 # -1 = no question asked, 0 = ask once, 1 = retry once, 2 = retry twice, etc.
DEFAULT_ARTICLE_DAYS = 7 #How old articles to read, older ones are skipped
DEFAULT_ARTICLE_LENGTH = 400 #Default length of the long article summary. Articles 100 words longer are read in full.
ALWAYS_READ_LONG = True # if True, always read the long summary and will skip making a short summary
use_playwright = True #If true, use Microsoft Playwright to access anti-scraping web pages


### RSS feeds
- Please tell me if you have more feeds to add something is incorrect or missing so I can fix it!
- The list was refined and formatted with the help of AI so please tell me errors I missed, like a bad description.


### TODO! Features to add!
- Add Linus TTS - possibly using gtts, suggestions are welcome
- Add functionality to save and load (file? registry?) information, for example:
  - Read articles - to remember what you already read/heard
  - RSS feed list
  - Ollama path
  - Article length
  - Article days
- Possible add command line options to set these values, overriding both the defaults in the script and the saved options
- Make a database of articles
- Make a database for the RSS feeds, or just add more fields to the list
- Add feedback on the feeds - Maybe at the end of the reading of a feed - connect to db on the web server?
  - Then maybe host a db for feeds there too - then just sync at start
- Make main fit on one page
