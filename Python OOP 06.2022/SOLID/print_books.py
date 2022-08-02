class Book:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content


class Formatter:

    def format(self, book: Book) -> str:
        return book.content


class PrePrintFlyer:

    def format(self, book: Book):
        return f"----------\n{book.title}\n----------\n{book.author}\n----------"


class Printer:

    def __init__(self, formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(book)


normal_formatter = Formatter()
flyer_formatter = PrePrintFlyer()

book_1 = Book("Alice in Wonderland", "Lewis Carroll", "We are all mad here.")

printer_1 = Printer(normal_formatter)

printer_2 = Printer(flyer_formatter)

print(printer_1.get_book(book_1))

print()
print()

print(printer_2.get_book(book_1))
