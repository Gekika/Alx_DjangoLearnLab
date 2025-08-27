
# Create a book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Output (book instance created successfully)
print(book)
# Expected output:
# <Book: 1984 by George Orwell (1949)>
