"""
Non-nominal tests for the GET operation

@Author: M. Miralles
"""

import datasets.dataset01 as dataset01
import pytest
import requests
import configuration.add_books_database as add_books_database
import configuration.reset_database as reset_database
import configuration.variables as variables
from http import HTTPStatus


@pytest.fixture(scope='class')
def test_configuration():
    print("Suite setup")
    # Add 1 book to the database
    book_list = [dataset01.book1]
    add_books_database.add_books_database(book_list)
    yield
    print("Suite teardown")
    reset_database.reset_database()


class TestGetNegative:
    def test_get_empty_database(self):
        book_url = variables.MAIN_PATH
        response = requests.get(book_url)
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate empty list
        assert response.json() == []

    def test_get_book_non_existing_id(self, test_configuration):
        book_url = variables.MAIN_PATH + "/1005"
        response = requests.get(book_url)

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Book not found'

    @pytest.mark.parametrize("wrong_id", [
        ("-1"), ("0"), ("1,1"), ("all"), ("1+1"), ("!?*1")])
    def test_get_book_wrong_book_id(self, test_configuration, wrong_id):
        book_url = variables.MAIN_PATH + '/' + wrong_id
        response = requests.get(book_url)

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Book not found'

    def test_get_book_wrong_path(self):
        book_url = variables.SERVER_ADDRESS + '/bookrs'
        response = requests.get(book_url)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers['Content-Type'] == 'text/html; charset=utf-8'
        assert 'The requested URL was not found on the server' in response.text
