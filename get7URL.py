import requests
from bs4 import BeautifulSoup

article_urls_7news = []
urls= ['https://www.7news.com.au/sport', 
       'https://www.7news.com.au/entertainment',
       'https://www.7news.com.au/politics', 
       'https://www.7news.com.au/business/finance', 
       'https://www.7news.com.au/lifestyle']


while len(article_urls_7news) < 80:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = soup.find_all('div', class_= 'css-c8eknp-StyledSNEnt efjxvb10')

        for article in articles:
            link = article.find('a')['href'] 

            if link.startswith('/sport'):
                link = 'https://www.7news.com.au' + link
            if link.startswith('/news'):
                link = 'https://www.7news.com.au' + link
            if link.startswith('/entertainment'):
                link = 'https://www.7news.com.au' + link
            if link.startswith('/politics'):
                link = 'https://www.7news.com.au' + link
            if link.startswith('/lifestyle'):
                link = 'https://www.7news.com.au' + link
            if link.startswith('/business'):
                link = 'https://www.7news.com.au' + link
            if link not in article_urls_7news:
                article_urls_7news.append(link)
            if len(article_urls_7news) == 80:
                break

with open("7newsURLs.txt", "w") as f:
    for url in article_urls_7news:
        f.write(url + "\n")

print(article_urls_7news)