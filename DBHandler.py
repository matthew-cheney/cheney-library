import sqlite3
import json

from Exceptions.exceptions import BookAlreadyInDB

DB_FILENAME = 'db/book_metadata.db'

def add_book_to_db(book):
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE isbn=?", (book.isbn,))
    if (c.fetchone() is not None):
        raise BookAlreadyInDB(f'{book.isbn} already in the database')

    params = (book.date_added, book.isbn, book.url, book.title, json.dumps(book.authors), json.dumps(book.subjects), json.dumps(book.subject_places), json.dumps(book.subject_people), json.dumps(book.subject_times), json.dumps(book.publishers), json.dumps(book.publish_places), book.publish_date, book.cover_filename, book.number_of_pages, book.weight)
    c.execute("INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", params)
    conn.commit()
