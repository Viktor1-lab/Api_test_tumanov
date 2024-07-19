import allure
import requests
from api_test_memes.endpoints.base_api import BaseApi


class PutMem(BaseApi):
    @allure.step('Izmenenie mema')
    def put_update_mem(self, get_post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url_meme}/{get_post_id}',
            json=payload,
            headers=headers
        )
        print(self.response)
        return self.response
