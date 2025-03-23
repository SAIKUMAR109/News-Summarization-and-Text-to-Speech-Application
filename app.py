# app.py
import gradio as gr
from api import analyze_company_news

def process_company(company_name):
    """Process company name and format output for Gradio."""
    report = analyze_company_news(company_name)
    if "error" in report:
        return report["error"], {}, None
    
    articles_output = [
        {"Title": a["title"], "Summary": a["summary"], "Sentiment": a["sentiment"], 
         "Topics": ", ".join(a["topics"]), "URL": a["url"]}
        for a in report["articles"]
    ]
    analysis_output = {
        "Sentiment Distribution": report["comparative_analysis"]["sentiment_distribution"],
        "Common Topics": ", ".join(report["comparative_analysis"]["common_topics"]),
        "Summary": report["comparative_analysis"]["summary"]
    }
    return articles_output, analysis_output, report["audio"]

iface = gr.Interface(
    fn=process_company,
    inputs=gr.Textbox(label="Company Name", placeholder="Enter a company name (e.g., Tesla)"),
    outputs=[
        gr.Dataframe(label="Articles"),
        gr.JSON(label="Comparative Analysis"),
        gr.Audio(label="Hindi Summary")
    ],
    title="News Summarization and TTS"
)
iface.launch()
