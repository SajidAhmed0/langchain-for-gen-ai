from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama

import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="simple API server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

modelOpen = ChatOpenAI()

## ollama llama2
modelLlama = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay aobut {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem aobut {topic} with 100 words") 

add_routes(
    app,
    prompt1 | modelOpen,
    path="/essay"
)

add_routes(
    app,
    prompt2 | modelLlama,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)