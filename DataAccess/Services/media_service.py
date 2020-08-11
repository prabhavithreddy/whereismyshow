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
from urllib.parse import urlparse

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

    def get_providers(self):
        list_of_providers = list()
        for provider in self.provider_repository.query().all():
            list_of_providers.append(provider.dict())
        return list_of_providers

    def add_media(self, media_json) -> SaveResult:

        titles = list()

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
                if not show["Id"] or not show["Title"] or not show["Provider"]:
                    self.logger.info("Show doesn't contain the required information.\n{}".format(json.dumps(show)))
                    continue

                if self.title_repository.query().filter_by(title_id=show["Id"]).scalar():
                    self.logger.info("Title Id: {} already exists in database".format(show["Id"]))
                    continue

                title = Title()
                title.title_id = show["Id"]
                title.name = show["Title"]
                title.picture = show["ImageUrl"]

                provider_name = show["Provider"]["Name"]
                provider = next(filter(lambda r: r.name == provider_name, self.Providers),None)
                if not provider:
                    provider_base_url = None
                    provider_logo_url = None
                    if not provider["url"]:
                        parseResult = urlparse(provider["url"])
                        provider_base_url = "{}://{}".format(parseResult.scheme, parseResult.netloc)
                        provider_logo_url = "images/{}".format(provider_name.replace(' ', ''))
                    provider = Provider(provider_name, show["Provider"]["Icon"], provider_base_url, provider_logo_url)
                    save_result = self.provider_repository.Add(provider)
                    if not save_result.is_saved:
                        continue
                    else:
                        self.Providers.append(provider)

                title_provider = TitleProvider(title.id, provider.id, show["Provider"]["Url"])
                title.title_provider.append(title_provider)

                if not show["ExternalLinks"] or len(show["ExternalLinks"]) == 0:
                    self.logger.info("Show doesn't contain any ExternalLinks.")
                else:
                    for externalLink in show["ExternalLinks"]:
                        reference = next(filter(lambda r: r.name == externalLink["Name"], self.References),None)
                        if not reference:
                            url = externalLink["Url"]
                            reference = Reference(externalLink["Name"], url[:url.rfind('/')])
                            save_result = self.reference_repository.Add(reference)
                            if not save_result.is_saved:
                                self.logger.info("Unable to save the references:\n {}".format(json.dumps(reference)))
                                continue
                            else:
                                self.References.append(reference)

                        title_reference = TitleReferences(title.id, reference.id, externalLink["Id"])
                        title.title_references.append(title_reference)
                        self.References.append(reference)

                titles.append(title)

            if len(titles) > 0:
                save_result = self.title_repository.AddBulk(titles)
                if save_result.is_saved:
                    return SaveResult(True, "Titles added successfully.")
                else:
                    return SaveResult(False, "Unable to add any titles.")
            else:
                return SaveResult(False, "Unable to add any titles.")
        except Exception as ex:
            self.logger.error("Exception while parsing media json", ex)
            return SaveResult(False, "Exception while adding media.", ex)


if __name__ == "__main__":
    media_service = MediaService()
    print(media_service.add_media(open("shows.json","r").read()))