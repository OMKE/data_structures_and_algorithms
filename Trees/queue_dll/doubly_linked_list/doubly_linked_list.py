from .node import Node
from .empty_exception import Empty


class DoublyLinkedList:
    def __init__(self):
        self._header = Node(None, None, None) 
        self._trailer = Node(None, None, None) 
        self._header._next = self._trailer  
        self._trailer._prev = self._header  
        self._size = 0 

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first_node(self):
        if self.is_empty():  
            raise Empty("Lista is empty, it doesnt have first node!")
        return self._header._next

    def last_node(self):
        if self.is_empty():
            raise Empty("List is empty, it doesn't have last node!")
        return self._trailer._prev

    def first(self):
        try:
            return self.first_node()._element
        except Empty as e:
            print(e)

    def last(self):
        try:
            return self.last_node()._element
        except Empty as e:
            print(e)

    def add_first(self, e):
        new_node = Node(e, self._header, self._header._next) 
        self._header._next._prev = new_node  
        self._header._next = new_node  
        self._size += 1  

    def add_last(self, e):
        new_node = Node(e, self._trailer._prev, self._trailer)  
        self._trailer._prev._next = new_node  
        self._trailer._prev = new_node 
        self._size += 1

    def insert_between(self, e, predecessor, successor):
        newest = Node(e, predecessor, successor)  
        predecessor._next = newest  
        successor._prev = newest
        self._size += 1  
        return newest  

    def delete_node(self, node):
        if self.is_empty(): 
            raise Empty("It's impossible to remove an element. List is empty!")
        predecessor = node._prev 
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1 
        element = node._element 
        node._prev = node._next = node._element = None  
        return element 
