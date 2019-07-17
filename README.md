# openweathermap_prometheus_python
An open source python script to fetch weather data OpenWeatherMap and expose it in a Prometheus format.
It can be configured using a YAML file to fetch different locations/cities.

* [System requirements](#system-requirements)
* [Features](#features)
* [Changelog](#changelog)
* [Installing](#installing)
* [Configuring project](#configuring-project)
* [References](#references)
* [License](#license)

## System requirements
* Unix-like OS
* Python  2.7.x
* Client libraries installes for:
  * OpenWeatherMap - [pyowm](https://github.com/csparpa/pyowm)
  * [Prometheus python client](https://github.com/prometheus/client_python)

## Features
- fetch data from [OpenWeatherMap-API](http://openweathermap.org/api) with configurable interval
- configuration file can have city names or long/lat
- data is exposed in [Prometheus](https://prometheus.io/) metrics format

## Installing
1. Clone the project. 
2. Install the required python libraries:
```shell
pip install prometheus_client PyYAML pyowm
```

## Configuring project
Copy 'weather.yml.dist' to 'weather.yml' - change the settings to your needs.

## References
* [OpenWeatherMap web API docs](http://openweathermap.org/api)
* [Prometheus](https://prometheus.io/)
* [Prometheus client libraries](https://prometheus.io/docs/instrumenting/clientlibs/)
* [pyowm - OpenWeatherMap API-Wrapper](https://github.com/csparpa/pyowm)

## License
[MIT License](https://github.com/lugark/openweathermap_prometheus_python/LICENSE)