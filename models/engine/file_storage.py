#!usr/bin/python3
"""
storage by serialization and deserialization model
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class that serializes instances to Json file 
    and deserializes Json file to instances"""

    __file__path = 'file.json'
    _objects = {}

    def all(self):
        """returns dict _objects"""
        return self._objects

    def new(self, obj):
        """
        sets in  __objects the obj with key(<obj class name>.id)
        """
        self._objects['{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects to Json file"""
        with open(FileStorage.__file__path, mode='w') as file:
            another_dict = {}
            for k, val in self._objects.items():
                another_dict[k] = val.to_dict()
            json.dump(another_dict, file)

    def reload(self):
        """deserializes the Json file to _objects"""
        try:
            with open(FileStorage.__file__path, mode='r') as file:
                new_dict = json.load(file)
                for k, v in new_dict.items():
                    self._objects[k] = eval(v['__class__'])(**v)
        except FileNotFoundError:
            pass 
