from pytz import all_timezones, timezone
from datetime import datetime

#datum = datetime.strptime('2019-10-30T16:41:24+0200', "%Y-%m-%dT%H:%M:%S%z")
datum = datetime.strptime('2019-10-30T16:41:24Z', "%Y-%m-%dT%H:%M:%S%z")
print(datum)
now_pacific = datum.astimezone(timezone('Europe/Amsterdam'))
print(now_pacific)
datum_string = '2019-10-30T16:41:24Z'

print(datetime.strptime(datum_string,"%Y-%m-%dT%H:%M:%S%z").astimezone(timezone('Europe/Amsterdam')))