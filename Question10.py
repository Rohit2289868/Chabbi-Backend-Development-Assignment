from datetime import datetime, timedelta

def f(date, n):
    date = datetime.strptime(date, "%y-%m-%d")
    new_date = date - timedelta(days=n)
    
    return new_date

date = input("Date = ")
n = int(input("n = "))

print(f(date, n))