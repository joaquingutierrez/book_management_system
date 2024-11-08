class Genre:
    def __init__ (self, id, name):
        self.id = self.__validateId(id)
        self.name = self.__validateGenreName(name)
        self.is_active = True

    
    def __validateGenreName(self, name):
        name = name.strip()
        if not isinstance(name, str) or not 3 <= len(name) <= 20:
            raise ValueError("El nombre del género debe tener entre 3 y 20 caracteres")
        return name.ljust(20)
    
    def __validateId(self, id):
        if isinstance(id, str):
            try:
                id = int(id)
            except ValueError:
                raise ValueError("El id debe ser un número entero válido.")
        if not 1 <= id:
            raise ValueError("El id del género debe ser un número mayor a 1 entero.")
        return int(id)
    
    def __str__(self):
        return f"ID: {self.id} - Género: {self.name}"