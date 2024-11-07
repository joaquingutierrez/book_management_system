class Book:

    def __init__(self, title, authors, page_count, isbn, edition_year, editorial, genre_id):
        self.title = self.__validateTitle(title)
        self.authors = self.__validateAuthors(authors)
        self.page_count = self.__validatePageCount(page_count)
        self.isbn = self.__validateIsbn(isbn)
        self.edition_year = self.__validateEditionYear(edition_year)
        self.editorial = self.__validateEditorial(editorial)
        self.genre_id = self.__validateGenreId(genre_id)
    
    def __validateTitle(self, title):
        title = title.strip()
        if not isinstance(title, str) or not 4 <= len(title) <= 30:
            raise ValueError("El título debe tener entre 4 y 30 caracteres")
        return title

    def __validateAuthors(self, authors):
        if not isinstance(authors, list) or not (1 <= len(authors) <= 3):
            raise ValueError("La lista de autores debe tener entre 1 y 3 nombres")
        valid_authors = []
        for author in authors:
            author = author.strip()
            if not isinstance(author, str) or not (4 <= len(author) <= 30):
                raise ValueError("El nombre del autor debe tener entre 4 y 30 caracteres")
            valid_authors.append(author)
        return valid_authors
    
    def __validatePageCount(self, page_count):
        if not page_count.isdigit():
            raise ValueError("La cantidad de páginas debe ser un número")
        page_count = int(page_count)
        if not (1 <= page_count):
            raise ValueError("La cantidad de páginas debe tener al menos 1")
        return page_count
    
    def __validateIsbn(self, isbn):
        isbn_numbers = isbn.replace("-", "").replace(" ", "")

        if len(isbn_numbers) == 10 and isbn_numbers[:-1].isdigit():
            total = 0
            for i, value in enumerate(isbn_numbers[:-1], 1):
                total += i * int(value)
            rest = total % 11
            control_digit = isbn_numbers[-1]
            if control_digit.isdigit() and (0 <= rest <= 9 and rest == int(control_digit)) or control_digit.upper() == "X":
                return isbn
            raise ValueError("El dígito de control es incorrecto.")

        elif len(isbn_numbers) == 13 and isbn_numbers.isdigit():
            total = 0
            for i, value in enumerate(isbn_numbers[:-1], 1):
                if i % 2 == 0:
                    total += 3 * int(value)
                else:
                    total += int(value)
            control_digit = int(isbn_numbers[-1])
            if (10 - total % 10) % 10 == control_digit:
                return isbn
            raise ValueError("El dígito de control es incorrecto.")
        else:
            raise ValueError("El ISBN tiene un formato incorrecto.")

    def __validateEditionYear(self, edition_year):
        if not edition_year.isdigit():
            raise ValueError("El año de la editorial debe ser un número")
        edition_year = int(edition_year)
        if edition_year < 0:
            raise ValueError("El año de la editorial debe ser mayor a cero")
        return edition_year

    def __validateEditorial(self, editorial):
        editorial = editorial.strip()
        if not isinstance(editorial, str) or not 4 <= len(editorial) <= 30:
            raise ValueError("La editorial debe ser una cadena de entre 4 y 30 caracteres")
        return editorial
    
    def __validateGenreId(self, genre_id):
        genre_id = genre_id.strip()
        if not genre_id.isdigit() and not 1 <= int(genre_id):
            raise ValueError("El id del géro debe ser un número mayor a 1")
        return int(genre_id)

    def __str__ (self):
        genre = self.gerGenre()
        return f"{self.title} - Género: {genre}"