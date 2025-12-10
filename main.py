from fastapi import FastAPI
from pydantic import BaseModel
from rag import ask_question
from config import settings
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class QuestionRequest(BaseModel):
    question : str

app = FastAPI(
    title="RAG Chatbot",
    description="ask question about accessibility")

@app.post("/ask")
def ask_questionapi(user_input:QuestionRequest):
    logging.info(f"Question received: {user_input.question[:50]}...")  # Log the question
    result = ask_question(user_input.question)
    logging.info("Question answered successfully")  # Log success
    return result

@app.get("/")
def root():  # No async needed
    logging.info("Health check accessed") 
    return {"message": "RAG Chatbot is running!"}

if __name__ == "__main__":
    import uvicorn
    logging.info("Starting FastAPI server...")
    uvicorn.run("main:app", host=settings.APP_HOST, port=settings.APP_PORT, reload=settings.RELOAD)
