from pathlib import Path

from loaders.docx_loader import DOCXLoader
from loaders.pdf_loader import PDFLoader


class LoaderFactory:

    @staticmethod
    def create(
        file_path: str | Path,
    ):

        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            return PDFLoader()

        if suffix == ".docx":
            return DOCXLoader()

        raise ValueError(f"Unsupported file type: {suffix}")
