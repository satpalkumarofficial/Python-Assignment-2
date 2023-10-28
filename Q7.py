"""
Q7.Write a Python program to create a class named Book with attributes title, author and
    price. Implement methods to display the book’s information and apply a discount on the
    price. Also, implement a subclass named EBook with an additional attribute format.
    Override the display method for the EBook subclass."""


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price}"

    def apply_discount(self, discount):
        if 0 < discount < 1:
            self.price = self.price - (self.price * discount)
            return f"Price after {discount*100}% discount: ${self.price}"
        else:
            return "Invalid discount value. Please provide a value between 0 and 1 (exclusive)."

class EBook(Book):
    def __init__(self, title, author, price, e_format):
        super().__init__(title, author, price)
        self.format = e_format

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price}\nFormat: {self.format}"


book1 = Book("Python Programming", "Guido van Rossum", 30)
print(book1.display_info())
print(book1.apply_discount(0.2))

ebook1 = EBook("Eloquent JavaScript", "Marijn Haverbeke", 25, "PDF")
print(ebook1.display_info())
print(ebook1.apply_discount(0.1))
