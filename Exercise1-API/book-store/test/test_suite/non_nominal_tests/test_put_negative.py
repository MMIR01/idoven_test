"""
Non-nominal tests for the PUT operation

@Author: M. Miralles
"""

import datasets.dataset03 as dataset03
import datasets.dataset04 as dataset04
import pytest
import requests
import configuration.add_books_database as add_books_database
import configuration.reset_database as reset_database
import configuration.variables as variables
from http import HTTPStatus


@pytest.fixture(autouse=True, scope='class')
def test_configuration():
    print("Suite setup")
    # Add 1 book to the database
    # We use database03 as we are going to use the same modified books
    add_books_database.add_books_database([dataset03.book1])
    yield
    print("Suite teardown")
    reset_database.reset_database()


class TestPutNegative():
    def test_update_book_non_existing_id(self):
        book_url = variables.MAIN_PATH + "/1005"
        response = requests.put(book_url, json=dataset04.book2)

        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Book not found'

    def test_update_book_id(self):
        # Add a book and get the id
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=dataset04.book2)
        assert response.status_code == HTTPStatus.CREATED
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        data = response.json()
        book_id = data[variables.BOOK_ID]
        # Modify that book and the book_id
        book_url = variables.MAIN_PATH + '/' + book_id
        response = requests.put(book_url, json=dataset04.book2_update_id)
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        data = response.json()
        # The book_id is the one provided by the database
        assert data[variables.BOOK_ID] == book_id
        assert data[variables.BOOK_ID] != \
            dataset04.book2_update_id[variables.BOOK_ID]

    def test_update_book_extra_field(self):
        book_url = variables.MAIN_PATH + '/1'
        response = requests.put(book_url, json={"extra_field": "extra"})

        # The extra field is ignored and the book is not updated
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Check the extra field is not in the database
        book = response.json()
        assert book.get('extra_field') is None

    @pytest.mark.parametrize("book_data, field", [
        (dataset03.book1_wrong_type_title, variables.TITLE),
        (dataset03.book1_wrong_type_author, variables.AUTHOR),
        (dataset03.book1_wrong_type_published_date, variables.PUBLISHED_DATE),
        (dataset03.book1_wrong_type_isbn, variables.ISBN),
        (dataset03.book1_wrong_type_price, variables.PRICE)
    ])
    def test_update_book_wrong_field_type(self, book_data, field):
        book_url = variables.MAIN_PATH + '/1'
        response = requests.put(book_url, json=book_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # If the field type is wrong, the field is reject, so it is considered
        # missing and therefore the book is not updated
        data = response.json()
        assert data['error'] == 'Missing required fields'

        # Check the book is not modified
        response = requests.get(book_url)
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        data = response.json()
        assert data[field] == dataset03.book1[field]

    def test_update_book_wrong_date_format(self):
        book_url = variables.MAIN_PATH + '/1'
        response = requests.put(
            book_url, json=dataset03.book1_wrong_type_published_date_format)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Wrong date format. Expected: YYYY-MM-DD'

    def test_update_book_wrong_isbn_format(self):
        book_url = variables.MAIN_PATH + '/1'
        response = requests.put(
            book_url, json=dataset03.book1_wrong_isbn_format)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Wrong ISBN format. Expected: 13 digits'

    @pytest.mark.parametrize("book_data", [
        (dataset03.book1_wrong_price_zero),
        (dataset03.book1_wrong_price_negative),
        (dataset03.book1_empty_price)
    ])
    def test_update_book_wrong_price_format(self, book_data):
        book_url = variables.MAIN_PATH + '/1'
        response = requests.put(book_url, json=book_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == \
            'Wrong price: it cannot be negative, zero or empty'

    @pytest.mark.parametrize("book_data, field", [
        (dataset03.book1_long_title, variables.TITLE),
        (dataset03.book1_long_author, variables.AUTHOR),
        (dataset03.book1_long_price, variables.PRICE)
    ])
    def test_update_book_long_field(self, book_data, field):
        book_url = variables.MAIN_PATH + '/1'
        response = requests.put(book_url, json=book_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == field + ' too long'

    def test_update_book_using_post(self):
        book_url = variables.MAIN_PATH + '/1'
        response = requests.post(book_url, json=dataset03.book2)

        # Code 405 = Method Not Allowed
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
