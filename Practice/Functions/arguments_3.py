def f1(arg1,arg2,arg3=4,arg4=8):
  print(arg1,arg2,arg3,arg4)

#f1() #TypeError: f1() missing 2 required positional arguments: 'arg1' and 'arg2'
f1(10,20)
f1(10,20,30,40)
#f1(10,20,arg3=30,40) # SyntaxError: positional argument follows keyword argument
f1(10,20,300,arg4=400)


