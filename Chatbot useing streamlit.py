from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import os
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.header("Hugging Face Chat Model ")
# Hugging Face API key
user_input=st.text_input("ENTER YOUR PROMPT")


# Create a chat prompt template
chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("human", "{input}"),
    ]
)

# fill the template with user input
filled_prompt = chat_template.format_prompt(input=user_input)

# initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Generate Response"):
    api_key = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
    # Hugging Face model endpoint
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.2-3B-Instruct",
        task="text-generation",
        huggingfacehub_api_token=api_key,
        temperature=0.7,
        max_new_tokens=100
    )
    # Uncomment the line below if you want to use an API key
    model = ChatHuggingFace(llm=llm)
    result = model.invoke(filled_prompt)  # Invoke the model with the filled prompt
    # Append the user input and model response to chat history
    st.session_state.chat_history.append({"role":"user","content": user_input})
    st.session_state.chat_history.append({"role":"assistant","content": result.content})

# Display chat history
if st.session_state.chat_history:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.write(f"You: {message['content']}")
        else:
            st.write(f"Assistant: {message['content']}")