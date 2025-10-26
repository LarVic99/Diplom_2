import sys 
sys.path.append('..')

import allure
import pytest
import requests
from data import *
from urls import URLs


class Test_Create_User: # Тесты создания пользователя
    
    @allure.title('Тест создания уникального пользователя')
    def test_create_user_true(self, user_generate_and_delete):
        response = requests.post(URLs.URL_CREATE_USER, json = user_generate_and_delete) # Создаем пользователя
        assert response.status_code == ResponsesCode.Ok and ResponsesMessage.Succes in str(response.json()) # Сверяем код ответа и текст сообщения

    @allure.title('Тест создания пользователя, который уже зарегистрирован')
    def test_create_duplicate_user_true(self, user_generate_and_delete):
        requests.post(URLs.URL_CREATE_USER, json = user_generate_and_delete) # Создаем пользователя 1
        response2 = requests.post(URLs.URL_CREATE_USER, json = user_generate_and_delete) # Создаем пользователя 2
        assert response2.status_code == ResponsesCode.Forbidden and ResponsesMessage.User_already_exists == response2.json() # Сверяем код ответа и текст сообщения

    @allure.title('Тест создания пользователя с незаполненным одним из обязательных полей (email, password, name)')
    @pytest.mark.parametrize('user_data', UserLoginData.not_full_user_data)
    def test_create_user_without_field_true(self, user_data):
        response = requests.post(URLs.URL_CREATE_USER, json = user_data) # Создаем пользователя 
        assert response.status_code == ResponsesCode.Forbidden and response.json() == ResponsesMessage.User_required_fields # Сверяем код ответа и текст сообщения
