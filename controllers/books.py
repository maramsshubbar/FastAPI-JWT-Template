from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models.book import BookModel
from serializers.book import BookSchema, BookCreateSchema , BookUpdateSchema
from database import get_db

from dependencies.get_current_user import get_current_user
from models.user import UserModel

router = APIRouter()


@router.get("/", response_model=list[BookSchema])
def get_books(db: Session = Depends(get_db)):
    books = db.query(BookModel).all()
    return books


@router.get("/{book_id}", response_model=BookSchema)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("/", response_model=BookSchema, status_code=201)
def create_book(
    book: BookCreateSchema,
    db: Session = Depends(get_db),
    user: UserModel = Depends(get_current_user)
):
    new_book = BookModel(
        title=book.title,
        author=book.author,
        user_id=user.id
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book




@router.put("/{book_id}", response_model=BookSchema)
def update_book(
    book_id: int,
    book: BookUpdateSchema,
    db: Session = Depends(get_db)
):
    existing_book = db.query(BookModel).filter(
        BookModel.id == book_id
    ).first()

    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")

    existing_book.title = book.title
    existing_book.author = book.author

    db.commit()
    db.refresh(existing_book)

    return existing_book



@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = db.query(BookModel).filter(
        BookModel.id == book_id
    ).first()

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}
