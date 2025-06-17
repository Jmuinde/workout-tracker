#!/usr/bin/env python3
"""
Base model module
"""
import uuid
from  datetime import datetime
import models
class BaseModel:
    """
    Defines all the common attributes/methods of other classes
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                # ingnore __class__ attribute
                if k == "__class__":
                    continue
                # convert created_at, and updated_at to string objects
                if k in ("created_at", "updated_at") and isinstance(v, str):
                    setattr(self, k, datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """
        Method to print string representaion of the 
        class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        Updates the updated_at public attribute with 
        current datetime
        """
        self.updated_at=datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        return {
            **self.__dict__,
            "created_at":self.created_at.isoformat(),
            "updated_at":self.updated_at.isoformat(),
            "__class__":self.__class__.__name__}
