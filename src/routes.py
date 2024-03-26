from fastapi import APIRouter, Depends, HTTPException
from .database import SessionLocal
from sqlalchemy.orm import Session

from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

from src.schemas.userSchema import User, UserCreate
from src.schemas.postSchema import Post, PostCreate

from src.crud.userCrud import *
from src.crud.postCrud import *

router = APIRouter(
    prefix='/users',
    tags=['users'],
    responses={404: {'description': 'Not found'}}
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post('/', response_model=User)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db), ):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.get('/{user_id}', response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router.post('/{user_id}/posts/', response_model=Post)
async def create_post_for_user(user_id: int, item: PostCreate, db: Session = Depends(get_db)):
    return create_user_post(db=db, item=item, user_id=user_id)


@router.get("/", response_model=Post)
async def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = get_posts(db, skip=skip, limit=limit)
    return posts
