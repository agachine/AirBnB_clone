#!/usr/bin/env python3
"""Review class"""
from models.base_model import BaseModel


class Review:
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
