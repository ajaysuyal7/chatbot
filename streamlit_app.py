import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

# Show title and description.
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Chatbot with Groq")
st.write(
    "This is a simple chatbot that uses Groq's API to generate responses. "
)

    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.(display previous message)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.

    # user input
if prompt : 
    st.chat_input("Type Here"):
        # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

        '''headers={
            "Authorization": f'Bearer {GROQ_API_KEY}",
            "Content_type': 'application/json",
        }
            
        body = {
            'model'='llama3-8b-8192'
            'message'=[
                {'role':m['role'],'content':m['content']} 
                for m in st.session_state.messages ]
        }'''

        # Generate a response using the groq API.
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages],
        stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        
        # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response["choices"][0]["message"]["content"])
    st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
