class Book:
  def __init__(self,title:str,author:str):
    self.title = title
    self.author = author
  def __str__(self):
    return (f"{self.bks.title} published by {self.bks.author}")

class EBook(Book):
  def __init__(self, title:str, author:str, file_size:int):
    self.file_size = file_size
    super().__init__(title, author)

class PrintBook(Book):
  def __init__(self, title:str, author:str,page_count:int):
    self.page_count = page_count
    super().__init__(title, author)

class Library:  # Implementing composition
  def __init__(self):
    self.books = []
  def add_book(self,book):
    self.book = book
    self.books.append(book)
  def list_books(self):
    self.bks = Book("good man","Ibrahim")
    self.bke = EBook("good man","Ibrahim",42)
    self.bkp = PrintBook("good man","Ibrahim",50)
    print(f"Book: {self.bks.title} published by {self.bks.author}")
    print(f"EBook: {self.bks.title} published by {self.bks.author}, File Size: {self.bke.file_size}KB")
    print(f"PrintBook: {self.bks.title} published by {self.bks.author}, Page Count: {self.bkp.page_count} ")
my_book = Book()
my_ebook = EBook()
my_print_book = PrintBook()
my_library = Library()