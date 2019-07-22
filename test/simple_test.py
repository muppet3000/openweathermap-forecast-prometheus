import OpenWeatherMap
import pytest

def test_owm_client():
    actual = OpenWeatherMap.get_owm_client({'owm': {'api_key': 'sadf78as9fhsdafg7s', 'cities': ['Munich']}, 'general': {'sleep_timer': 30}})
    assert isinstance(actual, OpenWeatherMap.api.OwmClient)

def test_owm_client_fail_no_owm_config():
    with pytest.raises(AssertionError):
        OpenWeatherMap.get_owm_client({'api_key': 'sadf78as9fhsdafg7s', 'cities': ['Munich']})

def test_owm_client_fail_no_api_key():
    with pytest.raises(AssertionError):
        OpenWeatherMap.get_owm_client({'owm': {'cities': ['Munich']}, 'general': {'sleep_timer': 30}})

def test_formatter_setup():
    assert True