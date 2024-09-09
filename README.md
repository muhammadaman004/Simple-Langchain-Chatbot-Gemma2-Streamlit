# Langchain Chatbot Demo with Gemma2 💬

This project is a demonstration of a conversational chatbot built using LangChain and the Gemma2 language model. The chatbot is designed to assist users by answering questions and providing relevant information in a chat-like interface using Streamlit.

## 📋 Project Overview

The Langchain Chatbot Demo uses the LangChain framework and the Ollama model Gemma2 to create an interactive chatbot. The chatbot engages with users in real-time, responding to queries with helpful and concise answers.

## 🚀 Features

- **Interactive Chat Interface:** The chatbot provides a smooth chat experience with real-time question-answering capabilities.
- **Customizable Prompt:** Easily adjustable prompts to fine-tune the assistant’s behavior.

## 🛠️ Tech Stack

- **LangChain:** For building the prompt templates and managing interactions with the LLM.
- **Ollama Model (Gemma2):** A large language model used to generate responses.
- **Streamlit:** Used to create an interactive, user-friendly chat interface.
- **Python:** The core language used for development.

## 📦 Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/langchain-chatbot-demo.git
   cd langchain-chatbot-demo

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Download the Gemma2 Model:**

    Ensure you have the Ollama CLI installed on your system. To download the Gemma2 model, run the following command:
    ```bash
    ollama pull gemma2:2b
    ```
    This step is essential to ensure the model is available for the chatbot to use.

5. **Create a .env file:**

    In the root directory, create a .env file and add your API keys:
    ```bash
    LANGCHAIN_API_KEY=your_langchain_api_key
    LANGCHAIN_PROJECT=your_langchain_project

6. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
