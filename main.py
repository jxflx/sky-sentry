import time
from config import SLEEP_INTERVAL
from weather_api import get_realtime, get_forecast
from logic import itsRaining, rainDirection
from notifier import log, notify

def imAwake():
    from datetime import datetime
    now = datetime.now().hour
    return not (23 <= now or now < 7)

while True:
    if imAwake():
        try:
            realtime = get_realtime()
            values = realtime["data"]["values"]

            if itsRaining(values) and rainDirection(values) == 0:
                log("Ya está lloviendo pero no afecta a las ventanas :)")
            else:
                forecast = get_forecast()
                values5 = forecast["timelines"]["minutely"][5]["values"]

                direction = rainDirection(values5)
                if direction == 1:
                    log("Lluvia en el cuarto (oeste)")
                    notify("Lluvia en 5 min", "Cierra la ventana del cuarto!")
                elif direction == 2:
                    log("Lluvia en la oficina (este)")
                    notify("Lluvia en 5 min", "Cierra la ventana de la oficina!")
                else:
                    log("No hacer nada")

        except Exception as e:
            log(f"Error: {e}")
    else:
        log("Estoy dormido :)")

    time.sleep(SLEEP_INTERVAL)
