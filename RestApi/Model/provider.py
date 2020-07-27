import json

class Provider(object):
    Id:str = None
    Url:str = None
    Name:str = None
    Icon:str = None

    def __init__(self, id:str, name:str, url:str, icon:str):
        self.Id = id
        self.Url = url
        self.Name = name
        self.Icon = icon

    def dict(self):
        dictionary = dict()
        dictionary["Id"] = self.Id
        dictionary["Url"] = self.Url
        dictionary["Name"] = self.Name
        dictionary["Icon"] = self.Icon
        return dictionary
    def __repr__(self):
        return json.dumps(self.dict())

if __name__ == "__main__":
    provider = Provider("1","IMDB","https://www.netflix.com/title/80138262","https://utellyassets7.imgix.net/locations_icons/utelly/black_new/NetflixIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18")
    print(provider)
