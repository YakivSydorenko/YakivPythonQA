import pytest
import requests


@pytest.mark.http
def test_first_request():
    response = requests.get('https://api.github.com/zen')

    print(f'response is: {"Practicality beats purity."}')


@pytest.mark.http
def test_second_request():
    response = requests.get('https://api.github.com/users/defunkt')
    body = response.json()
    response.status_code = 200
    headers = response.headers

    assert body['name'] == 'Chris Wanstrath'
    assert response.status_code == 200
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    response = requests.get('https://api.github.com/users/sergii_butenko')
    response_status_code = 404
    
    assert response_status_code == 404