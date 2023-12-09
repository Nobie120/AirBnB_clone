#!/usr/bin/python3
""" The class module for FileStrorage """
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review



class FileStorage:
    """ class for storage handling """

    __objects = {}
    __file_path = 'file.json'

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """  serializes __objects to
        the JSON file (path: __file_path) """
        objects_dict = {}
        for key, value in FileStorage.__objects.items():
            objects_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """  deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised) """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name = value['__class__']
                class_obj = globals()[class_name]
                instance = class_obj(**value)
                self.new(instance)

        except FileNotFoundError:
            pass
