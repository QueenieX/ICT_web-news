import requests
from bs4 import BeautifulSoup

url = 'https://wwos.nine.com.au/nrl/live-scores-2023-round-5-results-sharks-vs-warriors-bulldogs-vs-cowboys-updates-kick-off-time-news/e51fd120-1f39-4f7d-9b22-9e81a78489f6'
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

# Extract the text from the HTML element
content_text = article_content.text.strip()


print(title_text)

print(content_text)