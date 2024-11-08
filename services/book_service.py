from repositories.book_repository import BookRepository

class BookService:
    def __init__ (self, db_path):
        self.book_repository = BookRepository(db_path)
    
    def addBook(self, book):
        result = self.book_repository.searchBookByIsbn(book.isbn)
        if result is None:
            id = self.book_repository.add(book)
            return id
        print("Error al agregar el libro")

    def deleteBook(self, id):
        result = self.book_repository.searchById(id)
        if result is not None:
            id = self.book_repository.delete(id)
            return id
        print("Error al eliminar el libro")


    def getBookByTitle(self, title):
        result = self.book_repository.getBookByTitle(title)
        if result:
            return result
        print("Error al buscar el libro")

    def updateBook(self, updated_book):
        result = self.book_repository.searchById(updated_book.id)
        if result:
            return self.book_repository.update(updated_book)
        print("Error al actualizar el libro")

    def getAllBooks(self):
        result = self.book_repository.getAll()
        if result:
            return result
        print("Error, no fue posible cargar los libros.")