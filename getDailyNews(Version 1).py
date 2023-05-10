import feedparser

rss_urls = [
    "https://www.news.com.au/content-feeds/latest-news-national/",
    "https://7news.com.au/rss-feeds",
    "https://www.9news.com.au/rss"
]

for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)
    for entry in feed.entries:
        print(entry.link)

        
        
        
import feedparser
import requests
from bs4 import BeautifulSoup
import datetime

rss_urls = [
    "https://www.news.com.au/content-feeds/latest-news-national/",
    "https://7news.com.au/rss-feeds",
    "https://www.9news.com.au/rss"
]

for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)
    for entry in feed.entries:
        print(entry.link)
        
        if entry.link.startswith("https://www.news.com.au"):
            response = requests.get(entry.link)
            soup = BeautifulSoup(response.text, "html.parser")
            link = entry.link
            title = entry.title.strip()
                
            date_str = soup.find('div', id='publish-date').text.strip().split(' - ')[0]
            published_date = datetime.datetime.strptime(date_str, "%B %d, %Y %I:%M%p")
        
        elif entry.link.startswith("https://7news.com.au"):
            response = requests.get(entry.link)
            soup = BeautifulSoup(response.text, "html.parser")
            article = soup.find('div', class_='css-c8eknp-StyledSNEnt efjxvb10')
            link = entry.link
            title = entry.title.strip()
                
            date_str = soup.find('time')['datetime']
            published_date = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M%z")
        else:
            # For 9news.com.au, use the pubDate attribute
            if "published" in entry:
                published_date = datetime.datetime.strptime(
                    entry.published, "%a, %d %b %Y %H:%M:%S %z"
                )
            else:
                continue

