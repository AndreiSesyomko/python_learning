
import datetime

def date_in_future(integer):
    current_datetime = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    if not isinstance(integer, int): return current_datetime
    delta = datetime.datetime.strptime(current_datetime, '%d-%m-%Y %H:%M:%S')
    result = delta + datetime.timedelta(days=integer)
    result = result.strftime('%d-%m-%Y %H:%M:%S')
    return result

print(date_in_future([]))
print(date_in_future(2))