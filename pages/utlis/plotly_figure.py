from datetime import datetime
from turtle import pd

import plotly.graph_objects as go
import streamlit as st
import pandas_ta as ta
import yfinance


# def plotly_table(dataframe):
#     headerColor = 'grey'
#     rowEvenColor ='#f8fafd'
#     rowOddColor = '#e1efff'

#     fig = go.Figure(data=[go.Table(
#         header=dict(
#             values=["<b><b>"]+["<b>"+str(i)[:10]+"<b>" for i in dataframe.columns],
#             line_color='#0078ff',fill_color='#0078ff',
#             align="center",font=dict(color="white", size=15),height=35,
#         ),
#         cells=dict(
#             values=[["<b>"+str(i)+"<b>" for i in dataframe.index]]+[dataframe[i]for i in dataframe.columns], fill_color=[[rowOddColor, rowEvenColor] * len(dataframe)],
#             align="left", line_color="white", font=dict(color="black", size=15)
#         ))
#         ])

#     fig.update_layout(height=400, margin=dict(l=0, r=0, t=0, b=0))
#     return fig


import plotly.graph_objects as go


def plotly_table(dataframe):

    headerColor = "#808080"
    rowEvenColor = "#f8fafd"
    rowOddColor = "#e1efff"

    # Create alternating row colors
    row_colors = []

    for i in range(len(dataframe)):
        if i % 2 == 0:
            row_colors.append(rowEvenColor)
        else:
            row_colors.append(rowOddColor)

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=["<b></b>"]
                    + [f"<b>{str(col)[:10]}</b>" for col in dataframe.columns],
                    line_color="#0078ff",
                    fill_color="#0078ff",
                    align="center",
                    font=dict(color="white", size=15),
                    height=35,
                ),
                cells=dict(
                    values=[
                        [f"<b>{i}</b>" for i in dataframe.index]
                    ]
                    + [
                        dataframe[col].tolist()
                        for col in dataframe.columns
                    ],
                    fill_color=row_colors,
                    align="left",
                    line_color="white",
                    font=dict(color="black", size=15),
                    height=30,
                ),
            )
        ]
    )

    fig.update_layout(
        height=400,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return fig



def filter_data(dataframe, num_period):

    if num_period == "1d":
        date = dataframe.index[-1] - pd.tseries.offsets.BDay(1)

    elif num_period == "5d":
        date = dataframe.index[-1] - pd.tseries.offsets.BDay(5)

    elif num_period == "1mo":
        date = dataframe.index[-1] - pd.tseries.offsets.DateOffset(months=1)

    elif num_period == "3mo":
        date = dataframe.index[-1] - pd.tseries.offsets.DateOffset(months=3)

    elif num_period == "6mo":
        date = dataframe.index[-1] - pd.tseries.offsets.DateOffset(months=6)

    elif num_period == "1y":
        date = dataframe.index[-1] - pd.tseries.offsets.DateOffset(years=1)

    elif num_period == "5y":
        date = dataframe.index[-1] - pd.tseries.offsets.DateOffset(years=5)

    elif num_period == "ytd":
        date = pd.Timestamp(
            datetime.datetime(dataframe.index[-1].year, 1, 1)
        )

    else:
        date = dataframe.index[0]

    return dataframe.reset_index()[dataframe.reset_index()["Date"] > date]






def close_chart(dataframe, num_period= False):

    if num_period:
        dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Open"],
            mode="lines",
            name="Open",
            line=dict(width=2, color="#9b2f77")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Close"],
            mode="lines",
            name="Close",
            line=dict(width=2, color="black")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["High"],
            mode="lines",
            name="High",
            line=dict(width=2, color="#0077ff")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Low"],
            mode="lines",
            name="Low",
            line=dict(width=2, color="red")
        )
    )

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="white",
        legend=dict(
            yanchor="top",
            xanchor="right"
        )
    )

    return fig


def candlestick(dataframe, num_period):

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=dataframe["Date"],
            open=dataframe["Open"],
            high=dataframe["High"],
            low=dataframe["Low"],
            close=dataframe["Close"]
        )
    )

    fig.update_layout(
        showlegend=False,
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    return fig

def RSI(dataframe, num_period):

    dataframe["RSI"] = ta.rsi(dataframe["Close"])

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["RSI"],
            name="RSI",
            marker_color="orange",
            line=dict(
                width=2,
                color="orange"
            )
        )
    )

    # Overbought line
    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=[70] * len(dataframe),
            name="Overbought",
            marker_color="red",
            line=dict(
                width=2,
                color="red",
                dash="dash"
            )
        )
    )

    # Oversold line
    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=[30] * len(dataframe),
            name="Oversold",
            marker_color="#7f00ff",
            line=dict(
                width=2,
                color="#7f00ff",
                dash="dash"
            )
        )
    )

    fig.update_layout(
    yaxis_range=[0, 100],
    height=200,
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(l=0, r=20, t=20, b=0),
    legend=dict(
        orientation="h",
        yanchor="top",
        y=1.02,
        xanchor="right",
        x=1
    )
)

    return fig




def Moving_average(dataframe, num_period):

    dataframe["SMA"] = ta.sma(dataframe["Close"], 50)

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Open"],
            mode="lines",
            name="Open",
            line=dict(width=2, color="#9b2f77")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Close"],
            mode="lines",
            name="Close",
            line=dict(width=2, color="black")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["High"],
            mode="lines",
            name="High",
            line=dict(width=2, color="#0077ff")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["Low"],
            mode="lines",
            name="Low",
            line=dict(width=2, color="red")
        )
    )

    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["SMA"],
            mode="lines",
            name="SMA",
            line=dict(width=2, color="#ff8c00")
        )
    )

    fig.update_xaxes(rangeslider_visible=True)

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=20, t=20, b=0),
        plot_bgcolor="white",
        paper_bgcolor="white",
        legend=dict(
            yanchor="top",
            xanchor="right"
        )
    )

    return fig


def MACD(dataframe, num_period):

    macd = ta.macd(dataframe["Close"]).iloc[:, 0]
    macd_signal = ta.macd(dataframe["Close"]).iloc[:, 1]
    macd_hist = ta.macd(dataframe["Close"]).iloc[:, 2]

    dataframe["MACD"] = macd
    dataframe["MACD_Signal"] = macd_signal
    dataframe["MACD_Hist"] = macd_hist

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()

    # MACD line
    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["MACD"],
            name="MACD",
            mode="lines",
            line=dict(
                width=2,
                color="orange"
            )
        )
    )

    # Signal line
    fig.add_trace(
        go.Scatter(
            x=dataframe["Date"],
            y=dataframe["MACD_Signal"],
            name="Signal",
            mode="lines",
            line=dict(
                width=2,
                color="red",
                dash="dash"
            )
        )
    )

    # Histogram
    colors = [
        "green" if value >= 0 else "red"
        for value in dataframe["MACD_Hist"]
    ]

    fig.add_trace(
        go.Bar(
            x=dataframe["Date"],
            y=dataframe["MACD_Hist"],
            name="Histogram",
            marker_color=colors
        )
    )

    fig.update_layout(
        height=300,
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(
            l=0,
            r=20,
            t=20,
            b=0
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    return fig
















































