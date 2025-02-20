
import requests
from configuration import URL_SERVICE, CREATE_USER_PATH, KITS_PATH

def post_new_client_kit(kit_body, auth_token):
    url = f"{URL_SERVICE}{KITS_PATH}"
    headers = {'Authorization': f'Bearer {auth_token}'}
    response = requests.post(url, json=kit_body, headers=headers)
    return response

def create_new_user():
    url = f"{URL_SERVICE}{CREATE_USER_PATH}"
    response = requests.post(url)
    return response.json().get("authToken")
