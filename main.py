import os
from langchain_google_genai import GoogleGenerativeAI
import streamlit as st

# Ensure the OpenAI API key is set correctly
os.environ['GOOGLE_API_KEY'] = "AIzaSyAks1XmPxk_me6XfzcUh3_LrqLcRBZVdYM"  # Ensure `openai_key` is the correct OpenAI key

# Streamlit framework
st.title("Langchain demo with GoogleGenerativeAI")
input_text = st.text_input("Search the topic you want")

# Initialize conversation history
if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []

# Function to update conversation history
def update_conversation_history(user_input, response):
    st.session_state['conversation_history'].append(f"User: {user_input}")
    st.session_state['conversation_history'].append(f"Bot: {response}")
    
# OpenAI LLMs
llm = GoogleGenerativeAI(model="gemini-pro", temperature=0.8)

if input_text:
    # Include conversation history in the input
    conversation_input = "\n".join(st.session_state['conversation_history']) + f"\nUser: {input_text}\nBot:"
    response = llm(conversation_input)
    update_conversation_history(input_text, response)
    st.write(response)
