import requests
from bs4 import BeautifulSoup

article_urls_9news = []
base_url = 'https://www.9news.com.au/national'


page_num = 1
while len(article_urls_9news) < 333:
    url = base_url + f'/{page_num}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        link = article.find('a')['href']
        if link.startswith('/'):
            link = base_url + link
        if link not in article_urls_9news:
            article_urls_9news.append(link)
        if len(article_urls_9news) == 333:
            break
    page_num += 1


# Save the site URLs to a file
with open("9newsURLs.txt", "w") as f:
    for url in article_urls_9news:
        f.write(url + "\n")