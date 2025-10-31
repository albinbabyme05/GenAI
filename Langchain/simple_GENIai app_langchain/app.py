import os
from dotenv import load_dotenv


from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
 
#Langsmith tracking
os.environ["LANGCHIAN_APIKEY"] = os.getenv("LANGCHIAN_APIKEY")
os.environ["LANGCHIAN_PROJECT "] = os.getenv("LANGCHIAN_PROJECT")
os.environ["LANGCHIAN_TRACING_V2"]  = "true"



# prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You are a helpful assistant"),
        ("user", "Question:{question}")
    ]
)


#stramlit frame work

st.title("Langchain demo LLama3")
input_text = st.chat_input("Whta question you have in mind ? ")

#llama model
llm_model = OllamaLLM(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm_model|output_parser


if input_text:
    st.write(chain.invoke({"question" : input_text}))