import pytest
from weather.fetch import get_weather

def test_invalid_city():
    result = get_weather("InvalidCityName123")
    assert "error" in result
