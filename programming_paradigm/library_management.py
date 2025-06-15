class Book:
    """Represents a book in a library with a title, author, and checkout status."""
    
    def __init__(self, title, author):
        """Init book with title, author, and checkout status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        """Mark book as available."""
        if self._is_checked_out:
            self._is_checked_out = False

    def is_available(self):
        """Return whether book is available for borrowing."""
        return not self._is_checked_out


class Library:
    """Represents a library that contains a collection of books."""
    
    def __init__(self):
        """Init library with an empty book list."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                break

    def return_book(self, title):
        """Return a book by its title if it's currently checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                break

    def list_available_books(self):
        """List all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
