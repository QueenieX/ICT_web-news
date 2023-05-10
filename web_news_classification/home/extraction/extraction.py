import requests
from bs4 import BeautifulSoup
from datetime import datetime


def extract(url):
    response = requests.get(url)

    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

def extract7news(soup):
    # Extract the article title -- 7news
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

def extract9news(soup):
    
    # Extract the article title
    title = soup.find('h1').text.strip()
    datetime = soup.find('time').text.strip()
    
    # Find all the div elements with class="block-content"
    article_contents = soup.find_all('div', class_='block-content')

    # Extract the text content from all the span elements in each block-content div
    content = ""
    for content_div in article_contents:
        content_spans = content_div.find_all('span')
        for span in content_spans:
            content += span.text.strip() + " "
    

def extractnews(soup):
    article = soup.find_all('article', id='story')

    title = soup.find('h1')
    title_text = title.text.strip()

    datetime = soup.find('div', class_='byline_publish')
    date_text = datetime.text.strip()
    # Find the HTML element that contains the news content
    article_content = soup.find('div', id='story-primary')
    content_text = article_content.text.strip()
    