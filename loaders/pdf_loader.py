from pathlib import Path

from pypdf import PdfReader

from loaders.base_loader import BaseLoader
from models.document import Document


class PDFLoader(BaseLoader):

    def load(
        self,
        file_path: Path
    ) -> Document:

        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:

                pages.append(text)

        return Document(
            id=file_path.stem,
            source=file_path,
            text="\n".join(pages)
        )