# News-Summarization-and-Text-to-Speech-Application


## Overview
This project is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. The application uses web scraping, NLP, and audio synthesis to deliver structured insights.

## Features
✅ Extracts news articles related to a given company using web scraping (BeautifulSoup).
✅ Summarizes the news content using a Transformer-based model (BART).
✅ Performs sentiment analysis to classify news as Positive, Negative, or Neutral.
✅ Conducts a comparative sentiment analysis across multiple news sources.
✅ Converts the final summary into Hindi speech using gTTS.
✅ Provides a web-based interface using Gradio.
✅ Exposes APIs using FastAPI for backend processing.
✅ Deployable on Hugging Face Spaces.

## Tech Stack
- **Python**
- **FastAPI** (Backend APIs)
- **Gradio** (Frontend UI)
- **BeautifulSoup** (Web Scraping)
- **Transformers** (Summarization & NLP)
- **VADER Sentiment Analyzer**
- **gTTS** (Text-to-Speech)
- **Uvicorn** (ASGI server for FastAPI)

## Installation
To set up and run the project locally, follow these steps:

### Prerequisites
Ensure you have Python 3.8+ installed on your system.

### Clone the Repository
```sh
git clone https://github.com/your-username/news-summarization-tts.git
cd news-summarization-tts
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run FastAPI Backend
```sh
uvicorn main:app --host 127.0.0.1 --port 8000
```

### Run Gradio Frontend
```sh
Gradio run app.py
```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/news/{company}` | Fetches news articles, performs sentiment analysis, and generates Hindi TTS |

Example:
```sh
curl http://127.0.0.1:8000/news/Tesla
```

## Expected Output Format
```json
{
    "Company": "Tesla",
    "Articles": [
        {
            "Title": "Tesla's New Model Breaks Sales Records",
            "Summary": "Tesla's latest EV sees record sales in Q3...",
            "Sentiment": "Positive"
        }
    ],
    "Comparative Sentiment Analysis": {
        "Positive": 1,
        "Negative": 0,
        "Neutral": 0
    },
    "Audio File": "output.mp3"
}
```

## Deployment
To deploy the application on **Hugging Face Spaces**, follow these steps:
1. Create a new **Hugging Face Space**.
2. Select **`Gradio`** as the framework.
3. Upload the project files.
4. Configure the `requirements.txt`.
5. Deploy and test the application.

## Assumptions & Limitations
- The application scrapes news from Google News and may not retrieve full article content.
- The sentiment analysis is based on the VADER lexicon, which works best on social media-like text.
- TTS conversion is limited to Hindi using `gTTS`, which requires an internet connection.


