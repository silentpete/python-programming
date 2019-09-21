# import the datetime function from the datetime library
from datetime import datetime, timedelta

# import the timedelta function from the datetime library
from datetime import timedelta

print('get the current time')
current_date = datetime.now()

print('print the current time')
print(current_date)

print('create a one day length delta object')
one_day = timedelta(days=1)
print(one_day)
print('subtract 1 day from the currect time')
yesterday = current_date - one_day
print('print one day agos date')
print(yesterday)

print('day '+ str(yesterday.day))
print('month ' + str(yesterday.month))
print('year ' + str(yesterday.year))

birthdate = input("what is your birthdate (yyyy/mm/dd): ")
birthdate_date = datetime.strptime(birthdate, '%Y/%m/%d')
print(birthdate_date - one_day)
