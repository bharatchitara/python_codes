#PF-Assgn-58
#from wheel.signatures.djbec import double
def validate_credit_card_number(card_number):
    #start writing your code here
    count = len(str(card_number))
    #print(count)
    lst=[]
    
    sum_lst=[]
    double_lst=[]
    even_lst = []
    if(count==16):
        card_number = str(card_number)
        for i in range(16):
            lst.append(card_number[i])
        
        lst.reverse()
        even_lst=lst
    
        for i in range(16):
            if(i%2!=0):
                sum_lst.append(lst[i])
            
        for i in sum_lst:
            double_lst.append(int(i)*2)
        #print(double_lst)
        temp=0
        while(temp<2):
            
            for i in double_lst:
            
                if(i>9):
                    rem = int(i)%10
                    last = int(i)//10
                    add = rem+last
                
                    double_lst.append(add)
                    double_lst.remove(i)
            
            temp+=1         
        #print(double_lst)
        
        
        s = sum(double_lst)
        addition=0
        for i in range(len(even_lst)):
            if(i%2==0):
                addition += int(even_lst[i])
        #print(addition)
        
        tem= s+addition
        
        if(tem%10==0):
            result = True
        else:
            result = False
    
    
    
    return result
    
    

card_number= 4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")