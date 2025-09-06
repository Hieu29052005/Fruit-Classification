import streamlit as st
from detect import detect_fruit

st.title("Fruit Detection with Bounding Boxes")

uploaded_file = st.file_uploader("Upload a fruit image", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Run detection
    output_img = detect_fruit(uploaded_file)

    st.image(output_img, caption="Detected Fruits", use_container_width=True)

