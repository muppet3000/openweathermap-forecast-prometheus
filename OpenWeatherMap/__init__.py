from . import api
from . import formatter
from pyowm import OWM

def get_owm_client(config):
    owm_config = config.get('owm')
    assert owm_config is not None, 'No config section for OpenWeather found'
    assert 'api_key' in owm_config, 'No api-key for OpenWeather found'

    api_key = str(owm_config.get('api_key'))

    #TODO - Consider adding section for customer 'config_dict' - https://pyowm.readthedocs.io/en/latest/v3/pyowm-configuration-description.html

    owm = OWM(api_key)

    return api.OwmClient(owm_config, owm)
