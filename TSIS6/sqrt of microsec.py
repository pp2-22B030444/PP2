import time
import math
def sqrt(str,ms):
    print(time.time())
    time.sleep(ms/1000)
    print(f'Square root of {str} after {ms}  miliseconds is {math.sqrt(str)}')
    #print(time.time())

str=int(input("Write number:"))
ms=int(input("Write microsec:"))
sqrt(str,ms)   