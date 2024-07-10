import pytest
import requests
import allure
from api_test_memes.endpoints.base_api import BaseApi


class Get_id(BaseApi) :
    @allure.step('create torrrken')
    def create_user(self, payload, headers=None) :
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url_autiriz1}',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        print(self.response.json())

        return self.response