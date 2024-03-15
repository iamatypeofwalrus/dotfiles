# conda install pytz
import datetime

def join_array_for_query(arr):
  quoted_and_comma_array = [f'"{item}"' for item in arr]
  return ', '.join(quoted_and_comma_array)

def today():
  return datetime.date.today().strftime('%Y%m%d')

def yesterday():
  return (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')