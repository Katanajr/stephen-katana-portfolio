import streamlit as st

st.title("REFEREES")

st.markdown("""
**DR. VANCY KEBUT**  
H.O.D  
DEPARTMENT OF COMPUTER SCIENCE AND INFORMATICS    
KARATINA UNIVERSITY  
NYERI  
EMAIL: vkebut@karu.ac.ke | vancychep@yahoo.com  
TEL NO: +254 721 657 646

**MADAM LIZ MURABU**  
STUDENTS ADMINISTRATOR-IDEAL  
 KEMRI WELLCOME TRUST RESEARCH PROGRAMME  
KILIFI  
EMAIL:lmurabu@gmail.com | LMurabu@kemri-wellcome.org    
TEL NO: +254 710 453 622
            
**MR. SAMUEL SIFUNA**  
MONITORING, EVALUATION, ACCOUNTABILITY, RESEARCH AND LEARNING LEAD    
KEMRI WELLCOME TRUST RESEARCH PROGRAMME   
KILIFI     
EMAIL: samuelsifuna9@gmail.com | SSifuna@kemri-wellcome.org  
TEL NO: +254 728 433961 
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
