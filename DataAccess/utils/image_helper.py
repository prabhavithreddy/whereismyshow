import requests
import urllib.parse
from bs4 import BeautifulSoup
import re

def get_image(name:str):
    url = "https://www.bing.com/images/search?q={}".format(urllib.parse.quote(name))
    r = requests.get(url)
    x = re.findall("(<img> class=\"mimg\")", r.text)
    print(x)

def get_images(name:str):
    url = "https://www.bing.com/images/search?q={}".format(name)
    r = requests.get(url)
    print(url)
    parser = BeautifulSoup(r.text, "html.parser")
    x = parser.findAll("a", {'class':'thumb'})[0]
    print(x["href"])


if __name__ == '__main__':
    get_images('amazon prime video penguin')