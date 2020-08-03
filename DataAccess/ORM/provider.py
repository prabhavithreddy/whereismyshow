import json
from datetime import datetime

from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import relationship

from Models.base import Base


class Provider(Base):
    __tablename__ = 'provider'
    __table_args__ = {'schema': 'dbo'}

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    icon_url = Column('icon_url', String)
    url = Column('url', String)
    logo = Column('logo', String)
    inserted_date = Column('inserted_date', String, default=datetime.utcnow())

    def __init__(self, name: str, icon_url: str, url:str = None, logo:str = None):
        self.name = name
        self.icon_url = icon_url
        self.url = url
        self.logo = logo

    def __repr__(self):
        return json.dumps(self.__dict__)
