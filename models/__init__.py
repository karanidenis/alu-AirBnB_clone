#!usr/bin/python3

"""
creating an instance of FileStorage
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()