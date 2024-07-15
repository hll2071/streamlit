import streamlit as st
if st.button("Save"):
    if 'title' not in st.session_state :
        title = st.text_input("Movie title")