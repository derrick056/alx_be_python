class Book:
    """Represents a book with a title, an author, and its availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Manages a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a book to the library."""
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"The book '{title}' has been checked out.")
                    return
        print(f"The book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Returns a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"The book '{title}' has been returned.")
                    return
        print(f"The book '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
