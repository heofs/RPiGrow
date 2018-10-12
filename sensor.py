import os


def get_temp(sensor):
    base_dir = '/sys/bus/w1/devices/'
    filename = sensor + '/w1_slave'
    file_location = base_dir + filename

    try:
        with open(file_location, 'r') as f:
            lines = f.readlines()

    except FileNotFoundError:
        return 'Error'

    words = lines[1].split()
    temp = int(words[-1].replace('t=', ''))
    return "{0:.1f}".format(temp/1000)
