from repositories.book_repository import BookRepository
from .base_services import BaseService

class BookService(BaseService):
    def __init__ (self, db_path):
        super().__init__(BookRepository(db_path))

    def getBookByTitle(self, title):
        result = self.repository.getBookByTitle(title)
        if result:
            return result
        print("Error al buscar el libro")