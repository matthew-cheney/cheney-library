import sqlite3
import json

from Exceptions.exceptions import BookAlreadyInDB
from models.Book import Book

DB_FILENAME = 'db/book_metadata.db'


def _get_conn_c():
    conn = sqlite3.connect(DB_FILENAME)
    c = conn.cursor()
    return conn, c


def add_book_to_db(book):
    conn, c = _get_conn_c()
    try:
        c.execute("SELECT * FROM books WHERE isbn=?", (book.isbn,))
        if (c.fetchone() is not None):
            raise BookAlreadyInDB(f'{book.isbn} already in the database')

        params = (book.date_added, book.isbn, book.url, book.title, json.dumps(book.authors), json.dumps(book.subjects), json.dumps(book.subject_places), json.dumps(book.subject_people), json.dumps(book.subject_times), json.dumps(book.publishers), json.dumps(book.publish_places), book.publish_date, book.cover_url, book.number_of_pages, book.weight)
        c.execute("INSERT INTO books VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", params)
        conn.commit()
    finally:
        conn.close()


def get_all_books():
    conn, c = _get_conn_c()
    try:
        c.execute("SELECT * FROM books")
        db_books = c.fetchall()
        books = []
        for book in db_books:
            books.append(_db_book_to_model(book))
        return books
    finally:
        conn.close()


def delete_book_by_isbn(isbn):
    conn, c = _get_conn_c()
    try:
        c.execute("DELETE FROM books WHERE isbn=?", (isbn,))
        conn.commit()
    finally:
        conn.close()


def _db_book_to_model(book):
    date_added = book[0]
    isbn = book[1]
    url = book[2]
    title = book[3]
    authors = book[4]
    subjects = book[5]
    subject_places = book[6]
    subject_people = book[7]
    subject_times = book[8]
    publishers = book[9]
    publish_places = book[10]
    publish_date = book[11]
    cover_url = book[12]
    number_of_pages = book[13]
    weight = book[14]
    return Book(
        date_added=date_added,
        isbn=isbn,
        url=url,
        title=title,
        authors=authors,
        subjects=subjects,
        subject_places=subject_places,
        subject_people=subject_people,
        subject_times=subject_times,
        publishers=publishers,
        publish_places=publish_places,
        publish_date=publish_date,
        cover_url=cover_url,
        number_of_pages=number_of_pages,
        weight=weight,
    )