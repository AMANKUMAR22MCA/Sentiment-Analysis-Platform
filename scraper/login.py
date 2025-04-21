import requests

def get_access_token(email, password):
    url = "http://localhost:8000/api/users/login/"
    response = requests.post(url, json={"email": email, "password": password})
    if response.status_code == 200:
        return response.json()["access"]
    else:
        raise Exception("Login failed. Check credentials.")
