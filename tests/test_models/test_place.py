#!/usr/bin/python3
"""Test Place"""
import unittest
# import pep8
# from models import place
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """Test Place class"""

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_place = Place()
        self.assertTrue(isinstance(my_place, BaseModel))

    # def test_pep8(self):
    #     """test for pep8"""
    #     style = pep8.StyleGuide(quiet=True)
    #     file1 = 'models/place.py'
    #     file2 = 'tests/test_models/test_place.py'
    #     result = style.check_files([file1, file2])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warning).")
        
    # def test_attrs_are_class_attrs(self):
    #     for attr in self.attr_list:
    #         self.assertTrue(hasattr(Place, attr))

    def test_class_attrs(self):
        self.assertIs(type(self.my_place.name), str)
        self.assertIs(type(self.my_place.city_id), str)
        self.assertIs(type(self.my_place.user_id), str)
        self.assertIs(type(self.my_place.description), str)
        self.assertIs(type(self.my_place.number_bathrooms), int)
        self.assertIs(type(self.my_place.max_guest), int)
        self.assertIs(type(self.my_place.number_rooms), int)
        self.assertIs(type(self.my_place.price_by_night), int)
        self.assertIs(type(self.my_place.latitude), float)
        self.assertIs(type(self.my_place.longitude), float)
        self.assertIs(type(self.my_place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
