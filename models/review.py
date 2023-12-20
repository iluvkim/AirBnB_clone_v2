#!/usr/bin/python3
"""Defines the Review class"""

from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_type

class Review(BaseModel, Base):
    """Stores review information for the HBNB project"""
    __tablename__ = 'reviews'

    if storage_type == 'db':
        # Define columns for the 'reviews' table in the database
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        # Default values for non-database storage
        place_id = ""
        user_id = ""
        text = ""
