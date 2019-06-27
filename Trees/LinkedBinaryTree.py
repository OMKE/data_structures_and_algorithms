from BinaryTree import BinaryTree
from Node import Node
from Position import Position

class LinkedBinaryTree(BinaryTree):

    def __init__(self):
        self.root_node = None
        self.size = 0


    """
    ** validate **
    desc:
        private
        returns node from position if position is valid
    params:
        p - position, 
    return: Node - node
    """
    def _validate(self, p):
        if not isinstance(p, Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p doesn't belong to this container")
        if p.node.parent is p.node:
            raise TypeError("p is no longer valid")
        return p.node

    def _make_position(self, node):
        return Position(self, node) if node is not None else None


    def __len__(self):
        return self.size
    

    def get_root(self):
        return self._make_position(self.root_node)

    def get_parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def get_left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)
    
    def get_right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def add_root(self, e):
        if self.root_node is not None:
            raise ValueError("Root node already exists")
        
        self.size = 1
        self.root_node = Node(e)
        return self._make_position(self.root_node)

    def add_left(self, p, e):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError("Left child already exists")
        
        self.size += 1
        node.left = Node(e)
        return self._make_position(node.left)
    

    def add_right(self, p, e):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError("Right child already exists")
        self.size += 1
        node.right = Node(e)
        return self._make_position(node.right)
    

    def replace(self, p, e):
        node = self._validate(p)
        old = node.element
        node.element = e
        return old
        
    


    
    def delete(self, p):

        node = self._validate(p)
        if self.num_children(node) == 2:
            raise ValueError("p has two childs")
        
        child = node.left if node.left else node.right
        if child is not None:
            child.parent = node.parent
        if node is self.root_node:
            self.root_node = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self.size -= 1
        node.parent = node
        return node.element

    def attach(self, p, t1, t2):

        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("Position p must be a leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")

        self.size += len(t1) + len(t2)
        if not t1.is_empty():
            t1.root_node.parent = node
            node.left = t1.root_node
            t1.root_node = None
            t1.size = 0
        if not t2.is_empty():
            t2.root_node.parent = node
            node.right = t2.root_node
            t2.root_node = None
            t2.size = 0
        

    
            