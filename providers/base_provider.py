from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
        max_new_tokens: int = 256,
    ) -> str:
        pass

    @abstractmethod
    def health_check(self) -> bool:
        pass