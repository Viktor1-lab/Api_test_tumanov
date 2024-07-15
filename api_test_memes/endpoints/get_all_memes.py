import requests
import allure
from api_test_memes.endpoints.base_api import BaseApi


class GetAllMemes(BaseApi):
    @allure.step('Get all memes')
    def get_memes(self, headers=None):
        self.response = requests.get(
            f'{self.url_base}/meme',
            headers=headers
        )
        return self.response
