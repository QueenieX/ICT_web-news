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
        
        if entry.link.startswith("https://www.news.com.au/content-feeds/latest-news-national/" or "https://www.news.com.au/content-feeds/latest-news-world/"):
            response = requests.get(entry.link)
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all('div', class_='story-article')
            for article in articles:
                link = article.find('a')['href']
                title = article.find('a').text.strip()
                
                date_str = article.find('div', class_='byline_publish').text.strip().split(' - ')[0]
                published_date = datetime.datetime.strptime(date_str, "%B %d, %Y")

                article_content = soup.find('div', id='story-primary')
                content_text = article_content.text.strip()
                
        else:
            # For 9news.com.au, use the pubDate attribute
            if "published" in entry:
                published_date = datetime.datetime.strptime(
                    entry.published, "%a, %d %b %Y %H:%M:%S %z"
                ).timetuple()
                response = requests.get(entry.link)

                # Create a BeautifulSoup object from the response content
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.find('h1').text.strip()
                article_contents = soup.find_all('div', class_='block-content')

                # Extract the text content from all the span elements in each block-content div
                content = ""
                for content_div in article_contents:
                    content_spans = content_div.find_all('span')
                    for span in content_spans:
                        content += span.text.strip() + " "
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
