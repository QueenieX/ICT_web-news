import requests
from bs4 import BeautifulSoup
import re

article_urls_9news = []
urls= ['https://www.9news.com.au/just-in',
       'https://www.9news.com.au/world',
       'https://www.9news.com.au/politics']


while len(article_urls_9news) < 30:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            link = article.find('a')['href']
            if link.startswith('/'):
                link = url + link
            if link not in article_urls_9news:
                article_urls_9news.append(link)
            if link.startswith('/video'):
                re.link
            if len(article_urls_9news) == 30:
                break


# Save the site URLs to a file
with open("9newsURLs.txt", "a") as f:
    for url in article_urls_9news:
        f.write(url + "\n")