
"""
** APosition **
desc:
    Abstract Position class
"""
class APosition:


    
    def get_element(self):
        raise NotImplementedError("Must be implemented by a subclass")
    
    
    def __eq__(self, other):
        raise NotImplementedError("Must be implemented by a subclass")

    
    
    def __ne__(self, other):
        return not self == other