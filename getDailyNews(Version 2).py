import feedparser
from bs4 import BeautifulSoup
import requests
import datetime

# Define the RSS URLs for the three websites
rss_urls = [
    "https://www.news.com.au/content-feeds/latest-news-national/",
    "https://7news.com.au/rss-feeds",
    "https://www.9news.com.au/rss"
]

# Define today's date as a datetime object
today = datetime.date.today()

# Create a set to store the URLs of the articles published today
today_article_urls = set()

# Loop through each RSS URL
for rss_url in rss_urls:
    # Parse the RSS feed
    feed = feedparser.parse(rss_url)

    # Loop through each article in the feed
    for entry in feed.entries:
        # Check if the entry has a published date
        if "published_parsed" in entry:
            # Use the published date as the article's date
            date = datetime.date(*entry.published_parsed[:3])
        else:
            # Try to use other date attributes
            if "updated_parsed" in entry:
                date = datetime.date(*entry.updated_parsed[:3])
            elif "created_parsed" in entry:
                date = datetime.date(*entry.created_parsed[:3])
            else:
                # Skip the article if there is no date attribute
                continue

        # Check if the article was published today
        if date == today:
            # Get the article's URL
            url = entry.link

            # Check if the article's URL is already in the set
            if url not in today_article_urls:
                # Add the URL to the set
                today_article_urls.add(url)

                # Print the article's date and URL
                print(date, url)

