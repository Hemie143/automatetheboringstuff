import datetime
import time

print(datetime.datetime.now())
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
print(dt.year, dt.month, dt.day)        # (2019, 10, 21)
print(dt.hour, dt.minute, dt.second)    # (16, 29, 0)

print(datetime.datetime.fromtimestamp(1000000))
print(datetime.datetime.fromtimestamp(time.time()))

halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
print(halloween2019 == oct31_2019)
print(halloween2019 > newyears2020)
print(newyears2020 > halloween2019)
print(newyears2020 != oct31_2019)

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)        # (11, 36548, 0)
print(delta.total_seconds())                                # 986948.0
print(str(delta))                                           #  '11 days, 10:09:08'

dt = datetime.datetime.now()
print(dt)
thousandDays = datetime.timedelta(days=1000)
print(dt + thousandDays)

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
print(oct21st)                                              # datetime.datetime(2019, 10, 21, 16, 29)
print(oct21st - aboutThirtyYears)                           # datetime.datetime(1989, 10, 28, 16, 29)
print(oct21st - (2 * aboutThirtyYears))                     # datetime.datetime(1959, 11, 5, 16, 29)

halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
