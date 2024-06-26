#!/usr/bin/python3
"""definition of a State and an instance """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ This will create a State class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
