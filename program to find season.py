month = input("Input the month (e.g. January, February etc.): ")
day = int(input("Input the day: "))

if month in ('January', 'February', 'March'):
	season = 'fall'
elif month in ('April', 'May', 'June'):
	season = 'summer'
elif month in ('July', 'August', 'September'):
	season = 'spring'
else:
	season = 'winter'

if (month == 'March') and (day > 19):
	season = 'summer'
elif (month == 'June') and (day > 20):
	season = 'spring'
elif (month == 'September') and (day > 21):
	season = 'fall'
elif (month == 'December') and (day > 20):
	season = 'winter'

print("Season is",season)
