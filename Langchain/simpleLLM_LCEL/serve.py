from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from  langserve import add_routes

load_dotenv()

qroq_apikey = os.getenv("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=qroq_apikey)


system_template = "Translate the following into {language}"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("user", "{text}")
    ]
)

parser = StrOutputParser()

chain = prompt|model|parser


#app definition

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server using langchain runnable interfaces",
)



add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)




