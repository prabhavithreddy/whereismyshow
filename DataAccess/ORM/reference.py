import json
from sqlalchemy import Column, Integer, String
from Models.base import Base


class Reference(Base):
    __tablename__ = 'reference'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    icon_url = Column('icon_url', String)
    inserted_date = Column('inserted_date', String)

    def __init__(self, name: str, icon_url:str):
        self.name = name
        self.icon_url = icon_url

    def __repr__(self):
        dictionary = dict()
        dictionary['id'] = self.id
        dictionary['name'] = self.name
        dictionary['icon_url'] = self.icon_url
        return json.dumps(dictionary)
