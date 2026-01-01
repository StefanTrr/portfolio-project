import numpy as np
import pandas as pd
import streamlit as stl
import plotly.express as px

#Title
stl.title("Trading Portfolio Dashboard")

#Data read from spreadsheet
sheet_id = "1Y06jKZNi-ocLG5fagqb-2lkZCUOpZKk3EtaK6j81S-w"
data = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")


#Change the 'date' into the right date format and then replace index with the date
data["Date"] = pd.to_datetime(data["Date"], format="%m/%d/%Y")
data.set_index(["Date"] , inplace=True)

#Change the Base value into a float
data["Base"] = data["Base"].str.replace(",", ".", regex=False).astype(float)

#Create the chart using plotly
fig = px.line(data, x = data.index, y = ["Base"], title = "Trading Portfolio Using Invalidated EMH Strategy")
stl.plotly_chart(fig)
stl.caption("rebased to 100")

#Tabs
About, Strategy, Return_data = stl.tabs(["About", "Strategy", "Return Data"])

with About:
    stl.header("What's this?")
    stl.write ("Hey im stefan and this is my personal and active stock portfolio based on a strategy that i built, and you can find more about it in the strategy tab. I started this project to show how my strategy performs againsts various market regime. I will be updating this project every few weeks or days. The portfolio return data will be documented with the highest level of accuracy to ensure it reflects actual and verifiable performance. You can do a reality check in the return data tab to check its reliability. For a side note, i can't disclose some informations about the strategy due to a possible alpha decay. But more updates are coming to this project")
    stl.subheader("Author")
    stl.write("If you have any suggestions or just want to know more about this project, strategy, etc, just message me at @stfntrr or just any other platform in general. btwww, single, M, 20 yo, 170cm, into music and films, hmu ;) AOWKWKWKWKWK")

with Strategy:
    stl.header("Inefficient Market Strategy")
    stl.write("The logic or foundation behind my strategy is built upon the assumption that Indonesian stock market is inefficient (not to be mistaken with weak form efficient). This is because the Indonesia capital market is not yet developed and is still 'immature', this inefficiency causes an anomaly that can be exploited. My strategy is to rebalance the portfolio quarterly using a predetermined criterias. This portfolio will not offer lucrative return but a predictable return that beats the market. So every quarter this portfolio will contain a new set of stocks, furthermore every weighing is equal. Every major update of this strategy will be marked with a time-stamp to better see the difference in performance.")

with Return_data:
    stl.header("Dataset transparency")
    data

stl.write(" ")
stl.caption("updated as of january 2026")

#Favicon & page title
stl.set_page_config(page_title="Portfolio Project")
