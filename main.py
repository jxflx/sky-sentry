import time
from config import SLEEP_INTERVAL
from weather_api import get_forecast, dayWrap
from logic import rainDirection, imAwake
from notifier import log, notify

while True:
    if imAwake():
        try:
            dayWrap()

            forecast = get_forecast()
            dataCurrent = forecast["timelines"]["minutely"][0]["values"]
            data5Min = forecast["timelines"]["minutely"][6]["values"]

            if(rainDirection(data5Min) and rainDirection(dataCurrent)):
                log("Ya esta lloviendo y hacia alguna ventana")
            elif(rainDirection(data5Min) == 1):
                log("lluvia este")
                notify("Lluvia al este en 5 minutos!", "Cierra las ventanas de la oficina y el balcon!")
            elif(rainDirection(data5Min) == 2):
                log("lluvia oeste")
                notify("Lluvia al oeste en 5 minutos!", "Cierra las ventanas de uriel y de tu cuarto!")
            else:
                log("NO hagas nada :))")
        except Exception as e:
            log(f"Error: {e}")
    else:
        log("Estoy dormido :)")

    time.sleep(SLEEP_INTERVAL)
