from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    author : str
    user_id : int

    class Config:
        orm_mode = True



class BookCreateSchema(BaseModel):
    title: str
    author : str


class BookUpdateSchema(BaseModel):
    title: str
    author: str
