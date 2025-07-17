# test_map_app.py
import os
import app
import pytest
from unittest.mock import patch

@patch("app.requests.get")
def test_get_distance(mock_get):
    fake_response = {
        "status": "OK",
        "rows": [{
            "elements": [{
                "status": "OK",
                "distance": {"text": "12.3 km"}
            }]
        }]
    }
    mock_get.return_value.json.return_value = fake_response
    os.environ["GOOGLE_API_KEY"] = "fakekey"

    result = app.get_distance("New York, NY", "Boston, MA")
    assert result == "12.3 km"
