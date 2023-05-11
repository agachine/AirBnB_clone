#!/usr/bin/python3
import json
from datetime import datetime


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
                for key, obj in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict[key]['created_at'] = datetime.datetime.strptime(
                        obj_dict[key]['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    obj_dict[key]['updated_at'] = datetime.datetime.strptime(
                        obj_dict[key]['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    obj_class = models[class_name]
                    FileStorage.__objects[key] = obj_class(**obj)
        except FileNotFoundError:
            pass

