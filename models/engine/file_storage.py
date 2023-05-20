#!/usr/bin/python3
import json
import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects = {}
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                from models.place import Place
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.review import Review
                from models.user import User

            
            # Add the new classes to obj_class dictionary
                obj_class = {
                    "BaseModel": BaseModel,
                    "Place": Place,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Review": Review
                 }
                obj_dict = {k: obj_class[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
                FileStorage.__objects = obj_dict

        except FileNotFoundError:
            pass
