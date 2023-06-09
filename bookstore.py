"""
Bookstore fot ISPRAS TDD task
"""

import random
import unittest


class TDD(unittest.TestCase):
    def test_0_add_to_cart(self):
        self.assertEqual(store.add_to_cart(0), "Book 0 added")
        self.assertEqual(store.add_to_cart(4), "Book 4 added")
        self.assertEqual(store.add_to_cart(11), "Bookstore doesn't have so much books!")
        self.assertEqual(store.add_to_cart(-1), "Only books numbers are allowed!")

    def test_1_remove_from_cart(self):
        self.assertEqual(store.remove_from_cart(0), "Book 0 removed")
        self.assertEqual(store.remove_from_cart(4), "Book 4 removed")
        self.assertEqual(store.remove_from_cart(1), "There aren't any books in the cart!")
        store.add_to_cart(4)
        self.assertEqual(store.remove_from_cart(1), "There isn't that book in the cart!")
        store.add_to_cart(0)
        self.assertEqual(store.remove_from_cart(0), "Book 0 removed")

    def test_2_check_sale(self):
        store.add_to_cart(0)
        self.assertEqual(store.check_sale(), "2%")
        store.add_to_cart(1)
        self.assertEqual(store.check_sale(), "3%")
        store.add_to_cart(2)
        self.assertEqual(store.check_sale(), "4%")
        store.add_to_cart(3)
        self.assertEqual(store.check_sale(), "5%")
        store.remove_from_cart(4)
        store.remove_from_cart(3)
        store.remove_from_cart(2)
        store.remove_from_cart(1)
        self.assertEqual(store.check_sale(), "0%")

    def test_3_catalog(self):
        self.assertEqual(store.catalog(), 1)


class Book:
    def __init__(self, title, price, genre, id):
        self.title = title
        self.price = price
        self.genre = genre
        self.id = id

    def __str__(self):
        id = "#{:d}".format(self.id)
        title = "Title: " + self.title
        price = "Price: {:d}".format(self.price)
        genre = "Genre: " + self.genre

        return id + '\n' + title + '\n' + price + '\n' + genre


class Bookstore:
    def __init__(self):
        self.books_count = random.randrange(5, 10)
        self.books = []
        for i in range(self.books_count):
            title = "Book " + str(i)
            price = random.randrange(100, 1000)
            genre = random.choice(['Fantastic', 'Fantasy', 'Manga'])
            self.books.append(Book(title, price, genre, i))
        self.cart = []

    def catalog(self):
        print("Total number of books: {:d}".format(store.books_count))
        for i in range(store.books_count):
            print(store.books[i])
            print()

        return 1

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

    def remove_from_cart(self, id):
        if len(self.cart) == 0:
            print("There aren't any books in the cart!")
            return "There aren't any books in the cart!"

        for i in range(len(self.cart)):
            if self.cart[i].id == id:
                del self.cart[i]

                print("Book {:d} removed".format(id))

                return "Book {:d} removed".format(id)

        print("There isn't that book in the cart!")

        return "There isn't that book in the cart!"

    def check_sale(self):
        if len(self.cart) == 2:
            print("2%")

            return "2%"

        elif len(self.cart) == 3:
            print("3%")

            return "3%"

        elif len(self.cart) == 4:
            print("4%")

            return "4%"

        elif len(self.cart) == 5:
            print("5%")

            return "5%"

        else:
            print("0%")

            return "0%"


store = Bookstore()

unittest.main()
