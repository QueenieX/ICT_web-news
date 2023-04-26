import requests
from bs4 import BeautifulSoup

# Read the site URLs from the file
article_urls_9news = []
with open("9newsURLs.txt", "r") as f:
    for line in f:
        article_urls_9news.append(line.strip())

print(f)

# Make a GET request to the article URL
for url in article_urls_9news:
    response = requests.get(url)
    print(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    article = soup.find_all('content')
        
    # Extract the article title
    title = soup.find('h1')
    title_text = title.text.strip()

    # Find the HTML element that contains the news content
    article_content = soup.find('div', class_='article__body')

    print(title_text)

    print(article_content)