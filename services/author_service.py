from repositories.author_repository import AuthorRepository

class AuthorService:
    def __init__ (self, db_path):
        self.author_repository = AuthorRepository(db_path)
    
    def addAuthor(self, author):
        result = self.author_repository.searchById(author.id)
        if result is None:
            id = self.author_repository.add(author)
            return id
        print("Error al agregar el Autor")

    def deleteAuthor(self, id):
        result = self.author_repository.searchById(id)
        if result is not None:
            id = self.author_repository.delete(id)
            return id
        print("Error al eliminar el autor")


    def getAuthorByName(self, name):
        result = self.author_repository.getAuthorByName(name)
        if result:
            return result
        print("Error al buscar el autor")

    def updateAuthor(self, updated_author):
        result = self.author_repository.searchById(updated_author.id)
        if result:
            return self.author_repository.update(updated_author)
        print("Error al actualizar el autor")

    def getAllGenres(self):
        result = self.author_repository.getAll()
        if result:
            return result
        print("Error, no fue posible cargar los autores.")