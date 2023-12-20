#!/usr/bin/python3
"""Defines the User class"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represents a user with various attributes"""
    __tablename__ = 'users'

    if storage_type == 'db':
        # Define columns for the 'users' table in the database
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        # Define relationships with other tables in the database
        places = relationship('Place', backref='user',
                              cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                               cascade='all, delete, delete-orphan')
    else:
        # Default values for non-database storage
        email = ""
        password = ""
        first_name = ""
        last_name = ""

