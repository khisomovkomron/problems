from functools import wraps, partial
from typing import Callable


def lower(function):
    @wraps(function)
    def wrapper(arg1):
        func = function(arg1)
        if func:
            return "Valuable style"
        else:
            return False
    
    return wrapper


@lower
def new_style(style: str) -> bool:
    if style == "new":
        return True
    elif style == "old":
        return False


def uppercase_decorator(func):
    @wraps(func)
    def wrapper():
        return func().upper()
    
    return wrapper


@uppercase_decorator
def say_hi():
    'This is say hi'
    return 'hello'


def apply_func(a: int, b: int, func: Callable[[int, int], int]) -> int:
    return int(round((func(a, b))))


def divide(a: int, b: int) -> int:
    return round(a / b)


# Partial functions allow us to fix a certain number of arguments of a function and generate a new function.
g = partial(divide, b=3)


# passing arguments to decorator
def decorator_with_Args(decorator_arg1, decorator_arg2, decorator_arg3):
    def weather_decorator(function):
        @wraps(function)
        def wrapper(arg1, arg2, arg3):
            'This is wrapper function'
            print(f'this is new Weather in {decorator_arg2} at the height {decorator_arg3} is {decorator_arg1}')
            print(f'this is new Weather in {arg2} at the height {arg3} is {arg1}')
            
            return function(arg1, arg2, arg3)
            
        return wrapper
    return weather_decorator


temp = 28
@decorator_with_Args(34, 'Moscow', 899)
def getting_weather(temp, location: str = 'Dushanbe', height: int = 819) -> str:
    
    return f'Weather in {location} at the height {height} is {temp}'


if __name__ == '__main__':
    # print(new_style('new'))
    # print(new_style('old'))
    
    # print(say_hi())
    # print(say_hi.__name__)
    # print(say_hi.__doc__)
    #
    # # print(apply_func(3, 6, divide))
    # print(g(a=6))
    
    print(getting_weather(32, 'Tashkent', 1234))
