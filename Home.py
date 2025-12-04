
import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

st.write("# Welcome to my App! ")

st.markdown(
    """
    This is the **Home Page**   \n
    this app consists two features \n
    1-  EDA TOOL \n
    2-House prediction model
    
    """
)

st.sidebar.success("Select a page above.")


