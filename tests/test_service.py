import unittest.mock as mock
import pytest
import requests
import src.service as service


@mock.patch("src.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):
    mock_get_user_from_db.return_value = "Mock Dave"
    user_name: str = service.get_user_from_db(1)
    assert user_name == "Mock Dave"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Dave Johnson"}
    mock_get.return_value = mock_response
    data = service.get_users()

    assert data == {"id": 1, "name": "Dave Johnson"}


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        service.get_users()
