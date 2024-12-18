class BaseService:
    def __init__ (self, repository):
        self.repository = repository
    
    def add(self, item):
        try:
            result = self.repository.searchById(item.id)
            if result is None:
                id = self.repository.add(item)
                return id
            print("Error al agregar el elemento")
        except Exception as e:
            print("Error al agregar el elemnto: ", e)

    def delete(self, id):
        result = self.repository.searchById(id)
        if result is not None:
            id = self.repository.delete(id)
            return id
        print("Error al eliminar el elemento")

    def update(self, updated_item):
        try:
            result = self.repository.searchById(updated_item.id)
            if result is not None:
                return self.repository.update(updated_item)
        except ValueError as e:
            print(f"Error al actualizar el elemento: {e}")

    def getAll(self):
        result = self.repository.getAll()
        if result:
            return result
        print("Error, no fue posible cargar los elementos.")

    def purge_inactive(self):
        return self.repository.purge_inactive()
    
    def getItemById(self, id):
        result = self.repository.getItemById(id)
        if result is not None:
            return result
        return None