import logging, requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('rain.log')]
)

def log(msg):
    logging.info(msg)

def notify(title, message):
    requests.post("https://ntfy.sh/weatherAPI1554", data=message, headers={"Title": title})
