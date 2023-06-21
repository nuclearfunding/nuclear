import requests
from applications.exceptions import BadResponse


class HTTPClient:
    def __init__(self, default_retry=3):
        self.retry_count = default_retry

    def post(self, url, headers, data):
        response = None
        for attempt in range(self.retry_count):
            response = self._post(url, headers=headers, json=data)
            if response.status_code in [200, 201, 202]:
                return response
            elif 500 > response.status_code:
                raise BadResponse(response)

        raise BadResponse(response)

    def get(self, url, headers):
        response = None
        for attempt in range(self.retry_count):
            response = self._post(url, headers=headers, json=data)
            if response.status_code in [200, 201, 202]:
                return response
            elif 500 > response.status_code:
                raise BadResponse(response)

        raise BadResponse(response)

    def _post(self, url, headers, data):
        response = requests.post(url, headers=headers, json=data)
        return response