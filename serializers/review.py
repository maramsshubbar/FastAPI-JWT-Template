from pydantic import BaseModel


class ReviewSchema(BaseModel):
    id: int
    text: str
    rating: int
    book_id: int

    class Config:
        orm_mode = True


class ReviewCreateSchema(BaseModel):
    text: str
    rating: int



class ReviewUpdateSchema(BaseModel):
    text: str
    rating: int