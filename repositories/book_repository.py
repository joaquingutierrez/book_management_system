import pickle
import io
import os
import os.path

from .base_repository import BaseRepository

class BookRepository(BaseRepository):
    def __init__(self, db_path):
        super().__init__(db_path)

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
    
    def getBooksByGenreId(self, genre_id):
        try:
            with open(self.db_path, "rb") as f:
                books = []
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if book.genre_id == genre_id:
                        books.append(book)
            return books
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getBooksByAuthorId(self, author_id):
        try:
            with open(self.db_path, "rb") as f:
                books = []
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if author_id in book.authors:
                        books.append(book)
            return books
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getBooksByEditorialId(self, editorial_id):
        try:
            with open(self.db_path, "rb") as f:
                books = []
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if book.editorial_id == editorial_id:
                        books.append(book)
            return books
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getBooksByEditorialIdWithinDateRange(self, editorial_id, start_year, end_year):
        try:
            books = []
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if book.editorial_id == editorial_id and start_year <= book.edition_year <= end_year:
                        books.append(book)
            return books
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getAuthorsByEditorialId(self, editorial_id):
        try:
            authors = []
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if book.editorial_id == editorial_id:
                        for author_id in book.authors:
                            if author_id not in authors:
                                authors.append(author_id)
            return authors
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getBooksByYear(self, year):
        try:
            books = []
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if book.edition_year == year:
                        books.append(book)
            return books
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getBooksByWord(self, word):
        try:
            books = []
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    book = pickle.load(f)
                    if word in book.title:
                        books.append(book)
            return books
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None