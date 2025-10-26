import sys 
sys.path.append('..')

import allure
import pytest
import requests
from data import *
from urls import URLs


class TestLoginUser: # Тесты авторизации пользователя
    
    @allure.title('Тест логина пользователя со всеми обязательными полями')
    def test_user_login_full_data_true(self, user_create_and_delete):
        response = requests.post(URLs.URL_LOGIN_USER, json=user_create_and_delete) # Логиним пользователя
        assert response.status_code == ResponsesCode.Ok and ResponsesMessage.Succes in str(response.json()) # Сверяем код ответа и текст сообщения

    @allure.title('Тест логина пользователя с неверным логином/паролем')
    @pytest.mark.parametrize('user_data', [
        {'email': 'wrong1@example.com', 'password': '123456'},
        {'email': 'wrong2@example.com', 'password': 'abcdef'}
    ])  # Перебор неверных данных
    def test_user_login_not_full_data_true(self, user_data):
        response = requests.post(URLs.URL_LOGIN_USER, json=user_data) # Логиним пользователя
        assert response.status_code == ResponsesCode.Unauthorized and response.json() == ResponsesMessage.Incorrect_email_or_password # Сверяем код ответа и текст сообщения
