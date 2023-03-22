#!/usr/bin/python3
import json
import os
import datetime

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in objects with key"""
        key = "{}.{}".format(obj.__class__.name___, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to the json file path"""
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))
 
    def classes(self):
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        classes = {
           "Basemodel": BaseModel,
           "City": City,
           "Place": Place,
           "State": State,
           "Amenity": Amenity,
           "Review": Review
        }
        return classes

    def reload(self):
        """deserialize the json file to objects"""
        if not path.isfile(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            serialized_objects = json.load(f)

        deserialized_objects = {}

        for obj_id, serialized_obj in serialized_objects.items():
            class_name = serialized_obj['__class__']
            if class_name in self.classes():
                obj_class = self.classes()[class_name]
            else:
                continue

            deserialized_obj = obj_class(**serialized_obj)
            deserialized_objects[obj_id] = deserialized_obj

        FileStorage.__objects = deserialized_objects

    def attributes(self):
        """returns valid attributes and their type"""
        attributes = {
            "BaseModel":
            {
                "id": str,
                "created_at": datetime.datetime,
                "updated_at": datetime.datetime
            },
            "User":
            {
                "email": str,
                "password": str,
                "first_name": str,
                "last_name": str
            },
            "State":
            {
                "name": str
            },
            "City":
            {
                "state_id": str,
                "name": str
            },
            "Amenity":
            {
                "name": str
            },
            "Place":
            {
                "city_id": str,
                "user_id": str,
                "name": str,
                "description": str,
                "number_rooms": int,
                "number_bathroom": int,
                "max_guest": int,
                "price_by_night": int,
                "latittude": float,
                "longitude": float,
                "amenity_ids": str
            },
            "Review":
            {
                "place_id": str,
                "user_id": str,
                "text": str
            }
        }
        return attributes
