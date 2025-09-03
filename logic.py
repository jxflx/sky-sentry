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
        if 214 <= windDirec <= 334:
            return 1  # cuarto (este)
        elif 30 <= windDirec <= 150:
            return 2  # oficina (oeste)
    return 0
