from LinkedBinaryTree import LinkedBinaryTree
from queue_dll.queue import QueueDLL
from stack_dll.stack import StackDLL


class BinarySearchTree(LinkedBinaryTree):
    def __init__(self):
        super().__init__()
    
    def __iter__(self):
        for p in self.positions():
            yield p.get_element()

    
    def insert_element(self, e):
        if self.get_root() is None:
            self.add_root(e)
        else:
            self.insert_node(self.get_root(), e)

    
    def insert_node(self, root_p, value):
        if value <= root_p.get_element():
            if root_p.node.left:
                self.insert_node(self.get_left(root_p), value)
            else:
                self.add_left(root_p, value)
        elif value > root_p.get_element():
            if root_p.node.right:
                self.insert_node(self.get_right(root_p), value)
            else:
                self.add_right(root_p, value)


    

    def inorder(self):
        if not self.is_empty():
            for other in self._subtree_inorder(self.get_root()):
                yield other

    def _subtree_inorder(self, p):

        if self.get_left(p) is not None:
            for other in self._subtree_inorder(self.get_left(p)):
                yield other
        if self.get_right(p) is not None:
            for other in self._subtree_inorder(self.get_right(p)):
                yield other

    
    def preorder(self):
        if not self.is_empty():
            for other in self._subtree_preorder(self.get_root()):
                yield other

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    
    def postorder(self):
        if not self.is_empty():
            for other in self._subtree_postorder(self.get_root()):
                yield other
    

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p
    
    def positions(self):
        # return self.inorder()
        return self.preorder()
        # return self.postorder()


    def breadth_first(self):

        if not self.is_empty():
            wrapper = QueueDLL()
            wrapper.enqueue(self.get_root())
            while not wrapper.is_empty():
                p = wrapper.dequeue()
                yield p
                for c in self.children(p):
                    wrapper.enqueue(c)

    
    def depth_first(self):
        if not self.is_empty():
            stack = StackDLL()
            stack.push(self.get_root())
            while not stack.is_empty():
                p = stack.pop()
                yield p
                for c in self.children(p):
                    stack.push(c)


    def binary_search(self, e, p):
        if p is None:
            return None
        
        if e == p.get_element():
            return p

        if e < p.get_element():
            return self.binary_search(e, self.get_left(p))
        
        else:
            return self.binary_search(e, self.get_right(p))




    
    
        

                