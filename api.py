# api.py
from utils import (get_articles, analyze_sentiment, extract_topics, 
                  generate_comparative_analysis, translate_to_hindi, generate_speech)

def analyze_company_news(company_name):
    """Analyze news for a company and return a structured report."""
    articles = get_articles(company_name)
    if not articles:
        return {"error": "No articles found."}
    
    # Process articles
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["text"])
        article["topics"] = extract_topics(article["text"])
    
    # Comparative analysis
    comparative_analysis = generate_comparative_analysis(articles)
    
    # Generate audio
    hindi_summary = translate_to_hindi(comparative_analysis["summary"])
    audio_file = generate_speech(hindi_summary)
    
    return {
        "company": company_name,
        "articles": articles,
        "comparative_analysis": comparative_analysis,
        "audio": audio_file
    }
