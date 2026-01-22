'''
import datetime
now=datetime.datetime.now()
print("Current date and time:",now)

from datetime import date,time,datetime
today=date.today()
print("Today's date:",today)
print("Current year:",today.year)
print("current month",today.month)
print("current day",today.day)
print("current weekday:",today.weekday())
print("current is iso weekday:",today.isoweekday())
print("current iso format:",today.isoformat())

'''
'''
from datetime import date,time,datetime
now=datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.timetuple())
print(now.isoformat())
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%I:%M :%S %p"))
print(now.strftime("%A, %b, %d, %Y"))
print(now.strftime("%I:%M:%S %p"))

'''


from datetime import date,time,datetime,timedelta
now=datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.timetuple())
print(now.isoformat())
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%I:%M :%S %p"))
print(now.strftime("%A, %b, %d, %Y"))
print(now.strftime("%I:%M:%S %p"))


from datetime import date,time,datetime,timedelta

today=date.today()
now=datetime.now()
n=now+timedelta(days=5)
m=now-timedelta(days=5)
a=now+timedelta(hours=5)
b=now-timedelta(hours=5)
print("Today's date:",today)
print("Current date and time:",now)
print("Date and time after 5 days:",n)
print("Date and time before 5 days:",m)
print("Date and time after 5 hours:",a)
print("Date and time before 5 hours:",b)

import platform
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.machine())
print(platform.processor())
