import math
import datetime
import calendar
print(math.ceil(2.3))
print(math.floor(2.3))
l=[1,2,4,5,1]
print(math.fsum([1,2,3,4]))
print(math.fsum(l))


print(math.gcd(1,3,2,6))
print(math.floor(math.sqrt(81)))

print(math.exp(2))
print(math.expm1(2))
print(math.log2(100))
print(math.pow(2,4))


print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

dt=datetime.datetime(2020,10,20)
print((dt.month))
print((dt.year))
print((dt.day))
print((dt.hour))
print((dt.minute))
print((dt.second))

print(dt.today())
print((dt.min))
print((dt.max))

tt=datetime.time(6,10,55,192121)
t2=datetime.time(23,59,59)
print(tt.hour)
print(tt.minute)
print(tt.second)
print(tt.max)
print(tt.min)
print(tt)
print(t2)



cal=calendar.HTMLCalendar()
print(cal.formatmonth(2022,4))
