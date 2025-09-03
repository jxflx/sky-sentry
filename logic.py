from datetime import datetime

def imAwake():
    now = datetime.now().hour
    return not (24 <= now or now < 7)

def itsRaining(res):
    return res["precipitationProbability"] >= 50

def rainDirection(res):
    windDirec = res["windDirection"]

    if itsRaining(res):
        if 244 <= windDirec <= 304:
            return 1  # cuarto (oeste)
        elif 60 <= windDirec <= 120:
            return 2  # oficina (este)
    return 0
