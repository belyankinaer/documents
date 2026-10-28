from .article import Article
from .document_manager import DocumentManager
from .letter import Letter
from .report import Report

if __name__ == "__main__":
    manager = DocumentManager()

    manager.add(Report("Годовой отчет", "Иванов", "2026"))
    manager.add(Letter("Приглашение на встречу", "Петров", "Сидоров"))
    manager.add(Article("Полиморфизм в Python", "Смирнова", "Хакер"))

    for result in manager.process_all():
        print(result)
