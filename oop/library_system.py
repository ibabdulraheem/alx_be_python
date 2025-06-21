class Book:
  def __init__(self,title:str,author:str):
    self.title = title
    self.author = author

class EBook(Book):
  def __init__(self, title=str, author=str, file_size = int):
    self.file_size = file_size
    super().__init__(title, author)

class PrintBook(Book):
  def __init__(self, title=str, author=str,page_count = int):
    self.page_count = page_count
    super().__init__(title, author)

class Library:  # Implementing composition
  def __init__(self,books = []):
    self.books = books
  def add_book(self,book):
    self.book = book
    self.books.append(book)
