class Book:

    def __init__(self, id, title, authors, page_count, isbn, edition_year, editorial_id, genre_id):
        self.id = self.__validateId(id)
        self.title = self.__validateTitle(title)
        self.authors = self.__validateAuthors(authors)
        self.page_count = self.__validatePageCount(page_count)
        self.isbn = self.__validateIsbn(isbn)
        self.edition_year = self.__validateEditionYear(edition_year)
        self.editorial_id = self.__validateId(editorial_id)
        self.genre_id = self.__validateId(genre_id)
        self.is_active = True

    def __validateId(self, id):
        if isinstance(id, str):
            if not id.isdigit() or not 1 <= int(id):
                raise ValueError("El id del género debe ser un número mayor a 1 entero.")
        return int(id)
    
    def __validateTitle(self, title):
        title = title.strip()
        if not isinstance(title, str) or not 4 <= len(title) <= 50:
            raise ValueError("El título debe tener entre 4 y 50 caracteres")
        return title.ljust(50)

    def __validateAuthors(self, authors):
        if not isinstance(authors, list) or not (1 <= len(authors) <= 3):
            raise ValueError("La lista de autores debe tener entre 1 y 3 nombres")
        valid_authors = []
        for author in authors:
            if not author.isdigit() or not int(author) >= 1:
                raise ValueError("El id del autor es inválido")
            valid_authors.append(int(author))
        for i in range(len(valid_authors), 3):
            valid_authors.append(0)
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
            raise ValueError("El dígito de control es incorrecto para un isbn de 10 digitos.")

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
            raise ValueError("El dígito de control es incorrecto para un isbn de 13 digitos.")
        else:
            raise ValueError("El ISBN tiene un formato incorrecto.")

    def __validateEditionYear(self, edition_year):
        if not edition_year.isdigit():
            raise ValueError("El año de la editorial debe ser un número")
        edition_year = int(edition_year)
        if edition_year < 0:
            raise ValueError("El año de la editorial debe ser mayor a cero")
        return edition_year

    def __str__ (self):
        return f"{self.title} - Género: {self.genre_id} \n" \
                f"Año: {self.edition_year} \n" \
                f"IDs de los Autores: {self.authors} \n" \
                f"Nro de Páginas: {self.page_count} \n" \
                f"ISBN: {self.isbn} \n" \
                f"ID de la Editorial: {self.editorial_id} \n"