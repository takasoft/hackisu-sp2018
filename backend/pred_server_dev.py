import json

import tensorflow as tf
from flask import Flask, request, jsonify
from keras.models import model_from_json

FLASK_HOST = '127.0.0.1'
FLASK_PORT = 5000
FLASK_DEBUG = True

app = Flask(__name__)
model = None
graph = None


def load_model():
    global model
    # load json and create model
    with open('model.json', 'r') as f:
        loaded_model_json = f.read()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("model.h5")
    print("Loaded model from disk")

    # evaluate loaded model on test data
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    global graph
    graph = tf.get_default_graph()


@app.route('/predict', methods=['POST'])
def predict():
    data = {'success': False}

    if request.method == 'POST':
        if request.data:
            raw_data = request.data
            raw_data = raw_data.decode('UTF-8')
            raw_data = json.loads(raw_data)

            print(raw_data)

            with graph.as_default():
                preds = model.evaluate(pred_time, verbose=0)
            data['preds'] = preds

            data['success'] = True

    return jsonify(data)


if __name__ == '__main__':
    print('loading model')
    load_model()
    print('starting server')
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)
