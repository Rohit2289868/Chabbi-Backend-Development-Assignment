from datetime import datetime, timedelta

def f(from_date, to_date, diff):
    from_date = datetime.strptime(from_date, "%y-%m-%d")
    to_date = datetime.strptime(to_date, "%y-%m-%d")
    
    difference = abs(to_date - from_date)
    
    if difference < timedelta(days = diff):
        return True
    else:
        return False

from_date = input("Enter From Date = ")
to_date = input("Enter To Date = ")
diff = int(input("Enter difference = "))

print(f(from_date, to_date, diff))