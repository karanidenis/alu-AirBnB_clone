"""
Tests the base model attributes
"""


from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    Checks every aspect of creation of a base model
    """

    def setUp(self) -> None:
        self.b1 = BaseModel()
        self.b3 = BaseModel()
        self.b1_to_dict  = self.b1.to_dict()
        self.b2 = BaseModel(**self.b1_to_dict)

    def test_to_dict_method(self):
        """
        checks if the to_dict method converts the basemodel to dictionary
        """
        self.assertEqual(type(self.b1_to_dict), dict)
    
    def test_to_dict(self):
        """testing to dict method"""
        self.assertIsInstance(self.b1_to_dict['updated_at'], str)

    def test_id_when_obj_created(self):
        """
        checks if an id is created when basemodel object is instantiated
        """

        self.assertIsNotNone(self.b1.id)

    def test_obj_is_instance(self):
        """
        checks if the instance b1 and b2 are instances of BaseModel class
        """

        self.assertIsInstance(self.b1, BaseModel);
        self.assertIsInstance(self.b2, BaseModel)

    def test_str_(self):
        """ checks id __str__ prints a readable representation"""
        self.assertEqual(str(self.b1), f"[{self.b1.__class__.__name__}] ({self.b1.id}) {self.b1.__dict__}") 

    def test_created_at_obj_created(self):
        self.assertIsNotNone(self.b1.created_at)

    def test_save(self):
        self.b1.save()
        self.b3.save()
        self.assertNotEqual(self.b1.updated_at, self.b3.updated_at)


if __name__ == '__main__':
    unittest.main()