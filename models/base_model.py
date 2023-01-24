#!usr/bin/python3

"""
the base model for the Airbnb clone project
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    The base class for all classes
    """
    def __init__(self):
        """
        initialising 
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ readable format """
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"

    def save(self):
        """
        return a new value of updated_at
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """return dictionary"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['self.created_at'] = self.created_at.isoformat()
        new_dict['self.created_at'] = self.updated_at.isoformat()
        return new_dict