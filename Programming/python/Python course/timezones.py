from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York')
tz_London = pytz.timezone('Europe/London')

datetime_NY = datetime.now(tz_NY)
datetime_London = datetime.now(tz_London)

print("NY time:", datetime_NY.strftime("%H:%M:%S"))
print("London time:", datetime_London.strftime("%H:%M:%S"))

print("This time:", datetime.now().hour)
print("NY time:", datetime.now(pytz.timezone('America/New_York')).hour)
print("London time:", datetime.now(pytz.timezone('Europe/London')).hour)
