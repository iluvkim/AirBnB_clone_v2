#!/usr/bin/python3
""" """

import os
from models.city import City
from tests.test_models.test_base_model import test_basemodel

class test_City(test_basemodel):
    """ tests for city """

    def test_name(self):
        """ testing name type"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
        def test_state_id(self):
        """ testing state_id type """
        new = self.value()
        self.assertEqual(type(new.state_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))

        def __init__(self, *args, **kwargs):
        """ init the test class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City
