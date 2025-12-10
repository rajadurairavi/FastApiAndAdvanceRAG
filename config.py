from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DOCUMENTS_DIR: Path = Path("./knowledgebase")  # Add default
    EMBEDDING_MODEL_NAME: str = "all-MiniLM-L6-v2"
    LLM_MODEL_NAME: str = "llama-3.1-8b-instant"
    GROQ_API_KEY: str | None = None
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 100  # Fix typo: OVERPLAP -> OVERLAP
    SEARCH_TOP_K: int = 7
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = 8000  # Should be int, not str
    RELOAD: bool = False

    class Config:  # This should be inside Settings
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()  # Lowercase 'settings'