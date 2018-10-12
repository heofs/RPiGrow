import requests
import time
from sensor import get_temp

settings = {
    "url": "http://192.168.1.40:80/envlog/temp/",
    "interval": 180
}
sensors = {
    "28-0416816c98ff": "reservoir",
    "28-041692e89dff": "inside_tent",
    "28-0316013259ff": "outside_tent",
}

def post_value(sensorid, location, value):
    r = requests.post(settings["url"], data={
        "sensor": str(sensorid),
        "location": str(location),
        "value": float(value)
    })
    print(r.status_code, r.reason)


while True:
    for key in sensors:
        temp = get_temp(key)
        post_value(key, sensors[key], temp)

    time.sleep(30)
