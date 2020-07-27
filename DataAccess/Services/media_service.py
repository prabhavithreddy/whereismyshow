from typing import List

from Models.save_result import SaveResult
from ORM.provider import Provider
from ORM.reference import Reference
from ORM.title import Title
from ORM.title_provider import TitleProvider
from ORM.title_references import TitleReferences
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

    def add_media(self, media_json) -> SaveResult:

        titles = list()
        references = list()

        if not media_json:
            return SaveResult(False, "There is no data available")
        show_titles = None
        try:
            if isinstance(media_json, str):
                show_titles = json.loads(media_json)
            else:
                show_titles = media_json

            if not show_titles:
                return SaveResult(False, "There is no data.")

            for show in show_titles:
                title = Title()
                if not show["Id"] or not show["Title"] or not show["Provider"]:
                    self.logger.info("Show doesn't contain the required information.\n{}".format(json.dumps(show)))
                    continue
                title.title_id = show["Id"]
                title.name = show["Title"]
                title.picture = show["ImageUrl"]

                save_result = self.title_repository.Add(title)
                if not save_result.is_saved:
                    self.logger.info("Unable to save the show.\n{}".format(json.dumps(show)))
                    continue
                else:
                    titles.append(title)

                provider_name = show["Provider"]["Name"]
                provider = None
                if provider_name not in [provider.name for provider in self.Providers]:
                    provider = Provider(provider_name, show["Provider"]["Icon"])
                    save_result = self.provider_repository.Add(provider)
                    if not save_result.is_saved:
                        continue

                title_provider = TitleProvider(title.id, provider.id, show["Provider"]["Url"])
                save_result = self.title_provider_repository.Add(title_provider)
                if not save_result.is_saved:
                    continue
                title_reference = None
                if not show["ExternalLinks"] or len(show["ExternalLinks"]) == 0:
                    self.logger.info("Show doesn't contain any ExternalLinks.")
                else:
                    for externalLink in show["ExternalLinks"]:
                        if externalLink["Name"] not in [reference.name for reference in self.References]:
                            url = externalLink["Url"]
                            reference = Reference(externalLink["Name"], url[:url.rfind('/')])
                            save_result = self.reference_repository.Add(reference)
                            if not save_result.is_saved:
                                self.logger.info("Unable to save the references:\n {}".format(json.dumps(reference)))
                                continue
                            else:
                                title_reference = TitleReferences(title.id, reference.id, externalLink["Id"])
                                self.title_references_repository.Add(title_reference)
                                self.References.append(reference)

            if len(titles) == 0:
                return SaveResult(False, "Unable to add any titles.")
            else:
                return SaveResult(True, "Titles added successfully.")
        except Exception as ex:
            self.logger.error("Exception while parsing media json", ex)
            return SaveResult(False, "Exception while adding media.", ex)


if __name__ == "__main__":
    media_service = MediaService()
    print(media_service.add_media(open("shows.json","r").read()))