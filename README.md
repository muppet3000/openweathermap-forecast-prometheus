# openweathermap_prometheus_python
![GitHub](https://img.shields.io/github/license/muppet3000/openweathermap-forecast-prometheus.svg)
![Travis (.org)](https://img.shields.io/travis/muppet3000/openweathermap-forecast-prometheus.svg)
<br>
Forked from https://github.com/lugark/openweathermap_prometheus_python (2021-06)

An open source python script to fetch weather data OpenWeatherMap and expose it in a Prometheus format.
It can be configured using a YAML file to fetch different locations/cities.

* [System requirements](#system-requirements)
* [Features](#features)
* [Changelog](#changelog)
* [Installing](#installing)
* [Configuring project](#configuring-project)
* [References](#references)
* [License](#license)

## Goal
The eventual goal of this repository is to produce a 10-day forecast for each of the locations and export it via a prometheus endpoint.
The original repository by lugark provides an excellent framework, but doesn't export the required data via prometheus

## System requirements
* Unix-like OS
* Python  3.7.x
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
pip install -r requirements.txt
```

## Configuring project
Copy 'weather.yml.dist' to 'weather.yml' - change the settings to your needs.

## References
* [OpenWeatherMap web API docs](http://openweathermap.org/api)
* [Prometheus](https://prometheus.io/)
* [Prometheus client libraries](https://prometheus.io/docs/instrumenting/clientlibs/)
* [pyowm - OpenWeatherMap API-Wrapper](https://github.com/csparpa/pyowm)

## License
[MIT License](https://github.com/muppet3000/openweathermap-forecast-prometheus/LICENSE)
