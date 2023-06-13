# Playground for testing *args and **kwargs

def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    
    return n

print(calculate(2, add=3, multiply=5))