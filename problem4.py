'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two -digit numbers is:
    9009 = 91 x 99 

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def checkPalindrome(p):
    #Turn number into string
    word = str(p)
    
    #Strings are lists, so iterate forwards and backwards simultaneously through the list, 
    # checking the front and back letter against each other.
    length = len(word)-1
    for i in range(0, length):
        #If ever they don't match, the number is not palindromic.
        if(word[i] != word[length-i]):
            return False
        
        #If ever the two iterating points cross, then there is no point in checking further,
        # the number must be palindromic
        if(i >= length - i):
            return True

def findLargestPalindrome():
    largestPalindrome = 0
    palindrome = 0

    #Iterate through each variable.
    #Iteration stops at a minimum of 100, as the question specifies that 
    # the two numbers that produce the palindrome must be 3-digits.
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            palindrome = i * j
            
            if(checkPalindrome(palindrome)):
                if(palindrome > largestPalindrome):
                    largestPalindrome = palindrome


    return largestPalindrome

if __name__ == "__main__":
    print(f"The largest palindrome made from the product of two 3-digit numbers is {findLargestPalindrome()}")