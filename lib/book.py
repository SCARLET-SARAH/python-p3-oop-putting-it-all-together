#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        if isinstance(page_count, int):
            self.page_count = page_count
        else:
            raise ValueError("page_count must be an integer")

    def __str__(self):
        return f"{self.title} ({self.page_count} pages)"

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
def test_requires_int_page_count(self):
    book = Book("And Then There Were None", 272)
    with self.assertRaises(ValueError):
        book.page_count = "not an integer"

    
    
        