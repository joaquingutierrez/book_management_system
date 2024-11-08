import pickle
import io
import os
import os.path

class IdsRepository:
    def __init__ (self, db_path):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            with open(self.db_path, "wb") as f:
                ids = {
                    'genre_id': 0,
                    'editorial_id': 0,
                    'author_id': 0,
                    'book_id': 0
                }
                pickle.dump(ids, f)

    def _get_id(self, key):
        try:
            with open(self.db_path, "rb") as f:
                ids = pickle.load(f)
                return ids.get(key, None)
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getGenreId(self):
        return self._get_id('genre_id')
    
    def getEditorialId(self):
        return self._get_id('editorial_id')

    def getAuthorId(self):
        return self._get_id('author_id')

    def getBookId(self):
        return self._get_id('book_id')


    def _update_id(self, key, newId):
        try:
            with open(self.db_path, "rb") as f:
                ids = pickle.load(f)
            if key in ids:
                ids[key] = newId
            with open(self.db_path, "wb") as f:
                pickle.dump(ids, f)
            return newId
        except Exception as e:
            print(f"Error al leer o escribir el archivo: {e}")
        return None

    def updateGenreId(self, newId):
        return self._update_id('genre_id', newId)

    def updateEditorialId(self, newId):
        return self._update_id('editorial_id', newId)

    def updateAuthorId(self, newId):
        return self._update_id('author_id', newId)

    def updateBookId(self, newId):
        return self._update_id('book_id', newId)