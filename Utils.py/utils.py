import feedparser
from newspaper import Article
from langdetect import detect
import nltk

nltk.download('punkt')

def get_articles(company_name, num_articles=10):
    """
    Fetch and parse news articles for a given company.
    
    Args:
        company_name (str): Name of the company.
        num_articles (int): Number of articles to fetch (default: 10).
    
    Returns:
        list: List of dictionaries containing article details.
    """
    query = company_name.replace(' ', '+')
    rss_url = f"https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    articles = []
    
    for entry in feed.entries:
        if len(articles) >= num_articles:
            break
        url = entry.link
        try:
            article = Article(url)
            article.download()
            article.parse()
            # Ensure article is in English
            if detect(article.text) == 'en':
                article.nlp()  # Generate summary
                articles.append({
                    'title': article.title,
                    'summary': article.summary,
                    'text': article.text,
                    'url': url
                })
        except Exception as e:
            print(f"Error processing {url}: {e}")
    return articles
