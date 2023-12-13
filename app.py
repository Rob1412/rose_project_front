# ----------------------Import libraries----------------------

import requests
import streamlit as st
import time
from PIL import Image

# ----------------------Markdown function----------------------

def formatting(string):
    return f'''<p style="font-family: sans-serif; font-size: 18px; font-weight: bold; text-align: center;">{string}</p>'''

# ----------------------Page config----------------------

st.set_page_config(page_title="The Rose Project!", page_icon="🌹")

# ----------------------Page content----------------------

# URL for back-end API:

url = 'https://roserose4rose-ozkpyxorwq-ew.a.run.app'

# Set background colour (other choices: #EB5890, #EC7776):

st.markdown(
    """
    <style>
    .stApp {
        background-color: #EB5890 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Add logo at top of page:

st.image(".streamlit/rose logo.png", use_column_width=True)

# Add subheader:

st.markdown(
    '''
    <p style="font-family: sans-serif; font-size: 35px; font-weight: bold; text-align: center;">
    An iris-istable flower classification project
    </p>
    ''', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.write("")

# Change font and size

font_style = '''
     <style>
         body {
             font-family: 'PT Sans Narrow', sans-serif;
             font-size: 24px;
         }
     </style>
 '''
st.markdown(font_style, unsafe_allow_html=True)

# File uploader

img_file_buffer = st.file_uploader(label="Upload flower here", label_visibility='collapsed')

st.write("")

# Split into two columns (one for picture of flower, one for Rose's prediction):

col1, col2 = st.columns(2)

col1.markdown(
    """
    <div style="font-family: 'PT Sans Narrow', sans-serif; background-color: #db92b3; font-size: 24px; padding: 10px; border-radius: 10px; text-align: center">
    Your flower:
    </div>
    """, unsafe_allow_html=True)
col1.write("")

col2.markdown(
    """
    <div style="font-family: 'PT Sans Narrow', sans-serif; background-color: #db92b3; font-size: 24px; padding: 10px; border-radius: 10px; text-align: center">
    Rose says:
    </div>
    """, unsafe_allow_html=True)
col2.write("")

if img_file_buffer is None:

    col1.image(".streamlit/offer_flower.png", use_column_width=True)

    col2.image(".streamlit/rose_hi.png", use_column_width=True)

else:

    # Display the image user uploaded in column 1:

    col1.markdown(formatting("Here is the flower you gave to Rose!"), unsafe_allow_html=True)
    col1.image(Image.open(img_file_buffer), use_column_width=True)

    # Give the prediction in column 2:

    with col2:

        placeholder2 = col2.empty()

        placeholder3 = col2.empty()

        with st.spinner("Rose is looking at your flower..."):

            time.sleep(1)

            placeholder = st.empty()

            placeholder.image(".streamlit/rose_curious2_flipped.png")

            # Get bytes from the file buffer
            img_bytes = img_file_buffer.getvalue()

            # Make request to  API
            res = requests.post(url + "/upload_image", files={'img': img_bytes})

            time.sleep(5)

            placeholder.empty()

        if res.status_code == 200:

            returnval = res.json()
            pred_class = returnval['pred_class']
            pred_prob = returnval['pred_prob']
            how_much_pink = returnval['how_much_pink']

            # Display the result
            if pred_prob < 75:
                placeholder2.markdown(formatting("I don't even know what this is!"), unsafe_allow_html=True)
                placeholder3.image(Image.open(".streamlit/rose_flower_sad.png"), use_column_width=True)
            else:
                if pred_class == "rose":
                    if how_much_pink == 2:
                        placeholder2.markdown(formatting("A pink rose! My favourite!"), unsafe_allow_html=True)
                        placeholder3.image(Image.open(".streamlit/rose_super_awesome.png"), use_column_width=True)
                    else:
                        placeholder2.markdown(formatting("It's a rose, but it's not pink, is it?"), unsafe_allow_html=True)
                        placeholder3.image(Image.open(".streamlit/rose_not_impressed.png"), use_column_width=True)
                else:
                    if how_much_pink == 2:
                        placeholder2.markdown(formatting(f"This is a {pred_class}; at least it's pink!"), unsafe_allow_html=True)
                        placeholder3.image(Image.open(".streamlit/rose_question_mark.png"), use_column_width=True)
                    else:
                        placeholder2.markdown(formatting(f"This is a {pred_class}; it's not even pink!"), unsafe_allow_html=True)
                        placeholder3.image(Image.open(".streamlit/rose_no.png"), use_column_width=True)
        else:
            placeholder2.markdown("**Oops**, something went wrong 😓 Please try again.")
