import requests

settings = {
    "api": {
        "url": "http://192.168.1.40:80/envlog/temp/"
    },
    "hardware": {
        "interval": 180
    }
}


def post_value(url, sensorid, value):
    r = requests.post(url, data={
        "sensorinfo": int(sensorid),
        "value": float(value)
    })
    print(r.status_code, r.reason)


# print(settings["api"]["url"])


def get_sensor_indexes(url):
    sensor_indexes = {}
    response = requests.get(url)
    for x in response.json():
        sensor_indexes[x["address"]] = x["id"]
    return sensor_indexes
