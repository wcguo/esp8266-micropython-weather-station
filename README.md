# esp8266-micropython-weather-station

Little weather station build on micropython for esp8266.

Weather API used for this project is https://openweathermap.org/api.

## Getting Started

Setting up is simple, it is necessary to get ID of city you want to display weather data from.

Easiest way is to navigate to https://openweathermap.org/city, type in your city, select it and in address bar will be ID of that particular city.

You also need to register for API key to be able to use their service.

### Prerequisites

Some ESP board, ESP8266 or ESP32 it doesn't matter.

Openweathermap.org API key.

### Installing

In script you can define wifi name and password, city ID and API key.

## Running the tests

Script outputs current weather data or 5 day forecast for selected city.

To expand project I will add oled screen to display data.

## Built With

* [micropython](https://www.micropython.org/)

## Authors

* **Nenad Filipovic** - *Initial work* - [nenadfilipovic](https://github.com/nenadfilipovic)