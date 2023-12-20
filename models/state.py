#!/usr/bin/python3
""" State Module for HBNB project """

from models import storage_type
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class / table model"""
    __tablename__ = 'states'
    if storage_type == 'db':
        # Define the 'name' column for the 'states' table in the database
        name = Column(String(128), nullable=False)

        # Define the relationship with the 'City' table in the database
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        # Default value for non-database storage
        name = ''

        @property
        def cities(self):
            ''' Returns the list of City instances associated with the current State.

                This property is used in non-database storage to simulate the
                relationship between State and City using FileStorage.
            '''
            from models import storage

            # Retrieve all City instances
            cities = storage.all(City)
            related_cities = []

            # Filter cities with matching state_id
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)

            return related_cities
