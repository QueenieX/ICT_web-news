import feedparser
import requests
from bs4 import BeautifulSoup
import datetime

rss_urls = [
    "https://www.news.com.au/content-feeds/latest-news-national/",
    "https://www.news.com.au/content-feeds/latest-news-world/",
    "https://www.9news.com.au/rss"
]

for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)
    for entry in feed.entries:
        print(entry.link)
        
        if entry.link.startswith("https://www.news.com.au/content-feeds/latest-news-national/"):
            response = requests.get(entry.link)
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all('div', class_='story-article')
            for article in articles:
                link = article.find('a')['href']
                title = article.find('a').text.strip()
                
                date_str = article.find('div', class_='byline_publish').text.strip().split(' - ')[0]
                published_date = datetime.datetime.strptime(date_str, "%B %d, %Y")
        
        elif entry.link.startswith("https://www.news.com.au/content-feeds/latest-news-world/"):
            response = requests.get(entry.link)
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all('div', class_='story-article')
            for article in articles:
                link = article.find('a')['href']
                title = article.find('a').text.strip()
                
                date_str = article.find('div', class_='byline_publish').text.strip().split(' - ')[0]
                published_date = datetime.datetime.strptime(date_str, "%B %d, %Y")
        else:
            # For 9news.com.au, use the pubDate attribute
            if "published" in entry:
                published_date = datetime.datetime.strptime(
                    entry.published, "%a, %d %b %Y %H:%M:%S %z"
                ).timetuple()
            else:
                continue
            
        # Convert the published date to a Python datetime object
        published_datetime = datetime.datetime.fromtimestamp(
            datetime.datetime(*published_date[:6]).timestamp()
        )

        # Check if the published date is today
        today = datetime.datetime.today().date()
        if published_datetime.date() == today:
            # Print the published date in ISO 8601 format
            print(published_datetime.isoformat(), entry.link)