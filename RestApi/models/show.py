import json
from typing import Dict, List, Any, Union

from models.provider import Provider
from models.external_link import ExternalLink
from utils.logger import Logger
class Show(object):
    Id:str = None
    ImageUrl:str = None
    Title:str = None
    Provider: Provider = None
    ExternalLinks: list = None
    logger = Logger(__name__)
    def __init__(self):
        self.ExternalLinks = list()

    def getShows(self, json_data: str):
        shows = list()
        if not json_data:
            return shows
        try:
            data = json.loads(json_data)
            if not data["results"]:
                return shows
            for result in data["results"]:
                show = Show()
                show.Id = result["id"]
                show.ImageUrl = result["picture"]
                show.Title = result["name"]
                if not result["locations"]:
                    shows.append(show.dict())
                    return shows

                show.Provider = Provider(result["locations"][0]["id"],
                                         result["locations"][0]["display_name"],
                                         result["locations"][0]["url"],
                                         result["locations"][0]["icon"]).dict()
                if not result["external_ids"]:
                    shows.append(show.dict())
                    return shows

                show.ExternalLinks.append(
                    ExternalLink
                        (
                            result["external_ids"]["imdb"]["id"],
                            "IMDB",
                            result["external_ids"]["imdb"]["url"]
                        ).dict()
                )
                show.ExternalLinks.append(
                    ExternalLink
                        (
                            result["external_ids"]["wiki_data"]["id"],
                            "WIKI",
                            result["external_ids"]["wiki_data"]["url"]
                        ).dict()
                )
                shows.append(show.dict())
            return shows

        except Exception as ex:
            self.logger.error("Exception while parsing Shows: {}".format(ex))
            return shows
    def dict(self):
        return self.__dict__

    def __repr__(self):
        return json.dumps(self.dict())

if __name__ == "__main__":
    from services.mock_service import MockService
    shows = Show().getShows(MockService().getData())
    print(json.dumps(shows))