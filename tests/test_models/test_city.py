#!/usr/bin/python3
"""Test City"""
import unittest
# import pep8
# from models import city
from models.city import City
from models.base_model import BaseModel


class City_testing(unittest.TestCase):
     """Test city class"""
    
     def setUp(self):
        """Return to "" class attributes"""
        City.name = ""
        City.state_id = ""

    
     def test_instance(self):
        """test instance."""
        city = City()
        self.assertIsInstance(city, City)
        # self.assertIsInstance(city, BaseModel)

     def test_is_class(self):
         """test instance."""
         city = City()
         self.assertEqual(str(type(city)),
                        "<class 'models.city.City'>")

     def test_field_types(self):
         """ Test field attributes of user """
         my_city = City()
         self.assertTrue(type(my_city.name) == str)
         self.assertTrue(type(my_city.state_id) == str)


if __name__ == '__main__':
   unittest.main()
