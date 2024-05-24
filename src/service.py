import requests

USERS_URL = "https://jsonplaceholder.typicode.com/users"
database = {1: "Dave", 2: "Joe", 3: "Quagmire"}


def get_user_from_db(user_id: int) -> str:
    return database.get(user_id)


def get_users():
    response = requests.get(USERS_URL)
    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError
