"""
Nominal tests for the GET operation

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


class TestGet:
    @pytest.mark.parametrize("book_data, expected_status, expected_id", [
        (dataset01.book1, HTTPStatus.OK, "1"),
        (dataset01.book2, HTTPStatus.OK, "2"),
        (dataset01.book3, HTTPStatus.OK, "3")
    ])
    def test_get_book(self, book_data, expected_status, expected_id):
        book_url = variables.MAIN_PATH + '/' + expected_id
        response = requests.get(book_url)
        # Validate response code and header content type
        assert response.status_code == expected_status
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload. The data received is the same as the inserted
        # during the setup
        book = response.json()
        assert book[variables.TITLE] == book_data[variables.TITLE]
        assert book[variables.AUTHOR] == book_data[variables.AUTHOR]
        assert book[variables.PUBLISHED_DATE] == \
               book_data[variables.PUBLISHED_DATE]
        assert book[variables.ISBN] == book_data[variables.ISBN]
        assert book[variables.PRICE] == book_data[variables.PRICE]
        # Make sure the ID is as expected
        assert book[variables.BOOK_ID] == expected_id

    def test_get_all_books(self):
        book_url = variables.MAIN_PATH
        response = requests.get(book_url)

        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        books = response.json()
        databooks = [dataset01.book1, dataset01.book2, dataset01.book3]

        # All books returned in the json
        item = 0
        first_id = 1
        for book in books:
            assert book[variables.TITLE] == databooks[item][variables.TITLE]
            assert book[variables.AUTHOR] == databooks[item][variables.AUTHOR]
            assert book[variables.PUBLISHED_DATE] == \
                   databooks[item][variables.PUBLISHED_DATE]
            assert book[variables.ISBN] == databooks[item][variables.ISBN]
            assert book[variables.PRICE] == databooks[item][variables.PRICE]
            # Make sure the ID is as expected
            assert book[variables.BOOK_ID] == str(first_id)
            item += 1
            first_id += 1
