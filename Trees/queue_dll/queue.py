from .doubly_linked_list.doubly_linked_list import DoublyLinkedList
from .empty_exception import Empty


class QueueDLL:
    def __init__(self):
        self._data = DoublyLinkedList()

    def __len__(self):
        return len(self._data)

    def first(self):
        """
        Vraca element koji se nalazi na pocetku reda.
        :return: element sa pocetka reda
        """
        if self.is_empty():
            raise Empty("Queue is empty, first element is unaccessible.")
        return self._data.first()

    def is_empty(self):
        return self._data.is_empty()

    def enqueue(self, e):
        """
        Dodaje element na kraj strukture
        :param e: element koji dodajemo
        :return:
        """
        self._data.add_last(e)

    def dequeue(self):
        """
        Uklanja element sa pocetka reda
        :return: element sa pocetka strukture
        """
        if self.is_empty():
            raise Empty("Queue is empty, element can not be removed.")
        return self._data.delete_node(self._data.first_node())
