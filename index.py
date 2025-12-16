import streamlit as st
import cv2
import numpy as np

st.markdown("""
    <style>
    img {
        border: 1px solid #dbdbdb;
        min-width:200px
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Correcting Nonuniform Illumination",
    layout="centered"
)

st.title("Correcting Nonuniform Illumination")
st.write("Aplikasi untuk memperbaiki pencahayaan citra yang tidak merata")

uploaded = st.file_uploader(
    "Upload citra (jpg / png)",
    type=["jpg", "jpeg", "png"]
)

if uploaded:
    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    st.subheader("Citra Asli")
    st.image(img, clamp=True, channels="GRAY")

    # Estimasi iluminasi
    illumination = cv2.GaussianBlur(img, (0, 0), sigmaX=50, sigmaY=50)

    # Koreksi
    corrected = cv2.divide(img, illumination, scale=255)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Estimasi Iluminasi")
        st.image(illumination, clamp=True, channels="GRAY")
    with col2:
        st.subheader("Hasil Koreksi")
        st.image(corrected, clamp=True, channels="GRAY")

    st.success("Koreksi pencahayaan berhasil.")
