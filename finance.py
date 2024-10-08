import streamlit as st
import pandas as pd
import datetime
import yfinance as yf
st.set_page_config("Stock Market")
date=datetime.date.today()
var=st.sidebar.selectbox("Select Ticker Symbol:",options=["NFLX","AAPL","GOOG","AMZN","META"])
list=yf.download(var,start="2024-09-1",end=datetime.date.today())
df=pd.DataFrame(list)
st.header(f"Stocks of {var}->")
st.write(df)
st.subheader("Analyzing open value:")
st.line_chart(df,y='Open')
st.subheader("Analyzing close value of:")
st.line_chart(df,y='Close')
st.subheader("Analyzing Adj Close value with bar chart:")
st.bar_chart(df,y='Adj Close')
#    API_KEY = "10f1f4d38d1025e47ebc8c84cb6d893f"
