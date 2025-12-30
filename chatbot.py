from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
import os
load_dotenv()
#Streamlit_page_setup
st.set_page_config(
    page_title="ChatBot",
    page_icon="🤖",
    layout="centered",
)
st.title("💬 Generative AI Chatbot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

user_prompt=st.chat_input("Ask Chatbot...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user", "content":user_prompt})
    response=llm.invoke(
        input=[{"role":"assistant", "content": "you are a helpful chatbot"}, *st.session_state.chat_history]
    )
    assitant_response=response.content
    st.session_state.chat_history.append({"role":"assistant","content": assitant_response})
    with st.chat_message("assistant"):
        st.markdown(assitant_response)