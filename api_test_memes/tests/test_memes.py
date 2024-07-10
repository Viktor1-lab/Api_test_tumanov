import pytest
import allure
from api_test_memes.tests.data import payloads


def test_create_user(create_user_endpoint):
    create_user_endpoint.create_user(payload=payloads.name)
    create_user_endpoint.check_status_code_is_(200)
    # create_user_endpoint.check_response_name_is_(payloads.new_object.get('name'))
