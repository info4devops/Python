def decor_for_wish(func):
  def inner(name):
    if name == 'Sunny':
      print('Hello Sunny Bad morning')
    else:
      func(name)
  return inner
    
@ decor_for_wish
def wish(name):
  print('Hello',name,'Good Morning')

wish('Virat')
wish('Sunny')
