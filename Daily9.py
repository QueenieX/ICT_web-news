import requests
from bs4 import BeautifulSoup
from datetime import date

# Read the site URLs from the file
article_urls_9news = []
with open("9newsURLs.txt", "r") as f:
    for line in f:
        article_urls_9news.append(line.strip())

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

        print(title)
        print(date_text)
        print(url)
        print(content)
        print('\n')

    else:
        print('\n')