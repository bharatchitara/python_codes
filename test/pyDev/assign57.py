#PF-Assgn-57
def check_prime(number):
    temp =2  #remove pass and write your logic here. if the number is prime return true, else return false
    while(temp>1 and temp <number):
        if(number%temp==0):
            return False
            
        else:
            temp+=1
    return True

def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
    #Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    lst=[]
    count= len(str(num))
    #print(count)
    powTen = pow(10, count - 1) 
    lst.append(num)
    for i in range(count-1): 
          
        firstDigit = num // powTen 
        
        left = (num * 10 + firstDigit - 
               (firstDigit * powTen * 10)) 
        lst.append(left)  
        # Update the original number 
        num = left 
    
    return lst

def get_circular_prime_count(limit):
     #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    li=[]
    flag=flag1=0
    
    for i in range(2,limit):
        x= rotations(i)
        #if(rotations(i) is not None):
        for j in x:
            
            if(check_prime(j)):
                
                
            
            else:
                break
    
    list(set(li))
    li.sort()
                        
    return list(set(li))
            
#Provide different values for limit and test your program
print(get_circular_prime_count(100))