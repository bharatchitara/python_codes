# Python3 code to find largest prime 
# factor of number 
import math 

# A function to find largest prime factor 
def maxPrimeFactors (n): 
    maxPrime = -1
    
    while n % 2 == 0: 
        maxPrime = 2
        n >>= 1     # equivalent to n /= 2 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        while n % i == 0: 
            maxPrime = i 
            n = n / i 
    if n > 2: 
        maxPrime = n 
    
    return int(maxPrime) 

# Driver code to test above function 
n = 15
print(maxPrimeFactors(n)) 
