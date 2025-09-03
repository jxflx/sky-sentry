from datetime import datetime

def imAwake():
    now = datetime.now().hour
    return not (23 <= now or now < 7)

def itsRaining(res):
    return res["precipitationProbability"] >= 50

def rainDirection(res):
    windDirec = res["windDirection"]

    if itsRaining(res):
        if 244 <= windDirec <= 304:
            return 1  # oficina (este)
        elif 60 <= windDirec <= 120:
            return 2  # cuarto (oeste)
    return 0
