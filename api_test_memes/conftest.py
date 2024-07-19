import pytest
import requests
import allure
from api_test_memes.endpoints.authorize_post import PostAuthorize
from api_test_memes.endpoints.get_all_memes import GetAllMemes
from api_test_memes.tests.data.payloads import name, new_mem
from api_test_memes.endpoints.create_mem import CreateMem
from api_test_memes.endpoints.update_mem import PutMem
from api_test_memes.endpoints.delet_mem import DeleteMem
from api_test_memes.endpoints.get_id import GetID


url = 'http://167.172.172.115:52355'


@pytest.fixture()
def create_token():
    return PostAuthorize().create_token(name)


@pytest.fixture()
def get_memes_all():
    return GetAllMemes()


@pytest.fixture()
def create_new_mem():
    return CreateMem()


@pytest.fixture()
def mem_id(create_new_mem, create_token):
    payload = new_mem
    create_new_mem.create_mem(payload=payload,
                              headers={'authorization': f'{create_token}'})
    id_mem = create_new_mem.response.json()['id']
    print(id_mem)
    yield id_mem


@pytest.fixture()
def update_post():
    return PutMem()


@pytest.fixture()
def delet_mem():
    return DeleteMem()


@pytest.fixture()
def check_get_id():
    return GetID()