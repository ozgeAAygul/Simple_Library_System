class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    return f"{self.title} - {self.author}"

class Library:
  
  def __init__(self):
    self.books = []

  def add_book(self, book):
    self.books.append(book)
    print("Book added:)")

  def remove_book(self, title):
    for book in self.books:
      if book.title == title:
        self.books.remove(book)
        print("Book removed")
        return
    print("Book is not found!")


  def list_books(self):
    if not self.books:
       print("There is no book")
       return
    print("\nBooks in library:")
    for book in self.books:
       print(book)
    print()
  
lib = Library()

while True:
  choice = input("1-Add  2-List  3-Remove  4-Quit: ")

  if choice == "1":
    title = input("Title: ")
    author = input("Author: ")
    lib.add_book(Book(title, author))

  elif choice == "2":
    lib.list_books()

  elif choice == "3":
    title = input("Title to remove: ")
    lib.remove_book(title)
  elif choice == "4":
    break

  


