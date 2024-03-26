from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(40), unique=True, index=True)
    hashed_password = Column(String(40))
    is_active = Column(Boolean, default=True)

    posts = relationship('PostModel', back_populates='owner')
