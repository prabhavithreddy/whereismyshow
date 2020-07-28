import json
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from Models.base import Base
from ORM.provider import Provider
from ORM.title import Title


class TitleProvider(Base):
    __tablename__ = 'title_provider'
    __table_args__ = {'schema': 'dbo'}

    id = Column('id', Integer, primary_key=True)
    title_id = Column('title_id', Integer, ForeignKey(Title.id))
    provider_id = Column('provider_id', Integer, ForeignKey(Provider.id))
    url = Column('url', String)
    inserted_date = Column('inserted_date', String, default=datetime.utcnow())

    def __init__(self, title_id:int, provider_id:int, url:str):
        self.title_id = title_id
        self.provider_id = provider_id
        self.url = url

    def __repr__(self):
        dictionary = dict()
        dictionary['id'] = self.id
        dictionary['title_id'] = self.title_id
        dictionary['provider_id'] = self.provider_id
        dictionary['url'] = self.url
        dictionary['inserted_date'] = self.inserted_date
        return json.dumps(dictionary)
