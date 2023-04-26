import requests
from bs4 import BeautifulSoup

# Read the site URLs from the file
article_urls_7news = []
with open("7newsURLs.txt", "r") as f:
    for line in f:
        article_urls_7news.append(line.strip())

print(f)

# Make a GET request to the article URL
for url in article_urls_7news:
    response = requests.get(url)
    print(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    article = soup.find_all('main', id='content')

    title = soup.find('h1')

    # Find the HTML element that contains the news content
    article_content = soup.find('div', id='ArticleContent')

    # Extract the text from the HTML element

    print(article_content)

    print(title)