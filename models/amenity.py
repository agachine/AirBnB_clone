#!/usr/bin/env python3
"""Amenity class inherits BaseModel"""
from models import *


class Amenity(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
