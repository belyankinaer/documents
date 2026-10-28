from .document import Document


class Article(Document):
    def __init__(self, title: str, author: str, journal: str = "Журнал"):
        super().__init__(title, author)
        self._journal = journal

    def process(self) -> str:
        return f"Статья '{self._title}' ({self._author}) опубликована в '{self._journal}'"
