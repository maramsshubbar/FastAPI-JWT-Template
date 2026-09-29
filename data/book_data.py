from models.book import BookModel


def create_test_books():
    book1 = BookModel(
        title="The Hobbit",
        author="J.R.R. Tolkien",
        user_id=1
    )

    book2 = BookModel(
        title="Harry Potter",
        author="J.K. Rowling",
        user_id=2
    )

    book3 = BookModel(
        title="The Alchemist",
        author="Paulo Coelho",
        user_id=3
    )

    return [book1, book2, book3]


book_list = create_test_books()