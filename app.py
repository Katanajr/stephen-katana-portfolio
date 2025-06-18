import streamlit as st
from PIL import Image
import os
import base64

# Page config
st.set_page_config(page_title="Stephen Katana Portfolio", layout="centered")

# Inject custom CSS
st.markdown("""
    <style>
            body{
            background-color; #ffffff;}
        .main {
            max-width: 800px;
            margin: auto;
            padding-top: 40px;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center;
            color: #1F4E79;
            font-size: 3em;
        }
        h2 {
            text-align: center;
            color: #2874A6;
            font-size: 1.5em;
        }
        p {
            font-size: 18px;
            line-height: 1.6;
            color: #333333;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1>KATANA STEPHEN NGONYO</h1>", unsafe_allow_html=True)
st.markdown("<h2>Welcome to My Portfolio Website</h2>", unsafe_allow_html=True)

# Load and display profile image centered
img_path = os.path.join(os.path.dirname(__file__), "assets", "profile.png")
if os.path.exists(img_path):
    with open(img_path, "rb") as img_file:
        img_bytes = img_file.read()
        encoded = base64.b64encode(img_bytes).decode()
        st.markdown(
            f"""
            <div style='text-align: center; margin: 20px 0;'>
                <img src='data:image/png;base64,{encoded}' width='150'/>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("🖼️ Add `profile.png` in the `assets/` folder.")

# Description
st.markdown("""
<p style="font-size: 18px; line-height: 1.6; color: #ffffff;">
Hi, I'm <strong>Stephen Katana</strong>, a passionate IT professional with experience in programming, support, and project development.<br>
Use the left sidebar to explore different sections of my portfolio.
</p>  
""", unsafe_allow_html=True)
