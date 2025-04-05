from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

st.header('Research Tool')
user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    if user_input:
        if 'model' in locals():  # Check if model is initialized
            result = model.invoke(user_input)
            st.write(result.content)
        else:
            st.error("Model initialization failed. Check your API key.")
    else:
        st.warning("Please enter a prompt.")
