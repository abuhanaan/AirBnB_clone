#!/usr/bin/python3
"""module containing FilrStorage class"""

import json
import os
class FileStorage():
    """class that serializes instances to json files and deserialises json files to objects"""


    __file_path ="file.json"
    __objects = {}

    def all(self):
        """method returning dictionary __object"""

        return FileStorage.__objects

    def new(self, obj):
        """method tha sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__object[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="utf_8") as fl:
            my_dictionary = {k:v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(my_dictionary, fl)

    def reload(self):
        """deserializes json files to objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf_8") as j_file:
                object_dict = json.load(f_file)

                for key in object_dict.keys():
                    my_class = object_dict[key]["__class__"]
                    FileStorage.__objects[key] = eval(my_class)(**object_dict[key])      

