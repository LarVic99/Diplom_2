import sys 
sys.path.append('..')
from faker import Faker
import requests
from urls import *

fake = Faker()

def generate_email(): # Генерируем email
    return fake.email()
def generate_password(): # Генерируем password
    return fake.password(10)
def generate_name(): # Генерируем name
    return fake.user_name()


class UserLoginData(): # Класс списков из email, пароля и имени
    
    full_user_data = { # Создаем список из email, password, name
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
        }

    not_full_user_data = [ # Данные для теста создания пользователя без одного из обязательных полей
        {"email": "", "password": generate_password(), "name": generate_name()}, # Без email
        {"email": generate_email(), "password": "", "name": generate_name()}, # Без password
        {"email": generate_email(), "password": generate_password(), "name": ""} # Без name
        ]

    login_data = [ # Данные для теста логина пользователя
        {"email": full_user_data["email"], "password": full_user_data["password"]}, # Полные данные
        {"email": generate_email(), "password":full_user_data["password"]}, # Неверный email
        {"email": full_user_data["email"], "password": generate_password()} # Неверный password
        ] 


class ResponsesCode: # Коды ответов
    Ok = 200
    Created = 201 
    Bad_Request = 400
    Unauthorized = 401
    Forbidden = 403
    Internal_Server_Error = 500


class ResponsesMessage: # Сообщения ответов
    Succes = "'success': True"
    No_Succes = "'success': False"
    User_already_exists = {"success": False, "message": "User already exists"}
    User_required_fields = {"success": False, "message": "Email, password and name are required fields"}
    Incorrect_email_or_password = {"success": False, "message": "email or password are incorrect"}
    NoIngredient_in_order = {"success": False, "message": "Ingredient ids must be provided"}
    Redirect = "/login"
 

class HashIngredientData():
    response = requests.get(URLs.URL_GET_INGRIDIENTS)
    ingredient = response.json()
    correct_hash_ingred = {'ingredients': [ingredient["data"][0]['_id'], ingredient['data'][1]['_id']]} # Подставляем хеши-ингридиентов
    no_hash_ingred = {'ingredients': []}
    incorrect_hash_ingred = {"ingredients": [ingredient["data"][0]['_id'], "1a2b3c4d5e"]} # Подставляем хеш 1 ингридиента и 1 неверный
