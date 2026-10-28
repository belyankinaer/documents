from .document import Document


class Report(Document):
    def __init__(self, title: str, author: str, period: str = "Q1"):
        super().__init__(title, author)
        self._period = period

    def process(self) -> str:
        return f"Отчет '{self._title}' ({self._author}) за {self._period}: данные собраны и проверены"
