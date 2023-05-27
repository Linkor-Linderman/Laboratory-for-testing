import requests

BASE_URL = 'http://localhost:5000/'


def get_form():
    response = requests.get(BASE_URL)
    return response


def post_for_result(n=None):
    post_data = {"number": n}
    response = requests.post(BASE_URL, data=post_data)
    return response
