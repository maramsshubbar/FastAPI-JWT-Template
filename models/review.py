from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class ReviewModel(BaseModel):

    __tablename__ = "reviews"
    title = Column(String)
    text = Column(String)
    rating = Column(Integer)


    book_id = Column(Integer, ForeignKey("book.id"))

    book = relationship("BookModel", back_populates="reviews")
    