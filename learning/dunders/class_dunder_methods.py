class Dunders:
    
    # def __new__(cls, *args, **kwargs):
    #     pass
    
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        """the __str__ function is supposed to return a human-readable format,
        which is good for logging or to display some information about the object"""
        return print(f"Name: {self.name}")
        
    def __repr__(self):
        """ the __repr__ function returns an “official” string representation of the object"""
        return print(f'Dunders(name={self.name})')
    
    
# d = Dunders(name='Dunders')
# d.__str__()
# d.__repr__()


class Person:
    
    def __new__(cls, name):
        print(f'Creating a new {cls.__name__} object ...')
        obj = object.__new__(cls)
        return obj
    
    def __init__(self, name):
        print(f'Initializing the person object ...')
        self.name = name
        

# person = Person(name='John')
# print(person)

# person = object.__new__(Person, 'Komron')
# print(person.__dict__)
# person.__init__('John')
# print(person.__dict__)
# print(person)

class Person1:
    """use the __new__() method when you want to tweak the object at the instantiated time"""
    def __new__(cls, first_name, lastname):
        # create a new object
        obj = super().__new__(cls)
        
        # initialize attributes
        obj.first_name = first_name
        obj.last_name = lastname
        
        # inject new attribute
        obj.full_name = f'{first_name} {lastname}'
        return obj
    
person = Person1('Joe', 'Doe')
print(person.full_name)
print(person.__dict__)

# The __new__() is a static method of the object class.

# When you create a new object by calling the class,
# Python calls the __new__() method to create the
# object first and then calls the __init__() method
# to initialize the object’s attributes.

# Override the __new__() method if you want to tweak the
# object at creation time.