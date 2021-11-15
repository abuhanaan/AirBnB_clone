#!/usr/bin/python3
"""base class module containing the Base model class"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """class defining common attributes and methods for other classes"""
    

    def __init__(self, *args, **kwargs):
        """base instance initialization"""

        if kwargs != None and kwargs != {}:
            for key in kwargs.keys():
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """method returning string representation of an instance"""


        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """method updating updated_at attribute with the current date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return object's dictionary representation"""
        
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
