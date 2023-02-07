#!usr/bin/python3

"""
the base model for the Airbnb clone project
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    The base class for all classes
    """
    def __init__(self, *args, **kwargs):
        """new instance"""
        if kwargs.__len__() > 0:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.fromisoformat(v)
                    setattr(self, k, v)
                    continue
                if k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """ readable format """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        return a new value of updated_at
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        return new_dict
