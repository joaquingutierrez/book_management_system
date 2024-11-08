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
            editorialMenu()
        elif op == 3:
            authorMenu()
        elif op == 4:
            bookMenu()
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

def editorialMenu():
    op = 0
    while op != 9:
        print("Menu de Editoriales de libros")
        print("1. Agregar una Editorial")
        print("2. Eliminar una Editorial")
        print("3. Modificar una Editorial")
        print("4. Lista de Editoriales")
        print("9. Salir")
        op = int(input('\nIngrese número de la opción elegida: '))

        if op == 1:
            print("\n\tAgregar una Editorial")
            name = input("Ingrese el nombre de la Editorial: ")
            id = ids_repository.getEditorialId() + 1
            newEditorial = Editorial(id, name)
            editorial_service.add(newEditorial)
            ids_repository.updateEditorialId(id)
        elif op == 2:
            print("\n\tEliminar una Editorial")
            id = int(input("Ingrese el id de la Editorial: "))
            while not isinstance(id, int) or not int(id) >= 1:
                print("Por favor, introduzca un número mayor o igual a 1")
                id = input("Ingrese el id de la Editorial: ")
            editorial_service.delete(int(id))
        elif op == 3:
            print("\n\tModificar una Editorial")
            id = input("Ingrese el id de la editorial o 0 para salir: ")
            while True and id != 0:
                newName = input("Ingrese el nuevo nombre de la editorial: ")
                try:
                    updated_editorial = Editorial(id, newName)
                    editorial_service.update(updated_editorial)
                    break
                except Exception as e:
                    print(f"Error al crear la Editorial: {e}")
                print("Por favor, introduzca un número mayor o igual a 1")
                id = input("Ingrese el id de la Editorial o 0 para salir: ")
        elif op == 4:
            print("Lista de Editoriales")
            editorials = editorial_service.getAll()
            if not editorials:
                print("No hay Editoriales cargados")
            else:
                for editorial in editorials:
                    print(editorial)
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

def authorMenu():
    op = 0
    while op != 9:
        print("Menu de Autores de libros")
        print("1. Agregar un Autor")
        print("2. Eliminar un Autor")
        print("3. Modificar un Autor")
        print("4. Lista de Autores")
        print("9. Salir")
        op = int(input('\nIngrese número de la opción elegida: '))

        if op == 1:
            print("\n\tAgregar un Autor")
            name = input("Ingrese el nombre del Autor: ")
            id = ids_repository.getAuthorId() + 1
            newAuthor = Author(id, name)
            author_service.add(newAuthor)
            ids_repository.updateAuthorId(id)
        elif op == 2:
            print("\n\tEliminar un Autor")
            id = int(input("Ingrese el id del Autor: "))
            while not isinstance(id, int) or not int(id) >= 1:
                print("Por favor, introduzca un número mayor o igual a 1")
                id = input("Ingrese el id del Autor: ")
            author_service.delete(int(id))
        elif op == 3:
            print("\n\tModificar un Autor")
            id = input("Ingrese el id del Autor o 0 para salir: ")
            while True and id != 0:
                newName = input("Ingrese el nuevo nombre del Autor: ")
                try:
                    updated_author = Editorial(id, newName)
                    author_service.update(updated_author)
                    break
                except Exception as e:
                    print(f"Error al crear el Autor: {e}")
                print("Por favor, introduzca un número mayor o igual a 1")
                id = input("Ingrese el id del autor o 0 para salir: ")
        elif op == 4:
            print("Lista de Autores")
            authors = author_service.getAll()
            if not authors:
                print("No hay autores carcados")
            else:
                for author in authors:
                    print(author)
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

def bookMenu():
    op = 0
    while op != 9:
        print("Menu de libros")
        print("1. Agregar un Libro")
        print("2. Eliminar un Libro")
        print("3. Modificar un Libro")
        print("4. Lista de Libros")
        print("9. Salir")
        op = int(input('\nIngrese número de la opción elegida: '))

        if op == 1:
            print("\n\tAgregar un Libro")
            createBook()
        elif op == 2:
            print("\n\tEliminar un Libro")
            id = int(input("Ingrese el id del Libro: "))
            while not isinstance(id, int) or not int(id) >= 1:
                print("Por favor, introduzca un número mayor o igual a 1")
                id = input("Ingrese el id del Libro: ")
            book_service.delete(int(id))
        elif op == 3:
            print("\n\tModificar un Libro")
            id = input("Ingrese el id del Libro o 0 para salir: ")
            while True:
                try:
                    title = input("Ingrese el título del Libro: ")
                    authors = insertAuthors()
                    page_count = input("Ingrese la cantidad de páginas del Libro: ")
                    isbn = input("Ingrese el isbn del Libro: ")
                    edition_year = input("Ingrese el año de la edición del Libro: ")
                    editorial_id = input("Ingrese el id de la Editorial del Libro: ")
                    genre_id = input("Ingrese el ID del Género del Libro: ")

                    updatedBook = Book(id, title, authors, page_count, isbn, edition_year, editorial_id, genre_id)
                    book_service.update(updatedBook)
                    break
                except Exception as e:
                    print(f"Error al modificar el Libro: {e}")
        elif op == 4:
            print("Lista de Libros")
            books = book_service.getAll()
            if not books:
                print("No hay autores carcados")
            else:
                for book in books:
                    print(book)
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

def createBook():
    while True:
        try:
            title = input("Ingrese el título del Libro: ")
            authors = insertAuthors()
            page_count = input("Ingrese la cantidad de páginas del Libro: ")
            isbn = input("Ingrese el isbn del Libro: ")
            edition_year = input("Ingrese el año de la edición del Libro: ")
            editorial_id = input("Ingrese el id de la Editorial del Libro: ")
            genre_id = input("Ingrese el ID del Género del Libro: ")

            id = ids_repository.getBookId() + 1
            newBook = Book(id, title, authors, page_count, isbn, edition_year, editorial_id, genre_id)
            book_service.add(newBook)
            ids_repository.updateAuthorId(id)
            break
        except ValueError as e:
            print("Error al crear el libro: ", e)
            print("Por favor, intente ingresar los datos nuevamente.\n")


def insertAuthors():
    authors = []
    author_id = input("Ingrese el ID del autor.")
    authors.append(author_id)
    sub_op = input("¿Desea agregar otro autor? S/N")
    while sub_op.upper() != "N" or len(authors) <= 3:
        author_id = input("Ingrese el ID del autor.")
        authors.append(author_id)
        if len(authors) == 3:
            break
        sub_op = input("¿Desea agregar otro autor? S/N")
    return authors