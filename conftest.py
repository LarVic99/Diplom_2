import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import requests
from data import *
from urls import *

@pytest.fixture(scope='function')
def delete_user():
    """
    Фикстура для удаления пользователя по логину и паролю.
    Используется через yield для передачи данных пользователя.
    """
    users_to_delete = []

    yield users_to_delete  # сюда будут добавлять user_data из других фикстур

    for user_data in users_to_delete:
        # Логиним пользователя для получения токена
        response = requests.post(URLs.URL_LOGIN_USER, json=user_data)
        if response.status_code == 200:
            token = response.json().get('accessToken')
            headers = {'Authorization': token}
            # Удаляем созданного пользователя
            requests.delete(URLs.URL_DELETE_USER, headers=headers)


@pytest.fixture(scope='function')
def user_generate_and_delete(delete_user): 
    # Генерация данных пользователя и удаление пользователя
    user = UserLoginData.full_user_data # Данные пользователя
    delete_user.append(UserLoginData.login_data[0]) # добавляем в список для удаления
    return user # Передадим данные и подождем


@pytest.fixture(scope='function')
def user_create_and_delete(delete_user): 
    # Генерация данных пользователя, создание и удаление пользователя
    user = UserLoginData.full_user_data # Данные пользователя
    requests.post(URLs.URL_CREATE_USER, json=user) # Создаем пользователя
    user_data = UserLoginData.login_data[0]
    delete_user.append(user_data) # добавляем в список для удаления
    yield user_data # Передадим данные и подождем


@pytest.fixture(scope='function')
def user_create_login_and_delete(delete_user): 
    # Генерация данных пользователя, создание, авторизация и удаление пользователя
    user = UserLoginData.full_user_data # Данные пользователя
    requests.post(URLs.URL_CREATE_USER, json=user) # Создаем пользователя
    user_data = UserLoginData.login_data[0]
    response = requests.post(URLs.URL_LOGIN_USER, json=user_data) # Логиним пользователя с верными login и password
    token = response.json().get('accessToken') # Вытаскиваем accessToken из ответа
    delete_user.append(user_data) # добавляем в список для удаления
    yield token # Передадим данные token'a и подождем
