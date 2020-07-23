from ORM.provider import Provider
from Base.repository_base import RepositoryBase


class ProviderRepository(RepositoryBase):

    def __init__(self):
        super().__init__()

    def query(self):
        return super().query(Provider)

    def Map(self, session_entity: Provider, modified_entity: Provider) -> Provider:
        if session_entity is None or modified_entity is None:
            return None
        session_entity.id = modified_entity.id
        session_entity.name = modified_entity.name
        session_entity.image_url = modified_entity.image_url
        session_entity.inserted_date = modified_entity.inserted_date
        return session_entity
