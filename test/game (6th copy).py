# #example of getter method & encapsulation. 
# 
# class Account: 
#     def __init__(self,account_no,balance): 
#         self.__account_no = account_no 
#         self.__balance = balance 
#     def get_account# #example of getter method & encapsulation. 
# 
# class Account: 
#     def __init__(self,account_no,balance): 
#         self.__account_no = account_no 
#         self.__balance = balance 
#     def get_account_no(self): 
#         return self.__account_no 
#     def get_balance(self): 
#         return self.__balance 
# 
# account1 = Account(1034846,120000) 
# print(account1.get_account_no())
# print(account1.get_balance())_no(self): 
#         return self.__account_no 
#     def get_balance(self): 
#         return self.__balance 
# 
# account1 = Account(1034846,120000) 
# print(account1.get_account_no())
# print(account1.get_balance())


#PF-Assgn-42
def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    
    #Accepts the list of factors and returns the largest prime factor

def find_f(num):
    # Python3 code to find largest prime 
# factor of number 
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


# This code is contributed by "Sharad_Bhardwaj". 
#Accepts the number and returns the largest prime factor of the number

def find_g(num):
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number

#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))