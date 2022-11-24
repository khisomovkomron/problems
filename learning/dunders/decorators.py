class Decorators:
    
    def __init__(self, new, old, other):
        self.__new = new  # private instance of attribute value
        self.__old = old
        self.__other = other
    
    # property decorators add new method to Class,
    # you can call class new method by Class().new
    @property
    def new(self):
        return self.__new
    
    # setter is used when value of method instance is changed to new value
    @new.setter
    def new(self, value):
        self.__new = value
    
    @property
    def old(self):
        return self.__old
    
    @old.setter
    def old(self, value):
        self.__old = value
    
    @property
    def others(self):
        return self.__other
    
    # deleter deletes created method from a class
    @others.deleter
    def others(self):
        print('Deleting')
        del self.__other


# decorators = Decorators('new', 'old', 'others')
# print(decorators.old)
# print(decorators.new)
# print(decorators.others)
#
# decorators.old = "OLD1"
# decorators.new = "NEW1"
# print(decorators.old)
# print(decorators.new)
#
# del decorators.others
# print(decorators.others)


class Student:
    name = 'John'
    
    def __init__(self, age):
        self.age = age
    
    # It can access class attributes, but not the instance attributes.
    @classmethod
    def new_classmethod(cls):
        print(f'Get new_classmethod and class attribute {cls.name}')
        # f'but cannot access instance attributes age: {cls.age} ')


student = Student('20')
student.new_classmethod()
