# FastAPI Advanced RAG System

A production-ready **Retrieval-Augmented Generation (RAG)** system built with FastAPI that provides intelligent answers about web accessibility using WCAG guidelines.

## 🌟 Features

- **Advanced RAG Pipeline**: Uses LangChain with FAISS vector store for efficient document retrieval
- **FastAPI REST API**: Clean, documented API endpoints with automatic OpenAPI documentation
- **Accessibility Expertise**: Specialized knowledge base focused on WCAG 2.2 guidelines and best practices
- **Performance Optimized**: Lazy loading, vector store persistence, and efficient chunking
- **Configurable**: Environment-based configuration with sensible defaults
- **Production Ready**: Comprehensive logging, error handling, and health checks

## 🏗️ Architecture

```
├── main.py              # FastAPI application entry point
├── rag.py              # RAG system implementation
├── config.py           # Configuration management
├── embedding_creator.py # Vector embeddings creation
├── docs_loaders.py     # Document loading utilities
├── prompts.py          # AI prompt templates
├── knowledgebase/      # Source documents (PDF, TXT)
├── vector_store/       # FAISS vector embeddings
└── .env               # Environment variables
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)
- GROQ API key for LLM access

### Installation

1. **Clone and navigate to the project**:
   ```bash
   cd FastApiAndAdvanceRAG
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install fastapi uvicorn langchain langchain-community langchain-huggingface langchain-groq faiss-cpu pydantic pydantic-settings sentence-transformers pypdf
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   EMBEDDING_MODEL_NAME=all-MiniLM-L6-v2
   LLM_MODEL_NAME=llama-3.1-8b-instant
   CHUNK_SIZE=800
   CHUNK_OVERLAP=100
   SEARCH_TOP_K=7
   APP_HOST=127.0.0.1
   APP_PORT=8000
   RELOAD=False
   ```

5. **Initialize the vector store** (first time only):
   ```bash
   python embedding_creator.py
   ```

6. **Start the server**:
   ```bash
   python main.py
   ```

The API will be available at `http://127.0.0.1:8000`

## 📚 API Documentation

### Endpoints

#### `POST /ask`
Ask questions about web accessibility.

**Request Body**:
```json
{
  "question": "What are the WCAG guidelines for color contrast?"
}
```

**Response**:
```json
{
  "question": "What are the WCAG guidelines for color contrast?",
  "answer": "According to WCAG 2.2 guidelines, color contrast requirements..."
}
```

#### `GET /`
Health check endpoint.

**Response**:
```json
{
  "message": "RAG Chatbot is running!"
}
```

### Interactive Documentation

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 🔧 Configuration

The system uses environment-based configuration through the `config.py` file:

| Variable | Default | Description |
|----------|---------|-------------|
| `DOCUMENTS_DIR` | `./knowledgebase` | Path to source documents |
| `EMBEDDING_MODEL_NAME` | `all-MiniLM-L6-v2` | HuggingFace embedding model |
| `LLM_MODEL_NAME` | `llama-3.1-8b-instant` | GROQ LLM model |
| `GROQ_API_KEY` | `None` | Your GROQ API key |
| `CHUNK_SIZE` | `800` | Document chunk size |
| `CHUNK_OVERLAP` | `100` | Overlap between chunks |
| `SEARCH_TOP_K` | `7` | Number of similar chunks to retrieve |
| `APP_HOST` | `127.0.0.1` | API server host |
| `APP_PORT` | `8000` | API server port |

## 📖 Usage Examples

### Using cURL

```bash
# Ask a question
curl -X POST "http://127.0.0.1:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are the keyboard navigation requirements?"}'

# Health check
curl http://127.0.0.1:8000/
```

### Using Python requests

```python
import requests

# Ask a question
response = requests.post(
    "http://127.0.0.1:8000/ask",
    json={"question": "How do I implement proper alt text for images?"}
)
print(response.json())
```

### Using JavaScript/fetch

```javascript
// Ask a question
fetch('http://127.0.0.1:8000/ask', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    question: 'What are the WCAG success criteria for forms?'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🗂️ Adding New Documents

1. **Add documents** to the `knowledgebase/` directory (supports PDF and TXT files)
2. **Delete the existing vector store**:
   ```bash
   rm -rf vector_store/
   ```
3. **Recreate embeddings**:
   ```bash
   python embedding_creator.py
   ```
4. **Restart the server**

## 🎯 Domain Expertise

This system specializes in **Web Accessibility** and includes knowledge about:

- WCAG 2.2 Guidelines
- Accessibility Best Practices
- Keyboard Navigation
- Screen Reader Compatibility
- Color Contrast Requirements
- Form Accessibility
- ARIA Labels and Roles
- Mobile Accessibility

## 🛠️ Development

### Project Structure

```
FastApiAndAdvanceRAG/
│
├── main.py                 # FastAPI app and routes
├── rag.py                  # RAG system core logic
├── config.py               # Configuration management
├── embedding_creator.py    # Vector store creation
├── docs_loaders.py         # Document loading utilities
├── prompts.py              # AI prompt templates
├── knowledgebase/          # Source documents
│   ├── Accessibility_BestPractices.txt
│   └── Accessibility_Guidelines.pdf
├── vector_store/           # FAISS vector embeddings
│   └── index.faiss
├── .env                    # Environment variables
└── README.md               # This file
```

### Key Components

- **FastAPI**: Web framework for the REST API
- **LangChain**: Framework for building RAG applications
- **FAISS**: Vector similarity search and clustering
- **HuggingFace**: Embedding models
- **GROQ**: Fast LLM inference
- **Pydantic**: Data validation and settings management

## 🔍 How It Works

1. **Document Processing**: Documents are loaded from `knowledgebase/` and split into chunks
2. **Embedding Creation**: Text chunks are converted to vector embeddings using HuggingFace models
3. **Vector Storage**: Embeddings are stored in FAISS index for fast similarity search
4. **Query Processing**: User questions are embedded and matched against stored vectors
5. **Context Retrieval**: Most similar document chunks are retrieved as context
6. **Answer Generation**: LLM generates answers using retrieved context and the user question

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [API Documentation](http://127.0.0.1:8000/docs) when the server is running
2. Review the logs for error messages
3. Ensure your GROQ API key is properly configured
4. Verify all dependencies are installed correctly

## 🔮 Future Enhancements

- [ ] Authentication and user management
- [ ] Conversation history and context
- [ ] Response caching for performance
- [ ] Multi-language support
- [ ] Advanced search filters
- [ ] Real-time document updates
- [ ] Analytics and usage metrics

---

**Built with ❤️ using FastAPI, LangChain, and modern RAG techniques**