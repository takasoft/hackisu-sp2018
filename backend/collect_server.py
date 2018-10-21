from flask import request, Flask, jsonify
from influxdb import InfluxDBClient
import json


DB_NAME = 'eeg'
DB_HOST = 'localhost'
DB_PORT = 8086

FLASK_HOST = '0.0.0.0'
FLASK_PORT = 6001
FLASK_DEBUG = False


client = InfluxDBClient(host=DB_HOST, port=DB_PORT)
client.create_database(DB_NAME)
client.get_list_database()
client.switch_database(DB_NAME)

app = Flask(__name__)


@app.route('/collect', methods=['POST'])
def collect():
    res = {'success': False}

    if request.method == 'POST':
        if request.data:
            try:
                raw_data = request.data
                raw_data = raw_data.decode('UTF-8')
                raw_data = json.loads(raw_data)

                print(raw_data)

                data = []
                for i in range(len(raw_data)):
                    data.append({
                        'measurement': 'raw',
                        'tags': {
                            'userID': raw_data[i]['userID'],
                            'train': raw_data[i]['train'],
                            'activity': raw_data[i]['activity']
                        },
                        'time': raw_data[i]['time'],
                        'fields': {
                            'Q': float(raw_data[i]['raw']['Q']),
                            'R': float(raw_data[i]['raw']['R']),
                            'S': float(raw_data[i]['raw']['S']),
                            'T': float(raw_data[i]['raw']['T'])
                        }
                    })
                    data.append({
                        'measurement': 'alpha',
                        'tags': {
                            'userID': raw_data[i]['userID'],
                            'train': raw_data[i]['train'],
                            'activity': raw_data[i]['activity']
                        },
                        'time': raw_data[i]['time'],
                        'fields': {
                            'Q': float(raw_data[i]['alpha']['Q']),
                            'R': float(raw_data[i]['alpha']['R']),
                            'S': float(raw_data[i]['alpha']['S']),
                            'T': float(raw_data[i]['alpha']['T'])
                        }
                    })
                    data.append({
                        'measurement': 'gamma',
                        'tags': {
                            'userID': raw_data[i]['userID'],
                            'train': raw_data[i]['train'],
                            'activity': raw_data[i]['activity']
                        },
                        'time': raw_data[i]['time'],
                        'fields': {
                            'Q': float(raw_data[i]['gamma']['Q']),
                            'R': float(raw_data[i]['gamma']['R']),
                            'S': float(raw_data[i]['gamma']['S']),
                            'T': float(raw_data[i]['gamma']['T'])
                        }
                    })

                print(data)

                client.write_points(data)

                res['success'] = True
            except Exception as e:
                print('error')
                print(e)

    return jsonify(res)


if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
