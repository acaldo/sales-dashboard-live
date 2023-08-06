import pandas as pd
import plotly.express as px
import streamlit as st

#emoji
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:",layout="wide")


# read excel
def get_data_from_excel():
    df = pd.read_excel(
        io="data/supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    return df

df = get_data_from_excel()

st.dataframe(df)



# Sidebar

st.sidebar.header("Please filter Here:")
city = st.sidebar.multiselect(
    'Select the City:',
    options=df['City'].unique(),
    default=df['City'].unique(),
    
)

city = st.sidebar.multiselect(
    'Select the City:',
    options=df['City'].unique(),
    default=df['City'].unique(),
    
)