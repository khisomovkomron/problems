"""By creating a class and following the Singleton pattern,
you can enforce that even if any number of instances were
created, they will still refer to the original class.

The Singleton can be accessible globally, but it is not a
global variable. It is a class that can be instanced at any
time, but after it is first instanced, any new instances
will point to the same instance as the first.

For a class to behave as a Singleton, it should not contain
any references to self but use static variables, static
methods and/or class methods."""

from abc import ABC, abstractmethod

"""Variables declared at class level are static variables
that can be accessed directly using the class name without
the class needing to be instantiated first.

cls is a reference to the class

self is a reference to the instance of the class

_new_ gets called before _init_,

_new_ has access to class level variables

_init_ references self that is created when the class is instantiated

By using _new_, and returning a reference to cls, we can force the class
to act as a singleton. For a class to act as a singleton, it should not
contain any references to self."""


class IGame(ABC):
    
    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        """Must implement add_winner"""
        

class Leaderboard:
    _table = {}
    
    @classmethod
    def print(cls):
        """A class level method"""
        print('___________LEADERBOARD___________')
        for key, value in sorted(cls._table.items()):
            print(f'|\t{key}\t|\t{value}\t|')
    
    @classmethod
    def add_winner(cls, position, name):
        cls._table[position] = name


class Game1(IGame):
    
    def __init__(self):
        self.leaderboard = Leaderboard()
        
    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)
        
        
class Game2(IGame):
    """Game2 implements IGame"""

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)
        

class Game3(Game2):
    """Game 3 Inherits from Game 2 instead of implementing IGame"""


if __name__ == '__main__':
    
    Game1 = Game1()
    Game1.add_winner(2, 'Cosmo')

    Game2 = Game2()
    Game2.add_winner(3, 'Sean')
    #
    Game3 = Game3()
    Game3.add_winner(1, 'Emmy')
    
    # Game1.leaderboard.print()
    # Game2.leaderboard.print()
    Game3.leaderboard.print()