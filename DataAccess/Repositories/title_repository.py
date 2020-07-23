from ORM.title import Title
from Base.repository_base import RepositoryBase


class TitleRepository(RepositoryBase):

    def __init__(self):
        super().__init__()

    def query(self):
        return super().query(Title)

    def Map(self, session_entity: Title, modified_entity: Title) -> Title:
        if session_entity is None or modified_entity is None:
            return None
        session_entity.id = modified_entity.id
        session_entity.title_id = modified_entity.title_id
        session_entity.picture = modified_entity.picture
        session_entity.name = modified_entity.name
        session_entity.inserted_date = modified_entity.inserted_date
        return session_entity

if __name__ == '__main__':
    title = Title("5d91416b302b840050ad2718","https://utellyassets9-1.imgix.net/api/Images/8698c96ae0e0038b81b661c8b2068ca1/Redirect","Lucifer")
    TitleRepository().Add(title)