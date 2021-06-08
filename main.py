
import pytz,datetime

year=int(input("Enter year: "))
month=int(input("Enter month: "))
day=int(input("Enter day"))
hour=int(input("Enter hour: "))
minuite=int(input("Enter minuite:"))

#convert into a date
users_time=datetime.datetime(year,month,day,hour,minuite)
cairo_timezone=pytz.timezone('Africa/Cairo')
cairo_time=pytz.utc.localize(users_time).astimezone(cairo_timezone)
kenya_timezone=pytz.timezone('Africa/Nairobi')
kenya_time=pytz.utc.localize(users_time).astimezone(kenya_timezone)
print("kenya time is",kenya_time.isoformat())
print("Cairos time is",cairo_time.isoformat())
print("london time is",users_time.isoformat())