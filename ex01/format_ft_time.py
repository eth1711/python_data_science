import datetime 
import time

x = "Seconds since January 1, 1970: {:,.4f} or {:.2e}"
time = time.time()
txt = datetime.datetime.now()

print(x.format(time, time))

print(txt.strftime("%b %d %Y"))
