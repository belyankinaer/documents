from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author

    @property
    def get_title(self) -> str:
        return self._title

    @abstractmethod
    def process(self) -> str:
        pass
