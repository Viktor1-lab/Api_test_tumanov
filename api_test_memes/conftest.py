import pytest
import requests
import allure
from api_test_memes.endpoints.authorize_post import PostPosts
from api_test_memes.endpoints.get_meme import Get_id
from api_test_memes.endpoints.delet_user import DelUser


@allure.feature('Fixture')
@pytest.fixture()
def new_obj():
    payload = {
        "name": "NarateL"
    }
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload
    )
    new_obj_id = response.json()['id']
    print(f'Создание объекта {new_obj_id}')
    yield new_obj_id
    requests.delete(f'https://api.restful-api.dev/objects/{new_obj_id}')
    print(f'Удаление объекта {new_obj_id}')


@pytest.fixture()
def create_user_endpoint():
    return PostPosts()


@pytest.fixture()
def get_idi():
    return Get_id
