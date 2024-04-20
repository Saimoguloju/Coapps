from transformers import pipeline
import streamlit as st

pipe = pipeline('text-classification')

st.title('Sentiment Analysis')

user_input = st.text_input('Enter Your text: ')

if st.button("Get Sentiment"):
    if user_input:
        try:
            result = pipe(user_input)
            st.write("Sentiment: ", result[0]['label'])
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text to analyze.")
