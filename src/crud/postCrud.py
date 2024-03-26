from sqlalchemy.orm import Session
from src.models.postModel import PostModel
from src.schemas.postSchema import Post, PostCreate


def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def create_user_post(db: Session, item: PostCreate, user_id: int):
    db_post = PostModel(**item.model_dump(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
