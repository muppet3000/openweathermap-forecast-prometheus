import api
import formatter


def get_owm_client(config):
    owm_config = config.get('owm')
    assert owm_config is not None, 'No config section for OpenWeather found'
    assert 'api_key' in owm_config, 'No api-key for OpenWeather found'

    api_key = str(owm_config.get('api_key'))
    config_version = '2.5'
    if 'version' in owm_config:
        config_version = str(owm_config['version'])

    from pyowm import OWM
    owm = OWM(API_key=api_key, version=config_version)

    return api.OwmClient(owm_config, owm)
