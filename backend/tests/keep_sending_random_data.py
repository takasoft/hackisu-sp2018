import requests
import random
from datetime import datetime, timezone
import time
import json


def gen_rand_data():
    return {
        'userID': 'steve',
        'time': datetime.now(timezone.utc).isoformat(),
        "raw": {
            "Q": random.uniform(0, 1682.815),
            "R": random.uniform(0, 1682.815),
            "S": random.uniform(0, 1682.815),
            "T": random.uniform(0, 1682.815)
        },
        "alpha": {
            "Q": random.uniform(0, 1682.815),
            "R": random.uniform(0, 1682.815),
            "S": random.uniform(0, 1682.815),
            "T": random.uniform(0, 1682.815)
        },
        "gamma": {
            "Q": random.uniform(0, 1682.815),
            "R": random.uniform(0, 1682.815),
            "S": random.uniform(0, 1682.815),
            "T": random.uniform(0, 1682.815)
        }
    }


while True:

    data = [gen_rand_data()]

    r = requests.post('http://localhost:5001/collect', data=json.dumps(data), headers={'content-type': 'application/json'})
    print(r)

    time.sleep(1)
