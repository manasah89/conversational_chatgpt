import os
from constant import openai_key  # Make sure this module provides your OpenAI API key
from langchain_google_genai import GoogleGenerativeAI
import streamlit as st

# Ensure the OpenAI API key is set correctly
os.environ['GOOGLE_API_KEY'] = ""  # Ensure `openai_key` is the correct OpenAI key

# Streamlit framework
st.title("Langchain demo with OpenAI API")
input_text = st.text_input("Search the topic you want")

# OpenAI LLMs
llm = GoogleGenerativeAI(model="gemini-pro",temperature=0.8)

if input_text:
    st.write(llm(input_text))
