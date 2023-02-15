from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository

def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'])
        authors.append(author)

    return authors

def select(id):
    book = None
    sql = "SELECT * FROM books where id = %s"

    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], result['genre'], result['publisher'], author, result['id'])
    return book 