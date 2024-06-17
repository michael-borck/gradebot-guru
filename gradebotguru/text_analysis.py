import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import textstat


def analyze_sentiment(text: str) -> dict:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores


def analyze_style(text: str) -> dict:
    """
    Analyze the style of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing style metrics.
    """
    readability = textstat.flesch_reading_ease(text)
    word_count = len(text.split())

    return {
        "word_count": word_count,
        "readability": readability
    }
