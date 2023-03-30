import allure
from pytest_voluptuous import S
from schemas.user import *
from utils.endpoints import *


@allure.title('Creating a user')
def test_create_user_successfully(reqres, add_labels):
    name = 'Chev'
    job = 'leader'
    with allure.step('Sending a request to create a user'):
        create_user = reqres.post(USERS_ENDPOINT, {'name': name, 'job': job})

        assert create_user.status_code == 201
        assert create_user.json() == S(create_single_user)
        assert all(key in create_user.json() for key in ['name', 'job'])
        assert create_user.json()['name'] == name
        assert create_user.json()['job'] == job


@allure.title('Updating a user')
def test_update_user_successfully(reqres, add_labels):
    user_id = 2
    update_name = 'morpheus'
    update_job = 'follower'
    with allure.step('Sending a request to update a user'):
        update_user = reqres.put(USER_ENDPOINT_FORMAT.format(user_id), {'name': update_name, 'job': update_job})

        assert update_user.status_code == 200
        assert update_user.json() == S(update_single_user)
        assert all(key in update_user.json() for key in ['name', 'job'])
        assert update_user.json()['name'] == update_name
        assert update_user.json()['job'] == update_job


@allure.title('Successful registration and receiving token')
def test_register(reqres, add_labels):
    email = 'eve.holt@reqres.in'
    password = 'pistol'
    with allure.step('Register successfully'):
        register_successful = reqres.post(REGISTER_ENDPOINT, {'email': email, 'password': password})

        assert register_successful.status_code == 200
        assert all(key in register_successful.json() for key in ['id', 'token'])
        assert register_successful.json()['id'] == 4
        assert register_successful.json()['token'] == 'QpwL5tke4Pnpja7X4'


@allure.title('Registration with invalid data')
def test_register_with_invalid_data(reqres, add_labels):
    email = 'sydney@fife'
    password = 'pistol'
    with allure.step('Attempt to register with invalid data'):
        register_unsuccessful = reqres.post(REGISTER_ENDPOINT, {'email': email, 'password': password})

        assert register_unsuccessful.status_code == 400


@allure.title('Deleting a user')
def test_delete_user_successfully(reqres, add_labels):
    user_id = 2
    with allure.step('Sending request to delete a user'):
        delete_user = reqres.delete(USER_ENDPOINT_FORMAT.format(user_id))

        assert delete_user.status_code == 204
