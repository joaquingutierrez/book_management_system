from repositories.editorial_repository import EditorialRepository
from .base_services import BaseService

class EditorialService(BaseService):
    def __init__ (self, db_path):
        super().__init__(EditorialRepository(db_path))

    def getEditorialByName(self, name):
        result = self.repository.getEditorialByName(name)
        if result:
            return result
        print("Error al buscar la editorial")