import json
from sqlalchemy import Column, Integer, String
from Models.base import Base
from datetime import datetime

class Title(Base):
    __tablename__ = 'title'
    __table_args__ = {'schema': 'dbo'}
    schema = "dbo"
    id = Column('id', Integer, primary_key=True)
    title_id = Column('title_id', String)
    picture = Column('picture', String)
    name = Column('name', String)
    inserted_date = Column('inserted_date', String, default=datetime.utcnow())

    def __init__(self, title_id:str, picture:str, name:str):
        self.title_id = title_id
        self.picture = picture
        self.name = name

    def __repr__(self):
        dictionary = dict()
        dictionary['id'] = self.id
        dictionary['title_id'] = self.title_id
        dictionary['picture'] = self.picture
        dictionary['name'] = self.name
        dictionary['inserted_date'] = self.inserted_date
        return json.dumps(dictionary)
