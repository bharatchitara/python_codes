    #PF-Assgn-41
def find_ten_substring(num_str):
    #print(num_str[0]+num_str[1])
    lis=[]
    for i in range(0,len(num_str)-1):
        if((int)(num_str[i])+(int)(num_str[i+1])==10):
            #print (num_str[i]+num_str[i+1])
            x=(num_str[i]+num_str[i+1])
            lis.append(x)
    
    for i in range(0,len(num_str)-2):
        if((int)(num_str[i])+(int)(num_str[i+1])+(int)(num_str[i+2])==10):
            #print(num_str[i]+num_str[i+1]+num_str[i+2])
            y=(num_str[i]+num_str[i+1]+num_str[i+2])
            lis.append(y)
        
            
    for i in range(0,len(num_str)-3):      
        if( (int)(num_str[i]) + (int)(num_str[i+1]) + (int)(num_str[i+2]) + (int)(num_str[i+3])==10):
            #print(num_str[i]+num_str[i+1]+num_str[i+2]+num_str[i+3])
            z=(num_str[i]+num_str[i+1]+num_str[i+2]+num_str[i+3])
            lis.append(z)
    

            
    for i in range(0,len(num_str)-4):      
        if( (int)(num_str[i]) + (int)(num_str[i+1]) + (int)(num_str[i+2]) + (int)(num_str[i+3]) + (int)(num_str[i+4]) ==10):
            #print((int)(num_str[i]) + (int)(num_str[i+1]) + (int)(num_str[i+2]) + (int)(num_str[i+3]) + (int)(num_str[i+4]))
            k=(num_str[i]+num_str[i+1]+num_str[i+2]+num_str[i+3]+num_str[i+4])
            lis.append(k)
    
    print(lis)

            
num_str='2825302'
print("The number is:",num_str)

result_str=find_ten_substring(num_str)
