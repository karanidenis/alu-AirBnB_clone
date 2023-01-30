#!/usr/bin/python3
"""Test case for state class"""
import unittest
import pep8
from models import state
from models.state import state
from models.base_model import BaseModel

class TestStateClass(unittest.TestCase):
    """Test cases for state class"""

    def setUp(self):
        self.state = State()

        def test_is_instance(self):
         """test instance"""
        my_state = State()
        self.assertTrue(isinstance(my_state, BaseModel))

        def test_state_is_a_subclass_of_basemodel(self):
         self.assertTrue(issubclass(type(self.state), BaseModel))

         def test_class_attrs(self):
          self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))


if __name__ == '__main__':
    unittest.main()
