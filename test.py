from threading import*
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(4):
        print(f'Good Morning:{name}')
        time.sleep(2)
    l.release()

t1=Thread(target=wish,args=('Dhoni',))
t2=Thread(target=wish,args=('Virat',))
t1.start()
t2.start()

        