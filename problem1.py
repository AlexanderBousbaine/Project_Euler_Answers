"""
Project Euler Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sumOfFactorsBelow(n):
    
    sum = 0
    
    #limit iterations for efficiency - probably a better way to do this
    maxI = int(round(n/2.5))
    
    #for all integers in up to the given maximum
    for i in range(0, maxI):
        
        #add multiple of 3 to the sum if they are less than the maximum 
        #  and the multiple of 5 is not also a multiple of 3.
        sum += (i*3 if i*3 < n else 0) + (i*5 if (i*5 < n and (i*5)%3 != 0) else 0)
    
    return sum

if __name__ == "__main__":
    upperLimit = 1000
    print(f"Sum of multiples of 3 and 5 below {upperLimit} is {sumOfFactorsBelow(upperLimit)}")
