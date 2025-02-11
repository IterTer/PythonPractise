import streamlit as st
from PIL import Image


with st.expander("Start Camera"):
    # Start the camera
    camera_image=st.camera_input("Camera")


if camera_image:
    img = Image.open(camera_image)

    # Converting image to grayscale
    gray_img = img.convert("L")

    # Render image to the webpage
    st.image(gray_img)