import json

class BaseClass(object):
    def __repr__(self):
        return json.dumps(self.__dict__)

