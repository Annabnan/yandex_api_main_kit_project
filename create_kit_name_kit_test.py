import sender_stand_request
import data

def get_new_user_token(): # создание пользователя с получением токена
    user_response = sender_stand_request.post_new_user(data.user_body)
    return user_response.json()["authToken"]


def get_kit_body(name): # формирование тела запроса в создании набора
    kit_body = data.kit_body.copy()
    kit_body['name'] = name

    return kit_body


def get_empty_kit_body():  # пустое тело запроса в создании набора
    kit_body = data.kit_body.copy()
    kit_body.pop('name')

    return kit_body

def positive_assert(name):
    token = get_new_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()['name'] == name


def negative_assert_code_400(name):
    token = get_new_user_token()
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_kit(kit_body, token)

    assert response.status_code == 400


# Тест 1. Допустимое количество символов (1)
def test_create_kit_1_letter_in_name():
    positive_assert("а")


# Тест 2. Допустимое количество символов (511)
def test_create_kit_511_letter_in_name():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Ошибка. Недопустимое количество символов (0)
def test_create_kit_0_letter_in_name():
    negative_assert_code_400("")


# Тест 4. Ошибка. Недопустимое количество символов (512)
def test_create_kit_16_letter_in_name():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Допустимы английские буквы
def test_create_kit_english_letter_in_name():
    positive_assert("QWErty")


# Тест 6. Допустимы русские буквы
def test_create_kit_russian_letter_in_name():
    positive_assert("Мария")


# Тест 7. Допустимы специальные символы
def test_create_kit_has_special_symbol_in_name():
    positive_assert("\"№%@\",")


# Тест 8. Допустимы пробелы
def test_create_kit_has_space_in_name():
    positive_assert("Человек и КО")


# Тест 9. Допустимы цифры
def test_create_kit_has_number_in_name():
    positive_assert("123")


# Тест 10. Ошибка. Параметр не передан в запросе
def test_create_kit_no_name():
    token = get_new_user_token()
    kit_body = get_empty_kit_body()
    response = sender_stand_request.post_new_kit(kit_body, token)

    assert response.status_code == 400


# Тест 11. Ошибка. Передан другой тип параметра (число)
def test_create_kit_number_type_name():
    negative_assert_code_400(123)