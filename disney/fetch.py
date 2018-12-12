import logging

from disney.client import api
from disney.client import names
from disney import config

import influxdb

log = logging.getLogger(__name__)


def make_datas():
    datapoints = []
    for a in api.attractions():
        zh_name = names.translate(a.name)
        datapoint = {
            "measurement": "wait_minutes",
            "tags": {
                "name": a.name,
                "name_zh": zh_name,
            },
            "fields": {
                "value": a.wait_minutes,
            },
        }
        datapoints.append(datapoint)
        log.info("%s wait: %sm" % (zh_name, a.wait_minutes))

    return datapoints


def get_influxdb():
    db = influxdb.InfluxDBClient(config.INFLUXDB_HOST, config.INFLUXDB_PORT,
                                 config.INFLUXDB_USER, config.INFLUXDB_PASS,
                                 config.INFLUXDB_DB)
    db.create_database(config.INFLUXDB_DB)
    return db


def main():
    db = get_influxdb()
    datapoints = make_datas()
    assert db.write_points(datapoints, database='disney', batch_size=50)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        log.exception("exception")
