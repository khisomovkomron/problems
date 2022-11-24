class Dunders:
    
    # def __new__(cls, *args, **kwargs):
    #     pass
    
    def __init__(self, name):
        self.name = name
        
    # def __str__(self):
    #     """the __str__ function is supposed to return a human-readable format,
    #     which is good for logging or to display some information about the object"""
    #     return print(f"Name: {self.name}")
        
    def __repr__(self):
        """ the __repr__ function returns an “official” string representation of the object"""
        return print(f'Dunders(name={self.name})')
    
    
d = Dunders(name='Dunders')
d.__str__()
d.__repr__()
