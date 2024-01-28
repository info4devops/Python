class Book:
  
  def __init__(self,author,pages,price):
    self.author=author
    self.pages=pages
    self.price=price
  def __add__(self,other):
    total_pages=self.pages+other.pages
    desc='These books are Written by {} and {}'.format(self.author,other.author)
    print('These books Containe:{}'.format(total_pages))
    print(desc)
    print('The Total Cost of Books:{}'.format(self.price+other.price))
    return

b1=Book('Virat',100,111)
b2=Book('Rohit',200,222)
b1+b2
