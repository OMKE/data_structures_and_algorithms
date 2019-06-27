
"""
** Tree **
desc:
    Abstract tree class that class like binary tree should inherit
"""
class Tree:
    def get_root(self):
        raise NotImplementedError("Must be implemented by a subclass")

    
    def get_parent(self, p):
        raise NotImplementedError("Must be implemented by a subclass")

    
    def num_children(self, p):
        raise NotImplementedError("Must be implemented by a subclass")
    

    """
    ** children **
    desc:
        generates iteration of positions which represents children of positon p
    return: generator - iterations of children positions 
    """
    def children(self, p):
        raise NotImplementedError("Must be implemented by a subclass")


    """
    ** __len__ **
    desc:
        redefines method len
    return: int - returns container size
    """
    def __len__(self):
        raise NotImplementedError("Must be implemented by a subclass")

    """
    ** is_root **
    desc:
        checks if node on position p is root node
        
    return: bool - true if it is, else false
    """
    def is_root(self, p):
        return self.get_root() == p

    
    """
    ** is_leaf **
    desc:
        checks if node on position p is a leaf node
    return: bool - true if it is, else false
    """
    def is_leaf(self, p):
        return self.num_children(p) == 0


    def is_empty(self):
        return len(self) == 0


    
    """
    ** positions **
    desc:
        generates iterations of all positions in tree, it needs one of traversals (inorder/preorder/postorder)
    return: generator - iterations of positions in the tree
    """
    def positions(self):
        raise NotImplementedError("Must be implemented by a subclass")

    
    """
    ** __iter__ **
    desc:
        generates iterations of all elements in the tree
    """
    def __iter__(self):
        for p in self.positions():
            yield p.get_element()
    


    """
    ** depth **
    desc:
        returns a depth of position p in a relation of root node
    return: int - postion depth
    """
    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.get_parent(p))

    
    """
    ** height_r **
    desc:
        calculates height of subtree recursively whose root node is on position p
    return: int - height of passed subtree
    """
    def height_r(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height_r(c) for c in self.children(p))

    def height(self, p = None):
        if p is None:
            p = self.get_root()
        return self.height_r(p)