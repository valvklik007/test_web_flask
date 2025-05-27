import requests

class WeatherService:
    def __init__(self):
        self.__api_key = '68bc42d3015f4b6c86c112103251003'
        self.__url = f'http://api.weatherapi.com/v1/forecast.json?key={self.__api_key}'

    def getOneDayForecast(self, city:str):
        #Вернуть погоду
        params = {
            'q': city,
            'days': 1,
            'aqi': 'no',
            'alerts': 'no'
        }

        try:
            response = requests.get(self.__url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error API {e}")
            return None

