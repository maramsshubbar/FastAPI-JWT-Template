from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel

class BookModel(BaseModel):
    __tablename__ = "book"

    title = Column(String)
    author = Column(String)
    description = Column(String)
    published_year = Column(Integer)
    
    user_id = Column(Integer, ForeignKey("users.id") )

    user = relationship("UserModel", back_populates="books")
    reviews = relationship("ReviewModel", back_populates="book")
        