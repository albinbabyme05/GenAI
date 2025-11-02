import streamlit as st
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


from dotenv import load_dotenv
load_dotenv()



#lansmith tracking
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHIAN_PROJECT"] = os.getenv("LANGCHIAN_PROJECT")
# os.environ["LANGCHIAN_TRACING_V2"] = "true"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are pwoerful super computer answer the user queries "),
        ("user", "Questions : {question}")
    ]
)


def generate_response(question, llm_model, temperature, max_token):
    llm = Ollama(model=llm_model)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question" : question})
    
    return answer


# select ollama model
llm_model = st.sidebar.selectbox("Select a model", ["moondream", "llama3"])

#adjust responce params
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=0.7)
max_token = st.sidebar.slider("Max Token", min_value=50, max_value=150)

#user interface
st.write("Go ahead and ask any question ")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input, llm_model, temperature, max_token)
    st.write(response)
    
elif user_input:
    st.warning("Something gone wrong")

else:
    st.write("Please provide the user input")









