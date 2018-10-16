import requests


def post_sensor_data(url, sensorId, value):
    try:
        r = requests.post(url, data={
            "sensorinfo": int(sensorId),
            "value": float(value)
        })
        print(r.status_code, r.reason)
    except requests.exceptions.ConnectionError:
        print("Cant connect...")
        return False


def get_sensor_indexes(url):
    try:
        sensor_indexes = {}
        response = requests.get(url)
        for x in response.json():
            sensor_indexes[x["address"]] = x["id"]
        return sensor_indexes
    except requests.exceptions.ConnectionError:
        print("Cant connect...")
        return False


def post_new_sensor(url, sensorId, location):
    try:
        print("-" * 30)
        print("-" * 30)
        # GET information about sensor types
        db_sensortypes = requests.get(url + "sensortypes/").json()
        print("ID", "\t", "type", "\t\t", "unit")
        for sensortype in db_sensortypes:
            print(sensortype['id'], '\t',
                  sensortype['sensortype'], '\t', sensortype['unit'])

        sensortypeId = input("Enter an ID for a sensor type: \n")
        print("-" * 30)
        # POST information about new sensor
        r = requests.post(url, data={
            "address": str(sensorId),
            "sensorlocation": int(location),
            "sensortype": int(sensortypeId)
        })
        print(r.status_code, r.reason)
    except requests.exceptions.ConnectionError:
        print("Cant connect...")


def create_new_sensor(url, sensorId):
    try:
        print("Creating new sensor with id:", sensorId)
        db_locations = requests.get(url + "locations/").json()
        print("-" * 30)
        print("-" * 30)
        print("ID", "\t", "Location Name")
        for location in db_locations:
            print(location['id'], '\t', location['location'])
        print("new", '\t', 'for new location')
        location = input("Enter an ID for a location: \n")

        if location == "new":
            location = input("Enter the name of the new sensor location: \n")
            # POST new sensor location
            r = requests.post(url + "locations/", data={
                "location": str(location)
            })
            location = r.json()["id"]
            post_new_sensor(url, sensorId, location)
        elif location.isdigit():
            post_new_sensor(url, sensorId, location)
        else:
            print("Something went wrong.")

    except requests.exceptions.ConnectionError:
        print("Cant connect...")
