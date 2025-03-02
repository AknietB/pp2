from datetime import datetime, timedelta
now_date=datetime.now()
yesterday=now_date-timedelta(days=1)
tomorrow=now_date+timedelta(days=1)
print(yesterday)
print(now_date)
print(tomorrow)