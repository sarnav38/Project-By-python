import random
import datetime

ran = random.randint(0,5)
print(ran)

strtime = datetime.datetime.now().strftime('%H:%M:%S')
print(strtime)

tm = datetime.datetime.now()
print(tm)

dt = strtime = datetime.datetime.now().strftime('%d:%m:%Y')
print(dt)