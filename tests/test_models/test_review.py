#!/usr/bin/python3
"""Test case for review class"""
import unittest
# import pep8
from models.review import Review
from models.base_model import BaseModel

class TestReviewClass(unittest.TestCase):
    """Test case for review class"""

    def setUp(self):
        """Class attribute"""
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""

    # def test_pep8(self):
    #     """ test base and test_base for pep8 conformance """
    #     style = pep8.StyleGuide(quiet=True)
    #     file1 = 'models/review.py'
    #     file2 = 'tests/test_models/test_review.py'
    #     result = style.check_files([file1, file2])
    #     self.assertEqual(result.total_errors, 0,
    #                     "Found code style errors (and warning).")   

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_Review = Review()
        self.assertTrue(isinstance(my_Review, BaseModel))

    def test_field_types(self):
        """Test field"""
        my_Review = Review()
        self.assertTrue(type(my_Review.place_id) == str)
        self.assertTrue(type(my_Review.user_id) == str)
        self.assertTrue(type(my_Review.text) == str)


if __name__ == '__main__':
    unittest.main()
