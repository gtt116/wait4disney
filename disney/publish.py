import logging
import sys
import json
from datetime import datetime
from datetime import timedelta

from disney import fetch
from disney import history
from disney.client import names as name_map

log = logging.getLogger(__name__)


def to_timestamp(time_str):
    d = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')
    return d.strftime('%s')


def format_date(dt):
    return dt.strftime('%Y-%m-%d')

def get_last_date():
    last = datetime.now() - timedelta(days=14)
    return last.strftime('%Y-%m-%d')

def year():
    db = fetch.get_influxdb()
    last = get_last_date()
    log.debug("Get data from %s." % last)

    result = db.query(
        """
        SELECT
        mean("value")
        FROM "wait_minutes"
        where time >= '%s' GROUP BY time(1d) fill(0);
        """ % last)

    # Since the max value of `mean` is about 27.9, so we set the max
    # of frontend graph to 30 is enough.
    log.debug("Generating points")
    datas = []
    for point in result.get_points():
        time = point['time']
        value = "%.2f" % point['mean']
        history.update_yearly(time, value )



def get_day_top(date=None, top=25):
    if date is None:
        date = datetime.now()
        date = date.replace(hour=0, minute=0, second=0, microsecond=0)

    db = fetch.get_influxdb()
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

    short_date = format_date(date)
    ret = {
        'date': short_date,
        'games': games,
        'max': max_values,
        'mean': mean_values
    }
    history.update_daily(short_date, ret)


def main():
    if len(sys.argv) != 2:
        print("Usage: %s <year|day>" % sys.argv[0])
        sys.exit(1)

    cmd = sys.argv[1]
    cmd_map = {
        'year': year,
        'day': get_day_top,
    }
    try:
        cmd_map[cmd]()
    except Exception:
        log.exception('calling %s failed' % cmd)
