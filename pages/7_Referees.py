import streamlit as st

st.title("REFEREES")

st.markdown("""
**DR. VANCY KEBUT**  
H.O.D – DEPARTMENT OF COMPUTER SCIENCE AND INFORMATICS  
KARATINA UNIVERSITY  
Email: vkebut@karu.ac.ke  
Phone: +254 710 453622

**MADAM LIZ MURABU**  
HEAD OF TRAINING – KEMRI WELLCOME TRUST RESEARCH PROGRAMME  
Phone: +254 752 256753
""")
st.markdown("""
    <style>
        a {
            text-decoration: none;
            font-weight: bold;
            color: #1F4E79;
        }
        a:hover {
            color: #ff6600;
        }
    </style>
""", unsafe_allow_html=True)
with open("assets/Stephen_Katana_CV.pdf", "rb") as file:
    st.download_button(
        label="📄 Download My CV",
        data=file,
        file_name="Stephen_Katana_CV.pdf",
        mime="application/pdf"
    )
