import streamlit as st
from PIL import Image

# Converting image to grayscale
def convert_to_grayscale(img):
    img = Image.open(img)
    gray_img = img.convert("L")
    return gray_img

st.subheader("Color to Grayscale converter")
uploaded_image = st.file_uploader("Upload Image")


with st.expander("Start Camera"):
    # Start the camera
    camera_image=st.camera_input("Camera")

if uploaded_image:
    gray_img = convert_to_grayscale(uploaded_image)
    st.image(gray_img)

if camera_image:

    gray_img=convert_to_grayscale(camera_image)
    # Render image to the webpage
    st.image(gray_img)