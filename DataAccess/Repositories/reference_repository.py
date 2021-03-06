from ORM.reference import Reference
from Base.repository_base import RepositoryBase


class ReferenceRepository(RepositoryBase):

    def __init__(self):
        super().__init__()

    def query(self):
        return super().query(Reference)

    def Map(self, session_entity: Reference, modified_entity: Reference) -> Reference:
        if session_entity is None or modified_entity is None:
            return None
        session_entity.id = modified_entity.id
        session_entity.name = modified_entity.name
        session_entity.url = modified_entity.url
        session_entity.inserted_date = modified_entity.inserted_date
        return session_entity

if __name__ == '__main__':
    reference = Reference("IMDB", "https://www.imdb.com/title")
    ReferenceRepository().Add(reference)