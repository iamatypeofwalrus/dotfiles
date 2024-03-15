# conda install pytz
import datetime
import pandas as pd
import pytz

def parse_time(dt_str):
    # Separate the datetime string and the timezone part
    dt_naive_str, tz_str = dt_str[:-4], dt_str[-3:]
    
    # Parse the naive datetime string
    dt_naive = pd.to_datetime(dt_naive_str)

    # Timezone mappings for US timezones
    timezone_map = {
        'EST': 'America/New_York',
        'EDT': 'America/New_York',
        'CST': 'America/Chicago',
        'CDT': 'America/Chicago',
        'MST': 'America/Denver',
        'MDT': 'America/Denver',
        'PST': 'America/Los_Angeles',
        'PDT': 'America/Los_Angeles'
    }

    # Get the appropriate timezone from the map
    if tz_str in timezone_map:
        tz = pytz.timezone(timezone_map[tz_str])
        dt_aware = tz.localize(dt_naive)
    else:
        # Handle unexpected timezone
        raise ValueError(f"Unexpected timezone in {dt_str}")

    return dt_aware

def join_array_for_query(arr):
  quoted_and_comma_array = [f'"{item}"' for item in arr]
  return ', '.join(quoted_and_comma_array)

def today():
  return datetime.date.today().strftime('%Y%m%d')

def yesterday():
  return (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')