import requests
import time
from sensor_functions import get_temp, get_ds18_sensors
from API_functions import post_value, get_sensor_indexes

settings = {
    "api": {
        "sensors_url": "http://192.168.1.39:8000/sensors/",
        "readings_url": "http://192.168.1.39:8000/sensors/reading/"
    },
    "interval": 180
}

sensor_indexes = get_sensor_indexes(settings["api"]["sensors_url"])
active_sensors = get_ds18_sensors()
# print(sensor_indexes.keys())
# print(active_sensors)
for sensor in active_sensors:
    if sensor not in sensor_indexes.keys():
        print(sensor, 'is not in database.')
        print(sensor)

# while True:
#     sensor_readings = {}
#     try:
#         for sensor in active_sensors:
#             sensor_index = sensor_indexes[sensor]
#             sensor_value = get_temp(sensor)

#             post_value(settings["api"]["readings_url"], sensor_index, sensor_value)
#     except KeyboardInterrupt:
#         pass
#         # print("Keyboard interrupt")
#     # time.sleep(settings["interval"])

#     break