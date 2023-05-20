#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from uuid import uuid4
from datetime import datetime
from models import *


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel"""
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns string representation of BaseModel"""
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Saves the BaseModel instance"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of BaseModel"""
        my_dict = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    def to_json(self):
        """convert to json"""
        d = self.__dict__.copy()
        d["created_at"] = str(d["created_at"])
        if ("updated_at" in d):
            d["updated_at"] = str(d["updated_at"])
        d["__class__"] = type(self).__name__
        return d
