import os


def get_ds18_sensors():
    devices_dir = "/sys/bus/w1/devices/"

    try:
        if(not os.path.exists(devices_dir)):
            print('w1 folder not found.\nRunning modprobe commands..')
            os.system('sudo modprobe w1-gpio')
            os.system('sudo modprobe w1-therm')
            time.sleep(2)

    except FileNotFoundError:
        print('Folders not found.. Something went wrong.')
        return False

    sensor_list = []
    for filename in os.listdir(devices_dir):
        if os.path.isfile(devices_dir + filename + '/w1_slave'):
            with open(devices_dir + filename + '/w1_slave', 'r') as f:
                lines = f.readlines()
            words = lines[1].split()
            if ((words[-1][:2] == 't=')):
                print('Detected sensor: ' + filename)
                sensor_list.append(filename)

    if not sensor_list:
        print("Found not sensors.")

    return sensor_list


def get_temp(sensor):
    devices_dir = '/sys/bus/w1/devices/'
    filename = sensor + '/w1_slave'
    file_location = devices_dir + filename

    try:
        with open(file_location, 'r') as f:
            lines = f.readlines()

    except FileNotFoundError:
        return 'Error'

    words = lines[1].split()
    temp = int(words[-1].replace('t=', ''))
    return "{0:.1f}".format(temp/1000)


def get_humidity(sensor):
    pass
