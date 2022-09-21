
def reversed_integer(n):

    reversed_integer = 0
    remainder = 0
    
    while n > 0:
        remainder = n % 10
        reversed_integer = 10*reversed_integer + remainder
        n = n//10
        
    return reversed_integer




if __name__ == "__main__":
    
    n = 1234
    print(reversed_integer(n))