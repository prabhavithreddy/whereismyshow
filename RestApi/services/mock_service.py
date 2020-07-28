import json

class MockService(object):
    Data = None
    def __init__(self, file_path="..\Results.json"):
        self.Data = open(file_path,mode="r").read()
    def getData(self):
        return self.Data


if __name__ == '__main__':
    mockService = MockService("..\Results.json")
    print(mockService.getData())