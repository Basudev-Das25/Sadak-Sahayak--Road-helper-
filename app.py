import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

#Page Config
st.set_page_config(page_title="Sadak Sahayak", page_icon="🛣️")
st.write("Upload an image of a road to detect poyholes and damage.")

#Load Model
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

#Image Uploader
uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption= "Uploaded Image", use_column_width=True)

    if st.button("Analyse Road"):
        with st.spinner("Analyzing road conditions..."):
            results = model(image) #Prediction
            res_plotted = results[0].plot()  #Plot result
            res_image = Image.fromarray(res_plotted[..., ::-1])  #Image from BGR to RGB for display
            st.success("Analysis Completed!")
            st.image(res_image, caption="Detected Potholes", use_column_width=True)

            boxes = results[0].boxes  #Count potholes
            st.metric(label="Potholes Detected", value=len(boxes))

#Footer
st.markdown("---")
st.markdown("Built with YOLOv8 & Streamlit | Project for Safer Indian Roads. ")