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

