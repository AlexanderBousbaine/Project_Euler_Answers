'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2

For example, a=3, b=4, c=5. 

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
'''
def findProductOfTipletAddingTo(n):
    #c cannot be less than n/3 as then one cannot have a+b+c=n while also having a < b < c .
    cStart = int(n/3)

    #iterate through available range.
    for c in range(cStart, n):
        #b cannot be larger than c, so only ever iterate up to the value of c.
        for b in range(2, c):
            #a cannot be larger than b, so only ever iterate up to the value of b.
            for a in range(1, b):
                if((a**2)+(b**2) == c**2 and a+b+c == n):
                    return a*b*c


    #if you haven't found the right number by now, then you won't
    return -1

if __name__ == "__main__":
    target = 1000
    print(f"The largest product of 13 adjacent digits in the given number is {findProductOfTipletAddingTo(1000)}")