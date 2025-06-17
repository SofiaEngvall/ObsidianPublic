import feedparser
import requests
from bs4 import BeautifulSoup
import ollama
import speaker
import AI.ollama.python.listener as listener

s = speaker.Speaker()

# Example cybersecurity RSS feed
RSS_FEED_URL = "https://www.wired.com/category/security/feed/"

# Fetch and parse RSS feed
feed = feedparser.parse(RSS_FEED_URL)
entries = feed.entries
print(f"Fetched {len(entries)} articles from the feed.")

for entry in entries:
    title = entry.title
    link = entry.link
    print(f"\nTitle: {title}\nFetching: {link}")
    s.speak(f"\nTitle: {title}\nFetching: {link}")

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

        response = requests.get(link, headers=headers, allow_redirects=True, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract visible text from article
        paragraphs = soup.find_all('p')
        article_text = ' '.join(p.get_text() for p in paragraphs)
        word_count = len(article_text.split())

        print(f"Word count: {word_count}")

        if word_count > 250:
            print("Summarizing article...")
            summary = ollama.chat(model='llama3.2', messages=[
                {"role": "system", "content": "Summarize the following article in 200 to 300 words."},
                {"role": "user", "content": article_text}
            ])
            print("Summary:")
            print(summary['message']['content'])
            s.speak(summary.message.content)
        else:
            print(article_text)
            s.speak(article_text)

    except Exception as e:
        print(f"Failed to process article: {e}")
