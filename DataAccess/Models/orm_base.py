import inspect
import json
from Models.base import Base


class ORMBase(Base):
    __tablename__ = None
    def __repr__(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))

        dictionary = dict()
        for a in attributes:
            if not (a[0].startswith('__') and a[0].endswith('__')):
                property, value = a
                dictionary[property]=value

        return json.dumps(dictionary)