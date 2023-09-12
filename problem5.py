'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
'''
def findN():
    result = 0
    found = False
    #can't really articulate why the maths works, but it does in my head.
    divisors = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

    while not found:
        #increment value
        result+=1
        
        #for all divisors in list
        for num in divisors:
            #if current number can be evenly divided, then continue to check others
            found = (result%num == 0)
            
            #if not, then stop and start cycle again
            if(not found):
                break

            #if none fail the check, then loop ends and the return result
    
    return result

if __name__ == "__main__":
    whichPrime = 10001
    print(f"The smallest positive number evenly divisible by numbers 1 to 20 is {findN()}")