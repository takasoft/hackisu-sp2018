from flask import request, Flask, jsonify
from influxdb import InfluxDBClient
import json


DB_NAME = 'eeg_test'
DB_HOST = 'localhost'
DB_PORT = 8086

FLASK_HOST = '127.0.0.1'
FLASK_PORT = 5001
FLASK_DEBUG = True


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

                data = []
                for i in range(len(raw_data)):
                    data.append({
                        'measurement': 'data',
                        'tags': {
                            'userID': raw_data[i]['userID']
                        },
                        'time': raw_data[i]['time'],
                        'fields': {
                            'Q': raw_data[i]['Q'],
                            'R': raw_data[i]['R'],
                            'S': raw_data[i]['S'],
                            'T': raw_data[i]['T'],
                        }
                    })

                # print(data)

                client.write_points(data)

                res['success'] = True
            except Exception as e:
                print('error')
                print(e)

    return jsonify(res)


if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
