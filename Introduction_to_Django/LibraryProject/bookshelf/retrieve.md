# Retrieve the Created Book

```python
from bookshelf.models import Book

# Retrieve the first book
book = Book.objects.get(title="1984")

# Output book attributes
print(book.title)   # Expected: 1984
print(book.author)  # Expected: George Orwell
print(book.publication_year)  # Expected: 1949

