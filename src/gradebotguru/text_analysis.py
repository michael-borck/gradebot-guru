import textstat  # type: ignore[import-untyped]
from nltk.sentiment import SentimentIntensityAnalyzer  # type: ignore[import-untyped]


def analyze_sentiment(text: str) -> dict[str, float]:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing sentiment scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    # Type ignore for the return since nltk doesn't provide type hints
    return sentiment_scores  # type: ignore[no-any-return]


def analyze_style(text: str) -> dict[str, int | float]:
    """
    Analyze the style of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary containing style metrics.
    """
    readability = textstat.flesch_reading_ease(text)
    word_count = len(text.split())

    return {"word_count": word_count, "readability": readability}
