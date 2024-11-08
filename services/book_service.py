from repositories.book_repository import BookRepository

class BookService:
    def __init__ (self, db_path):
        self.book_repository = BookRepository(db_path)
    
    def addBook(self, book):
        result = self.book_repository.searchBookByIsbn(book.isbn)
        if result is None:
            isbn = self.book_repository.addBook(book)
            return isbn
        print("Error al agregar el libro")

    def deleteBook(self, isbn):
        result = self.book_repository.searchBookByIsbn(isbn)
        if result is not None:
            isbn = self.book_repository.deleteBook(isbn)
            return isbn
        print("Error al eliminar el libro")


    def getBookByTitle(self, title):
        result = self.book_repository.getBookByTitle(title)
        if result:
            return result
        print("Error al buscar el libro")

    def updateBook(self, updated_book):
        result = self.book_repository.searchBookByIsbn(updated_book.isbn)
        if result:
            return self.book_repository.updateBook(updated_book)
        print("Error al actualizar el libro")

    def getAllBooks(self):
        result = self.book_repository.getAllBooks()
        if result:
            return result
        print("Error, no fue posible cargar los libros.")