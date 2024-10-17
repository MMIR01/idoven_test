"""
Non-nominal tests for the DELETE operation

@Author: M. Miralles
"""

import datasets.dataset01 as dataset01
import pytest
import requests
import configuration.add_books_database as add_books_database
import configuration.reset_database as reset_database
import configuration.variables as variables
from http import HTTPStatus


@pytest.fixture(autouse=True, scope='class')
def test_configuration():
    print("Suite setup")
    # Add 3 books to the database
    book_list = [dataset01.book1, dataset01.book2, dataset01.book3]
    add_books_database.add_books_database(book_list)
    yield
    print("Suite teardown")
    reset_database.reset_database()


class TestDeleteNegative:
    @pytest.mark.parametrize("book_id", [
        ("1005"), ("0"), ("-1"), ("2.0")
    ])
    def test_delete_book_wrong_id(self, book_id):
        book_url = variables.MAIN_PATH + '/' + book_id
        response = requests.delete(book_url)

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Book not found'

    def test_delete_book(self):
        book_url = variables.MAIN_PATH + '/2'
        response = requests.delete(book_url)

        assert response.status_code == HTTPStatus.NO_CONTENT
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE

        # Try to remove the book again
        response = requests.delete(book_url)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Book not found'
