from models.review import ReviewModel


def create_test_reviews():
    review1 = ReviewModel(
        text="A very enjoyable book.",
        rating=5,
        book_id=1
    )

    review2 = ReviewModel(
        text="Interesting story with great characters.",
        rating=4,
        book_id=1
    )

    review3 = ReviewModel(
        text="A simple but meaningful story.",
        rating=5,
        book_id=3
    )

    return [review1, review2, review3]


review_list = create_test_reviews()