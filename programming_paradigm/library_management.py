class Book:
  def __init__(self,title,author,_is_checked_out= False):
    self.title = title
    self.author = author
    self._is_checked_out = _is_checked_out
  def checked_out(self):
    if not self._is_checked_out:
      self._is_checked_out is True
      return (f"Book '{self.title}' checked out.")
    else:
      return (f"Book '{self.title}' already checked out.")
  def return_book(self):
    if self._is_checked_out:
      self._is_checked_out is False
      return (f"Book '{self.title}' returned.")
    else:
      return (f"Book '{self.title}' already returned.")
  def __str__(self):
    status = "checked out" if self._is_checked_out else "Available"
    return (f"Book: {self.title} by {self.author}(status: {status})")
      

class Library:
  def __init__(self):
    self._books = []
  def add_book(self,book ):
    self._books[book].append(book)
  def check_out_book(self,title):
    self.title = title
    if book[title] in self._books:
      book = self._books [title]
      print(f"{book} is not checked out")
    elif book[title] not in self._books:
      print(f"{book} is checked out")
  def return_book(self,title):
    self.title = title
    if self.title in self._books:
      print(f"The {self._books} has been returned")
    else:
      print("The book has not been returned")
  def list_available_books(self):
    print(f"{self._books}")

    
    
    

    