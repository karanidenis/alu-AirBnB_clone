#!/usr/bin/python3
"""Test Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """Test Place class"""

    def setUp(self):
        self.testplace = Place()

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        self.assertTrue(isinstance(self.testplace, BaseModel))

    def test_class_attrs(self):
        self.assertIs(type(self.testplace.name), str)
        self.assertIs(type(self.testplace.city_id), str)
        self.assertIs(type(self.testplace.user_id), str)
        self.assertIs(type(self.testplace.description), str)
        self.assertIs(type(self.testplace.number_bathrooms), int)
        self.assertIs(type(self.testplace.max_guest), int)
        self.assertIs(type(self.testplace.number_rooms), int)
        self.assertIs(type(self.testplace.price_by_night), int)
        self.assertIs(type(self.testplace.latitude), float)
        self.assertIs(type(self.testplace.longitude), float)
        self.assertIs(type(self.testplace.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
