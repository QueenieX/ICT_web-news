import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Read the site URLs from the file
article_urls_7news = []
with open("7newsURLs.txt", "r") as f:
    for line in f:
        article_urls_7news.append(line.strip())

# Make a GET request to the article URL
for url in article_urls_7news:
    response = requests.get(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the article title
    title = soup.find('h1')
    title_text = title.text.strip()
    datetime_str = soup.find_all('time')
    datetime = datetime_str[0].get('datetime')

   
    # Find the HTML element that contains the news content
    article_contents = soup.find_all('article')
    # Extract the text content from all the span elements in each block-content div

    content = ""
    for content_div in article_contents:
        content_paras = content_div.find_all('p')
        for p in content_paras:
            content += p.text.strip() + " "

    print(url)
    print(title_text)
    print(f"{datetime}")
    print(content)
    print('\n')