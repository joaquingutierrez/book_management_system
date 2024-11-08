class Author:
    def __init__ (self, id, first_name, last_name):
        self.id = self.__validateId(id)
        self.fist_name = self.__validateName(first_name)
        self.last_name = self.__validateName(last_name)
        self.is_active = True

    
    def __validateName(self, name):
        name = name.strip()
        if not isinstance(name, str) or not 3 <= len(name) <= 30:
            raise ValueError("El nombre del género debe tener entre 3 y 30 caracteres")
        return name.ljust(30)
    
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
        return f"ID: {self.id} - Nombre: {self.fist_name} {self.last_name}"