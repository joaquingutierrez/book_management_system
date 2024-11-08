from repositories.author_repository import AuthorRepository
from .base_services import BaseService

class AuthorService(BaseService):
    def __init__ (self, db_path):
        super().__init__(AuthorRepository(db_path))
    
    def getAuthorByName(self, name):
        result = self.repository.getAuthorByName(name)
        if result:
            return result
        print("Error al buscar el autor")

    def getAuthorsByLastNameFirstLetter(self, letter):
        try:
            return self.repository.getAuthorsByLastNameFirstLetter(letter)
        except ValueError as e:
            print(f"Error al buscar el elemento: {e}")