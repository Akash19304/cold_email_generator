import streamlit as st

st.title("Cold Email Generator")
url_input = st.text_input("Enter URL of job: ")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager, blah blah blah", language='markdown')