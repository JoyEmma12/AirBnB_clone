#!/usr/bin/python3
import models
from datetime import datetime
from uuid import uuid4

class BaseModel:

    def __init__(self, *args, **kwargs):
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)


    def __str__(self):
        return "[{}] ({}) {}".\
            format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        mydict = self.__dict__.copy()
        mydict["__class__"] = type(self).__name__
        mydict["created_at"] = mydict["created_at"].isoformat()
        mydict["updated_at"] = mydict["updated_at"].isoformat()
        return mydict
