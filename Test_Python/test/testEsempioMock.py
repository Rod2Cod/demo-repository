
import requests
from unittest import mock
import random

def get_ip(url) -> str | None:
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["origin"]
    return None

def get_random_number() -> int:
    return random.randint(7, 10)

mock_response = mock.Mock(**{"status_code": 200, "json.return_value": {"origin": "0.0.0"}}) # Creo una finta risposta

""" Versione alternativa più lunga: 
mock_response = mock.Mock()
mock_response.status_code = 200
mock_response.json.return_value = {"origin": "0.0.0"}
"""

# Modifico le funzioni requests.get e random.randint
@mock.patch('random.randint')
@mock.patch('requests.get')
def test_get_json(mock_request, mock_random):
    mock_request.return_value = mock_response # Modifico il tipo di ritorno della funzione requests.get
    response = get_ip('https://httpbin.org/ip')

    mock_request.assert_called_with('https://httpbin.org/ip')
    mock_request.assert_called_once()

    assert response == "0.0.0"

    mock_random.return_value = 0 # Modifico il tipo di ritorno della funzione random.randint
    assert get_random_number() == 0