import streamlit as st
from langchain_helper import generate
st.title("Restraunt Name Generator")
cuisune=st.sidebar.text_input("**Cuisine ?**")#("Indian", "Italian", "Mexican", "Arabic", "American"))




if cuisune:
    response=generate(cuisune)
    st.header(response["restruant_name"].strip())
    menu=response["menu_items"].split(",")
    st.write("**Menu Items**")
    for item in menu:
        st.write("-",item)
