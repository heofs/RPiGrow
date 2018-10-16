import os

def get_ds18_sensors():
    sensorlist = ["123", '28-0416816c98ff', '28-041692e89dff', '28-0316013259ff']
    return sensorlist

def get_temp(sensor):
    base_dir = '/sys/bus/w1/devices/'
    filename = sensor + '/w1_slave'
    file_location = base_dir + filename

    try:
        with open(file_location, 'r') as f:
            lines = f.readlines()

    except FileNotFoundError:
        return 0.2
        return 'Error'

    words = lines[1].split()
    temp = int(words[-1].replace('t=', ''))
    return "{0:.1f}".format(temp/1000)

def get_humidity(sensor):
    pass