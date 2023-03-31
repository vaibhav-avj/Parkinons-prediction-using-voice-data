# import ..ParkinsonSource

import streamlit as st
from predict_page import show_predict_page
from streamlit_app import showRecordPage
st.sidebar.title('Welcome back!')
page = st.sidebar.selectbox('',("Record Audio","Predict"))


if page == "Record Audio":
    showRecordPage()
elif page == "Predict":
    show_predict_page()