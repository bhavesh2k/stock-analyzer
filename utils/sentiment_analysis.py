import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def fetch_news_headlines(ticker):
    url = f"https://www.google.com/search?q={ticker}+stock+news&tbm=nws"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    headlines = [a.text for a in soup.select('h3')]
    return headlines[:10]

def analyze_sentiment(headlines):
    sentiments = [analyzer.polarity_scores(h) for h in headlines]
    return sentiments
