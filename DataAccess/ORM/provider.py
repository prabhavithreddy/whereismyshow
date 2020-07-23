import json
from sqlalchemy import Column, Integer, String, DATETIME
from Models.base import Base


class Provider(Base):
    __tablename__ = 'provider'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    image_url = Column('image_url', String)
    inserted_date = Column('inserted_date', String)

    def __init__(self, name: str, image_url: str):
        self.name = name
        self.image_url = image_url

    def __repr__(self):
        dictionary = dict()
        dictionary['id'] = self.id
        dictionary['name'] = self.name
        dictionary['image_url'] = self.image_url
        dictionary['inserted_date'] = self.inserted_date
        return json.dumps(dictionary)
