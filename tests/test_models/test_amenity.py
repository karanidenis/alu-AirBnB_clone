#!/usr/bin/python3
"""test Amenity"""
import unittest
# import pep8
# import models
# import amenity
from models.amenity import Amenity
from models import storage


class Amenity_testing(unittest.TestCase):
    """Test Amenity class"""

    def setUp(self):
        """Return to "" class attributes"""
        with open("test.json", 'w'):
            storage._FileStorage__file_path = "test.json"
            storage._FileStorage__objects = {}
        Amenity.name = ""
   
    # def testpep8(self):
    #     """testing codestyle"""
    #     pepstylecode = pep8.StyleGuide(quiet=True)
    #     path_user = 'models/amenity.py'
    #     result = pepstylecode.check_files([path_user])
        
    def test_instance(self):
        """test instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_field_types(self):
        """ Test field attributes of user """
        my_Amenity = Amenity()
        self.assertTrue(type(my_Amenity.name) == str)

if __name__ == '__main__':
    unittest.main()
