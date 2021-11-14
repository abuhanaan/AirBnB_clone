#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Implementation of the Review Model.
    """

    place_id = ""
    user_id = ""
    text = ""
