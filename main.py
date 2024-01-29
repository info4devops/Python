import datetime
today = datetime.datetime.now()
s=str(today)
print(s)
#print(d)

s=repr(today)
print(s)
d=eval(s)
print(d)