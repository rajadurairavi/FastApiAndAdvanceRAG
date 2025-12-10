import os
import logging
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from config import settings
from pathlib import Path
from docs_loaders import load_all_documents

def create_and_save_embeddings(vector_store_path="./vector_store"):
    """
    Create embeddings from documents and save FAISS vector store to disk.
    This should be run once when documents change.
    """
    # Check if vector store already exists
    if os.path.exists(vector_store_path):
        print(f"Vector store already exists at {vector_store_path}")
        return
    
    # Documents loading steps
    try:
        docs = load_all_documents()
        logging.info(f"Successfully loaded {len(docs)} documents")
        print("documents loaded successfully")
    except Exception as e:
        logging.error(f"Failed to load documents: {e}")
        print(f"Documents are not loaded {e}")
        raise

    # Split the documents
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n", "\n\n", " ", ""],
        chunk_size=settings.CHUNK_SIZE, 
        chunk_overlap=settings.CHUNK_OVERLAP
    )

    splitdocs = splitter.split_documents(docs)
    print(f"Split documents into {len(splitdocs)} chunks")

    # Embedding the split tokens
    embedding = HuggingFaceEmbeddings(model_name=settings.EMBEDDING_MODEL_NAME)

    # Store the embeddings
    try:
        vectorstore = FAISS.from_documents(documents=splitdocs, embedding=embedding)
        # Save to disk
        vectorstore.save_local(vector_store_path)
        print(f"embedding values stored in vector store and saved to {vector_store_path}")
    except Exception as e:
        print(f"Embedding values are not stored: {e}")
        raise

if __name__ == "__main__":
    # Run this script to create embeddings
    create_and_save_embeddings()