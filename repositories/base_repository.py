import pickle
import io
import os
import os.path

class BaseRepository:
    def __init__ (self, db_path):
        self.db_path = db_path

    def add(self, item):
        try:
            with open(self.db_path, "ab") as f:
                pickle.dump(item, f)
                return item.id
        except Exception as e:
            print(f"Error al guardar el elemento: {e}")
            return None

    def delete(self, id):
        try:
            fp = self.searchById(id)
            if fp is None:
                raise Exception(f"Elemento con ID: {id} no encontrado.")
            with open(self.db_path, "r+b") as f:
                f.seek(fp, io.SEEK_SET)
                item = pickle.load(f)
                item.is_active = False
                f.seek(fp, io.SEEK_SET)
                pickle.dump(item, f)
                return id
        except Exception as e:
            print(f"Error al eliminar el libro: {e}")
            return None

    def update(self, updated_item):
        try:
            fp = self.searchById(updated_item.id)
            if not fp:
                raise Exception(f"ELemento con ID: {updated_item.id} no encontrado.")
            with open(self.db_path, "r+b") as f:
                f.seek(fp, io.SEEK_SET)
                pickle.dump(updated_item, f)
                return updated_item.id
        except Exception as e:
            print(f"Error al modificar el elemento: {e}")
            return None

    def searchById(self, id):
        try:
            with open(self.db_path, "rb") as f:
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    fp = f.tell()
                    item = pickle.load(f)
                    if item.id == id:
                        return fp
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None
    
    def getAll(self):
        try:
            result = []
            with open(self.db_path, "rb") as f:
                f.seek(0, io.SEEK_SET)
                s = os.path.getsize(self.db_path)
                while f.tell() < s:
                    item = pickle.load(f)
                    if item.is_active:
                        result.append(item)
                return result
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
        return None