import streamlit as st

if st.button("load"):
    st.write(st.session_state.title)