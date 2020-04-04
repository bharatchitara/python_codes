#PF-Tryout
def find_armstrong(number):
    temp=0
    x=number
    while(number>=1):
        remainder=number%10
        temp+=(remainder*remainder*remainder)
        number=number//10
        
    if(x==temp):
        return True
    return False

number=371
if(find_armstrong(number)):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")