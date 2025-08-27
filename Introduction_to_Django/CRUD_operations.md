create


from bookshelf.models import Book

# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output (book instance created successfully)
print(book)
# Expected output:
# <Book: 1984 by George Orwell (1949)>



# Retrieve the Created Book

```python
from bookshelf.models import Book

# Retrieve the first book
book = Book.objects.get(title="1984")

# Output book attributes
print(book.title)   # Expected: 1984
print(book.author)  # Expected: George Orwell
print(book.publication_year)  # Expected: 1949



# Update the Book Title

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Output updated book
print(book)
# Expected output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>



```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Check if any books remain
print(Book.objects.all())
# Expected output:
# <QuerySet []>  (empty list confirming deletion)

