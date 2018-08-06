from disney.client import api
from disney.client import names

import influxdb


def make_datas():
    datapoints = []
    for a in api.attractions():
        datapoint = {
            "measurement": "wait_minutes",
            "tags": {
                "name": a.name,
                "name_zh": names.translate(a.name),
            },
            "fields": {
                "value": a.wait_minutes,
            },
        }
        datapoints.append(datapoint)
        print datapoint

    return datapoints


def get_influxdb():
    host = 'localhost'
    port = 8086
    user = 'root'
    password = 'root'
    dbname = 'disney'

    db = influxdb.InfluxDBClient(host, port, user, password, dbname)
    db.create_database(dbname)
    return db


def main():
    db = get_influxdb()
    datapoints = make_datas()
    assert db.write_points(datapoints, database='disney', batch_size=50)


if __name__ == '__main__':
    main()
