import requests
import json


class OpenAi:
    BASE_URL = 'https://api.openai.com'

    def __init__(self):
        secret_file = open('secrets.json')
        self.api_key = json.load(secret_file)['openai_api_key']

    def create_chat_completion(self):
        url = self.BASE_URL + '/v1/chat/completions'
        request = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    'role': 'user',
                    'content': "Generate an investor report for me for my B2B Saas company doing $1.2M in revenue, growing 100% quarter on quarter. We are a AI apps platform for generating AI apps for tabular data - used by the likes of HelloFresh, American Eagle"
                }
            ]
        }
        response = requests.post(url, headers=self._generate_header(), json=request)
        print(vars(response))
        if response.status_code == 200:
            self.handle_response()


    def list_models(self):
        url = self.BASE_URL + '/v1/models'
        response = requests.get(url, headers=self._generate_header())
        print(vars(response))


    def handle_response(self, response):
        pass

    def handle_exceptions(self):

    def _generate_header(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }