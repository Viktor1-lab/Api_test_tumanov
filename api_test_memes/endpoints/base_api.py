import allure
import requests


class BaseApi:
    response_json: dict
    response = None
    headers = {'Content-Type': 'application/json'}
    url_base = 'http://167.172.172.115:52355'
    url_meme = 'http://167.172.172.115:52355/meme'
    url_autiriz = 'http://167.172.172.115:52355/authorize'

    @allure.step('Check staus code')
    def check_status_code_is_(self, code):
        assert self.response.status_code == code

    @allure.step('Check response name')
    def check_response_name_is_(self, text):
        assert self.response_json['text'] == text

    # @allure.step('Check response name')
    # def check_get_id(self, id):
    #     assert self.response.json()['id'] == id(str)
