import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

# Define the LangChain prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Your name is Jerry's Assistant."),
    ("user", "User query: {query}")
])
# Function to get response from Ollama
def get_response(user_input):
    llm = Ollama(model="mistral")  # Ensure you have Ollama installed and the model downloaded
    formatted_prompt = prompt.format(query=user_input)
    return llm.invoke(formatted_prompt)
# Streamlit UI
def main():
    st.title("Jerry's AI Assistant")
    st.write("Ask me anything!")

    user_input = st.text_input("Enter your query:")

    if st.button("Submit"):
        if user_input:
            response = get_response(user_input)
            st.write("### AI Response:")
            st.write(response)
        else:
            st.warning("Please enter a query!")
if __name__ == "__main__":
    main()
