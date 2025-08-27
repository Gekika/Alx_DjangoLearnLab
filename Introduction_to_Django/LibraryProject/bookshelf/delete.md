# Retrieve the book
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Check if any books remain
print(Book.objects.all())
# Expected output:
# <QuerySet []>  (empty list confirming deletion)

