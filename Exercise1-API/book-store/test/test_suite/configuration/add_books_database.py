"""
This file contains a method that adds books to the database. For that it uses 
the resource POST /books to add the required book.

It should be only use for suite/test setup.

@Author: M. Miralles
"""

import requests
from http import HTTPStatus
import configuration.variables as variables


def add_books_database(book_list: list):
    book_url = variables.MAIN_PATH
    book_added = 0
    for book_data in book_list:
        response = requests.post(book_url, json=book_data)
        assert response.status_code == HTTPStatus.CREATED
        book_added += 1
    print(f"Total books added: {book_added}")
