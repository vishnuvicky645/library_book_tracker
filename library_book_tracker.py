class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def __str__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        # Check for duplicate ISBN
        if any(book.isbn == isbn for book in self.books):
            print(f"Error: Book with ISBN {isbn} already exists.")
            return
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def find_book(self, identifier):
        # Search by ISBN or title (case-insensitive partial match for title)
        for book in self.books:
            if book.isbn == identifier or identifier.lower() in book.title.lower():
                return book
        return None

    def check_out(self, identifier):
        book = self.find_book(identifier)
        if not book:
            print(f"Error: Book '{identifier}' not found.")
            return
        if book.checked_out:
            print(f"Error: '{book.title}' is already checked out.")
            return
        book.checked_out = True
        print(f"Checked out: {book}")

    def check_in(self, identifier):
        book = self.find_book(identifier)
        if not book:
            print(f"Error: Book '{identifier}' not found.")
            return
        if not book.checked_out:
            print(f"Error: '{book.title}' is already available.")
            return
        book.checked_out = False
        print(f"Checked in: {book}")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\nLibrary Collection:")
        for book in self.books:
            print(book)

def main():
    library = Library()
    
    # Sample data
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    library.add_book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    library.add_book("1984", "George Orwell", "9780451524935")
    
    while True:
        print("\n=== Library Book Tracker ===")
        print("1. Add Book")
        print("2. Check Out Book")
        print("3. Check In Book")
        print("4. View All Books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author: ").strip()
            isbn = input("Enter ISBN: ").strip()
            library.add_book(title, author, isbn)
            
        elif choice == "2":
            identifier = input("Enter book title or ISBN to check out: ").strip()
            library.check_out(identifier)
            
        elif choice == "3":
            identifier = input("Enter book title or ISBN to check in: ").strip()
            library.check_in(identifier)
            
        elif choice == "4":
            library.display_books()
            
        elif choice == "5":
            print("Thank you for using the Library Book Tracker!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()