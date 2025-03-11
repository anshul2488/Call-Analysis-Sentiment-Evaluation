from transformers import pipeline

def analyze_sentiment(text):
    """Analyzes sentiment of the given text."""
    sentiment_analyzer = pipeline("sentiment-analysis")
    return sentiment_analyzer(text)[0] if len(text) > 5 else {"label": "NEUTRAL", "score": 0.5}
