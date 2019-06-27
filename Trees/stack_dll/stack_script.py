from stack import StackDLL as Stack
from empty_exception import Empty


s = Stack()

for i in reversed(range(10)):
    s.push(i)

for i in range(len(s)):
    try:
        print(s.pop(), end=" ")
    except Empty as e:
        print(e)
print()
try:
    print(s.pop())
except Empty as e:
    print(e)  
