import pytest
import allure
from api_test_memes.tests.data import payloads


@allure.step('Step 1, request for all memes')
@allure.feature('Get all memes')
def test_get_memes(get_memes_all, create_token):
    get_memes_all.get_memes(headers={'authorization': f'{create_token}'})
    get_memes_all.check_status_code_is_(200)


def test_get_id(check_get_id, create_token):
    check_get_id.get_id_(headers={'authorization': f'{create_token}'})
    check_get_id.check_status_code_is_(200)


@allure.step('Step 2, create mem')
def test_create_mem(create_new_mem, create_token):
    create_new_mem.create_mem(payload=payloads.new_mem,
                              headers={'authorization': f'{create_token}'})
    create_new_mem.check_status_code_is_(200)
    create_new_mem.check_response_name_is_(payloads.new_mem['text'])


@allure.step('Step 3, update your memes')
@pytest.mark.parametrize('colors', ['ddd', 5, "!@#$%"])
def test_update_mem(update_post, mem_id, create_token, colors):
    payload = payloads.update_mem
    payload['id'] = mem_id
    payload['info']['colors'] = colors
    update_post.put_update_mem(get_post_id=mem_id,
                               payload=payloads.update_mem,
                               headers={'authorization': f'{create_token}'})
    # print(payload)
    update_post.check_status_code_is_(200)


def test_delet_mem(delet_mem, mem_id, create_token):
    delet_mem.delete_mem(mem_id, create_token)
    delet_mem.check_status_code_is_(200)
