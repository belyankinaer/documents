from .document import Document


class DocumentManager:
    def __init__(self):
        self._documents: list[Document] = []

    def add(self, document: Document) -> None:
        self._documents.append(document)

    def process_all(self) -> list[str]:
        return [document.process() for document in self._documents]
