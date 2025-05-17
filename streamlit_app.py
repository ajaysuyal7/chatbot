import streamlit as st
from groq import GroqClient

# Show title and description.
st.title("💬 Chatbot with Groq")
st.write(
    "This is a simple chatbot that uses Groq's API to generate responses. "
    "To use this app, you need to provide an Groq API key, which you can get [here](https://console.groq.com/docs/api-reference)). "
    "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management

# ask For the API Key Securely
groq_api_key = st.secrets["groq"]["api_key"]

if not groq_api_key:
    st.info("Please add your Groq API key to continue.", icon="🗝️")
else:
    # Create an Groq client.
    client = GroqClient(api_key=Groq_api_key)

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
    if prompt := st.chat_input("What is up?"):
        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the groq API.
        response = client.chat.completions.create(
            model="llama-3",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        
        # Diaplay assistant response
        with st.chat_message("assistant"):
            st.markdown(response["choices"][0]["message"]["content"])
        st.session_state.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
            #response = st.write_stream(stream)
        #st.session_state.messages.append({"role": "assistant", "content": response})
