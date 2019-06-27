import time
import requests
import json
from datetime import datetime, timedelta
import tzlocal

_FORMAT = '%I:%M:%S %p'
_URL = 'https://api.sunrise-sunset.org/json?lat=52.150492&lng=-0.545676&date={}'


def _get_json(request):
    response = requests.get(request)
    parsed = json.loads(response.text)['results']
    return [parsed['civil_twilight_begin'], parsed['civil_twilight_end'], parsed['sunrise'], parsed['sunset']]


def get_curfew():
    today = datetime.today()
    dates = _get_json(_URL.format(today.isoformat()))

    localtime = time.localtime()
    
    hours_offset = 0
    if localtime.tm_isdst == 1:
        hours_offset = 1
    delta = timedelta(hours = hours_offset)

    print(delta)
    
    lock = datetime.strptime(dates[3], _FORMAT)
    unlock = datetime.strptime(dates[2], _FORMAT)
    lock = lock + delta
    unlock = unlock + delta

    print(lock)
    print(unlock)

    return lock, unlock
