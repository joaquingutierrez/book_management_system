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