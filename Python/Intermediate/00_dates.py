 #DATES
 
from datetime import datetime
now = datetime.now() 
timestamp = now.timestamp() #Es como un ID del tiempo (fecha) en el que algo se ha generado
print(timestamp)

def print_date(date):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    
print (print_date(now))

year_2023 = datetime(2023, 1 , 1, )
print_date(year_2023)

from datetime import time
current_time = time(21, 6, 8)
print_date(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date
current_date = date.today()
print_date(current_date)
print(current_date.day)
print(current_date.year)
print(current_date.month)
current_date = date(current_date.year, current_date.month + 1, current_date.day)
diff = year_2023 - now
print(diff)

from datetime import timedelta
start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 113)
print(end_timedelta + start_timedelta)
print(end_timedelta - start_timedelta)
print(end_timedelta * start_timedelta) #No se puede
print(end_timedelta / start_timedelta) #No se puede