import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def detect_tone(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    # Interpret sentiment_scores to get the tone (positive, negative, neutral)
    # You can define your own logic based on the scores.
    return tone

