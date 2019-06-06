import requests
import time
import logging

LOG = logging.getLogger(__file__)

class Attraction(object):

    def __init__(self, json_obj):
        self._json_obj = json_obj

        wait_time_obj = json_obj['waitTime']
        # [Closed, Operating, SeeTimesGuide, Down]
        self.status = wait_time_obj['status']

        self._wait_minutes = wait_time_obj.get('postedWaitMinutes', 0)

        self._fastpass_available = wait_time_obj['fastPass']['available']
        self._fastpass_start_time = wait_time_obj['fastPass'].get('startTime')
        self._fastpass_end_time = wait_time_obj['fastPass'].get('endTime')

        self.single_rider = wait_time_obj['singleRider']
        self.id = json_obj['id']

        # eg:
        # 1882;entityType=Attraction;destination=shdr
        # attAliceWonderlandMaze;entityType=Attraction;destination=shdr
        self.name = self.id.split(';', 1)[0].replace('att', '')

    def can_fastpass(self):
        if self._fastpass_available and self._fastpass_start_time != 'FASTPASSisNotAvailable':
            return True
        else:
            return False

    @property
    def wait_minutes(self):
        if self.status == 'Closed':
            return 0
        else:
            return self._wait_minutes

    def __repr__(self):
        return '%s - %s, %s' % (self.name, self.status, self.wait_minutes)


def get_token():
    headers = {
        'Host': 'authorization.shanghaidisneyresort.com',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'X-NewRelic-ID': 'Uw4BWVZSGwICU1VRAgkH',
        'X-Conversation-Id': 'shdrA5320488-E03F-4795-A818-286C658EEBB6',
        'Accept': 'application/json',
        'User-Agent': 'SHDR/4.1.1 (iPhone; iOS 9.3.5; Scale/2.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
    }

    data = 'assertion_type=public&client_id=DPRD-SHDR.MOBILE.IOS-PROD&client_secret=&grant_type=assertion'

    resp = requests.post('https://authorization.shanghaidisneyresort.com/curoauth/v1/token',
                         headers=headers, data=data)
    resp.raise_for_status()
    token = resp.json()['access_token']
    return token


def get_wait_time(token):
    """
    The item in entries schema:

        {
            u'waitTime': {
                u'status': u'Down',  # or u'Operating'
                u'postedWaitMinutes': 5,
                u'fastPass': {
                    u'available': True,
                    u'endTime': u'13: 45: 00',
                    u'startTime': u'12: 45: 00'
                },
                u'singleRider': True
            },
            u'id': u'attTronLightcyclePowerRun;entityType=Attraction;destination=shdr'
        },
    """
    headers = {
        'Host': 'apim.shanghaidisneyresort.com',
        'X-Conversation-Id': 'shdrA5320488-E03F-4795-A818-286C658EEBB6',
        'Accept': '*/*',
        'User-Agent': 'SHDR/4.1.1 (iPhone; iOS 9.3.5; Scale/2.00)',
        'Accept-Language': 'zh-cn',
        'Authorization': 'BEARER %s' % token,
    }

    resp = requests.get('https://apim.shanghaidisneyresort.com/facility-service/theme-parks/desShanghaiDisneyland;'
                        'entityType=theme-park;destination=shdr/wait-times?mobile=true&region=&region=CN',
                        headers=headers,
                        verify=False,
                        timeout=10)
    resp.raise_for_status()
    return resp.json()


def get_wait_time_list():
    for _ in xrange(3):
        try:
            token = get_token()
            response = get_wait_time(token)
        except (requests.HTTPError, requests.ConnectionError) as ex:
            LOG.error("Make request failed: %s, wait 1 second to retry." % ex)
            time.sleep(1)
        else:
            return response


def attractions():
    items = []
    raw_json = get_wait_time_list()
    LOG.debug(raw_json)
    for entity_json in raw_json['entries']:
        items.append(Attraction(entity_json))

    return items

