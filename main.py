from prometheus_client import start_http_server
import time
import yaml
import os.path
import sys
import OpenWeatherMap

pathname = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(pathname + '/weather.yml'):
    config = yaml.load(open(pathname + '/weather.yml', 'r'), Loader=yaml.Loader)
else:
    raise IOError('Config file "weather.yml" not found!')

sleep_timer = 30
if ('general' in config) & isinstance(config['general'],(list,dict)):
    sleep_timer = config['general'].get('sleep_timer', 30)

Owm = OpenWeatherMap.get_owm_api(config)


def process_request():
    # fetch new weather data
    OpenWeatherMap.formatter.format_owm_weather(Owm.call_owm())
    time.sleep(sleep_timer)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request()
