import requests
from config import API_KEY, LAT, LON

def get_realtime():
    url = "https://api.tomorrow.io/v4/weather/realtime"
    params = {"location": f"{LAT},{LON}", "units": "metric", "apikey": API_KEY}
    return requests.get(url, params=params, timeout=10).json()

def get_forecast():
    url = "https://api.tomorrow.io/v4/weather/forecast"
    params = {"location": f"{LAT},{LON}", "timesteps": "1m", "units": "metric", "apikey": API_KEY}
    return requests.get(url, params=params, timeout=10).json()



def dayWrap():
    from datetime import datetime
    now = datetime.now().hour
    if(now == 7):
        url = "https://api.tomorrow.io/v4/weather/forecast"
        params = {"location": f"{LAT},{LON}", "timesteps": "1h", "units": "metric", "apikey": API_KEY}

        resDay = requests.get(url, params=params, timeout=10).json()
        forecastList = resDay["timelines"]["hourly"]
        dayForecastList = forecastList[:17]
        #for h in dayForecastList:

