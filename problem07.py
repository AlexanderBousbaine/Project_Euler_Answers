'''
By listing the first six prime numbers, we can see the 6th prime is 13.

What is the 10,001st prime number?
'''
def findPrime(n):
    #'1' is not considered prime in this question.
    primes = [2]
    #Start on 3, as all even numbers, excepting 2, aren't prime
    prospectivePrime = 3
    numPrimesFound = 1

    #Carry on going until the number of primes found is correct
    while numPrimesFound != n:
        
        #Theory is that all numbers, except primes, have prime factors other than themselves, 
        # so to check for prime numbers, check for prime factors.
        foundPrime = True

        #check if new potential prime can be divided by any previously discovered prime numbers
        for prime in primes:
            if(prospectivePrime%prime == 0):
                #if yes to above, then discard and try again
                foundPrime = False
                break
            
        #if prime cannot be divided by any previously found primes
        if(foundPrime):
            #it must be prime, so add to list and cycle around again
            primes.append(prospectivePrime)
            numPrimesFound+=1

        #Increment by 2 each time to avoid even numbers - halves search space.
        prospectivePrime+=2

    return primes[len(primes)-1]

if __name__ == "__main__":
    whichPrime = 10001
    print(f"The {whichPrime}th prime number is {findPrime(whichPrime)}")