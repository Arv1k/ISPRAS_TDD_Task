"""
Bookstore fot ISPRAS TDD task
"""

import random

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
        self.books_count = random.randrange(10, 100)
        self.books = []
        for i in range(self.books_count):
            title = "Book " + str(i)
            price = random.randrange(100, 1000)
            genre = random.choice(['Fantastic', 'Fantasy', 'Manga'])
            self.books.append(Book(title, price, genre))

store = Bookstore()

print(store.books_count);
for i in range(store.books_count):
    print(store.books[i]);
    print()
