#!/usr/bin/env python3
"""Class user that inherits BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
