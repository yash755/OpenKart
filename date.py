from datetime import date
from datetime import timedelta

today = date.today()
# Month abbreviation, day and year

print (today)

yesterday = today - timedelta(days = 1)

print (yesterday)

print (yesterday.strftime("%y-%m-%d"))
