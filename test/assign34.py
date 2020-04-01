#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    flag=0
    num_list.sort()
    print(num_list)
    
    for i in range(0,len(num_list)):   
        for j in range(0,len(num_list)):     
            if(num_list[i]+ num_list[j]==n):
                flag+=1
                
    flag=flag//2
    return flag
    
  

num_list=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
print(find_pairs_of_numbers(num_list,n))