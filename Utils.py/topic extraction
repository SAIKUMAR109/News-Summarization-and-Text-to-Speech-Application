from keybert import KeyBERT

kw_model = KeyBERT()

def extract_topics(text, num_topics=3):
    """
    Extract key topics from the text.
    
    Args:
        text (str): Article content.
        num_topics (int): Number of topics to extract (default: 3).
    
    Returns:
        list: List of topic strings.
    """
    keywords = kw_model.extract_keywords(
        text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=num_topics
    )
    return [kw[0] for kw in keywords]
