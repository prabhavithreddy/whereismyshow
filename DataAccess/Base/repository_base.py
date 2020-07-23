from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from abc import ABC, abstractmethod
import asyncio
from Config.connection_string import ConnectionStrings
from Models.save_result import SaveResult
from Models.base import Base
from utils.logger import Logger


class RepositoryBase(ABC):

    connection_strings = None
    engine = None
    Session = None
    logger = Logger(__name__)
    def __init__(self):
        """Initializes engine and session for CRUD operations"""
        self.connection_strings = ConnectionStrings()
        self.engine = create_engine(self.connection_strings.get_sql_alchemy_con_string(), pool_pre_ping=True)
        self.Session = sessionmaker(bind=self.engine)

    def query(self, orm):
        if orm is None:
            raise ValueError("ORM type cannot be None")

        return self.Session().query(orm)

    def Add(self, entity: Base) -> SaveResult:
        result = SaveResult()
        if entity is None:
            raise ValueError("entity cannot be Null")
        if not isinstance(entity, Base):
            raise TypeError("entity {0} is not an ORM".format(type(entity)))
        try:
            return self.AddBulk([entity])
        except Exception as e:
            result.is_saved = False
            result.message = str(e)
            result.error = e
            self.logger.error("Exception occurred while adding a entity.", e)
        return result

    def AddAsync(self, entity: list):
        return asyncio.create_task(self.Add(entity))

    def AddBulk(self, entities: list) -> SaveResult:
        result = SaveResult()
        if entities is None:
            raise ValueError("entities cannot be Null")
        if not isinstance(entities, list):
            raise TypeError("entities should be type of list")
        try:
            session = self.Session()
            for entity in entities:
                if not isinstance(entity, Base):
                    continue
                session.add(entity)
            session.commit()
            result.is_saved = True
        except Exception as e:
            result.is_saved = False
            result.message = str(e)
            result.error = e
            self.logger.error("Exception occurred while adding a entity.", e)
        return result

    async def AddBulkAsync(self, entities):
        return asyncio.create_task(self.AddBulk(entities))

    def Update(self, entity: Base) -> SaveResult:
        result = SaveResult()
        if entity is None:
            raise ValueError("entity cannot be Null")
        if not isinstance(entity, Base):
            raise TypeError("entity {0} is not an ORM".format(type(entity)))
        try:
            return self.UpdateBulk([entity])
        except Exception as e:
            result.is_saved = False
            result.message = str(e)
            result.error = e
            self.logger.error("Exception occurred while adding a entity.", e)
        return result

    async def UpdateAsync(self, entity):
        return asyncio.create_task(self.Update(entity))

    def UpdateBulk(self, entities: list) -> SaveResult:
        result = SaveResult()
        if entities is None:
            raise ValueError("entities cannot be Null")
        if not isinstance(entities, list):
            raise TypeError("entities should be type of list")
        try:
            session = self.Session()
            for entity in entities:
                if not isinstance(entity, Base):
                    continue
                modified_entity = self.Map(session.query(entity.__class__).get(entity.id), entity)
            session.commit()
            result.is_saved = True
        except Exception as e:
            result.is_saved = False
            result.message = str(e)
            result.error = e
            self.logger.error("Exception occurred while Updating entities.", e)
        return result

    async def AddBulkAsync(self, entities):
        return asyncio.create_task(self.UpdateBulk(entities))

    @abstractmethod
    def Map(self, session_entity: Base, modified_entity: Base):
        pass

    def Delete(self, entity: Base) -> SaveResult:
        result = SaveResult()
        if entity is None:
            raise ValueError("entity cannot be Null")
        if not isinstance(entity, Base):
            raise TypeError("entity {0} is not an ORM".format(type(entity)))
        try:
            return self.DeleteBulk([entity])
        except Exception as e:
            result.is_saved = False
            result.message = str(e)
            result.error = e
            self.logger.error("Exception occurred while deleting an entity.", e)
        return result

    async def DeleteAsync(self, entity):
        return asyncio.create_task(self.Delete(entity))

    def DeleteBulk(self, entities: list) -> SaveResult:
        result = SaveResult()
        if entities is None:
            raise ValueError("entities cannot be Null")
        if not isinstance(entities, list):
            raise TypeError("entities should be type of list")
        try:
            session = self.Session()
            for entity in entities:
                if not isinstance(entity, Base):
                    continue
                deleted_entity = session.query(entity.__class__).get(entity.id)
                session.delete(deleted_entity)
            session.commit()
            result.is_saved = True
        except Exception as e:
            result.is_saved = False
            result.message = str(e)
            result.error = e
            self.logger.error("Exception occurred while deleting entities.", e)
        return result

    async def DeleteBulkAsync(self, entities):
        return asyncio.create_task(self.DeleteBulk(entities))
