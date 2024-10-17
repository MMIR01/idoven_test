"""
Test data used for non-nominal tests

@Author: M. Miralles
"""

book1 = {"title": "Book 1",
         "author": "Andrew A",
         "published_date": "2024-01-01",
         "isbn": "1111111111111",
         "price": 10.50}

book1_missing_title = {"author": "Andrew A",
                       "published_date": "2024-01-01",
                       "isbn": "1111111111111",
                       "price": 10.50}

book1_missing_author = {"title": "Book 1",
                        "published_date": "2024-01-01",
                        "isbn": "1111111111111",
                        "price": 10.50}

book1_missing_published_date = {"title": "Book 1",
                                "author": "Andrew A",
                                "isbn": "1111111111111",
                                "price": 10.50}

book1_missing_isbn = {"title": "Book 1",
                      "author": "Andrew A",
                      "published_date": "2024-01-01",
                      "price": 10.50}

book1_missing_price = {"title": "Book 1",
                       "author": "Andrew A",
                       "published_date": "2024-01-01",
                       "isbn": "1111111111111"}

book1_missing_all = {}

book1_empty_title = {"title": "",
                     "author": "Andrew A",
                     "published_date": "2024-01-01",
                     "isbn": "1111111111111",
                     "price": 10.50}

book1_empty_author = {"title": "Book 1",
                      "author": "",
                      "published_date": "2024-01-01",
                      "isbn": "1111111111111",
                      "price": 10.50}

book1_empty_price = {"title": "Book 1",
                     "author": "Andrew A",
                     "published_date": "2024-01-01",
                     "isbn": "1111111111111",
                     "price": ""}

book1_extra_field = {"title": "Book 1",
                     "author": "Andrew A",
                     "published_date": "2024-01-01",
                     "isbn": "1111111111111",
                     "price": 10.50,
                     "extra_field": "extra"}

book1_wrong_type_title = {"title": 123,
                          "author": "Andrew A",
                          "published_date": "2024-01-01",
                          "isbn": "1111111111111",
                          "price": 10.50}

book1_wrong_type_author = {"title": "Book 1",
                           "author": 123,
                           "published_date": "2024-01-01",
                           "isbn": "1111111111111",
                           "price": 10.50}

book1_wrong_type_published_date = {"title": "Book 1",
                                   "author": "Andrew A",
                                   "published_date": 123,
                                   "isbn": "1111111111111",
                                   "price": 10.50}

book1_wrong_type_isbn = {"title": "Book 1",
                         "author": "Andrew A",
                         "published_date": "2024-01-01",
                         "isbn": 123,
                         "price": 10.50}

book1_wrong_type_price = {"title": "Book 1",
                          "author": "Andrew A",
                          "published_date": "2024-01-01",
                          "isbn": "1111111111111",
                          "price": "10.50"}

book1_wrong_type_published_date_format = {"title": "Book 1",
                                          "author": "Andrew A",
                                          # Wrong date format
                                          "published_date": "01-01-2024",
                                          "isbn": "1111111111111",
                                          "price": 10.50}

book1_wrong_isbn_format = {"title": "Book 1",
                           "author": "Andrew A",
                           "published_date": "2024-01-01",
                           # ISBN has 13 numbers
                           "isbn": "1234567890123",
                           "price": 10.50}

book1_wrong_price_negative = {"title": "Book 1",
                              "author": "Andrew A",
                              "published_date": "2024-01-01",
                              "isbn": "1111111111111",
                              # Negative price
                              "price": -7500.50}

book1_wrong_price_zero = {"title": "Book 1",
                          "author": "Andrew A",
                          "published_date": "2024-01-01",
                          "isbn": "1111111111111",
                          # Zero price
                          "price": 0}

book1_long_price = {"title": "Book 1",
                    "author": "Andrew A",
                    "published_date": "2024-01-01",
                    "isbn": "1111111111111",
                    # It might overflow
                    "price": 10000000000000000.50}

book1_long_title = {"title": "a" * 256,
                    "author": "Andrew A",
                    "published_date": "2024-01-01",
                    "isbn": "1111111111111",
                    "price": 10.50}

book1_long_author = {"title": "Book 1",
                     "author": "a" * 256,
                     "published_date": "2024-01-01",
                     "isbn": "1111111111111",
                     "price": 10.50}

book2 = {"title": "Book 2",
         "author": "Bernard B",
         "published_date": "2024-03-03",
         "isbn": "2222222222222",
         "price": 20.50}

# Book in xml format
book3_xml = "<book> \
               <title>Book 3</title> \
                <author>Charlie C</author> \
                <published_date>2024-05-05</published_date> \
                <isbn>3333333333333</isbn> \
                <price>30.50</price> \
            </book>"

book4 = {"title": "Book 4",
         "author": "David D",
         "published_date": "2024-07-07",
         "isbn": "4444444444444",
         "price": 44.50}

book_with_id = {"book_id": "10",
                "title": "Book 5",
                "author": "Edward E",
                "published_date": "2024-09-09",
                "isbn": "5555555555555",
                "price": 100.50}