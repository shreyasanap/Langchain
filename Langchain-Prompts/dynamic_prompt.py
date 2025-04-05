from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate, load_prompt

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini Flash model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

st.header('Research Tool')

# User input selections
paper_input = st.selectbox(
    "Select Research Paper Name",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers",
     "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Load prompt template
template = load_prompt('template.json')

if st.button('Summarize'):
    if 'model' in locals():  # Ensure model is initialized
        # instead template.invoke & model.invoke we can make it like a chain
        # No need to manually pass output from template.invoke() to model.invoke().
        chain = template | model
        result = chain.invoke({
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input
        })
        st.write(result.content)
    else:
        st.error("Model initialization failed. Check your API key.")
