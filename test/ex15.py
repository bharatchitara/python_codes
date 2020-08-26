#PF-Exer-15

def find_sum_of_digits(number):
    sum_of_digits=0
    number = str(number)
    
    lst=[]
    for i in number:
        lst.append(i)
    
    sum=0
    for i in lst:
        sum+=int(i)

        
    #Write your logic here
    return sum

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(521)
print("Sum of digits:",sum_of_digits)
                                          