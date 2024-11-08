import pickle
import io
import os
import os.path

class GenreRepository:
    def __init__ (self, db_path):
        self.db_path = db_path

    def addGenre(self, genre):
        try:
            with open(self.db_path, "ab") as f:
                pickle.dump(genre, f)
                return genre.id
        except Exception as e:
            print(f"Error al guardar el libro: {e}")
            return None

    def deleteGenre(self, id):
        try:
            fp = self.searchGenreById(id)
            if fp is None:
                raise Exception(f"Género con id: {id} no encontrado.")
            with open(self.db_path, "r+b") as f:
                f.seek(fp, io.SEEK_SET)
                genre = pickle.load(f)
                genre.is_active = False
                f.seek(fp, io.SEEK_SET)
                pickle.dump(genre, f)
                return id
        except Exception as e:
            print(f"Error al eliminar el libro: {e}")
            return None

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

    def updateGenre(self, updated_genre):
        try:
            fp = self.searchGenreById(updated_genre.id)
            if not fp:
                raise Exception(f"Género con ID: {updated_genre.id} no encontrado.")
            with open(self.db_path, "r+b") as f:
                f.seek(fp, io.SEEK_SET)
                pickle.dump(updated_genre, f)
                return updated_genre.id
        except Exception as e:
            print(f"Error al modificar el género: {e}")
            return None

    def searchGenreById(self, id):
        try:
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    fp = f.tell()
                    genre = pickle.load(f)
                    if genre.id == id:
                        return fp
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getAllGenres(self):
        try:
            result = []
            with open(self.db_path, "rb") as f:
                f.seek(0, io.SEEK_SET)
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    genre = pickle.load(f)
                    if genre.is_active:
                        result.append(genre)
                return result
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None