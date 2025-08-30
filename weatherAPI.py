import requests
import time
from datetime import datetime, timedelta, timezone
import logging

# Solo archivo, sin consola
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rain.log')    # Solo archivo
    ]
)

API_KEY = "PJ1RA0FcwljEU01k1p9VOw1EjANJsqWe"
LAT, LON = 19.66265483919165, -99.15539969407077
SLEEP_INTERVAL = 300

def imAwake():
    now = datetime.now().hour
    if 23 <= now or now < 7:
        return False
    else:
        return True

def itsRaining(res):
    rainProbab = res["precipitationProbability"]

    if(rainProbab >= 50):
        return True
    else:
        return False

def rainDirection(res):
    # return 1 for east, 2 for west and 0 for none or other direction
    windDirec = res["windDirection"]

    if(itsRaining(res)):
        if(windDirec >= 244 and windDirec <=304):
            return 1
        elif(windDirec >= 60 and windDirec <=120):
            return 2
    else:
        return 0

while(1):
    if(imAwake() == True):
        try:
            # Pulls realtime weather conditions from API
            url = "https://api.tomorrow.io/v4/weather/realtime"

            params = {
                "location": f"{LAT},{LON}",
                "units": "metric",
                "apikey": API_KEY
            }

            responseRealTime = requests.get(url, params=params, timeout=10)
            responseRealTime.raise_for_status()
            dataRealTime = responseRealTime.json()


            if(itsRaining(dataRealTime["data"]["values"]) and rainDirection(dataRealTime["data"]["values"]) == 0):
                logging.info("Ya esta lloviendo :))")
            else:
                url = "https://api.tomorrow.io/v4/weather/forecast"

                params = {
                    "location": f"{LAT},{LON}",
                    "timesteps": "1m",
                    "units": "metric",
                    "apikey": API_KEY
                }

                responseForecast = requests.get(url, params=params, timeout=10)
                responseForecast.raise_for_status()
                dataForecast = responseForecast.json()

                # revisar ventana del este y oeste
                if(rainDirection(dataForecast["timelines"]["minutely"][5]["values"]) == 1):
                    logging.info("llueve a tu cuarto")
                    requests.post("https://ntfy.sh/weatherAPI1554",
                    data="Cierra la ventana de tu cuarto!",
                    headers={ "Title": "Lluvia en 5 minutos o menos!" })
                elif(rainDirection(dataForecast["timelines"]["minutely"][5]["values"]) == 2):
                    logging.info("llueve a la ventana de la oficina")
                    requests.post("https://ntfy.sh/weatherAPI1554",
                    data="Cierra la ventana de la oficina!",
                    headers={ "Title": "Lluvia en 5 minutos o menos!" })
                else:
                    logging.info("NO hagas nada")
                    
        except Exception as e:
            logging.error(f"Error: {e}")
    else:
        logging.info("Estoy dormido :)")
    
    time.sleep(SLEEP_INTERVAL)