
class BadResponse(Exception):
    def __init__(self, data):
        self.data = data

class OpenAiException(Exception):
    pass


class OpenAiRetryableException(OpenAiException):
    pass


class OpenAiNonRetryableException(OpenAiException):
    pass