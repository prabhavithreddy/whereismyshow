from ORM.title_references import TitleReferences
from Base.repository_base import RepositoryBase


class TitleProviderRepository(RepositoryBase):

    def __init__(self):
        super().__init__()

    def query(self):
        return super().query(TitleReferences)

    def Map(self, session_entity: TitleReferences, modified_entity: TitleReferences) -> TitleReferences:
        if session_entity is None or modified_entity is None:
            return None
        session_entity.id = modified_entity.id
        session_entity.title_id = modified_entity.title_id
        session_entity.reference_id = modified_entity.reference_id
        session_entity.meta_data = modified_entity.url
        session_entity.inserted_date = modified_entity.inserted_date
        return session_entity