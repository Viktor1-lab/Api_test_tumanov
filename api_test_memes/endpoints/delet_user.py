# import pytest
import requests
import allure
from api_test_memes.endpoints.base_api import BaseApi


class DelUser(BaseApi):
        @allure.step('create token')
        def delete_user(self, payload, headers=None):
            headers = headers if headers else self.headers
            self.response = requests.delete(
                f'{self.url_autiriz}',
                json=payload,
                headers=headers
            )
            user_token = self.response.json()['token']
            print(self.response.json())
            print(user_token)
            return user_token