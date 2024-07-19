import allure
import requests
from api_test_memes.endpoints.base_api import BaseApi


class CreateMem(BaseApi):
    @allure.step('Create Mem')
    def create_mem(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url_base}/meme',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        # print(self.response.json())
        return self.response
