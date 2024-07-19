import requests
import allure
from api_test_memes.endpoints.base_api import BaseApi


class GetID(BaseApi):
    @allure.step('Get ad')
    def get_id_(self, headers=None):
        self.response = requests.get(
            f'{self.url_base}/meme/1',
            headers=headers
        )
        print(self.response.json())
        return self.response
