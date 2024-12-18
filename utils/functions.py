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
        print("5. Generar Listados")
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
        elif op == 5:
            listingMenu()
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
        print("5. Depurar archivo")
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
        print("5. Depurar Archivo")
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
                editorial_service.purge_inactive()
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
        print("5. Depurar de Autores")
        print("9. Salir")
        op = int(input('\nIngrese número de la opción elegida: '))

        if op == 1:
            print("\n\tAgregar un Autor")
            fist_name = input("Ingrese el nombre del Autor: ")
            last_name = input("Ingrese el apellido del Autor: ")
            id = ids_repository.getAuthorId() + 1
            newAuthor = Author(id, fist_name, last_name)
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
                new_fist_name = input("Ingrese el nombre del Autor: ")
                new_last_name = input("Ingrese el apellido del Autor: ")
                try:
                    updated_author = Author(id, new_fist_name, new_last_name)
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
                author_service.purge_inactive()
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
        print("5. Depurar Archivo")
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
                    print("id: ", book.id, " - ", book)
        elif op == 5:
            print("¿Seguro que quiere depurar los datos?")
            sub_op = input("S/N")
            if sub_op.upper() == "S":
                book_service.purge_inactive()
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
            ids_repository.updateBookId(id)
            break
        except ValueError as e:
            print("Error al crear el libro: ", e)
            print("Por favor, intente ingresar los datos nuevamente.\n")


def insertAuthors():
    authors = []
    author_id = input("Ingrese el ID del autor.")
    authors.append(author_id)
    sub_op = input("¿Desea agregar otro autor? S/N")
    while sub_op.upper() != "N":
        author_id = input("Ingrese el ID del autor.")
        authors.append(author_id)
        if len(authors) == 3:
            break
        sub_op = input("¿Desea agregar otro autor? S/N")
    return authors

def listingMenu():
    op = 0
    while op != 11:
        print("Menu de Listados")
        print("1. Listar todos los Autores existentes.")
        print("2. Listar todos los libros existentes.")
        print("3. Listar todos los libros de un género determinado.")
        print("4. Listar todos los libros que posee un autor determinado.")
        print("5. Listar todos los libros de una editorial determinada.")
        print("6. Listar todos los libros de una editorial determinada en un rango de años de edición.")
        print("7. Listar todos los autores de una determinada editorial.")
        print("8. Listar todos los libros que fueron editados en un determinado año.")
        print("9. Listar todos los libros de los autores cuyos apellidos comienzan con una letra determinada.")
        print("10. Listar todos los libros cuyos títulos contengan una palabra determinada.")
        print("11. Salir")
        op = int(input('\nIngrese número de la opción elegida: '))

        if op == 1:
            print("\n\tListar todos los Autores existentes.")
            authors = author_service.getAll()
            if not authors:
                print("No hay autores cargados")
            else:
                for author in authors:
                    print(author)

        elif op == 2:
            print("\n\tListar todos los libros existentes")
            books = book_service.getAll()
            if not books:
                print("No hay libros cargados")
            else:
                for book in books:
                    print(f"ID: {book.id} {book}")

        elif op == 3:
            print("\n\tListar todos los libros de un género determinado.")
            genre_id = int(input("Ingrese el ID del Género deseado: "))
            books = book_service.getBooksByGenreId(genre_id)
            if not books:
                print("No se encontraron coincidencias")
            else:
                for book in books:
                    print(book)

        elif op == 4:
            print("\n\tListar todos los libros que posee un autor determinado.")
            author_id = int(input("Ingrese el ID del Autor deseado: "))
            books = book_service.getBooksByAuthorId(author_id)
            if not books:
                print("No se encontraron coincidencias")
            else:
                for book in books:
                    print(book)

        elif op == 5:
            print("\n\tListar todos los libros de una editorial determinada.")
            editorial_id = int(input("Ingrese el ID de la Editorial deseada: "))
            books = book_service.getBooksByEditorialId(editorial_id)
            if not books:
                print("No se encontraron coincidencias")
            else:
                for book in books:
                    print(book)
            
        elif op == 6:
            print("\n\tListar todos los libros de una editorial determinada en un rango de años de edición")
            editorial_id = int(input("Ingrese el ID de la Editorial deseada: "))
            try:
                start_year = int(input("Ingrese el año inicial: "))
                end_year = int(input("Ingrese el año final: "))
            except ValueError as e:
                print("Error, tipo de dato no valido: ", e)
            books = book_service.getBooksByEditorialIdWithinDateRange(editorial_id, start_year, end_year)
            if not books:
                print("No se encontraron coincidencias")
            else:
                for book in books:
                    print(book)
        
        elif op == 7:
            print("\n\tListar todos los autores de una determinada editorial.")
            editorial_id = int(input("Ingrese el ID de la Editorial deseada: "))
            authors_id = book_service.getAuthorsByEditorialId(editorial_id)
            authors = []
            for author_id in authors_id:
                author = author_service.getItemById(author_id)
                if author not in authors and author is not None:
                    authors.append(author)
            if not authors:
                print("No se encontraron coincidencias")
            else:
                for author in authors:
                    print(author)

        elif op == 8:
            print("\n\tListar todos los libros que fueron editados en un determinado año.")
            edition_year = int(input("Ingrese el año de la Edición: "))
            books = book_service.getBooksByYear(edition_year)
            if not books:
                print("No se encontraron coincidencias")
            else:
                for book in books:
                    print(book)

        elif op == 9:
            print("\n\tListar todos los libros de los autores cuyos apellidos comienzan con una letra determinada.")
            letter = input("Introduzca la primera letra del apellido del autor: ")
            authors = author_service.getAuthorsByLastNameFirstLetter(letter)
            books=[]
            for author in authors:
                author_books = book_service.getBooksByAuthorId(author.id)
                for book in author_books:
                    if book not in books:
                        books.append(book)
            if not books:
                print("No se encontraron coincidencias")
            else:
                for book in books:
                    print(book)

        elif op == 10:
            print("\n\tListar todos los libros cuyos títulos contengan una palabra determinada.")
            word = input("Introduzca la palabra a buscar: ")
            books = book_service.getBooksByWord(word)
            if not books:
                print("No se encontraron coincidencias")
            else:
                for book in books:
                    print(book)

        elif op == 11:
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida, intente de nuevo.")