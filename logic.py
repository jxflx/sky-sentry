from datetime import datetime
from config import DANGEROUS_CODES

def imAwake():
    now = datetime.now().hour
    return not (23 <= now or now < 7)

def dangerousPrecipitation(res):
    return str(res["weatherCode"]) in DANGEROUS_CODES

def rainDirection(res):
    windDirec = res["windDirection"]

    if dangerousPrecipitation(res):
        # Mantener la orientación de comentarios tal como vienen del API
        if 244 <= windDirec <= 304:
            return 1  # oficina (este)
        elif 60 <= windDirec <= 120:
            return 2  # cuarto (oeste)
        elif windDirec >= 330 or windDirec <= 30:
            return 3  # norte
        elif 150 <= windDirec <= 210:
            return 4  # sur
    return 0
