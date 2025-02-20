
from sender_stand_request import post_new_client_kit, create_new_user
from data import kit_body_1, kit_body_2, kit_body_3, kit_body_4, kit_body_5, kit_body_6, kit_body_7, kit_body_8, kit_body_9

def get_new_user_token():
    return create_new_user()

def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_1_char():
    positive_assert(kit_body_1)

def test_511_caracteres():
    positive_assert(kit_body_2)

def test_empty_name():
    negative_assert_code_400(kit_body_3)

def test_512_caracteres():
    negative_assert_code_400(kit_body_4)

def test_special_caracteres():
    positive_assert(kit_body_5)

def test_spaces_in_name():
    positive_assert(kit_body_6)

def test_numbers_in_name():
    positive_assert(kit_body_7)

def test_missing_name():
    negative_assert_code_400(kit_body_8)

def test_invalid_type():
    negative_assert_code_400(kit_body_9)
