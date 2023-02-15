import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("Frank", "Herbert")
author_repository.save(author1)
author2 = Author("Sarah", "J Maas")
author_repository.save(author2)

book_1 = Book("Dune", "Sci-Fi", "Chilton Books", author1)
book_repository.save(book_1)
book_2 = Book("Dune Messiah", "Sci-Fi", "Chilton Books", author1)
book_repository.save(book_2)
book_3 = Book("A Court of Throns and Roses", "Fantasy", "Bloomsbury", author2)
book_repository.save(book_2)



