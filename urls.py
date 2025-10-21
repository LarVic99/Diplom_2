import sys 
sys.path.append('..')

# Ссылки для тестирования сайта
class URLs:
    URL_STELLAR_BURGERS = 'https://stellarburgers.education-services.ru/' # Главная страница сайта STELLARBURGERS
    URL_GET_INGRIDIENTS = f'{URL_STELLAR_BURGERS}/api/ingredients' # Получение данных об ингредиентах
    URL_CREATE_ORDER = f'{URL_STELLAR_BURGERS}/api/orders' # Создание заказа (методом POST)
    URL_GET_ORDER = f'{URL_STELLAR_BURGERS}/api/orders' # Получить заказы (методом GET)
    URL_CREATE_USER = f'{URL_STELLAR_BURGERS}/api/auth/register' # Создание пользователя
    URL_LOGIN_USER = f'{URL_STELLAR_BURGERS}/api/auth/login' #  Авторизация пользователя
    URL_LOGOUT_USER = f'{URL_STELLAR_BURGERS}/api/auth/logout' # Выход пользователя из системы
    URL_DELETE_USER = f'{URL_STELLAR_BURGERS}/api/auth/user' # Удаление пользователя (методом DELETE)
