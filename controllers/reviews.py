from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.review import ReviewModel
from models.book import BookModel
from serializers.review import ReviewSchema, ReviewCreateSchema, ReviewUpdateSchema
from database import get_db

router = APIRouter()


@router.get("/{book_id}/reviews", response_model=list[ReviewSchema])
def get_reviews(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = db.query(BookModel).filter(
        BookModel.id == book_id
    ).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    reviews = db.query(ReviewModel).filter(
        ReviewModel.book_id == book_id
    ).all()

    return reviews



@router.post("/{book_id}/reviews", response_model=ReviewSchema, status_code=201)
def create_review(
    book_id: int,
    review: ReviewCreateSchema,
    db: Session = Depends(get_db)
):
    book = db.query(BookModel).filter(
        BookModel.id == book_id
    ).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    new_review = ReviewModel(
        text=review.text,
        rating=review.rating,
        book_id=book_id
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)

    return new_review



@router.get("/{book_id}/reviews/{review_id}", response_model=ReviewSchema)
def get_review(
    book_id: int,
    review_id: int,
    db: Session = Depends(get_db)
):
    review = db.query(ReviewModel).filter(
        ReviewModel.id == review_id,
        ReviewModel.book_id == book_id
    ).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    return review



@router.put("/{book_id}/reviews/{review_id}", response_model=ReviewSchema)
def update_review(
    book_id: int,
    review_id: int,
    review: ReviewUpdateSchema,
    db: Session = Depends(get_db)
):
    existing_review = db.query(ReviewModel).filter(
        ReviewModel.id == review_id,
        ReviewModel.book_id == book_id
    ).first()

    if not existing_review:
        raise HTTPException(status_code=404, detail="Review not found")

    existing_review.text = review.text
    existing_review.rating = review.rating

    db.commit()
    db.refresh(existing_review)

    return existing_review



@router.delete("/{book_id}/reviews/{review_id}")
def delete_review(
    book_id: int,
    review_id: int,
    db: Session = Depends(get_db)
):
    review = db.query(ReviewModel).filter(
        ReviewModel.id == review_id,
        ReviewModel.book_id == book_id
    ).first()

    if not review:
        raise HTTPException(status_code=404, detail="Review not found")

    db.delete(review)
    db.commit()

    return {"message": "Review deleted successfully"}