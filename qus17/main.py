import datetime
def count_saturday(year):
    start_date= datetime.date(year,1,1)
    num_days=(datetime.date(year + 1, 1, 1)- start_date).days
    num_saturdays= sum(1 for i in range(num_days) if (start_date + datetime.timedelta(i)).weekday()==5)
    return num_saturdays
num_satruday=count_saturday(2021)
print(num_satruday)