#PF-Assgn-37

#Global variables
child_id=(11,12,13,14,15)
chocolates_received=[22,33,44,55,66]

def calculate_total_chocolates():
    sum=0
    for i in chocolates_received:
        sum+=i
    return sum
    #Remove pass and write your logic here to find and return the total number of chocolates

def reward_child(child_id_rewarded,extra_chocolates):
    sum2=0
    
    sum3=0
    if child_id_rewarded not in child_id:
        print("Child id is invalid")
        
#         chocolates_received.append(extra_chocolates)
#         
#         print( calculate_total_chocolates())
#     
    else:
        value= child_id.index(child_id_rewarded)
        #print(value)
        temp=0
        
        chocolates_received[value]+=extra_chocolates
        
        print (chocolates_received)
        
        
        
    if extra_chocolates<1:
        print("Extra chocolates is less than 1")
        
    
    
        
    #Remove pass and write your logic here


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(11,2)