class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")

    def list_books(self):

        self.file.seek(0)
        self.list = self.file.readlines()

        for i in self.list:

            book_info = i.split(',')

            book_title = book_info[0]
            book_author = book_info[1]

            print(f"Book: {book_title}, Author: {book_author}")

    def add_book(self):

        self.title = input("Enter a Book Title: ")
        self.author = input("Enter a Book Author: ")
        self.year = input("Enter a Year First Published: ")
        self.pages = input("Enter a Number of Pages: ")

        self.file.write(self.title + "," + self.author + "," + self.year + "," + self.pages + "\n")

    def remove_book(self):

        self.user = input("Book Title: ")

        self.file.seek(0)
        self.liste_book = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for i in self.liste_book:
            if self.user not in i:
                self.file.write(i)
                # self.index = self.liste_book.index(i)
                # self.liste_book.remove(i)
                # del self.liste_book[self.index]
                # break

    def __del__(self):
        self.file.close()