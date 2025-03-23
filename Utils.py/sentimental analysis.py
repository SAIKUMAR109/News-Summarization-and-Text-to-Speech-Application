from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def analyze_sentiment(text):
    """
    Analyze sentiment of the given text.
    
    Args:
        text (str): Article content.
    
    Returns:
        str: Sentiment label (Positive, Negative, Neutral).
    """
    result = sentiment_pipeline(text[:512])[0]  # Truncate to 512 tokens
    return result['label'].capitalize()
