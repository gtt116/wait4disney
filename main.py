import disney_api as api

import influxdb


def main():
    host = 'localhost'
    port = 8086
    user = 'root'
    password = 'root'
    dbname = 'disney'

    db = influxdb.InfluxDBClient(host, port, user, password, dbname)
    db.create_database(dbname)

    datapoints = []
    for a in api.attractions():
        datapoint = {
            "measurement": "wait_minutes",
            "tags": {
                "name": a.name,
            },
            "fields": {
                "value": a.wait_minutes,
            },
        }
        datapoints.append(datapoint)
        print datapoint

    print db.write_points(datapoints, database='disney', batch_size=50)


if __name__ == '__main__':
    main()
