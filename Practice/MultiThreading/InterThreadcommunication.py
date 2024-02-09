from threading import*
import time
def producer():
  time.sleep(10)
  print('P:Producing Items')
  print('P:Gave Notification')
  e.set()
def consumer():
  print('C:Waiting for update')
  print('C:Got Notification from P')
  e.wait()

e=Event()
t1=Thread(target=producer)
t2=Thread(target=consumer)
t1.start()
t2.start()