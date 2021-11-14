#!/usr/bin/python3
"""This defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Inherits from the BaseModel Class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
