#PF-Assgn-59
def check_perfect_number(number):
    #start writing your code here
    temp=2
    lst=[1]
    while(temp<number):
        if(number%temp==0):
            
            lst.append(temp)
        temp+=1
        
    #print(lst)
    if(number==sum(lst)):
        return True
    else:
        return False    
    
    
def check_perfectno_from_list(no_list):
    list=[]
    for i in no_list:
        if(check_perfect_number(i)):
           list.append(i) 
   
    return list

perfectno_list=check_perfectno_from_list([18, 6, 4, 2, 1, 28, 496])
print(perfectno_list)