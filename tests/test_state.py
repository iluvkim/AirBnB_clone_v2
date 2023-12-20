#!/usr/bin/python3
""" """

from models.state import State
import os
from tests.test_models.test_base_model import test_basemodel

class test_state(test_basemodel):
    """ states test class"""

     def test_name3(self):
        """ testing state name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                         type(None))
        def __init__(self, *args, **kwargs):
        """ state test class init"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

