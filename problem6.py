'''
The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
def findSquareSumDifferenceUpto(n):
    #get sum of range from 1 to 100 and square it.
    squareOfSum = sum(range(1, n+1))**2
    #square each number from 1 to 100, then get the sum of that list.
    sumOfSquares = sum([i*i for i in range(1, n+1)])

    return squareOfSum - sumOfSquares

if __name__ == "__main__":
    upperLimit = 100
    print(f"The difference between the square of the sum and the sum of sqaures for all numbers below {upperLimit} is {findSquareSumDifferenceUpto(upperLimit)}")