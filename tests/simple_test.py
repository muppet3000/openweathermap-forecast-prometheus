import OpenWeatherMap

test_config = {'owm': {'api_key': 'sadf78as9fhsdafg7s', 'cities': ['Munich']}, 'general': {'sleep_timer': 30}}

def test_owm_client():
    actual = OpenWeatherMap.get_owm_client(test_config)
    assert isinstance(actual, OpenWeatherMap.api.OwmClient)

def test_formatter_setup():
    assert True

def test_formatter_setup():
    assert True

def test_formatter_setup():
    assert True