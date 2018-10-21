from influxdb import InfluxDBClient
from datetime import datetime, timezone


DB_NAME = 'eeg'
DB_HOST = 'localhost'
DB_PORT = 8086


client = InfluxDBClient(host=DB_HOST, port=DB_PORT)
client.create_database(DB_NAME)
client.get_list_database()
client.switch_database(DB_NAME)

data = []
with open('ASR_Sources/Data_F_Ind0001.txt') as f:
    data = f.read()

data = data.split('\n')
for i in range(len(data)):
    data[i] = data[i].replace(' ', '')
    data[i] = data[i].split(',')
    if len(data[i]) == 2:
        data[i] = (float(data[i][0]), float(data[i][1]))
        data[i] = {
            'measurement': 'data',
            'time': data[i][],
            'fields': {
                'x': data[i][0],
                'y': data[i][1]
            }
        }

# print(data)

client.write_points(data)
