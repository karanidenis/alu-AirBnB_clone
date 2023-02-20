#!/usr/bin/python3
"""Test case for User class"""
import unittest
# import pep8
# from models import user
from models.user import User
from models.base_model import BaseModel

class TestUserClass(unittest.TestCase):
    """Test cases for user class"""

    def setUp(self):
        """Class attributes"""
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""

    def test_class_doc(self):
        """Documentation"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_instance(self):
        """test instance."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_field_types(self):
        """Attributes"""
        my_user = User()
        self.assertTrue(type(my_user.email) == str)
        self.assertTrue(type(my_user.password) == str)
        self.assertTrue(type(my_user.first_name) == str)
        self.assertTrue(type(my_user.last_name) == str)

    def test_first_name(self):
        """test type"""
        my_user = User()
        self.assertEqual(type(my_user.first_name), str)

    def test_email(self):
        """TEST EMAIL TYPE"""
        my_user = User()
        self.assertEqual(type(my_user.email), str)

    def test_password(self):
        """test password type"""
        my_user = User()
        self.assertEqual(type(my_user.password), str)

    def test_last_name(self):
        """test last_name type"""
        my_user = User()
        self.assertEqual(type(my_user.last_name), str)


if __name__ == '__main__':
    unittest.main()
