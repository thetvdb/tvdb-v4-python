from unittest.mock import patch, MagicMock
import pytest
import json
from tvdb_v4_official import TVDB

VALID_API_KEY = "valid_api_key"
VALID_PIN = "valid_pin"


@pytest.fixture
def tvdb_instance():
    with patch("tvdb_v4_official.Auth") as MockAuth:
        MockAuth.return_value.get_token.return_value = "test_token"
        instance = TVDB(VALID_API_KEY, VALID_PIN)
        return instance


@patch("urllib.request.urlopen")
def test_get_artwork(mocked_urlopen, tvdb_instance):
    mock_response_content = json.dumps(
        {"status": "success", "data": {"id": 123, "type": "Poster"}, "links": {}}
    ).encode("utf-8")

    mock_response = MagicMock()
    mock_response.read.return_value = mock_response_content
    mock_response.__enter__.return_value = mock_response
    mocked_urlopen.return_value = mock_response

    artwork = tvdb_instance.get_artwork(123)
    assert artwork["id"] == 123
    assert artwork["type"] == "Poster"
