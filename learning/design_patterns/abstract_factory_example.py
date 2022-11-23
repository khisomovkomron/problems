from abc import ABC, abstractmethod

"""
Abstract FactoryA(ABC)
Product1 FactoryA(Abstract FactoryA)
Product2 FactoryA(Abstract FactoryA)
Product3 FactoryA(Abstract FactoryA)
FactoryA

Abstract FactoryB(ABC)
Product1 FactoryB(Abstract FactoryB)
Product2 FactoryB(Abstract FactoryB)
Product3 FactoryB(Abstract FactoryB)
FactoryB

Abstract GeneralFactory
GeneralFactory
    Call: FactoryA
    Call: FactoryB
"""


class IChair(ABC):
    
    @staticmethod
    @abstractmethod
    def get_dimensions():
        """A statis interface method"""
        
        
class SmallChair(IChair):
    
    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40
        
    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
    

class MediumChair(IChair):
    
    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60
        
    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }
    

class BigChair(IChair):
    
    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80
    
    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }


class ChairFactory:
    
    @staticmethod
    def get_chair(chair):
        try:
            if chair == 'BigChair':
                return BigChair()
            if chair == 'MediumChair':
                return MediumChair()
            if chair == 'SmallChair':
                return SmallChair()
            raise Exception('Chair not found')
        except Exception as _e:
            print(_e)
        return None
##########################################################

class ITable(ABC):
    
    @staticmethod
    @abstractmethod
    def get_dimensions():
        """A static interface method"""
        

class SmallTable(ITable):
    
    def __init__(self):
        self._width = 60
        self._height = 80
        self._depth = 120
        
    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class MediumTable(ITable):
    
    def __init__(self):
        self._width = 70
        self._height = 80
        self._depth = 110
    
    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class BigTable(ITable):
    
    def __init__(self):
        self._width = 70
        self._height = 80
        self._depth = 120
    
    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class TableFactory:
    @staticmethod
    def get_table(table):
        try:
            if table == 'BigTable':
                return BigTable()
            if table == 'MediumTable':
                return MediumTable()
            if table == 'SmallTable':
                return SmallTable()
            raise Exception('Table not found')
        except Exception as _e:
            print(_e)
        return None
##########################################################


class IHandler(ABC):
    
    @staticmethod
    def get_dimensions():
        """A static Interface method"""
        

class SmallHandler(IHandler):
    
    def __init__(self):
        self._depth = 10
        self._height = 10
        self._width = 10
        
    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }


class MediumHandler(IHandler):
    
    def __init__(self):
        self._depth = 20
        self._height = 20
        self._width = 20
    
    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }


class BigHandler(IHandler):
    
    def __init__(self):
        self._depth = 30
        self._height = 30
        self._width = 30
    
    def get_dimensions(self):
        return {
            'width': self._width,
            'depth': self._depth,
            'height': self._height
        }


class HandlerFactory:
    
    @staticmethod
    def get_handler(handler):
        try:
            if handler == 'BigHandler':
                return BigHandler()
            if handler == 'MediumHandler':
                return MediumHandler()
            if handler == 'SmallHandler':
                return SmallHandler()
            raise Exception('Handler not found')
        except Exception as _e:
            print(_e)
        return None
##########################################################


class IFurnitureFactory(ABC):
    
    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        """The statis Abstract Factory interface method"""
    
    
class FurnitureFactory(IFurnitureFactory):
    
    @staticmethod
    def get_furniture(furniture):
        try:
            if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
                return ChairFactory.get_chair(furniture)
            if furniture in ['SmallTable', 'MediumTable', 'BigTable']:
                return TableFactory.get_table(furniture)
            if furniture in ['SmallHandler', 'MediumHandler', 'BigHandler']:
                return HandlerFactory.get_handler(furniture)
            raise Exception('No Factory Found')
        except Exception as _e:
            print(_e)
        return None


if __name__ == '__main__':
    
    FURNITURE = FurnitureFactory.get_furniture('SmallChair')
    print(f'{FURNITURE.__class__}: {FURNITURE.get_dimensions()}')
    FURNITURE = FurnitureFactory.get_furniture('BigTable')
    print(f'{FURNITURE.__class__}: {FURNITURE.get_dimensions()}')
    FURNITURE = FurnitureFactory.get_furniture('MediumHandler')
    print(f'{FURNITURE.__class__}: {FURNITURE.get_dimensions()}')
