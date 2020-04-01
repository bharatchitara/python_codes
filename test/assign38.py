#PF-Assgn-38
#remaining
def check_double(number):
#     value=number*2
#     
#     number=(str)(number)
#     
#     for singles in number:
#         print singles
#     
#     for i in range(0,len(number)):
#         if(singles[i] in value):
#             return True
#         else:
#             return False
#         
    value =number*2
    value=(str)(value)
    number=(str)(number)
    
    for singles in value:
        li = list(singles.split(","))
        print(li)
    
    
    listToStr = ''.join(map(str, singles))
    
    if(number==singles):
        return True
    else:
        return False
    
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(125874))