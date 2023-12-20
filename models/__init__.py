#!/usr/bin/python3
"""This module selects and initializes the appropriate storage type."""

from os import getenv

# Retrieve the storage type from environment variables
storage_type = getenv('HBNB_TYPE_STORAGE')

# Check if the storage type is set to 'db' and instantiate the appropriate storage object
if storage_type == 'db':
    # If using a database, instantiate a DBStorage object
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
