"""
Nominal tests for the DELETE operation

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


class TestDelete:
    @pytest.mark.parametrize("book_data, expected_status, book_id", [
        (dataset01.book1, HTTPStatus.NO_CONTENT, "1"),
        (dataset01.book2, HTTPStatus.NO_CONTENT, "2"),
        (dataset01.book3, HTTPStatus.NO_CONTENT, "3")
    ])
    def test_delete_book(self, book_data, expected_status, book_id):
        book_url = variables.MAIN_PATH + '/' + book_id
        response = requests.delete(book_url)

        # Validate response code and header content type
        assert response.status_code == expected_status
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Verify an empty response body
        assert response.text == ""
        # Check the book is not in the database
        response = requests.get(book_url)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers['Content-Type'] == 'application/json'
        # Validate payload
        data = response.json()
        assert data['error'] == 'Book not found'
