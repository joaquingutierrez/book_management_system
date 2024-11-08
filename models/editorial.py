class Editorial:
    def __init__ (self, id, name):
        self.id = self.__validateId(id)
        self.name = self.__validateName(name)
        self.is_active = True

    
    def __validateName(self, name):
        name = name.strip()
        if not isinstance(name, str) or not 3 <= len(name) <= 40:
            raise ValueError("El nombre del género debe tener entre 3 y 40 caracteres")
        return name.ljust(40)
    
    def __validateId(self, id):
        if isinstance(id, str):
            try:
                id = int(id)
            except ValueError:
                raise ValueError("El id debe ser un número entero válido.")
        if not 1 <= id:
            raise ValueError("El id del género debe ser un número mayor a 1 entero.")
        return int(id)