import allure
import requests


class BaseApi:
    response_json = None
    response = None
    headers = {'Content-Type': 'application/json'}
    url_autiriz = 'http://167.172.172.115:52355/authorize'
    url_autiriz1 = 'http://167.172.172.115:52355/authorize/RKmc1krb9OgE2Jz'

    @allure.step('Check staus code')
    def check_status_code_is_(self, code):
        assert self.response.status_code == code

    @allure.step('Check response name')
    def check_response_name_is_(self, name):
        assert self.response_json['name'] == name