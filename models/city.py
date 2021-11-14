#!/usr/bin/python3
"""This defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city"""

    state_id = ""
    name = ""
