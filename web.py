import logging
import sys
import json
from datetime import datetime
from datetime import timedelta

import main as backend
import names as name_map

logging.basicConfig(format='[%(asctime)s] ' + logging.BASIC_FORMAT)
logging.BASIC_FORMAT = "%(levelname)s:%(name)s:%(message)s"
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def to_timestamp(time_str):
    d = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')
    return d.strftime('%s')


def format_date(dt):
    return dt.strftime('%Y-%m-%d')


def year():
    log.debug("Get data from influxdb.")
    db = backend.get_influxdb()

    result = db.query(
        """
        SELECT
        sum("value")
        FROM "wait_minutes"
        where time >= '2016-09-07' GROUP BY time(1d) fill(0);
        """)

    top = 0

    log.debug("Find the top sum value.")
    for point in result.get_points():
        sum_value = point['sum']

        if sum_value > top:
            top = sum_value

    log.debug("Generating points.")
    datas = []
    for point in result.get_points():
        time = point['time']
        sum_value = point['sum']
        value = 1000 * sum_value / top
        datas.append([time, value])

    print json.dumps(datas)


def get_day_top(date=None, top=25):
    if date is None:
        date = datetime.now()
        date = date.replace(hour=0, minute=0, second=0, microsecond=0)

    db = backend.get_influxdb()
    start = date
    end = date + timedelta(days=1)
    iql = '''
        SELECT
            max("value") as max,
            mean("value") as mean
        FROM wait_minutes
        WHERE time >= '%(start)s' and time < '%(end)s'
        GROUP by "name"
        ''' % {'start': format_date(start), 'end': format_date(end)}
    result = db.query(iql)

    stats = []
    for item in result.items():
        name = name_map.translate(item[0][1]['name'])
        datas = next(item[1])
        mean = datas['mean']
        max_ = datas['max']
        stats.append([name, int(mean), int(max_)])

    # sort by mean number
    stats.sort(key=lambda x: x[2], reverse=True)
    stats = stats[:top]
    stats.reverse()

    games = []
    mean_values = []
    max_values = []

    for row in stats:
        games.append(row[0])
        mean_values.append(row[1])
        max_values.append(row[2])

    ret = {
        'date': format_date(date),
        'games': games,
        'max': max_values,
        'mean': mean_values
    }
    print json.dumps(ret)


def many_days():
    dt = datetime(2016, 9, 7)
    while dt <= datetime(2017, 3, 27):
        ret = get_day_top(dt)
        with file('%s.json' % dt.strftime('%Y-%m-%d'), 'w') as output:
            print output
            output.write(ret)
        dt += timedelta(days=1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: %s <year|day|many_days>" % sys.argv[0]
        sys.exit(1)

    cmd = sys.argv[1]
    cmd_map = {
        'year': year,
        'day': get_day_top,
        'many_days': many_days,
    }
    try:
        cmd_map[cmd]()
    except Exception:
        log.exception('calling %s failed' % cmd)
