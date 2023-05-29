import feedparser
from dateutil import parser
import requests
from bs4 import BeautifulSoup
import datetime
from urllib.parse import urlparse
from datetime import date, timedelta

yesterday = date.today() - timedelta(days=1)
formattedY = yesterday.strftime("%B %d, %Y")
today = datetime.date.today()
formattedT = today.strftime("%B %d, %Y")

rss_urls = [
    "https://www.news.com.au/content-feeds/latest-news-national/",
    "https://www.news.com.au/content-feeds/latest-news-world/",
    "https://www.7news.com.au/rss/",
    "https://9news.com.au/just-in/rss"]

outputs = []
for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)

    for entry in feed.entries:

        if "published" in entry: # 9news&7news
            published_date = parser.parse(entry.published)
            date_text = published_date.strftime( "%B %d, %Y")
            response = requests.get(entry.link)

            # Create a BeautifulSoup object from the response content
            soup = BeautifulSoup(response.content, 'html.parser')

        else: #news.com.au
            response = requests.get(entry.link)
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('article')

            for article in articles:
                link_element = article.find('a', class_='storyblock_title_link')
                if link_element:
                    link = link_element['href']
                else:
                    link = " "
                news_date = soup.find('div', class_='byline_publish')
                date_text = news_date.text.strip().split(' - ')[0]

        if formattedT == date_text:
            title = entry.title
            link = entry.link


            if link.startswith("https://www.news.com.au/"):
                soup = BeautifulSoup(response.content, 'html.parser')
                article = soup.find_all('article', id='story')
                article_content = soup.find('div', id='story-primary')
                content_text = article_content.text.strip()

            elif link.startswith("https://www.9news.com.au/"):
                article_contents = soup.find_all('div', class_='block-content')
                content_text = ""
                for content_div in article_contents:
                    content_spans = content_div.find_all('span')
                    for span in content_spans:
                        content_text += span.text.strip() + " "
            else:
                article_contents = soup.find_all('article')
                content_text = ""
                for content_div in article_contents:
                    content_paras = content_div.find_all('p')
                    for p in content_paras:
                        content_text += p.text.strip() + " "

        print(link)
