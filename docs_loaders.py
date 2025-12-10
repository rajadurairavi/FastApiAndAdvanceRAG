# docs_loaders.py
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from config import settings

def load_all_documents():
    docs_dir = settings.DOCUMENTS_DIR
    documents = []
    
    # Load all PDF files
    for pdf_file in docs_dir.glob("*.pdf"):
        loader = PyPDFLoader(str(pdf_file))
        documents.extend(loader.load())
    
    # Load all text files
    for txt_file in docs_dir.glob("*.txt"):
        loader = TextLoader(str(txt_file))
        documents.extend(loader.load())
    
    return documents