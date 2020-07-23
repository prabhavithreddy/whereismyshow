import json
from datetime import datetime

from sqlalchemy import Column, Integer, String
from Models.base import Base


class TitleReferences(Base):
    __tablename__ = 'title_references'
    __table_args__ = {'schema': 'dbo'}

    id = Column('id', Integer, primary_key=True)
    title_id = Column('title_id', Integer)
    reference_id = Column('provider_id', Integer)
    meta_data = Column('url', String)
    inserted_date = Column('inserted_date', String, default=datetime.utcnow())

    def __init__(self, title_id: int, reference_id:int, meta_data: str):
        self.title_id = title_id
        self.reference_id = reference_id
        self.meta_data = meta_data

    def __repr__(self):
        dictionary = dict()
        dictionary['id'] = self.id
        dictionary['title_id'] = self.title_id
        dictionary['reference_id'] = self.reference_id
        dictionary['meta_data'] = self.meta_data
        dictionary['inserted_date'] = self.inserted_date
        return json.dumps(dictionary)
