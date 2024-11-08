class BaseService:
    def __init__ (self, repository):
        self.repository = repository
    
    def add(self, item):
        result = self.repository.searchById(item.id)
        if result is None:
            id = self.repository.add(item)
            return id
        print("Error al agregar el elemento")

    def delete(self, id):
        result = self.repository.searchById(id)
        if result is not None:
            id = self.repository.delete(id)
            return id
        print("Error al eliminar el elemento")

    def update(self, updated_item):
        result = self.repository.searchById(updated_item.id)
        if result:
            return self.repository.update(updated_item)
        print("Error al actualizar el elemento")

    def getAll(self):
        result = self.book_repository.getAll()
        if result:
            return result
        print("Error, no fue posible cargar los elementos.")