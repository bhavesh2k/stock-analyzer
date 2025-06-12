import streamlit as st
from utils.stock_data import fetch_stock_data, add_moving_averages
from utils.sentiment_analysis import fetch_news_headlines, analyze_sentiment
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="📊 Stock Market Analyzer", layout="wide")

st.title("📈 Stock Market Analyzer")
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):", "AAPL")

if ticker:
    df = fetch_stock_data(ticker)
    df = add_moving_averages(df)

    st.subheader(f"Price & Moving Averages for {ticker}")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close Price'))
    for col in df.columns:
        if 'SMA' in col:
            fig.add_trace(go.Scatter(x=df['Date'], y=df[col], name=col))
    st.plotly_chart(fig, use_container_width=True)

    # Sentiment Section
    st.subheader("🗞 Sentiment from News Headlines")
    headlines = fetch_news_headlines(ticker)
    sentiments = analyze_sentiment(headlines)

    sentiment_df = pd.DataFrame(sentiments)
    sentiment_df['Headline'] = headlines
    st.dataframe(sentiment_df[['Headline', 'compound', 'pos', 'neu', 'neg']])
