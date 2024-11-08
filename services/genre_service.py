from repositories.genre_repository import GenreRepository
from .base_services import BaseService

class GenreService(BaseService):
    def __init__ (self, db_path):
        super().__init__(GenreRepository(db_path))

    def getGenreByName(self, name):
        result = self.repository.getGenreByName(name)
        if result:
            return result
        print("Error al buscar el género")