from Models.save_result import SaveResult
from Repositories.provider_repository import ProviderRepository
from Repositories.reference_repository import ReferenceRepository
from Repositories.title_repository import TitleRepository
from Repositories.title_provider_repository import TitleProviderRepository
from Repositories.title_references_repository import TitleReferencesRepository

import json

from utils.logger import Logger


class MediaService(object):
    provider_repository = ProviderRepository()
    reference_repository = ReferenceRepository()
    title_repository = TitleRepository()
    title_provider_repository = TitleProviderRepository()
    title_references_repository = TitleReferencesRepository()
    Providers:list = None
    References:list = None
    logger = Logger(__name__)
    def __init__(self):
        self.Providers = self.provider_repository.query().all()
        self.References = self.reference_repository.query().all()

    def refresh_providers(self):
        self.Providers = self.provider_repository.query().all()

    def refresh_references(self):
        self.References = self.reference_repository.query().all()

    def add_media(self, media_json:str) -> SaveResult:
        if not media_json:
            return SaveResult(False, "There is no data available")
        data = None
        try:
            data = json.loads(media_json)
        except Exception as ex:
            self.logger.error("Exception while parsing media json", ex)
            return SaveResult(False, "media json is not a valid json file.")
        

if __name__ == "__main__":
    print(MediaService())