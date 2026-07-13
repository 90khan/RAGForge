from abc import ABC, abstractmethod
from pathlib import Path

from models.document import Document


class BaseLoader(ABC):

    @abstractmethod
    def load(self, file_path: Path) -> Document:
        pass
