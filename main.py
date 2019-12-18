import urequests


class WeatherStation:
    def __init__(self, city, api_key, api='https://api.openweathermap.org'):
        self.city = 'id=' + city
        self.api_key = '&appid=' + api_key
        self.api = api

    @staticmethod
    def use_wifi(network_name, network_pass):
        import network
        sta_if = network.WLAN(network.STA_IF)
        if not sta_if.isconnected():
            print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(network_name, network_pass)
            while not sta_if.isconnected():
                pass
        print('network config:', sta_if.ifconfig())

    def get_current_weather(self, network_name, network_pass):
        WeatherStation.use_wifi(network_name, network_pass)
        request_url = self.api + '/data/2.5/weather?' + self.city + self.api_key + '&units=metric'
        response = urequests.get(request_url)
        print("|City: ", response.json()['name'], '/', "Country: ", response.json()['sys']['country'])
        print("|Weather: ", response.json()['weather'][0]['main'], '-', response.json()['weather'][0]['description'])
        print("|Temperature: ", response.json()['main']['temp'], 'c')
        print("|Pressure: ", response.json()['main']['pressure'], 'hpa')
        print("|Humidity: ", response.json()['main']['humidity'], '%')
        print("|Wind speed: ", response.json()['wind']['speed'], 'm/s')

    def get_forecast(self, network_name, network_pass):
        WeatherStation.use_wifi(network_name, network_pass)
        request_url = self.api + '/data/2.5/forecast?' + self.city + '&cnt=7' + self.api_key + '&units=metric'
        response = urequests.get(request_url)
        print("|Weather for next 7 days:")
        print("|City: ", response.json()['city']['name'], '/', "Country: ", response.json()['city']['country'])
        for day in response.json()['list']:
            temperature = day['main']['temp']
            weather = day['weather'][0]['main'] + '-' + day['weather'][0]['description']
            min_temperature = day['main']['temp_min']
            max_temperature = day['main']['temp_max']
            pressure = day['main']['pressure']
            humidity = day['main']['humidity']
            wind = day['wind']['speed']
            print("Temperature: ", temperature, 'c', "Weather: ", weather, "Minimal temperature: ", min_temperature,
                  'c', "Maximal temperature: ", max_temperature, 'c', "Pressure: ", pressure, 'hpa', "Humidity: ",
                  humidity, '%', "Wind: ",
                  wind, 'm/s')


Test = WeatherStation('', '')  # City ID, API key
Test.get_current_weather('', '')  # Wifi credentials
Test.get_forecast('', '')  # Wifi credentials
