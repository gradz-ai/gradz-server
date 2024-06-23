import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.document_loader import DocumentLoader
from services.index_manager import IndexManager
from services.query_engine import QueryEngine

import logging
import sys

import os

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')


app = FastAPI(
    title="Document Query API",
    description="An API to query documents using a pre-built index.",
    version="1.0.0"
)

data_dir = "../data/telc-deutsche-a2-b1/"
index_dir = "../data/indexes/telc-deutsche-a2-b1/"

document_loader = DocumentLoader(data_dir)
index_manager = IndexManager(index_dir)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str
@app.on_event("startup")
async def startup_event():
    try:
        documents = document_loader.load_documents()
        index_manager.load_or_create_index(documents=documents)
        logging.info("Index loaded successfully.")
    except Exception as e:
        print(f"Error during startup: {e}")

@app.post("/query", response_model=dict, summary="Query the index", description="Query the document index and get a response.")
async def query_index(request: QueryRequest):
    try:
        index = index_manager.get_index()
        query_engine = QueryEngine(index)
        response = query_engine.query(request.query)
        logging.info(f"Query: {request.query}, Response: {response}")
        return {"response": QueryResponse(response=str(response))}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
