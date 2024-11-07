class Genre:
    def __init__ (self, id, name):
        self.id = self.__validateId(id)
        self.genre = self.__validateGenreName(name)
    
    def __validateGenreName(self, name):
        name = name.strip()
        if not isinstance(name, str) or not 3 <= len(name) <= 20:
            raise ValueError("El nombre del género debe tener entre 3 y 20 caracteres")
        return name
    
    def __validateId(self, id):
        id = id.strip()
        if not id.isdigit() or not 1 <= int(id):
            raise ValueError("El id del género debe ser un número mayor a 1 entero.")
        return int(id)