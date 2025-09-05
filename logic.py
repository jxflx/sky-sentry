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
        if 244 <= windDirec <= 304:
            return 1  # oficina (este)
        elif 60 <= windDirec <= 120:
            return 2  # cuarto (oeste)
    return 0
