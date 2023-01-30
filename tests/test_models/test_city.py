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

   #   def test_pep8(self):
   #       """ test base and test_base for pep8 conformance """
   #       style = pep8.StyleGuide(quiet=True)
   #       file1 = 'models/city.py'
   #       file2 = 'tests/test_models/test_city.py'
   #       result = style.check_files([file1, file2])
   #       self.assertEqual(result.total_errors, 0,
   #                       "Found code style errors (and warning).")

     def test_is_class(self):
         """test instance."""
         city = City()
         self.assertEqual(str(type(city)),
                        "<class 'models.city.City'>")

     def test_amenity_is_a_subclass_of_basemodel(self):
         self.assertTrue(issubclass(type(self.amenity), BaseModel))

     def test_field_types(self):
         """ Test field attributes of user """
         my_city = City()
         self.assertTrue(type(my_city.name) == str)
         self.assertTrue(type(my_city.state_id) == str)


if __name__ == '__main__':
   unittest.main()
