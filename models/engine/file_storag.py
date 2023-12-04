#!/usr/bin/python3
""" The class module for FileStrorage """


class FileStorage:
    """ class for storage handling """

    __objects = {}
    __file_path = 'file.json'

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj
        with key <obj class name>.id """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict

    def save(self):
        """  serializes __objects to
        the JSON file (path: __file_path) """
        with open(self.__file_path, 'w', encoding="UTF-8") as file:
            json.dump(self.__objects, file)

    def reload(self):
        """  deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; 
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised) """
        with open(self.__file_path, 'r') as file:
            self.__objects = json.load(file)
