import requests
from bs4 import BeautifulSoup
from datetime import date
from home.models import Newsarticles, Categories

def extract(url):
    response = requests.get(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

def extract7news():
    # Read the site URLs from the file
    article_urls_7news = []
    with open("7newsURLs.txt", "r") as f:
        for line in f:
            article_urls_7news.append(line.strip())
    output = []
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
        today = date.today().strftime('%Y-%m-%d')

        if today in datetime:
    
            # Find the HTML element that contains the news content
            article_contents = soup.find_all('article')
            # Extract the text content from all the span elements in each block-content div

            content = ""
            for content_div in article_contents:
                content_paras = content_div.find_all('p')
                for p in content_paras:
                    content += p.text.strip() + " "
        
        news = {title_text, url, content}
        output += news

    return output



def extract9news(soup):
    
    # Read the site URLs from the file
    article_urls_9news = []
    with open("9newsURLs.txt", "r") as f:
        for line in f:
            article_urls_9news.append(line.strip())

    output = []

    # Make a GET request to the article URL
    for url in article_urls_9news:
        response = requests.get(url)

        # Create a BeautifulSoup object from the response content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the article title
        title = soup.find('h1').text.strip()
        datetime = soup.find('time')
        date_text = datetime.text.strip()
        today = date.today().strftime("%B%e")

        if today in date_text:

            # Find all the div elements with class="block-content"
            article_contents = soup.find_all('div', class_='block-content')

            # Extract the text content from all the span elements in each block-content div
            content = ""
            for content_div in article_contents:
                content_spans = content_div.find_all('span')
                for span in content_spans:
                    content += span.text.strip() + " "
        news = {title, url, content}
        output += news

    return output

            
            

def extractnews(soup):
    # Read the site URLs from the file
    article_urls_news = []
    with open("newsURLs.txt", "r") as f:
        for line in f:
            article_urls_news.append(line.strip())

    # Make a GET request to the article URL
    for url in article_urls_news:
        response = requests.get(url)
        
        # Create a BeautifulSoup object from the response content
        soup = BeautifulSoup(response.content, 'html.parser')

        article = soup.find_all('article', id='story')

        title = soup.find('h1')
        title_text = title.text.strip()

        datetime = soup.find('div', id='publish-date')
        date_text = datetime.text.strip()
        today = date.today().strftime("%B%e")

        if today in date_text:
            # Find the HTML element that contains the news content
            
            article_content = soup.find('div', id='story-primary')
            content_text = article_content.text.strip()
            # Extract the text from the HTML element
            return title, url, content_text
        news = {title_text, url, content_text}
        output += news

    return output