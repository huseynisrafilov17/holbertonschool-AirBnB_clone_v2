#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", back_populates="user", cascade="delete")
    reviews = relationship("Review", back_populates="user", cascade="delete")
    
    @property
    def places():
        from models import storage
        objects = storage.all(Place)
        places = []
        for i in objects:
            if User.id == objects[i].user_id:
                places.append(objects[i])
        return places

    @property
    def reviews():
        from models import storage
        objects = storage.all(Review)
        reviews = []
        for i in objects:
            if User.id == objects[i].user_id:
                reviews.append(objects[i])
        return reviews
