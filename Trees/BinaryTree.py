from Tree import Tree

class BinaryTree(Tree):
    
    def get_left(self, p):
        raise NotImplementedError("Must be implemented by a subclass")

    def get_right(self, p):
        raise NotImplementedError("Must be implemented by a subclass")

    def sibling(self, p):

        parent = p.get_parent(p)
        if parent is None:
            return None
        else:
            if p == self.get_left(parent):
                return self.get_right(parent)
            else:
                return self.get_left(parent)

    

    """
    ** children **
    desc:
        generates iterations which represents children of positon p
    params:
        p - position (Position), 
    return: generator - object
    """
    def children(self, p):
        left = self.get_left(p)
        if left is not None:
            yield left
        right = self.get_right(p)
        if right is not None:
            yield right


