import streamlit as st
from PIL import Image
from matplotlib import image
import os



# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR)

IMAGE_PATH = os.path.join(dir_of_interest, "churn.png")

st.title('Hello! welcome to Streamlit Project')
st.header('Im :red[Irfan]')
st.subheader('Project on Churn_Prediction')




btn_click = st.button("Click me..!")

if btn_click == True:
    st.subheader("You view me :racehorse:")
    image = Image.open(IMAGE_PATH)
    st.image(image, caption='Process for ML Model')
    st.success('This is a success message!', icon="✅")



