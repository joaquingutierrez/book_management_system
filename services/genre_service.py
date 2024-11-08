from repositories.genre_repository import GenreRepository

class BookService:
    def __init__ (self, db_path):
        self.genre_repository = GenreRepository(db_path)
    
    def addGenre(self, genre):
        result = self.genre_repository.searchGenreById(genre.id)
        if result is None:
            id = self.genre_repository.addGenre(genre)
            return id
        print("Error al agregar el género")

    def deleteGenre(self, id):
        result = self.genre_repository.searchGenreById(id)
        if result is not None:
            id = self.genre_repository.deleteGenre(id)
            return id
        print("Error al eliminar el género")


    def getGenreByName(self, name):
        result = self.genre_repository.getGenreByName(name)
        if result:
            return result
        print("Error al buscar el género")

    def updateGenre(self, updated_genre):
        result = self.genre_repository.searchGenreById(updated_genre.id)
        if result:
            return self.genre_repository.updateGenre(updated_genre)
        print("Error al actualizar el género")

    def getAllGenres(self):
        result = self.genre_repository.getAllGenres()
        if result:
            return result
        print("Error, no fue posible cargar los géneros.")