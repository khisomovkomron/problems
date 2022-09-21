def majorityElement(nums: list[int]) -> int:

    d = {}
    
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    
    return max(d.keys(), key=d.get)
    
    
print(majorityElement(nums=[2,2,1,1,1,2,2]))


"""________________________________________ZIP_____________________________________"""


"""
The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
The zip() function returns an iterator of tuples based on the iterable objects.

- If we do not pass any parameter, zip() returns an empty iterator
- If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
- If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.

Suppose, two iterables are passed to zip(); one iterable containing three and other containing five elements.
Then, the returned iterator will contain three tuples. It's because the iterator stops when the shortest iterable is exhausted.
"""
numbers = [1,2,3,4,5]
words = ['one', 'two', 'three', 'four', 'five']

result = list(zip(numbers, words))
print(result)

"""________________________________________MAP_____________________________________"""
"""
map() function returns a map object(which is an iterator) of the results after applying the given function to each
item of a given iterable (list, tuple etc.)
"""
# map(iterator, objects)
# map should be wrapped into list to return its value print(list(map))

result = map(lambda x, y: x**2+y**2, numbers, reversed(numbers))
print(list(result))
