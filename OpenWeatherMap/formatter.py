from prometheus_client import Summary, Gauge, Info
import pyowm.weatherapi25.observation

WeatherInfo = Info('weather', 'Short information about weather dataset')
WeatherTemp = Gauge('weather_temperature',
                    'Temperature in Celsius; for large areas, min/max might differ',
                    ['name', 'type', 'id'])
WeatherHumidity = Gauge('weather_humidity',
                        'Relative humidity in percent',
                        ['name', 'id'])
WeatherWindSpeed = Gauge('weather_wind_speed',
                         'Wind speed. Unit: meter/sec',
                         ['name', 'id'])
WeatherWindDir = Gauge('weather_wind_direction',
                       'Wind direction, degrees (meteorological)',
                       ['name', 'id'])
WeatherRain = Gauge('weather_rain',
                    'Rain volume for the last 1/3 hour',
                    ['name', 'id', 'hours'])
WeatherSnow = Gauge('weather_snow',
                    'Snow volume for the last 1/3 hour',
                    ['name', 'id', 'hours'])
WeatherPressure = Gauge('weather_pressure',
                        'Atmospheric pressure in hPa',
                        ['name', 'id', 'level'])


def format_owm_weather(weather_list):
    for obs in weather_list:
        if not isinstance(obs, pyowm.weatherapi25.observation.Observation):
            continue
        weather = obs.weather
        location = obs.location
        WeatherInfo.info({'lastfetch': obs.reception_time(timeformat='iso')})

        WeatherTemp.labels(name=location.name,
                           type='current',
                           id=location.id).set(weather.temperature(unit='celsius')['temp'])
        WeatherTemp.labels(name=location.name,
                           type='temp_max',
                           id=location.id).set(weather.temperature(unit='celsius')['temp_max'])
        WeatherTemp.labels(name=location.name,
                           type='temp_min',
                           id=location.id).set(weather.temperature(unit='celsius')['temp_min'])

        wind = weather.wind()
        if ('speed' in wind):
            WeatherWindSpeed.labels(name=location.name, id=location.id).set(wind['speed'])
        if ('deg' in wind):
            WeatherWindDir.labels(name=location.name, id=location.id).set(wind['deg'])

        WeatherHumidity.labels(name=location.name,
                               id=location.id).set(weather.humidity)
    return
