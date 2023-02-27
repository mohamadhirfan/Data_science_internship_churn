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

IMAGE_PATH = os.path.join(dir_of_interest, "images", "model.png")
DATA_PATH = os.path.join(dir_of_interest, "data", "churn_dataset.csv")

st.title("Dashboard - Churn Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

IMAGE_PATH = os.path.join(dir_of_interest, "images", "model_0.png")
img = image.imread(IMAGE_PATH)
st.image(img)
IMAGE_PATH = os.path.join(dir_of_interest, "images", "model_01.png")
img = image.imread(IMAGE_PATH)
st.image(img)

IMAGE_PATH = os.path.join(dir_of_interest, "images", "model_1.png")
img = image.imread(IMAGE_PATH)
st.image(img)
IMAGE_PATH = os.path.join(dir_of_interest, "images", "model_02.png")
img = image.imread(IMAGE_PATH)
st.image(img)
IMAGE_PATH = os.path.join(dir_of_interest, "images", "model_03.png")
img = image.imread(IMAGE_PATH)
st.image(img)





