import streamlit as st

st.set_page_config(
    page_title="Trading App",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)


st.title("Trading Guide App :bar_chart:")

st.header("we provide the greatest platform  for you to collect all information prior to investing in stocks")

st.image("app.png")

st.markdown("## We provide the following services")

st.markdown("### :one: stock information")
st.write(" Through this page, you can see all the information about stock")


st.markdown("### :two: stock prediction")
st.write(" you can explore predicted closing price for the next 30 days based on historical stock data and advanced forecasting models.")

st.markdown("### :three: CAPM Returns")
st.write(" Discover how the capital asset pricing model (CAPM) calculates the expected returns of the different stocks asset based on its risk and the risk-free rate of return. This page provides you with a comprehensive understanding of the relationship between risk and return in the stock market.")


st.markdown("### :four: CAPM Beta")
st.write(" Calculates Beta and expected returns for Individual stocks")

























