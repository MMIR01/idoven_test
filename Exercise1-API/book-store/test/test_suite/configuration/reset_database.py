"""
This file contains a method that resets the database to its initial state.
For that it uses the resource /books to retrieve all the books and then
use /books

@Author: M. Miralles
"""

import requests
from http import HTTPStatus
import configuration.variables as variables


def reset_database():
    # Get all the books from the database
    book_url = variables.MAIN_PATH
    response = requests.get(book_url)
    books = response.json()
    # Clean up: remove all the books added during the tests
    for book in books:
        response = requests.delete(book_url + '/' + book['book_id'])
        assert response.status_code == HTTPStatus.NO_CONTENT

    # Check the database is empty
    response = requests.get(book_url)
    assert response.status_code == HTTPStatus.OK
    books = response.json()
    assert len(books) == 0
    print("Database reset")
