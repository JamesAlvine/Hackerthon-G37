import datetime
import time

# Gets todays date and stores it in date:
date = datetime.datetime.today().now().strftime("%Y, %b, %d")

# Getting today's name in short form:
day = datetime.date.today().strftime("%a")

weekdays = {"Mon": 0, "Tue": 1, "Wed": 2, "Thur": 3, "Fri": 4, "Sat": 5, "Sun": 6}
# Checking the today's fare:

if weekdays[day] in range(0, 5):
    fare = 100

elif day == 5:
    fare = 60

else:
    fare = 80

# Prints out today's information:
print("Date: ", date)
print("Day: ", day)
print("Fare: ", fare)