#!/usr/bin/env python3
"""Amenity class inherits BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
