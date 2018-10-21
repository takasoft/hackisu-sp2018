import tensorflow as tf
from flask import Flask, request, jsonify
from keras.models import model_from_json

FLASK_HOST = '0.0.0.0'
FLASK_PORT = 6002
FLASK_DEBUG = False

app = Flask(__name__)
model = None
graph = None


def load_model():
    pass


@app.route('/predict', methods=['POST'])
def predict():
    data = {'success': False}

    if request.method == 'POST':
        if 'time' in request.args:
            pred_time = request.args['time']

            data['preds'] = 'unfocused'

            data['success'] = True

    return jsonify(data)


if __name__ == '__main__':
    print('loading model')
    load_model()
    print('starting server')
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
