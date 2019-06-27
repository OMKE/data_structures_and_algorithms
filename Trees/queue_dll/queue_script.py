from queue import QueueDLL
from empty_exception import Empty


q = QueueDLL()
try:
    q.first()
except Empty as e:
    print(e)  # prints exception

q.enqueue(10)  
q.enqueue(12)  
q.enqueue(13)  

print(q.first())  
print(q.dequeue())  
print(q.first())  
