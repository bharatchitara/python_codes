#PF-Assgn-33

def find_common_characters(msg1,msg2):
    
    x= "".join(msg1.split())
    #print(x)
    #msg1=list(x)
    x= list(x)
    #print(x)
    y= "".join(msg2.split())
    #print(y)
    y=list(y)
    #print(y)
    #msg2=list(y)
    lst=[]
    flag=0
    str=""
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            if(x[i]==y[j]):
                if(x[i] in lst):
                    break
                else:
                    lst.append(x[i])
                    flag=1
    
    if(flag==0):
        return -1 
    
    for element in lst:
        str+= element
    return (str)
    
#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)