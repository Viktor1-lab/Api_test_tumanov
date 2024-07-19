import allure
import requests
from api_test_memes.endpoints.base_api import BaseApi


class DeleteMem(BaseApi):
    @allure.step('Delete mem')
    def delete_mem(self,  mem_id, create_token):
        headers = {'authorization': f'{create_token}'}
        self.response = requests.delete(f'http://167.172.172.115:52355/meme/{mem_id}',
                                        headers=headers)
        self.response = self.response
        return self.response