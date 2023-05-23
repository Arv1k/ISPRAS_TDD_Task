"""
Bookstore fot ISPRAS TDD task
"""

import random
import unittest
import cProfile


class TDD(unittest.TestCase):
    def test_add_to_cart(self):
        self.assertEqual(store.add_to_cart(0), "Book 0 added")
        self.assertEqual(store.add_to_cart(4), "Book 4 added")
        self.assertEqual(store.add_to_cart(11), "Bookstore doesn't have so much books!")
        self.assertEqual(store.add_to_cart(-1), "Only books numbers are allowed!")

class Book:
    def __init__(self, title, price, genre):
        self.title = title
        self.price = price
        self.genre = genre

    def __repr__(self):
        return "{:s} : {:d} : {:s}".format(self.title, self.price, self.genre)

    def __str__(self):
        title = "Title: " + self.title
        price = "Price: {:d}".format(self.price)
        genre = "Genre: " + self.genre

        return title + '\n' + price + '\n' + genre

class Bookstore:
    def __init__(self):
        self.books_count = random.randrange(5, 10)
        self.books = []
        for i in range(self.books_count):
            title = "Book " + str(i)
            price = random.randrange(100, 1000)
            genre = random.choice(['Fantastic', 'Fantasy', 'Manga'])
            self.books.append(Book(title, price, genre))
        self.cart = []

    def catalog(self):
        print("Total number of books: {:d}".format(store.books_count))
        for i in range(store.books_count):
            print("#{:d}".format(i))
            print(store.books[i]);
            print()

    def add_to_cart(self, id):
        if (id > 10):
            print("Bookstore doesn't have so much books!")
            return "Bookstore doesn't have so much books!"
        elif (id < 0):
            print("Only books numbers are allowed!")
            return "Only books numbers are allowed!"

        self.cart.append(self.books[id])

        print(self.books[id].title + " added")

        return self.books[id].title + " added"

store = Bookstore()

store.catalog()

unittest.main()
