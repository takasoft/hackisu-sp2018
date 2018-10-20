import pandas as pd

from influxdb import InfluxDBClient


def main():
    """Instantiate the connection to the InfluxDB client."""
    host = 'localhost'
    port = 8086
    user = 'root'
    password = 'root'
    dbname = 'test'
    # Temporarily avoid line protocol time conversion issues #412, #426, #431.
    protocol = 'json'

    client = InfluxDBClient(host, port, user, password, dbname)

    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2018-10-20T00:00:00Z",
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

    #print("Create database: " + dbname)
    #client.create_database(dbname)

    print("Write DataFrame")
    client.write_points(json_body)



if __name__ == '__main__':
    main()