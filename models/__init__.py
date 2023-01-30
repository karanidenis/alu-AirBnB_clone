#!usr/bin/python3

"""
creating an instance of FileStorage
"""
#from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()