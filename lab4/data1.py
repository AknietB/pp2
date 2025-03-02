from datetime import datetime, timedelta
curr_date=datetime.now()
five_date=curr_date-timedelta(days=5)
print(five_date)