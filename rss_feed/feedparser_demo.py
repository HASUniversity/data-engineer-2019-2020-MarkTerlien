import feedparser
result = feedparser.parse('https://alarmeringen.nl/feeds/region/brabant-noord.rss')
print(result["channel"]["language"])
print(len(result['entries']))
print(result.entries[0].description)