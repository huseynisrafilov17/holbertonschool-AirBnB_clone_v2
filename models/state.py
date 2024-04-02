#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities():
        from models import storage
        objects = storage.all(City)
        cities = []
        for i in objects:
            if State.id == objects[i].state_id:
                cities.append(objects[i])
        return cities
