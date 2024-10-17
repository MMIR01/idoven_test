"""
Nominal tests for the POST operation

@Author: M. Miralles
"""

import datasets.dataset01 as dataset01
import pytest
import requests
import configuration.reset_database as reset_database
import configuration.variables as variables
from http import HTTPStatus


@pytest.fixture(autouse=True, scope='class')
def test_configuration():
    # Suite setup: nothing to do
    yield
    print("Suite teardown")
    reset_database.reset_database()


class TestPost():
    @pytest.mark.parametrize("book_data, expected_status, expected_id", [
        (dataset01.book1, HTTPStatus.CREATED, "1"),
        (dataset01.book2, HTTPStatus.CREATED, "2"),
        (dataset01.book3, HTTPStatus.CREATED, "3")
    ])
    def test_add_book(self, book_data, expected_status, expected_id):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=book_data)

        # Validate response code and header content type
        assert response.status_code == expected_status
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload. The data received is the same as the one sent
        data = response.json()
        assert data[variables.TITLE] == book_data[variables.TITLE]
        assert data[variables.AUTHOR] == book_data[variables.AUTHOR]
        assert data[variables.PUBLISHED_DATE] == \
               book_data[variables.PUBLISHED_DATE]
        assert data[variables.ISBN] == book_data[variables.ISBN]
        assert data[variables.PRICE] == book_data[variables.PRICE]
        # Make sure the ID is as expected
        assert data[variables.BOOK_ID] == expected_id
