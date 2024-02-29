import streamlit as st
from resume_filter_frontend.backend_client import fetch_filtred_resumes
from settings import IMAGE_PATH


st.title("Resume Filter")
st.image(IMAGE_PATH)

st.markdown("#### Welcome to Resume Filter 🎊🎉 You personal assistant in HR process")
st.text("Choose JSON file with Vacancy and Resumes and press 'Filter Resume' button")

uploaded_file = st.file_uploader("JSON")

if st.button("Filter Resume"):
    if not uploaded_file:
        st.text("Please choose JSON file with Vacancy and Resumes")
        st.stop()

    data: bytes = uploaded_file.read()
    filtred_resumes: list[str] = fetch_filtred_resumes(data)

    st.text(filtred_resumes)
