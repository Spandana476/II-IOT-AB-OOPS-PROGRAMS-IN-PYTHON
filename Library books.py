class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"' {book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found: {book}")
                return book
        print(f"'{title}' not found.")
        return None
    def borrow_book(self, title):
        book = self.search_book(title)
        if book and book.is_available:
            book.is_available = False
            print(f"you borrowed '{book.title}'.")
        elif book:
            print(f"'{book.title}' is already borrowed.")
            
    def return_book(self, title):
        book = self.search_book(title)
        if book and not book.is_available:
            book.is_available = True
            print(f"you returned '{book.title}'.")
        elif book:
            print(f"'{book.title}'was not borrowed.")

lib = Library()
lib.add_book(Book("Python Basics", "John Doe"))
lib.add_book(Book("Data Science", "Jane Smith"))
lib.add_book(Book("Machine Learning", "Alan Turing"))

while True:
    choice = int(input('''
    ==== Library Menu ====
    1 -> Display All Books
    2 -> Add a Book
    3 -> Remove a Book
    4 -> Search a Book
    5 -> Borrow a Book
    6 -> Return a Book
    7 -> Exit
    Enter Choice: '''))

    if choice == 1:
        print ("\nLibrary Collection:")
        for b in lib.books:
            print(b)
    elif choice == 2:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        lib.add_book(Book(title, author))

    elif choice == 3:
        title = input("Enter book title to remove: ")
        lib.remove_book(title)

    elif choice == 4:
        title = input("Enter book title to search: ")
        lib.search_book(title)

    elif choice == 5:
        title = input("Enter book title to borrow: ")
        lib.borrow_book(title)

    elif choice == 6:
        title = input("Enter book title return: ")
        lib.return_book(title)

    elif choice ==7:
        print("Exiting Library System. Goodbye!")

    else:
        print("Invalid choice. Try again.")
