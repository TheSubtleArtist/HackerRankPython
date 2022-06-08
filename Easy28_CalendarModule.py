"""
The calendar module allows you to output calendars and provides additional useful functions for them.
class calendar.TextCalendar([firstweekday])
This class can be used to generate plain text calendars.

Task
You are given a date(in MM DD YYYY format). Your task is to find what the day is on that date.
"""
import calendar
"""
# My Code, not quite right
weekdays = {
	6:'Sunday',
	0:'Monday',
	1:'Tuesday',
	2:'Wednesday',
	3:'Thursday',
	4:'Friday',
	5:'Saturday'
}

m, d, y = input('in').split()

td = calendar.weekday(int(y), int(m), int(d))
for key, value in weekdays.items():
	if key == td:
		print(value.upper())

The output of this code is "inWEDNESDAY" in the hackerRank compiler, but have not idea why
"""

# Better Code

m, d, y = map(int,input().split())
print((calendar.day_name[calendar.weekday(y,m,d)]).upper())
