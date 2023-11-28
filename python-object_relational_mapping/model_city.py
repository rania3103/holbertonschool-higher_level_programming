#!/usr/bin/python3
"""a Python file similar to model_state.py named
model_city.py that contains the class definition of a City."""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sys import argv
Base = declarative_base()


class City(Base):
    """claas state that inherits from base"""
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey(states.id))
