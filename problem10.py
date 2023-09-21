"""
The sum of the primes below 10 is 2+3+5+7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt

def isPrime(n: int):

    if(n==2):
        return True

    limit = int(sqrt(n))+1

    for i in range(3, limit, 2):
        if(n%i==0):
            return False

    return True

def sumOfPrimesBelow(n):
    primes = [2]

    for i in range(3, n, 2):
        if(isPrime(i)):
            primes.append(i)

    return sum(primes)

if __name__ == "__main__":
    #Not as slow anymore
    upperLimit = 2000000
    print(f"Sum of primes below {upperLimit} is {sumOfPrimesBelow(upperLimit)}")
    