import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY="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"

# Initialize Groq client
client = Groq(api_key=API_KEY)

# Configure Streamlit page
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Chatbot with Groq")
st.write("This is a simple chatbot that uses Groq's API to generate responses.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
prompt = st.chat_input("Type here...")

if prompt:
    # Store and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Stream assistant response
    with st.chat_message("assistant"):
        response_stream = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=st.session_state.messages,
            stream=True,
        )
        full_response = ""
        response_container = st.empty()
        for chunk in response_stream:
            delta = chunk.choices[0].delta.content or ""
            full_response += delta
            response_container.markdown(full_response)
    
    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": full_response})
