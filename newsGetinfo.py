import requests
from bs4 import BeautifulSoup

# Read the site URLs from the file
article_urls_news = []
with open("newsURLs.txt", "r") as f:
    for line in f:
        article_urls_news.append(line.strip())

# Make a GET request to the article URL
for url in article_urls_news:
    response = requests.get(url)
    print(url)
    
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    article = soup.find_all('article', id='story')

    title = soup.find('h1')
    title_text = title.text.strip()

    datetime = soup.find('div', class_='byline_publish')
    date_text = datetime.text.strip()
    # Find the HTML element that contains the news content
    article_content = soup.find('div', id='story-primary')
    content_text = article_content.text.strip()
    # Extract the text from the HTML element
    print(title_text)
    print(date_text)
    print(content_text)
    print("\n")


