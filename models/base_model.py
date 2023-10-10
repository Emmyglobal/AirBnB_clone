#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel():

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.udated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
