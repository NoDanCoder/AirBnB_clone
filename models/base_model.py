#!/usr/bin/python3

""" Import Modules to get Time and ID generators """
from datetime import datetime
from models import storage
from uuid import uuid4 as uuid


class BaseModel:
    """ BaseModel Creator Structure. """

    def __init__(self, *args, **kwargs):
        """ BaseModel instance initialization and, add the obj to a buff. """
        if kwargs:
            self.set_by_kwargs(**kwargs)
        else:
            self.id = str(uuid())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    # Set properties by kwargs
    @staticmethod
    def isoparse(isoformat):
        """ parse a date from iso format to datetime object """
        return datetime.strptime(isoformat, "%Y-%m-%dT%H:%M:%S.%f")

    def set_by_kwargs(self, **kwargs):
        """ set properties by kwargs to a BaseModel instance """
        for k, v in kwargs.items():
            if k == 'created_at' or k == 'updated_at':
                setattr(self, k, self.isoparse(v))
            elif k != '__class__':
                setattr(self, k, v)

    # Modify Instances

    def save(self):
        """ Save changes of a BaseModel instances and update JSON file. """
        self.updated_at = datetime.now()
        storage.save()

    # Get info of instance

    def to_dict(self):
        """ Return all info of a BaseModel instance. """
        n_dict = self.__dict__.copy()
        n_dict['__class__'] = self.getType,
        n_dict['updated_at'] = self.updated_at.isoformat()
        n_dict['created_at'] = self.created_at.isoformat()
        return n_dict

    # Print info of instances

    @property
    def getType(self):
        """ retrieves self type """
        return self.__class__.__name__

    def f(self, string):
        """ sumulate f-strings available from python 3.6 """
        return string.format(**locals())

    def __str__(self):
        """ Prints info of a BaseModel instance. """
        return self.f('[{self.getType}] ({self.id}) {self.__dict__}')
