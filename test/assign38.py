#PF-Assgn-38

def check_double(number):
    number_list=[]
    temp=number
    while(temp>0):
        rem = temp%10
        number_list.append(rem)
        temp=temp//10
    
    number_list.sort()
    
    value=number*2
    x=value
    lst=[]
    while(x>0):
        rem = x%10
        lst.append(rem)
        x=x//10
    
    lst.sort()
    
    if(number*2==value and lst==number_list):
        return True
    else:
        return False
        
    
    
#Provide different values for number and test your program
print(check_double(124874))