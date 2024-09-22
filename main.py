import streamlit as st
from database.rules import connect_to_database
from workflows.comments_workflow import commentsapp
col1, col2 = st.columns(2)

connect_to_database()

with col1:
    st.subheader("Comments")
    text_input = st.text_input("Enter comments")
    if st.button("Submit Text"):
        st.write(f"You entered: {text_input}")
        user_input = {"messages": [text_input], "userid": "Anish"}
        for event in commentsapp.stream(user_input):
            st.write(event.values())
                

with col2:
    st.subheader("Attachments")
    file_type = st.selectbox("Select file type", ["PDF", "JPG"])
    if st.button("Submit File Type"):
        st.write(f"You selected: {file_type}")