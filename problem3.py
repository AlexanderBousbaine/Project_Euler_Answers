'''
The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600,851,475,143
'''

def findLargestPrimeFactorOf(n):
    #control variables
    largestFactor = 0
    currentFactor = 2
    dividend = n
    primes = [currentFactor]

    while dividend > largestFactor:
        #if the dividend can be divided without remainder by the current prime factor
        if(dividend%currentFactor==0):
            
            #if the current factor is a prime number that hasn't been tried yet, then add it to the list
            if(not primes.__contains__(currentFactor)):
                primes.append(currentFactor)

            #change largest factor if necessary
            largestFactor = currentFactor if currentFactor > largestFactor else largestFactor

            #perform division
            dividend /= currentFactor

        else:
            #if current prime number cannot smoothly divide the dividend,
            # find a new prime number.
            findNewPrime = True
            while findNewPrime:
                currentFactor+=1
                
                #avoid even numbers as they (apart from 2) cannot be prime
                if(currentFactor%2==0):
                    currentFactor+=1

                #check if new potential prime can be divided by any previously discovered prime numbers
                for prime in primes:
                    findNewPrime = False
                    if(currentFactor%prime == 0):
                        #if yes to above, then discard and try again
                        findNewPrime = True
                        break

    return largestFactor

if __name__ == "__main__":
    target = 600851475143
    print(f"The largest prime factor of {target} is {findLargestPrimeFactorOf(target)}")