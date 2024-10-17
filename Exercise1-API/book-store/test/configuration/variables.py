"""
Variables needed for the tests

@Author: M. Miralles
"""

# Server information
# When running the tests in a local environment, the SERVER_URL should be
#SERVER_URL = "http://127.0.0.1"
# When running the test from Docker:
# https://docs.docker.com/desktop/networking/#use-cases-and-workarounds-for-all-platforms
SERVER_URL = "http://host.docker.internal"

SERVER_PORT = "5000"
SERVER_ADDRESS = SERVER_URL + ":" + SERVER_PORT

MAIN_PATH = SERVER_ADDRESS + "/books"

# Other variables
CONTENT_TYPE = 'application/json'

BOOK_ID = 'book_id'
TITLE = 'title'
AUTHOR = 'author'
PUBLISHED_DATE = 'published_date'
ISBN = 'isbn'
PRICE = 'price'
