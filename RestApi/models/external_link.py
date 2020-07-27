import json

class ExternalLink(object):
    Id:str = None
    Name:str = None
    Url:str = None

    def __init__(self, id:str, name:str, url:str):
        self.Id = id
        self.Url = url
        self.Name = name

    def dict(self):
        dictionary = dict()
        dictionary["Id"] = self.Id
        dictionary["Url"] = self.Url
        dictionary["Name"] = self.Name
        return dictionary
    def __repr__(self):
        return json.dumps(self.dict())

if __name__ == "__main__":
    externalLink = ExternalLink("tt4052886","IMDB","https://www.imdb.com/title/tt4052886")
    print(externalLink)
