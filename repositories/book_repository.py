import pickle
import io
import os
import os.path

class BookRepository:
    def __init__ (self, db_path):
        self.db_path = db_path

    def addBook(self, book):
        try:
            with open(self.db_path, "ab") as f:
                pickle.dump(book, f)
                return book.isbn
        except Exception as e:
            print(f"Error al guardar el libro: {e}")
            return None

    def deleteBook(self, isbn):
        try:
            fp = self.searchBookByIsbn(isbn)
            if fp is None:
                raise Exception(f"Libro con ISBN {isbn} no encontrado.")
            with open(self.db_path, "r+b") as f:
                f.seek(fp, io.SEEK_SET)
                book = pickle.load(f)
                book.is_active = False
                f.seek(fp, io.SEEK_SET)
                pickle.dump(book, f)
                return isbn
        except Exception as e:
            print(f"Error al eliminar el libro: {e}")
            return None

    def getBookByTitle(self, title):
        try:
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if book.title == title:
                        return book
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None

    def updateBook(self, updated_book):
        try:
            fp = self.searchBookByIsbn(updated_book.isbn)
            if not fp:
                raise Exception(f"Libro con ISBN {updated_book.isbn} no encontrado.")
            with open(self.db_path, "r+b") as f:
                f.seek(fp, io.SEEK_SET)
                pickle.dump(updated_book, f)
                return updated_book.isbn
        except Exception as e:
            print(f"Error al modificar el libro: {e}")
            return None

    def searchBookByIsbn(self, isbn):
        try:
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    fp = f.tell()
                    book = pickle.load(f)
                    if book.isbn == isbn:
                        return fp
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getAllBooks(self):
        try:
            result = []
            with open(self.db_path, "rb") as f:
                f.seek(0, io.SEEK_SET)
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if book.is_active:
                        result.append(book)
                return result
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None