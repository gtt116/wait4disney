"""
A history persistence service for disney. Currently only support file storage.
"""
import os
import logging
import json

from disney import config

log = logging.getLogger(__name__)

PATH = config.REPORT_PATH
YEAR_PATH = os.path.join(PATH, "year.json")
LATEST_PATH = os.path.join(PATH, "latest.json")


def _get_yearly():
    if not os.path.exists(YEAR_PATH):
        return []
    with open(YEAR_PATH, 'r') as y:
        try:
            return json.loads(y.read())
        except ValueError:
            return []


def _save_json(path, content):
    log.info("Write to file %s." % path)
    with open(path, 'w') as y:
        y.write(json.dumps(content))
        y.flush()


def get_latest_yearly():
    yearly = _get_yearly()
    if not yearly:
        return None
    else:
        return yearly[-1][0]


def update_yearly(date, new_value):
    yearly = _get_yearly()
    if not yearly:
        yearly.append([date, new_value])
    else:
        for i, y in enumerate(yearly):
            if date == y[0]:
                yearly[i] = [date, new_value]
                break
        else:
            yearly.append([date, new_value])
            yearly.sort()

    log.info("Update %s -> %s" %(date, new_value))
    _save_json(YEAR_PATH, yearly)


def update_daily(date, values):
    path = os.path.join(PATH, "%s.json" % date)
    _save_json(path, values)
    update_latest(values)


def update_latest(values):
    _save_json(LATEST_PATH, values)


if __name__ == '__main__':
    print(get_latest_yearly())
    update_yearly("2018-08-06T00:00:00Z", "13")
    update_yearly("2018-08-02T00:00:00Z", "13")
    update_yearly("2018-08-02T00:00:00Z", "19")
    update_daily("2019-03-02", {})
