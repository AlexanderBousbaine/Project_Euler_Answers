"""
The sum of the primes below 10 is 2+3+5+7 = 17.

Find the sum of all the primes below two million.
"""
from datetime import datetime

def isPrime(n: int, l: list):

    for prime in l:
        if(n%prime==0):
            return False

    return True

def sumOfPrimesBelow(n):
    primes = [2]

    for i in range(3, n, 2):
        if(isPrime(i, primes)):
            primes.append(i)

    return sum(primes)

if __name__ == "__main__":
    #very slow solution - takes > 10 minutes to find answer
    upperLimit = 2000000
    print(datetime.now())
    print(f"Sum of primes below {upperLimit} is {sumOfPrimesBelow(upperLimit)}")
    print(datetime.now())
    