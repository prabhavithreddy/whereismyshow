import json
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from Models.base import Base
from ORM.reference import Reference
from ORM.title import Title

class TitleReferences(Base):
    __tablename__ = 'title_references'
    __table_args__ = {'schema': 'dbo'}

    id = Column('id', Integer, primary_key=True)
    title_id = Column('title_id', Integer, ForeignKey(Title.id))
    reference_id = Column('reference_id', Integer, ForeignKey(Reference.id))
    meta_data = Column('meta_data', String)
    inserted_date = Column('inserted_date', String, default=datetime.utcnow())

    def __init__(self, title_id: int, reference_id:int, meta_data: str):
        self.title_id = title_id
        self.reference_id = reference_id
        self.meta_data = meta_data

    def __repr__(self):
        return json.dumps(self.__dict__)
