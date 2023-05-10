import feedparser

rss_urls = [
    "https://www.news.com.au/content-feeds/latest-news-national/",
    "https://7news.com.au/rss-feeds",
    "https://www.9news.com.au/rss"
]

for rss_url in rss_urls:
    feed = feedparser.parse(rss_url)
    for entry in feed.entries:
        print(entry.link)
