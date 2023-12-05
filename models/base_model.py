#!/usr/bin/python3
""" The base class """
from datetime import datetime
import uuid
import models


class BaseModel:
    """ defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Instantiation of attributes """
        if kwargs and kwargs != {}:
            kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ str representation of the class """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates The update time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ dictionary containing all
        keys/values of __dict__ of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
