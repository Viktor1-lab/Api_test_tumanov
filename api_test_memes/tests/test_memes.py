import pytest
import allure
from api_test_memes.tests.data import payloads


def test_get_memes(get_memes_all, create_token):
    get_memes_all.get_memes(headers={'authorization': f'{create_token}'})
    get_memes_all.check_status_code_is_(200)
