"""Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each
publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor. Also
write the required initializers to both classes. Create a print_information method to both subclasses for printing out
all information of the publication in question. In the main program, create publications Donald Duck
(chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both
publications using the methods you implemented."""

class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        Publication.__init__(self, name)
        self.author = author
        self.page_count = page_count

    def print_book_information(self):
        print(self.name, self.author, self.page_count)

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        Publication.__init__(self, name)
        self.chief_editor = chief_editor

    def print_mag_information(self):
        print(self.name, self.chief_editor)


magazine = Magazine('Donald Duck', 'Aki Hyyppa')

book = Book('Compartment No. 6', 'Rosa Liksom', 192)

magazine.print_mag_information()
book.print_book_information()



