from abc import ABC, abstractmethod

# Item base class
class Item(ABC):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = False
    
    @abstractmethod
    def display_info(self):
        pass

# Book subclass
class Book(Item):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages
    
    def display_info(self):
        return f"Book: {self.title}, Author: {self.author}, Year: {self.year}, Pages: {self.pages}"

# Magazine subclass
class Magazine(Item):
    def __init__(self, title, author, year, issue):
        super().__init__(title, author, year)
        self.issue = issue
    
    def display_info(self):
        return f"Magazine: {self.title}, Author: {self.author}, Year: {self.year}, Issue: {self.issue}"

# LibraryUser class
class LibraryUser:
    def __init__(self, name):
        self.name = name
        self.borrowed_items = []

    def borrow(self, item):
        if item.is_borrowed:
            raise Exception(f"{item.title} is already borrowed by someone else.")
        else:
            self.borrowed_items.append(item)
            item.is_borrowed = True
            print(f"{self.name} borrowed {item.title}.")

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            item.is_borrowed = False
            print(f"{self.name} returned {item.title}.")
        else:
            raise Exception(f"{item.title} is not borrowed by {self.name}.")
    
    def list_borrowed_items(self):
        if self.borrowed_items:
            print(f"{self.name} has borrowed the following items:")
            for item in self.borrowed_items:
                print(f" - {item.display_info()}")
        else:
            print(f"{self.name} has not borrowed any items.")

# Library class
class Library:
    def __init__(self):
        self.items = []
        self.users = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added {item.title} to the library.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item.title} from the library.")
        else:
            raise Exception(f"{item.title} not found in library collection.")

    def register_user(self, user):
        self.users.append(user)
        print(f"Registered user: {user.name}")

    def borrow_item(self, user, item):
        if item not in self.items:
            raise Exception(f"{item.title} is not available in the library.")
        try:
            user.borrow(item)
        except Exception as e:
            print(e)

    def return_item(self, user, item):
        try:
            user.return_item(item)
        except Exception as e:
            print(e)

    def list_items(self):
        if self.items:
            print("Library items:")
            for item in self.items:
                print(f" - {item.display_info()}")
        else:
            print("No items in the library.")

    def list_available_items(self):
        available_items = [item for item in self.items if not item.is_borrowed]
        if available_items:
            print("Available items:")
            for item in available_items:
                print(f" - {item.display_info()}")
        else:
            print("No items are currently available.")

    def borrowed_summary(self):
        borrowed_items = [(item, user) for user in self.users for item in user.borrowed_items]
        if borrowed_items:
            print("Borrowed Items Summary:")
            for item, user in borrowed_items:
                print(f" - {item.title} is borrowed by {user.name}")
        else:
            print("No items are currently borrowed.")


# Main Program
def main():
    # Create library
    library = Library()

    # Create items
    book1 = Book("The Fault in Our Stars", "John Green", 2012, 313)
    book2 = Book("Harry Potter and the Sorcerer's Stone", "J.K Rowling, Olly Moss", 1997, 333)
    book3 = Book("The Hunger Games", "Suzanne Collins", 2008, 374)
    mag1 = Magazine("Vogue on location", "Collectif", 2019, "October")
    mag2 = Magazine("Vogue and the met", "Malle Chloe", 2020, "May")

    # Add items to library
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(book3)
    library.add_item(mag1)
    library.add_item(mag2)

    # Create users
    user1 = LibraryUser("Sofia")
    user2 = LibraryUser("Nikita")

    # Register users in the library
    library.register_user(user1)
    library.register_user(user2)

    # Borrowing process
    library.borrow_item(user1, book1)  
    library.borrow_item(user2, mag1)   
    library.borrow_item(user1, book2)  

    # Try to borrow an already borrowed book
    library.borrow_item(user2, book1)  

    # Listing borrowed items
    user1.list_borrowed_items()
    user2.list_borrowed_items()

    # Return items
    library.return_item(user1, book1)  

    # List available items
    library.list_available_items()

    # Display summary of borrowed items
    library.borrowed_summary()

# Run the program
if __name__ == "__main__":
    
    
    main()