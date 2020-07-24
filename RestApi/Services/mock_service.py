import json

class MockService(object):
    Data = None
    def __init__(self):
        self.Data = open("..\Results.json",mode="r").read()
    def getData(self):
        return self.Data


if __name__ == '__main__':
    mockService = MockService()
    print(mockService.getData())