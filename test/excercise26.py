#PF-Exer-26

def factorial(number):
    if(number<2):
        return 1
    return number*(factorial(number-1))
        
     #remove pass and write your logic to find and return the factorial of given number


def find_strong_numbers(num_list): 
    new_list =[] 
  
    for x in num_list: 
        temp = x 
        sum = 0
        while(temp): 
            rem = temp % 10
            sum += factorial(rem) 
            temp = temp // 10
        if(sum == x): 
            new_list.append(x) 
        else: 
            pass  
              
    return new_list 

   
#     for list in num_list:
#         sum=0
#         temp = list
#         check=list
#         while(list>=1):
#             value= list%10
#             sum+=factorial(value)
#             list=list//10
#         if(sum==list):
#             print(list)
#         else:
#             pass
#         
#     #return list
#             
            
#         for list2 in num_list:
#             if(list2==sum):
#                 print (list2)
#             break
                
        
    
            
     #remove pass and write your logic to find and return the list of strong numbers from the given list


num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
