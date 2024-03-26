from pydantic import BaseModel, EmailStr
from src.schemas.postSchema import Post


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int = None
    is_active: bool = True
    posts: list[Post] = []

    class Config:
        from_attributes = True
