import streamlit as st
from classify_comment import is_this_a_spam

# Streamlit app title and description
st.title("Comment Classification App")
st.write("Enter a comment to classify it as spam or not spam.")

# User input for comment
comment = st.text_input("Enter your comment:")

if comment:
    # Button to classify the comment
    if st.button("Classify"):
        answer = is_this_a_spam(comment)
        if answer == '1':
            st.write("Result: Not Spam")
        else:
            st.write("Result: Spam")
