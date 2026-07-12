from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass(slots=True)
class Settings:

    app_name: str = "RAGForge"

    ollama_model: str = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2"
    )

    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-small-en-v1.5"
    )

    chunk_size: int = 500

    chunk_overlap: int = 100

    top_k: int = 5

    max_new_tokens: int = 512

    vector_path: Path = BASE_DIR / "data" / "vectorstore"

    upload_path: Path = BASE_DIR / "data" / "uploads"


settings = Settings()

settings.vector_path.mkdir(
    parents=True,
    exist_ok=True,
)

settings.upload_path.mkdir(
    parents=True,
    exist_ok=True,
)