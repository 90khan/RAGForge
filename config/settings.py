from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass
class Settings:
    app_name: str = os.getenv("APP_NAME", "RAGForge")

    llm_provider: str = os.getenv(
        "LLM_PROVIDER",
        "ollama",
    )

    hf_model: str = os.getenv(
        "HF_MODEL",
        "Qwen/Qwen2.5-1.5B-Instruct",
    )

    ollama_model: str = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2",
    )

    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-small-en-v1.5",
    )

    vector_path: Path = BASE_DIR / "data" / "vectorstore"

    upload_path: Path = BASE_DIR / "data" / "uploads"

    cache_path: Path = BASE_DIR / "data" / "cache"


settings = Settings()

settings.vector_path.mkdir(parents=True, exist_ok=True)
settings.upload_path.mkdir(parents=True, exist_ok=True)
settings.cache_path.mkdir(parents=True, exist_ok=True)