import time
from sensor_functions import get_temp, get_ds18_sensors
from API_functions import post_sensor_data, get_sensor_indexes, create_new_sensor

settings = {
    "api": {
        "sensors_url": "http://192.168.1.39:8000/sensors/",
        "readings_url": "http://192.168.1.39:8000/sensors/reading/"
    },
    "interval": 180
}

sensor_indexes = get_sensor_indexes(settings["api"]["sensors_url"])
active_sensors = get_ds18_sensors()

# Check if active sensor is in database, if not, add it.
def match_sensor_index():
    for sensor in active_sensors:
        if sensor not in sensor_indexes.keys():
            print(sensor, 'is not in database.')
            create_new_sensor(settings["api"]["sensors_url"], sensor)

if active_sensors:
    match_sensor_index()

# Loop continuosly read data from sensors.
while True:
    try:
        for sensor in active_sensors:
            sensor_index = sensor_indexes[sensor]
            sensor_value = get_temp(sensor)

            post_sensor_data(
                settings["api"]["readings_url"], sensor_index, sensor_value)

    except KeyboardInterrupt:
        pass

    if not active_sensors:
        input("No sensors detected, plug in sensor and press ENTER")
        active_sensors = get_ds18_sensors()

    if active_sensors:
        time.sleep(settings["interval"])
