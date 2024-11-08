from models.book import Book
from models.genre import Genre
from services.book_service import BookService

genre1 = Genre("1", "Ficción")
genre2 = Genre("2", "Ciencia")
genre3 = Genre("3", "Fantasía")
genre4 = Genre("4", "Histórico")

book1 = Book("Cien años de soledad", ["Gabriel García Márquez"], "417", "978-84-376-0494-7", "1967", "Editorial Sudamericana", "1")
book2 = Book("El nombre de la rosa", ["Umberto Eco"], "512", "978-84-376-0495-4", "1980", "Editorial Planeta", "4")
book3 = Book("Fundación", ["Isaac Asimov"], "298", "978-0-553-80468-3", "1951", "Editorial El Aleph", "2")
book4 = Book("Harry Potter y la piedra filosofal", ["J.K. Rowling"], "309", "978-0-7475-3269-9", "1997", "Editorial Salamandra", "3")
book5 = Book("1984", ["George Orwell"], "328", "978-0-452-28423-4", "1949", "Editorial Seix Barral", "1")
book6 = Book("El hobbit", ["J.R.R. Tolkien"], "310", "978-0-618-00221-4", "1937", "Editorial Minotauro", "3")
book7 = Book("El psicoanalista", ["John Katzenbach"], "528", "978-84-397-4011-7", "2002", "Editorial Debolsillo", "1")
book8 = Book("Los juegos del hambre", ["Suzanne Collins"], "374", "978-0-439-02352-8", "2008", "Editorial Scholastic", "2")
book9 = Book("El código Da Vinci", ["Dan Brown"], "689", "978-0-385-50420-1", "2003", "Editorial Doubleday", "4")
book10 = Book("La sombra del viento", ["Carlos Ruiz Zafón"], "487", "978-84-670-1183-8", "2001", "Editorial Planeta", "4")

book_service = BookService("data/books")

def cargarLibros():
    book_service.addBook(book1)
    book_service.addBook(book2)
    book_service.addBook(book3)
    book_service.addBook(book4)
    book_service.addBook(book5)
    book_service.addBook(book6)
    book_service.addBook(book7)
    book_service.addBook(book8)
    book_service.addBook(book9)
    book_service.addBook(book10)

""" cargarLibros() """

""" book_service.deleteBook(book4.isbn) """


""" bookByTitle = book_service.getBookByTitle("El psicoanalista")
print(bookByTitle) """

all_books = book_service.getAllBooks()
for book in all_books:
    print(book)

""" book5.title = "1985"
book_service.updateBook(book5) """
