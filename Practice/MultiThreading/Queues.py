# Inter Thread communication using Queues
# FIFO,LIFO and Priority queues

import queue
q=queue.Queue() #FIFO
q.put(11)
q.put(5)
q.put(22)
print('::::::::::FIFO::::::::')
while not q.empty():
  print(q.get(),end=' ')

#LIFO
import queue
q=queue.LifoQueue() #LIFO
q.put(11)
q.put(5)
q.put(22)
print('\n::::::::::LIFO::::::::')
while not q.empty():
  print(q.get(),end=' ')
  
# Priority Queue
#LIFO
import queue
q=queue.PriorityQueue() #priority queue
q.put(11)
q.put(5)
q.put(22)
print('\n::::::::::LIFO::::::::')
while not q.empty():
  print(q.get(),end=' ')