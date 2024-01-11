#!/usr/bin/python3
"""Base class"""
import json
import os.path


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                for key, value in json.load(file).items():
                    self.new(BaseModel(**value))
