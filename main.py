from utils.functions import menu

from models.genre import Genre
from models.editorial import Editorial
from models.author import Author
from models.book import Book

from services.genre_service import GenreService
from services.editorial_service import EditorialService
from services.author_service import AuthorService
from services.book_service import BookService

genre_service = GenreService("data/genres")
editorial_service = EditorialService("data/editorials")
author_service = AuthorService("data/authors")
book_service = BookService("data/books")

menu()