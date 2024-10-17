"""
Tests for the PUT operations

@Author: M. Miralles
"""

import datasets.dataset01 as dataset01
import datasets.dataset02 as dataset02
import pytest
import requests
import configuration.add_books_database as add_books_database
import configuration.reset_database as reset_database
import configuration.variables as variables
from http import HTTPStatus


@pytest.fixture(autouse=True, scope='class')
def test_configuration():
    print("Suite setup")
    # Add 2 books to the database
    book_list = [dataset01.book1, dataset01.book2]
    add_books_database.add_books_database(book_list)
    yield
    print("Suite teardown")
    reset_database.reset_database()


class TestPut():
    @pytest.mark.parametrize("book_data, expected_status, expected_id", [
        (dataset02.book1_update_title, HTTPStatus.OK, "1"),
        (dataset02.book1_update_author, HTTPStatus.OK, "1"),
        (dataset02.book1_update_isbn, HTTPStatus.OK, "1"),
        (dataset02.book1_update_published_date, HTTPStatus.OK, "1"),
        (dataset02.book1_update_price, HTTPStatus.OK, "1"),
        (dataset02.book1_update_all, HTTPStatus.OK, "1"),
        (dataset02.book2_update_all, HTTPStatus.OK, "2")
    ])
    def test_update_book(self, book_data, expected_status, expected_id):
        book_url = variables.MAIN_PATH + '/' + expected_id
        response = requests.put(book_url, json=book_data)

        assert response.status_code == expected_status
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Check the data is updated
        data = response.json()
        for field in book_data.keys():
            assert data[field] == book_data[field]
        # The ID shouldn't have changed
        assert data[variables.BOOK_ID] == expected_id
