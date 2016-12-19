from datetime import datetime
import collections
import json

import main as backend


def to_timestamp(time_str):
    d = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')
    return d.strftime('%s')


def main():
    db = backend.get_influxdb()

    result = db.query("""SELECT sum("value") FROM "wait_minutes" where time >= '2016-09-07T00:00:00Z' GROUP BY time(1d) fill(null);""")

    payload = collections.OrderedDict()

    top = 0

    # find the top sum value
    for point in result.get_points():
        sum_value = point['sum']

        if sum_value > top:
            top = sum_value

    for point in result.get_points():
        time = to_timestamp(point['time'])
        sum_value = point['sum']
        payload[time] = 100 * sum_value / top

    print json.dumps(payload, indent=2)


if __name__ == '__main__':
    main()
