#!/usr/bin/python3
""" """

from models.amenity import Amenity
import os
from tests.test_models.test_base_model import test_basemodel

class test_Amenity(test_basemodel):
    """ amenity test class"""

     def test_name2(self):
        """testing name type """
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

        def __init__(self, *args, **kwargs):
        """inti the test class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
