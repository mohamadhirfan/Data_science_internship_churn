import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


DATA_PATH = os.path.join(dir_of_interest, "data", "churn_dataset.csv")

st.title("Dashboard - churn Data")


df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the Churn:", df['Churn'].unique())

col1, col2 = st.columns(2)


fig_1 = px.bar(df[df['Churn'] == species], x="InternetService",color='gender')
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.scatter(df[df['Churn'] == species],x="tenure",y="TotalCharges",color="gender")
col2.plotly_chart(fig_2, use_container_width=True)

