import json
import pytest
import requests
from api import Pets

pt = Pets()


@pytest.mark.parametrize("email, password, expected_status, expected_message", [
    ("@gmail.com", "12345", 400, 'Expected status 400 for invalid email'),  # Invalid email
    ("shulga19@gmail.com", "#", 400, 'Expected status 400 for invalid password'),  # Invalid password
    (" ", "12345", 400, 'Expected status 400 for missing email'),  # Missing email
    ("shulga19@gmail.com", " ", 400, 'Expected status 400 for missing password'),  # Missing password
    (" ", " ", 400, 'Expected status 400 for missing email and password'),  # Both fields missing
    ("shulga25@gmail.com", "12345 ", 400, 'Expected status 400 for missing email and password'),  # Not registered user
])
def test_get_token_negative(email, password, expected_status, expected_message):
    data = {"email": email, "password": password}
    response = requests.post(pt.base_url + 'login', data=json.dumps(data))

    status = response.status_code
    token = response.json().get('token', None)
    my_id = response.json().get('id', None)
    print(data, status, token, my_id)

    assert status == expected_status, expected_message