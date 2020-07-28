import json
from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from Models.base import Base


class Reference(Base):
    __tablename__ = 'reference'
    __table_args__ = {'schema': 'dbo'}

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    url = Column('url', String)
    inserted_date = Column('inserted_date', String, default=datetime.utcnow())

    def __init__(self, name: str, url:str):
        self.name = name
        self.url = url

    def __repr__(self):
        dictionary = dict()
        dictionary['id'] = self.id
        dictionary['name'] = self.name
        dictionary['url'] = self.url
        dictionary['inserted_date'] = self.inserted_date
        return json.dumps(dictionary)
