from .document import Document


class Letter(Document):
    def __init__(self, title: str, author: str, recipient: str = "Адресат"):
        super().__init__(title, author)
        self._recipient = recipient

    def process(self) -> str:
        return f"Письмо '{self._title}' ({self._author}) отправлено получателю {self._recipient}"
