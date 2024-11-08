import pickle
import io
import os
import os.path

from .base_repository import BaseRepository

class EditorialRepository(BaseRepository):
    def __init__(self, db_path):
        super().__init__(db_path)
        
    def __init__ (self, db_path):
        self.db_path = db_path

    def getEditorialByName(self, name):
        try:
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    editorial = pickle.load(f)
                    if editorial.name == name:
                        return editorial
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None