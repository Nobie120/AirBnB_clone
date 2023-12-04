#!/usr/bin/python3
""" The base class """
from datetime import datetime
import uuid

class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_a = datetime.now()
    def __str__:
        """ str representation of the class """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """ updates The update time """
        updated_at = daatetime.now()
    def to_dict(self):
        """ dictionary containing all
        keys/values of __dict__ of the instance """
        obj_dict = self.__dict__.copy
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
