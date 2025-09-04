import requests
from config import API_KEY, LAT, LON, WEATHER_CODE, DANGEROUS_CODES
from notifier import log, notify

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
    now = datetime.now()
    if(now.hour == 7) and (5 >= now.minute >= 0):
        url = "https://api.tomorrow.io/v4/weather/forecast"
        params = {"location": f"{LAT},{LON}", "timesteps": "1h", "units": "metric", "apikey": API_KEY}

        resDay = requests.get(url, params=params, timeout=10).json()
        forecastList = resDay["timelines"]["hourly"]
        dayForecastList = forecastList[:16]

        forecastTimeline = []

        for h in dayForecastList:
            weathertmp = h["values"]["weatherCode"]
            timetmp = datetime.fromisoformat(h["values"]["time"].replace("Z", "+00:00")).astimezone().hour

            if(weathertmp in DANGEROUS_CODES):
                forecastTimeline.append(timetmp)


        rainIntervals = []

        if forecastTimeline:
            inicio = forecastTimeline[0]
            prev = inicio

            for hora in forecastTimeline[1:]:
                if hora == prev + 1:
                    prev = hora
                else:  
                    rainIntervals.append([inicio, prev])
                    inicio = hora
                    prev = hora

            rainIntervals.append([inicio, prev])


        stringReport = "Hola! El clima de hoy será: "

        if rainIntervals:
            stringReport += "Lluvia a las: "
            for i in rainIntervals:
                stringReport += f"{i[0]} a las {i[1]} horas, "
        else:
            stringReport += " Sin precipitaciones fuertes notables"
        
        log(stringReport)
        notify("Reporte del Dia", stringReport)


            


            

