import requests
import allure
from api_test_memes.endpoints.base_api import BaseApi


class PostAuthorize(BaseApi):
        @allure.step('create token')
        def create_token(self, payload, headers=None):
            headers = headers if headers else self.headers
            self.response = requests.post(
                f'{self.url_autiriz}',
                json=payload,
                headers=headers
            )
            user_token = self.response.json()['token']
            print(self.response.json())
            print(user_token)
            return user_token
