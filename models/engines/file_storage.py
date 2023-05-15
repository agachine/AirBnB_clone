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
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
    """Deserializes the JSON file to __objects."""
    try:
        with open(FileStorage.__file_path, 'r') as file:
            obj_dict = json.load(file)
            from models.base_model import BaseModel
            obj_class = {"BaseModel": BaseModel}
            for key, obj in obj_dict.items():
                class_name, obj_id = key.split('.')
                class_name = obj.get('__class__', 'BaseModel')
                obj_dict[key] = obj_class[class_name](**obj)
            FileStorage.__objects = obj_dict
    except FileNotFoundError:
        pass

