from influxdb import InfluxDBClient
import random
import datetime
import time


def gen_rand_eeg():
    return {
        "Q": random.uniform(0, 1682.815),
        "R": random.uniform(0, 1682.815),
        "S": random.uniform(0, 1682.815),
        "T": random.uniform(0, 1682.815)
    }


def gen_rand_data():
    return {
        'measurement': 'data',
        'tags': {
            'userID': 'steve'
        },
        'time': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'fields': gen_rand_eeg()
    }


client = InfluxDBClient(host='localhost', port=8086)
client.create_database('eeg_test')
client.get_list_database()
client.switch_database('eeg_test')

while True:

    data = [gen_rand_data()]

    client.write_points(data)

    time.sleep(1)
