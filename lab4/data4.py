from datetime import datetime
date1='2025-01-10 13:43:15'
date2='2025-02-03 19:15:56'
date1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
diff=date2-date1
second=diff.total_seconds()
print(second)