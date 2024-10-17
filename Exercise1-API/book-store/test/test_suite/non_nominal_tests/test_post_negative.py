"""
Non-nominal tests for the POST operation

@Author: M. Miralles
"""

import datasets.dataset03 as dataset03
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


class TestPostNegative():
    def test_add_book_twice(self):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=dataset03.book2)

        assert response.status_code == HTTPStatus.CREATED
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload. The data received is the same as the one sent
        data = response.json()
        assert data[variables.BOOK_ID]
        assert data[variables.TITLE] == dataset03.book2[variables.TITLE]
        assert data[variables.AUTHOR] == dataset03.book2[variables.AUTHOR]
        assert data[variables.PUBLISHED_DATE] == \
               dataset03.book2[variables.PUBLISHED_DATE]
        assert data[variables.ISBN] == dataset03.book2[variables.ISBN]
        assert data[variables.PRICE] == dataset03.book2[variables.PRICE]

        # Add the same book again
        response = requests.post(book_url, json=dataset03.book2)
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Book already exists'

    @pytest.mark.parametrize("book_data", [
        (dataset03.book1_missing_title),
        (dataset03.book1_missing_author),
        (dataset03.book1_missing_published_date),
        (dataset03.book1_missing_isbn),
        (dataset03.book1_missing_price),
        (dataset03.book1_missing_all)
    ])
    def test_add_book_missing_field(self, book_data):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=book_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Missing required fields'

    @pytest.mark.parametrize("book_data", [
        (dataset03.book1_wrong_type_title),
        (dataset03.book1_wrong_type_author),
        (dataset03.book1_wrong_type_published_date),
        (dataset03.book1_wrong_type_isbn),
        (dataset03.book1_wrong_type_price)
    ])
    def test_add_book_wrong_field_type(self, book_data):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=book_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # If the field type is wrong, the field is reject, so it is considered
        # missing and therefore the book is not added
        data = response.json()
        assert data['error'] == 'Missing required fields'

    def test_add_book_wrong_date_format(self):
        book_url = variables.MAIN_PATH
        response = requests.post(
            book_url, json=dataset03.book1_wrong_type_published_date_format)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Wrong date format. Expected: YYYY-MM-DD'

    def test_add_book_wrong_isbn_format(self):
        book_url = variables.MAIN_PATH
        response = requests.post(
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
    def test_add_book_wrong_price_format(self, book_data):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=book_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Wrong price: it cannot be negative or zero'

    @pytest.mark.parametrize("book_data, field", [
        (dataset03.book1_long_title, variables.TITLE),
        (dataset03.book1_long_author, variables.AUTHOR),
        (dataset03.book1_long_price, variables.PRICE)
    ])
    def test_add_book_long_field(self, book_data, field):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=book_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == field + ' too long'

    def test_add_book_extra_field(self):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=dataset03.book1_extra_field)

        assert response.status_code == HTTPStatus.CREATED
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data[variables.BOOK_ID]
        book_id = data[variables.BOOK_ID]

        # Check the book is in the database
        book_url = variables.MAIN_PATH + '/' + book_id
        response = requests.get(book_url)
        assert response.status_code == HTTPStatus.OK
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Check the extra field is not in the database
        book = response.json()
        assert book.get('extra_field') is None

    def test_add_book_wrong_content_type(self):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=dataset03.book2,
                                 headers={'Content-Type': 'application/xml'})

        # Code 415 = Unsupported Media Type
        assert response.status_code == HTTPStatus.UNSUPPORTED_MEDIA_TYPE

    def test_add_book_xml_data(self):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=dataset03.book3_xml)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data['error'] == 'Wrong JSON format'

    def test_add_book_using_put(self):
        book_url = variables.MAIN_PATH
        response = requests.put(book_url, json=dataset03.book2)

        # Code 405 = Method Not Allowed
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

    def test_add_book_wrong_path(self):
        book_url = variables.SERVER_ADDRESS + '/boock/'
        response = requests.post(book_url, json=dataset03.book2)

        # Code 404 = Not Found
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_add_book_existing_book_path(self):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=dataset03.book2)

        assert response.status_code == HTTPStatus.CREATED
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload. The data received is the same as the one sent
        data = response.json()
        data_id = data[variables.BOOK_ID]

        # Add another book in the same path
        book_url = variables.MAIN_PATH + '/' + data_id
        response = requests.post(book_url, json=dataset03.book4)
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

    def test_add_book_with_book_id(self):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=dataset03.book_with_id)

        # The book has been created but the book_id has been ignored
        assert response.status_code == HTTPStatus.CREATED
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Validate payload
        data = response.json()
        assert data[variables.BOOK_ID] != \
               dataset03.book_with_id[variables.BOOK_ID]

    @pytest.mark.parametrize("book_data, field", [
        (dataset03.book1_empty_title, variables.TITLE),
        (dataset03.book1_empty_author, variables.AUTHOR),
    ])
    def test_add_book_empty_fields(self, book_data, field):
        book_url = variables.MAIN_PATH
        response = requests.post(book_url, json=book_data)

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.headers['Content-Type'] == variables.CONTENT_TYPE
        # Check the error message
        data = response.json()
        assert data['error'] == field + ' cannot be empty'
