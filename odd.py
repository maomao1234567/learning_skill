from datetime import datetime
import datetime as dt
import os
import sys

odds = [number for number in range(1, 60) if number % 2 != 0]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute seems a little odd")
else:
    print('Not an odd minute')

print(os.getcwd())
print(sys.platform)
print(sys.version)
print(os.getenv('HOME'))
print(dt.date.isoformat(dt.date.today()))
print(os.cpu_count())
