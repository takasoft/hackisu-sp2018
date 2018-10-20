import flask
from flask import request, Flask

app = Flask(__name__)


@app.route('/collect', methods=['POST'])
def collect():
    data = {'success': False}

    if request.method == 'POST':
        if request.args:
            print(request.args)

            data['success'] = True

    return flask.jsonify(data)


if __name__ == '__main__':
    print('starting server')
    app.run(host="0.0.0.0", port=6001)
