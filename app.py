import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the questions asked."),
        ("user", "Question: {question}")
    ]
)
st.set_page_config(page_title="Langchain Chatbot", page_icon="💬")
st.title("Langchain Chatbot Demo with Gemma2")

st.write("Welcome to the Langchain Chatbot! Ask any question, and I'll be here to help.")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
input_text = st.text_input(
    "Type your question here...",
    placeholder="Ask anything you'd like to know!",
)
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input_text:
    st.session_state.chat_history.append(("user", input_text))
    response = chain.invoke({"question": input_text})
    st.session_state.chat_history.append(("assistant", response))
    st.session_state.input_text = "" 

for role, text in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")
