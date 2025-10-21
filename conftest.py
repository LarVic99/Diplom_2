import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import allure
import pytest
import requests
from data import *
from urls import *

@pytest.fixture(scope='function')
def user_generate_and_delete(): # Генерация данных пользователя и удаление пользователя
    user = UserLoginData.full_user_data # Данные пользователя
    yield user # Передадим данные и подождем
    response = requests.post(URLs.URL_LOGIN_USER, json = UserLoginData.login_data[0]) # Логиним пользователя с полными данными
    token = response.json()['accessToken'] # Вытаскиваем accessToken из ответа
    headers = {'Authorization': token} # Подставляем токен
    requests.delete(URLs.URL_DELETE_USER, headers = headers) # Удаляем созданного пользователя

@pytest.fixture(scope='function')
def user_create_and_delete(): # Генерация данных пользователя, создание и удаление пользователя
    user = UserLoginData.full_user_data # Данные пользователя
    requests.post(URLs.URL_CREATE_USER, json = user) # Создаем пользователя
    user_data = UserLoginData.login_data 
    yield user_data # Передадим данные и подождем
    response = requests.post(URLs.URL_LOGIN_USER, json = user_data[0]) # Логиним пользователя с верными login и password
    token = response.json()['accessToken'] # Вытаскиваем accessToken из ответа
    headers = {'Authorization': token} # Подставляем токен
    requests.delete(URLs.URL_DELETE_USER, headers = headers) # Удаляем созданного пользователя

@pytest.fixture(scope='function')
def user_create_login_and_delete(): # Генерация данных пользователя, создание, авторизация и удаление пользователя
    user = UserLoginData.full_user_data # Данные пользователя
    requests.post(URLs.URL_CREATE_USER, json = user) # Создаем пользователя
    user_data = UserLoginData.login_data 
    response = requests.post(URLs.URL_LOGIN_USER, json = user_data[0]) # Логиним пользователя с верными login и password
    token = response.json()['accessToken'] # Вытаскиваем accessToken из ответа
    yield token # Передадим данные token'a и подождем
    headers = {'Authorization': token} # Подставляем токен
    requests.delete(URLs.URL_DELETE_USER, headers = headers) # Удаляем созданного пользователя
