from threading import*
def display():
    for i in range(1,4):
        print('Child Class')

t=Thread(target=display)
t.start()
for i in range(1,4):
    print('Main Class')
    