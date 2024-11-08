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
    
    def getBooksByGenreId(self, genre_id):
        try:
            return self.repository.getBooksByGenreId(genre_id)
        except ValueError as e:
            print(f"Error al actualizar el elemento: {e}")
    
    def getBooksByAuthorId(self, author_id):
        try:
            return self.repository.getBooksByAuthorId(author_id)
        except ValueError as e:
            print(f"Error al actualizar el elemento: {e}")
    
    def getBooksByEditorialId(self, editorial_id):
        try:
            return self.repository.getBooksByEditorialId(editorial_id)
        except ValueError as e:
            print(f"Error al actualizar el elemento: {e}")
    
    def getBooksByEditorialIdWithinDateRange(self, editorial_id, start_year, end_year):
        try:
            return self.repository.getBooksByEditorialIdWithinDateRange(editorial_id, start_year, end_year)
        except ValueError as e:
            print(f"Error al actualizar el elemento: {e}")

    def getBooksByYear(self, year):
        try:
            return self.repository.getBooksByYear(year)
        except ValueError as e:
            print(f"Error al actualizar el elemento: {e}")
    
    def getBooksByWord(self, word):
        try:
            return self.repository.getBooksByWord(word)
        except ValueError as e:
            print(f"Error al actualizar el elemento: {e}")
    
    def getAuthorsByEditorialId(self, editorial_id):
        try:
            return self.repository.getAuthorsByEditorialId(editorial_id)
        except ValueError as e:
            print(f"Error al actualizar el elemento: {e}")