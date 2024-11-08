from models.genre import Genre
from models.editorial import Editorial
from models.author import Author
from models.book import Book

from services.genre_service import GenreService
from services.editorial_service import EditorialService
from services.author_service import AuthorService
from services.book_service import BookService

from repositories.ids_repository import IdsRepository

genre_service = GenreService("data/genres")
editorial_service = EditorialService("data/editorials")
author_service = AuthorService("data/authors")
book_service = BookService("data/books")
ids_repository = IdsRepository("data/ids")


def menu():
    op = 0
    while op != 9:
        print("Menu principal")
        print("1. Menu de Géneros de libros")
        print("2. Menu de Editoriales")
        print("3. Menu de Autores")
        print("4. Menu de Libros")
        print("9. Salir")
        op = int(input('\t\tIngrese número de la opción elegida: '))

        if op == 1:
            genreMenu()
        elif op == 2:
            print("Menu de Editoriales")
        elif op == 3:
            print("Menu de Autores")
        elif op == 4:
            print("Menu de Libros")
        elif op == 9:
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def genreMenu():
    op = 0
    while op != 9:
        print("Menu de Géneros de libros")
        print("1. Agregar un Género")
        print("2. Eliminar un Género")
        print("3. Modificar un Género")
        print("4. Lista de Géneros")
        print("9. Salir")
        op = int(input('\nIngrese número de la opción elegida: '))

        if op == 1:
            print("\n\tAgregar un Género")
            name = input("Ingrese el nombre del género: ")
            id = ids_repository.getGenreId() + 1
            newGenre = Genre(id, name)
            genre_service.add(newGenre)
            ids_repository.updateGenreId(id)
        elif op == 2:
            print("\n\tEliminar un Género")
            id = int(input("Ingrese el id del género: "))
            while not isinstance(id, int) or not int(id) >= 1:
                print("Por favor, introduzca un número mayor o igual a 1")
                id = input("Ingrese el id del género: ")
            genre_service.delete(int(id))
        elif op == 3:
            print("\n\tModificar un Género")
            id = input("Ingrese el id del género o 0 para salir: ")
            while True and id != 0:
                newName = input("Ingrese el nuevo nombre del género: ")
                try:
                    updated_Genre = Genre(id, newName)
                    genre_service.update(updated_Genre)
                    break
                except Exception as e:
                    print(f"Error al crear el Género: {e}")
                print("Por favor, introduzca un número mayor o igual a 1")
                id = input("Ingrese el id del género o 0 para salir: ")
        elif op == 4:
            print("Lista de Géneros")
            genres = genre_service.getAll()
            if not genres:
                print("No hay géneros carcados")
            else:
                for genre in genres:
                    print(genre)
        elif op == 5:
            print("¿Seguro que quiere depurar los datos?")
            sub_op = input("S/N")
            if sub_op.upper() == "S":
                genre_service.purge_inactive()
        elif op == 9:
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida, intente de nuevo.")