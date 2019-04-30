from pyowm.exceptions import api_call_error
from pyowm.webapi25.owm25 import OWM25
import time
import datetime


class OwmApiWrapper:
    """
    Simple wrapper around pyowm to catch exceptions and to request multiple weather

    :param owm_config: The config section as dict for "owm"
    :type owm_config: dict
    :param api_client: The class OWM25 - THE Api class from pyowm
    :type api_client: OWM25

    """
    def __init__(self, owm_config, api_client):
        self.config = owm_config
        self.owm = api_client

    def call_owm(self):
        def get_city_weather():
            observed = list()
            if 'cities' in self.config:
                for city in self.config['cities']:
                    city_data = self.owm.weather_at_places(str(city), searchtype='accurate', limit=3)  # type: list
                    if len(city_data) != 0:
                        observed.append(city_data[0])
            return observed

        obs_list = list()
        try:
            obs_list.extend(get_city_weather())
        except (api_call_error.APICallTimeoutError, api_call_error.APIInvalidSSLCertificateError) as e:
            print '{} Error: {}'.format(datetime.datetime.now().isoformat(), e)
            time.sleep(10)
            return list()
        return obs_list
