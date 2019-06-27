from .doubly_linked_list.doubly_linked_list import DoublyLinkedList
from .empty_exception import Empty


class StackDLL:
    def __init__(self):
        self._data = DoublyLinkedList()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data.is_empty()

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._data.last()

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty!")
        elem = self.top()
        self._data.delete_node(self._data.last_node())
        return elem

    def push(self, e):
        self._data.add_last(e)
