#!/usr/bin/env python3
"""City inherits from BaseModel"""
from models import *


class City(BaseModel):
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
