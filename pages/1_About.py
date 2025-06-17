import streamlit as st

# Set page configuration
st.set_page_config(page_title="Stephen Katana | About", layout="centered")

# Inject CSS styling
st.markdown("""
    <style>
        .main {
            max-width: 800px;
            margin: auto;
            padding-top: 50px;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center;
            color: #1F4E79;
        }
        p {
            font-size: 18px;
            line-height: 1.6;
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>About</h1>", unsafe_allow_html=True)

# Body text
st.markdown("""
<p>
I'm <strong>Stephen Katana</strong>, an IT professional with a degree in <strong>Computer Science</strong>.<br>
I have a deep passion for technology, software development, and problem-solving.<br>
I'm committed to <strong>continuous learning</strong> and using my skills to build practical solutions.
</p>
""", unsafe_allow_html=True)

