import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PG Admission", page_icon="Picture1.png")
st.image("Picture1.png", width=150,)
st.title("Online Postgraduate Admission 🏫")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.image("PG_admission.png", width=350,)
external_link = "https://aastmtic2.aast.edu/PG_admission/"
st.markdown(f"Redirecting to [{external_link}]({external_link})")
