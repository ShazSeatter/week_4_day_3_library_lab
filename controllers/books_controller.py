from flask import Flask, render_template, request, redirect
from repositories import book_repository, author_repository
from models.book import Book

from flask import Blueprint

books_blueprint = Blueprint('books', __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template('books/index.html', title = "Books", all_books = books)


# NEW
# GET '/tasks/new'
# Return HTML form to the browser for us to fill in 


# CREATE
# POST '/tasks'
# Receieve the data from the form, and put new entry into database


# SHOW
# GET '/tasks/<id>'



# EDIT
# GET '/tasks/<id>/edit'



# UPDATE
# POST '/tasks/<id>'



# DELETE
# POST '/tasks/<id>'

@books_blueprint.route('/books/<id>/delete', methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')