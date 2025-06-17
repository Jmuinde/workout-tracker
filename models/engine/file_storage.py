#!/usr/bin/python3
"""
File storage module.
"""
import json
from models.base_model import BaseModel
class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    
    """Class attributes"""
    # Path to the json file storage
    __file_path = "file.json"

    # Stores all objects based on class name and id
    __objects = {}

    # Methods
    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        class_name = type(obj).__name__
        obj_id = obj.id
        key = f"{class_name}.{obj_id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to a json file.
        """
        new_obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(new_obj_dict, f)

    def reload(self):
        """Deserializing the jsnon file back to objects"""
        try:
            with open(FileStorage.__file_path, 'r', encoding="UTF-8") as f:
                object_load = json.load(f)
                new_obj_dict = {}
                for key, dict_obj in object_load.items():
                    class_name = key.split(".")[0]
                    obj = eval(class_name)(**dict_obj)
                    new_obj_dict[key] = obj
                FileStorage.__objects = new_obj_dict
        except FileNotFoundError:
            pass
