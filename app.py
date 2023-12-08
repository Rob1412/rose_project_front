# ----------------------Importing libraries----------------------

import streamlit as st
from streamlit_pills import pills
import pandas as pd
import numpy as np
from PIL import Image
import cv2
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
import os

# Imports for AgGrid
from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

# ----------------------Importing utils.py----------------------

import io
import snowflake as sf
from snowflake import connector
# Third-party libraries
from utils import (
    connect_to_snowflake,
    load_data_to_snowflake,
    load_data_to_postgres,
    connect_to_postgres
)
# ----------------------Page config--------------------------------------

st.set_page_config(page_title="The Rose Project!", page_icon="🌹")

# ----------------------Sidebar section--------------------------------

# Define the base URI of the API
#   - Potential sources are in `.streamlit/secrets.toml` or in the Secrets section
#     on Streamlit Cloud
#   - The source selected is based on the shell variable passend when launching streamlit
#     (shortcuts are included in Makefile). By default it takes the cloud API url
#if 'API_URI' in os.environ:
#    BASE_URI = st.secrets[os.environ.get('API_URI')]
#else:
#    BASE_URI = st.secrets['cloud_api_uri']
# Add a '/' at the end if it's not there
#BASE_URI = BASE_URI if BASE_URI.endswith('/') else BASE_URI + '/'
# Define the url to be used by requests.get to get a prediction (adapt if needed)
#url = BASE_URI + 'predict'


import requests
from dotenv import load_dotenv


# Example local Docker container URL
# url = 'http://api:8000'
# Example localhost development URL
# url = 'http://localhost:8000'
load_dotenv()
url = 'https://roserose4rose-ozkpyxorwq-ew.a.run.app'


# Set background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFC0CB !important; /* Pink color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create two columns: one for the image and one for the text
image_column, text_column = st.columns([1, 2])

# Display the image in the left column
image_column.image(".streamlit/rose.gif", use_column_width=True)

# Set the style for the text in the right column
text_column.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        h1 {
            font-family: 'Homemade Apple', cursive;
            font-size: 48px;
            color: #000000;
            text-align: center;
        }
        p {
            font-family: 'Roboto', sans-serif;
            font-size: 24px;
            color: #333333;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the title and subtitle in the right column
text_column.markdown(
    """
    <h1>
        The Rose Project!
    </h1>
    """,
    unsafe_allow_html=True
)

text_column.markdown(
    """
    <p>
        An iris-istable flower classification project
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("### Let's do a simple flower recognition 👇")
img_file_buffer = st.file_uploader('Upload an image')

if img_file_buffer is not None:

  col1, col2 = st.columns(2)

  with col1:
    ### Display the image user uploaded
    st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️")

  with col2:
    with st.spinner("Wait for it..."):
      ### Get bytes from the file buffer
      img_bytes = img_file_buffer.getvalue()

      ### Make request to  API (stream=True to stream response as bytes)
      res = requests.post(url + "/upload_image", files={'img': img_bytes})

      #if res.status_code == 200:
        ### Display the image returned by the API
      st.write(res.json())
      #else:
      #  st.markdown("**Oops**, something went wrong 😓 Please try again.")
      #  print(res.status_code, res.content)




c1, c2 = st.columns(2)
# Placeholder image for the right side
placeholder_image_path = ".streamlit/placeholder.png"

# Display images side by side
c2.subheader("Uploaded Image")
c2.image(".streamlit/isit.jpg", use_column_width=True)

c1.subheader("Placeholder Image")
c1.image(Image.open(placeholder_image_path), use_column_width=True)
