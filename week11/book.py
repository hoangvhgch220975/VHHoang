def load_books():
    books = {
        'Harry Potter vol 1': ['J.K. Rowling', 20.0],
        'Sherlock Holmes': ['Arthur Conan Doyle', 15.0],
        'Master Python in 21 Days': ['Alain Durant', 30.0],
        'The Lord of the Rings': ['J.R.R. Tolkien', 25.0]
    }
    return books

def load_names(books):
    return list(books.keys())