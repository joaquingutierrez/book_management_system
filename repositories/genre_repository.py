import pickle
import io
import os
import os.path

from .base_repository import BaseRepository

class GenreRepository(BaseRepository):
    def __init__(self, db_path):
        super().__init__(db_path)

    def getGenreByName(self, name):
        try:
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    genre = pickle.load(f)
                    if genre.name == name:
                        return genre
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None