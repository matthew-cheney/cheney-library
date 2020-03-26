from flask import render_template, redirect, url_for

import APIHandler
import DBHandler
from server import app


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/add-book/<isbn>')
def add_book(isbn):
    book = APIHandler.get_book_from_api(isbn)
    try:
        DBHandler.add_book_to_db(book)
    except DBHandler.BookAlreadyInDB:
        pass
    # with open(f'cover_images/{book.cover_filename}', 'rb') as f:
    #     image_data = f.read()
    # image_data = base64.b64decode(image_data)
    return render_template('book.html', book=book)


@app.route('/all-books')
def all_books():
    books = DBHandler.get_all_books()
    return render_template('allbooks.html', books=books)


@app.route('/delete-book/<isbn>')
def delete_book(isbn):
    DBHandler.delete_book_by_isbn(isbn)
    return redirect(url_for('all_books'))

