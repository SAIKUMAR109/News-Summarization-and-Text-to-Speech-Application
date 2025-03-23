from collections import Counter

def generate_comparative_analysis(articles):
    """
    Generate comparative analysis across articles.
    
    Args:
        articles (list): List of article dictionaries with sentiment and topics.
    
    Returns:
        dict: Comparative analysis including distribution, topics, and summary.
    """
    sentiments = [article['sentiment'] for article in articles]
    sentiment_counts = {
        'Positive': sentiments.count('Positive'),
        'Negative': sentiments.count('Negative'),
        'Neutral': sentiments.count('Neutral')
    }
    
    all_topics = [topic for article in articles for topic in article['topics']]
    topic_freq = Counter(all_topics)
    common_topics = [topic for topic, freq in topic_freq.items() if freq > 1]
    unique_topics = {
        article['title']: [topic for topic in article['topics'] if topic_freq[topic] == 1]
        for article in articles
    }
    
    dominant_sentiment = max(sentiment_counts, key=sentiment_counts.get)
    summary = (
        f"Overall, the news coverage is mostly {dominant_sentiment.lower()}, with "
        f"{sentiment_counts[dominant_sentiment]} out of {len(articles)} articles being {dominant_sentiment}. "
        f"The most common topics are {', '.join(common_topics[:3])}. "
        "However, there are unique perspectives in some articles, such as "
    )
    for title, topics in unique_topics.items():
        if topics:
            summary += f"'{title}' discussing {', '.join(topics)}, "
    summary = summary.rstrip(', ') + '.'
    
    return {
        'sentiment_distribution': sentiment_counts,
        'common_topics': common_topics,
        'unique_topics': unique_topics,
        'summary': summary
    }
