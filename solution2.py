import itertools

def fib():
    a = 0
    b = 1
    while True:
        n = a + b
        yield n
        a = b
        b = n

print(sum([x for x in itertools.takewhile(lambda x: x <= 4000000, fib()) if x % 2 == 0]))
        
        
        
        
