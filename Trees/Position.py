
from APosition import APosition


class Position(APosition):


    """
    ** constructor **
    desc:
        initializes position object
    params:
        container - linked binary tree, 
        node - node which this position contains
    """
    def __init__(self, container, node):
        self.container = container
        self.node = node

    
    def get_element(self):
        return self.node.element
    
    def __eq__(self, other):
        return type(other) is type(self) and other.node is self.node

    