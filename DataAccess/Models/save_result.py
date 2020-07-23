import json

class SaveResult:

    is_saved = None
    message = None
    error = None

    def __init__(self, is_saved: bool = False, message: str = None, error: Exception = None):

        self.is_saved = is_saved
        self.message = message
        self.error = error

    def __str__(self) -> str:
        dictionary = dict()
        dictionary['is_saved'] = self.is_saved
        dictionary['message'] = self.message
        dictionary['error'] = self.error
        return json.dumps(dictionary)

