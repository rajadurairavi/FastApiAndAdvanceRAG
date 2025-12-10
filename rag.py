import os
import logging
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from config import settings
from prompts import ACCESSIBILITY_PROMPT
from embedding_creator import create_and_save_embeddings

# Global variables for lazy loading
_retriever = None
_chain = None

def load_vector_store(vector_store_path="./vector_store"):
    """Load FAISS vector store from disk, create if it doesn't exist"""
    if not os.path.exists(vector_store_path):
        print("Vector store not found. Creating embeddings...")
        create_and_save_embeddings(vector_store_path)
    
    # Load embeddings model
    embedding = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL_NAME)
    
    # Load vector store from disk
    vectorstore = FAISS.load_local(vector_store_path, embedding, allow_dangerous_deserialization=True)
    print("Vector store loaded successfully from disk")
    
    return vectorstore

def get_rag_chain():
    """Initialize and return the RAG chain (lazy loading)"""
    global _retriever, _chain
    
    if _chain is not None:
        return _chain
    
    # Load vector store
    vectorstore = load_vector_store()
    
    # Create retriever
    _retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": settings.SEARCH_TOP_K})
    
    # Initialize LLM
    llm = ChatGroq(groq_api_key=settings.GROQ_API_KEY, model_name=settings.LLM_MODEL_NAME)
    
    # Create prompts
    prompts = ChatPromptTemplate.from_template(ACCESSIBILITY_PROMPT)
    
    # Build chain
    _chain = {"context": _retriever, "question": RunnablePassthrough()} | prompts | llm | StrOutputParser()
    
    return _chain


def ask_question(question: str):
    """Process a question using the RAG system"""
    logging.info(f"Processing question: {question[:50]}...")
    
    # Get the RAG chain (lazy loading)
    chain = get_rag_chain()
    
    # Invoke the chain with the question
    response = chain.invoke(question)
    logging.info("Question processed successfully")
    
    return {
        "question": question,
        "answer": response
    }

