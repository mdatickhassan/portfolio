
from datetime import datetime

import datetime

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import ta
from pages.utlis.plotly_figure import plotly_table, close_chart, candlestick, Moving_average, RSI, MACD

# setting page configuartion
st.set_page_config(
    page_title="Stock Analysis",
    page_icon="page_with_curl",
    layout="wide"
)

st.title("Stock Analysis")

col1, col2, col3 = st.columns(3)

today = datetime.date.today()

with col1:
    ticker = st.text_input("Stock Ticker", "TSLA")
with col2:
    start_date = st.date_input("Choose Start Date", datetime.date(today.year -1, today.month, today.day))
with col3:
   end_date = st.date_input("Choose End Date", datetime.date(today.year, today.month, today.day))
    

st.subheader(ticker)

stock = yf.Ticker(ticker)

st.write(stock.info['longBusinessSummary'])
st.write(stock.info['sector'])
st.write(stock.info['fullTimeEmployees'])
st.write(stock.info['website'])

col1, col2 = st.columns(2)

with col1:
    df = pd.DataFrame(index = ['Market Cap','Beta','EPS', 'PE Ratio'])
    df[''] = [stock.info["marketCap"],stock.info["beta"],stock.info["trailingEps"],stock.info["trailingPE"]]

    fig = plotly_table(df)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    df = pd.DataFrame(index=['Quick Ratio','Revenue per Share','Profit Margins','Debt to Equity','Return on Equity'])
    df[''] = [stock.info["quickRatio"],stock.info["revenuePerShare"],stock.info["profitMargins"],stock.info["debtToEquity"],stock.info["returnOnEquity"]]
    fig = plotly_table(df)
    st.plotly_chart(fig, use_container_width=True)



data = yf.download(ticker, start=start_date, end=end_date)

col1, col2, col3 = st.columns(3)
daily_change = data['Close'].iloc[-1] - data['Close'].iloc[-2]
col1.metric("Daily Change", str(round(data['Close'].iloc[-1],2)), str(round(daily_change,2)))


last_10_df = data.tail(10).sort_index(ascending=False).round(2)
fig_df = plotly_table(last_10_df)

st.write("### Historical data last 10 days")
st.plotly_chart(fig_df, use_container_width=True)


col1, col2, col3, col4, col5, col6, col7 = st.columns(
    [1, 1, 1, 1, 1, 1, 1]
)

num_period = ""

with col1:
    if st.button("1D"):
        num_period = "1d"

with col2:
    if st.button("1M"):
        num_period = "1mo"

with col3:
    if st.button("3M"):
        num_period = "3mo"

with col4:
    if st.button("YTD"):
        num_period = "ytd"

with col5:
    if st.button("1Y"):
        num_period = "1y"

with col6:
    if st.button("5Y"):
        num_period = "5y"

with col7:
    if st.button("MAX"):
        num_period = "max"


col1, col2, col3 = st.columns([1,1,4])
with col1:
    chart_type = st.selectbox('',('Line Chart', 'Candle Stick', 'OHLC'))

with col2:
    if chart_type == 'Candle':

        indicators = st.selectbox('',('RSI', 'MACD'))
    else:
        indicators = st.selectbox('',('RSI', 'MACD', 'Moving Average'))



ticker = yf.Ticker(ticker)
new_df1 = ticker.history(period="max")
data1 = ticker.history(period="max")

if num_period == '':

    if chart_type == "Candle" and indicators == "RSI":
        st.plotly_chart(candlestick(data1, '1y'),use_container_width=True)
        st.plotly_chart(RSI(data1, '1y'), use_container_width=True)


    if chart_type == "Candle" and indicators == "MACD":
        st.plotly_chart(candlestick(data1, '1y'), use_container_width=True)
        st.plotly_chart( MACD(data1, '1y'), use_container_width=True)


    if chart_type == "Line" and indicators == "RSI":
        st.plotly_chart(close_chart(data1, '1y' ),use_container_width=True)
        st.plotly_chart( RSI(data1, '1y'), use_container_width=True)


    if chart_type == "Line" and indicators == "Moving Average":
        st.plotly_chart( Moving_average(data1, '1y'),use_container_width=True)

    if chart_type == "Line" and indicators == "MACD":
        st.plotly_chart(close_chart(data1, '1y'),use_container_width=True)
        st.plotly_chart(MACD(data1, '1y'),use_container_width=True)

else:

    if chart_type == "Candle" and indicators == "RSI":
        st.plotly_chart(candlestick(new_df1),num_period,use_container_width=True)
        st.plotly_chart(RSI(new_df1),num_period,use_container_width=True)

    if chart_type == "Candle" and indicators == "MACD":
        st.plotly_chart(candlestick(new_df1),num_period,use_container_width=True)
        st.plotly_chart(MACD(new_df1),num_period,use_container_width=True)

    if chart_type == "Line" and indicators == "RSI":
        st.plotly_chart( close_chart(new_df1),num_period,use_container_width=True)
        st.plotly_chart(RSI(new_df1),num_period,use_container_width=True)

    if chart_type == "Line" and indicators == "Moving Average":
        st.plotly_chart(Moving_average(new_df1),num_period,use_container_width=True)

    if chart_type == "Line" and indicators == "MACD":
        st.plotly_chart(close_chart(new_df1),num_period,use_container_width=True)
        st.plotly_chart(MACD(new_df1),num_period,use_container_width=True)