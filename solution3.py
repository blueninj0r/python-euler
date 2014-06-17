import math
import itertools

def naiveprimes():
    primes = [2]
    yield 2
    curr = 3
    while True:
        for p in primes:
            if curr % p == 0:
                break
        else:
            primes.append(curr)
            yield curr
        curr+=1
        print(primes)

def primefactors(n):
    primes = []
    while n % 2 == 0:
        primes += [2]
        n /= 2

    if n == 1:
        return primes

    p = 3

    while p * p <= n:
        if n % p == 0:
            primes += [p]
            n /= p
        else:
            p += 2
            
    return primes + [n]

print(max(primefactors(600851475143)))
