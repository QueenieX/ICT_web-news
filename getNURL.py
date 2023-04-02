import requests
from bs4 import BeautifulSoup

article_urls_news = []
urls= ['https://www.news.com.au', 
       'https://www.news.com.au/national', 
       'https://www.news.com.au/entertainment',
       'https://www.news.com.au/politics', 
       'https://www.news.com.au/travel', 
       'https://www.news.com.au/lifestyle']

while len(article_urls_news) < 333:
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = soup.find_all('article')

        for article in articles:
            link = article.find('a', class_ ='storyblock_title_link')['href']
            
            if link.startswith('/'):
                link = url + link
            if link not in article_urls_news:
                article_urls_news.append(link)
                
            if len(article_urls_news) == 333:
                break


with open("newsURLs.txt", "w") as f:
    for url in article_urls_news:
        f.write(url + "\n")