from flask import Flask
from APIHandler import *
from DBHandler import *
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/add-book/<isbn>')
def add_book(isbn):
    book = get_book_from_api(isbn)
    try:
        add_book_to_db(book)
    except BookAlreadyInDB:
        pass
    return book.__repr__()
