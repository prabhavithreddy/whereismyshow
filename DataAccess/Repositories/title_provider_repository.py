from ORM.title_provider import TitleProvider
from Base.repository_base import RepositoryBase


class TitleProviderRepository(RepositoryBase):

    def __init__(self):
        super().__init__()

    def query(self):
        return super().query(TitleProvider)

    def Map(self, session_entity: TitleProvider, modified_entity: TitleProvider) -> TitleProvider:
        if session_entity is None or modified_entity is None:
            return None
        session_entity.id = modified_entity.id
        session_entity.title_id = modified_entity.title_id
        session_entity.provider_id = modified_entity.provider_id
        session_entity.url = modified_entity.url
        session_entity.inserted_date = modified_entity.inserted_date
        return session_entity