"""# rejalashtirish
import sched
import time
from datetime import datetime

scheduler = sched.scheduler(time.time, time.sleep)

def schedule_event(name, start):
   now = time.time()
   elapsed = int(now - start)
   print('elapsed=',elapsed, 'name=', name)

start = time.time()
print('START:', time.ctime(start))
scheduler.enter(4, 1, schedule_event, ('EVENT_1', start))
scheduler.enter(10, 1, schedule_event, ('EVENT_2', start))

scheduler.run()
print("end:",datetime.now())
"""

import socket
server = socket.socket()
server.bind(('localhost',12345))
server.listen()
client, addr = server.accept()
print ("connection request from: " + str(addr))