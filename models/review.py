#!/usr/bin/python3
"""
reviews module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """defines review class
    inherits from basemodel"""

    place_id = ""  # will be place.id
    user_id = ""  # will be user.id
    text = ""
