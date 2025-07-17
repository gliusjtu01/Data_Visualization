# test_app.py
import os
import app
import pytest

def test_real_api():
    if "GOOGLE_API_KEY" not in os.environ:
        pytest.skip("GOOGLE_API_KEY not set")

    distance = app.get_distance("San Francisco, CA", "Los Angeles, CA")
    assert "mi" in distance or "km" in distance
