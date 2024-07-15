import pytest
import requests
import allure
from api_test_memes.endpoints.authorize_post import PostPosts
from api_test_memes.endpoints.get_all_memes import GetAllMemes
from api_test_memes.tests.data.payloads import name


url = 'http://167.172.172.115:52355'


@allure.feature('Fixture')
@pytest.fixture()
def create_new_token():
    payload = {
        "name": "Tumanio"
    }
    response = requests.post(
        url,
        json=payload
    )
    new_tokens = response.json()['token']
    print(f'Создание объекта {new_tokens}')
    yield new_tokens
    # requests.delete(f'https://api.restful-api.dev/objects/{new_obj_id}')
    # print(f'Удаление объекта {new_obj_id}')


@pytest.fixture()
def create_token():
    return PostPosts().create_token(name)


@pytest.fixture()
def get_memes_all():
    return GetAllMemes()