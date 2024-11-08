from repositories.genre_repository import GenreRepository

class BookService:
    def __init__ (self, db_path):
        super().__init__(GenreRepository(db_path))

    def getGenreByName(self, name):
        result = self.repository.getGenreByName(name)
        if result:
            return result
        print("Error al buscar el género")