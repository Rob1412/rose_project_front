# ----------------------Importing libraries----------------------

import requests
import streamlit as st
from PIL import Image

# ----------------------Page config--------------------------------------

st.set_page_config(page_title="The Rose Project!", page_icon="🌹")

# ----------------------Sidebar section--------------------------------

url = 'https://roserose4rose-ozkpyxorwq-ew.a.run.app'

# Set background color

st.markdown(
    """
    <style>
    .stApp {
        background-color: #EB5890 !important; /* Pink color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

##EB5890
##EC7776

logo_column = st.image("rose_avatar/rose logo.png", use_column_width=True)
#logo_column.image("rose_avatar/Rose logo.png", use_column_width=True)

st.markdown('<p style="font-family: \'PT Sans Narrow\', sans-serif; font-size: 38px; font-weight: bold; text-align: center;">An iris-istable flower classification project</p>',
            unsafe_allow_html=True)

# Upload image
img_file_buffer = st.file_uploader('Upload an image of a flower of your choice')

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

if img_file_buffer is not None:

    col1, col2 = st.columns(2)

    with col1:
        # Display the image user uploaded
        st.image(Image.open(img_file_buffer), caption="Here's the image you uploaded ☝️")

    with col2:
        with st.spinner("Wait for it..."):
            # Get bytes from the file buffer
            img_bytes = img_file_buffer.getvalue()

            # Make request to  API
            res = requests.post(url + "/upload_image", files={'img': img_bytes})

            if res.status_code == 200:
                # Display the image returned by the API
                st.write(res.json())
            else:
                st.markdown("**Oops**, something went wrong 😓 Please try again.")


c1, c2 = st.columns(2)
# Placeholder image for the right side
placeholder_image_path = ".streamlit/rose_hi.png"

# Display images side by side
c2.subheader("Rose says:")
c2.image(".streamlit/rose_curious2_flipped.png", use_column_width=True)

c1.subheader("Your flower")
c1.image(Image.open(placeholder_image_path), use_column_width=True)





# Create two columns: one for the image and one for the text
#image_column, text_column = st.columns([1, 2])

# Display the image in the left column
#image_column.image(".streamlit/rose.gif", use_column_width=True)

# Set the style for the text in the right column
#text_column.markdown(
#     """
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
#         h1 {
#             font-family: 'Homemade Apple', cursive;
#             font-size: 48px;
#             color: #000000;
#             text-align: center;
#         }
#         p {
#             font-family: 'Roboto', sans-serif;
#             font-size: 24px;
#             color: #333333;
#             text-align: center;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Display the title and subtitle in the right column
#text_column.markdown(
#     """
#     <h1>
#         The Rose Project!
#     </h1>
#     """,
#     unsafe_allow_html=True
# )

# #text_column.markdown(
#     """
#     <p>
#         An iris-istable flower classification project
#     </p>
#     """,
#     unsafe_allow_html=True
# )
