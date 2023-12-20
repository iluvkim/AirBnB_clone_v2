#!/usr/bin/python3
"""Defines the Amenity class"""

from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """Represents an amenity for the HBNB project"""

    __tablename__ = 'amenities'

    if storage_type == 'db':
        # Define column for the 'amenities' table in the database
        name = Column(String(128), nullable=False)
    else:
        # Default value for non-database storage
        name = ""
