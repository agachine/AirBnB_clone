#!/usr/bin/env python3
"""State inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    name = ""

    def __init__(self, *args, **kwargs):
        super(State, self).__init__(*args, **kwargs)
