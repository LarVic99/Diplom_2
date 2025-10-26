import sys 
sys.path.append('..')

import allure
import pytest
import requests
from data import *
from urls import URLs


# Интерфейс для взаимодействия с API
class ApiClient:
    def __init__(self, token: str = None):
        self.token = token

    def set_token(self, token: str):
        self.token = token

    def create_order(self, ingredients_hashes: list, auth: bool = True):
        """
        Создание заказа
        :param ingredients_hashes: список хешей ингредиентов
        :param auth: использовать токен или нет
        """
        headers = {'Authorization': self.token} if auth and self.token else {}
        response = requests.post(URLs.URL_CREATE_ORDER, json=ingredients_hashes, headers=headers)
        return response


class TestCreateOrder: # Тесты создания заказа

    @allure.title('Тест создания заказа с авторизацией и с ингридиентами')
    def test_order_create_auth_user_true(self, user_create_login_and_delete):
        client = ApiClient(user_create_login_and_delete) # Подставляем токен
        payload = HashIngredientData.correct_hash_ingred # Хеши ингридиентов
        response = client.create_order(payload)
        assert response.status_code == ResponsesCode.Ok and ResponsesMessage.Succes in str(response.json()) # Сверяем код ответа и текст сообщения

    @allure.title('Тест создания заказа без авторизации')
    def test_order_create_noauth_user_true(self):
        client = ApiClient()
        payload = HashIngredientData.correct_hash_ingred # Хеши ингридиентов
        response = client.create_order(payload, auth=False)
        assert response.status_code == ResponsesCode.Forbidden and ResponsesMessage.Redirect in str(response.headers) # Сверяем код ответа и текст сообщения

    @allure.title('Тест создания заказа без ингридиентов')
    def test_order_create_no_hash_ingred_true(self, user_create_login_and_delete):
        client = ApiClient(user_create_login_and_delete) # Подставляем токен
        payload = HashIngredientData.no_hash_ingred # Хеши ингридиентов
        response = client.create_order(payload)
        assert response.status_code == ResponsesCode.Bad_Request and ResponsesMessage.No_Succes in str(response.json()) # Сверяем код ответа и текст сообщения

    @allure.title('Тест создания заказа с неверным хешем ингридиентов')
    def test_order_create_incorrect_hash_ingred(self, user_create_login_and_delete):
        client = ApiClient(user_create_login_and_delete) # Подставляем токен
        payload = HashIngredientData.incorrect_hash_ingred # Хеши ингридиентов
        response = client.create_order(payload)
        assert response.status_code == ResponsesCode.Internal_Server_Error # Сверяем код ответа и текст сообщения
