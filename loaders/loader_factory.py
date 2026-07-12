from pathlib import Path

from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DOCXLoader


class LoaderFactory:

    @staticmethod
    def create(
        file_path: Path
    ):

        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            return PDFLoader()

        if suffix == ".docx":
            return DOCXLoader()

        raise ValueError(
            f"Unsupported file type : {suffix}"
        )