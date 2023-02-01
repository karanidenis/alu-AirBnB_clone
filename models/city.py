#!/usr/bin/python3
"""
city module
"""

from .base_model import BaseModel


class City(BaseModel):
    """ defines city class
    inherit from Basemodel"""

    state_id = ""  # state id
    name = ""
