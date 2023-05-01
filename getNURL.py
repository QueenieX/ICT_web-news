import requests
from bs4 import BeautifulSoup

article_urls_news = []
urls= ['https://www.news.com.au/travel', 
       'https://www.news.com.au/world',
       'https://www.news.com.au/national', 
       'https://www.news.com.au/entertainment',
       'https://www.news.com.au/finance', 
       'https://www.news.com.au/technology', 
       'https://www.news.com.au/lifestyle',
       'https://www.news.com.au/sport']

while len(article_urls_news) < 10:
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
                
            if len(article_urls_news) == 10:
                break


with open("newsURLs.txt", "a") as f:
    for url in article_urls_news:
        f.write(url + "\n")