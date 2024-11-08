class Author:
    def __init__ (self, id, name):
        self.id = self.__validateId(id)
        self.name = self.__validateName(name)
        self.is_active = True

    
    def __validateName(self, name):
        name = name.strip()
        if not isinstance(name, str) or not 3 <= len(name) <= 30:
            raise ValueError("El nombre del género debe tener entre 3 y 30 caracteres")
        return name
    
    def __validateId(self, id):
        id = id.strip()
        if not id.isdigit() or not 1 <= int(id):
            raise ValueError("El id del género debe ser un número mayor a 1 entero.")
        return int(id)