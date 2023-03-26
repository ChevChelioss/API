import allure
from pytest_voluptuous import S
from schemas.user import *
from utils.endpoints import USERS_ENDPOINT, USER_ENDPOINT_FORMAT, REGISTER_ENDPOINT


def test_create_user_successfully(reqres):
    """
    Test case for successfully creating a user.
    """
    name = 'Chev'
    job = 'leader'
    with allure.step('create_user_successfully'):
        create_user = reqres.post(USERS_ENDPOINT, {'name': name, 'job': job})

        assert create_user.status_code == 201
        assert create_user.json() == S(create_single_user)
        assert all(key in create_user.json() for key in ['name', 'job'])
        assert create_user.json()['name'] == name
        assert create_user.json()['job'] == job


def test_update_user_successfully(reqres):
    """
    Test case for successfully updating a user.
    """
    user_id = 2
    update_name = 'morpheus'
    update_job = 'follower'
    with allure.step('update_user_successfully'):
        update_user = reqres.put(USER_ENDPOINT_FORMAT.format(user_id), {'name': update_name, 'job': update_job})

        assert update_user.status_code == 200
        assert update_user.json() == S(update_single_user)
        assert all(key in update_user.json() for key in ['name', 'job'])
        assert update_user.json()['name'] == update_name
        assert update_user.json()['job'] == update_job


def test_register_successfully(reqres):
    """
    Test case for successful registration.
    """
    email = 'eve.holt@reqres.in'
    password = 'pistol'
    with allure.step('register_successfully'):
        register_successful = reqres.post(REGISTER_ENDPOINT, {'email': email, 'password': password})

        assert register_successful.status_code == 200
        assert all(key in register_successful.json() for key in ['id', 'token'])
        assert register_successful.json()['id'] == 4
        assert register_successful.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_register_unsuccessfully(reqres):
    """
    Test case for unsuccessful registration.
    """
    email = 'sydney@fife'
    password = 'pistol'
    with allure.step('register_unsuccessfully'):
        register_unsuccessful = reqres.post(REGISTER_ENDPOINT, {'email': email, 'password': password})

        assert register_unsuccessful.status_code == 400


def test_delete_user_successfully(reqres):
    """
    Test case for successfully deleting a user.
    """
    user_id = 2
    with allure.step('delete_user_successfully'):
        delete_user = reqres.delete(USER_ENDPOINT_FORMAT.format(user_id))

        assert delete_user.status_code == 204
