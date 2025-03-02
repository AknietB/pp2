import math
import time
def sqrtt(number,ms):
    time.sleep(ms/1000)
    res=math.sqrt(number)
    print(f"Square root of {number} after {ms} milliseconds is {res}")
num=int(input())
ms=int(input())
sqrtt(num,ms)