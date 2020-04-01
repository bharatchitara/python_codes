#PF-Assgn-26

def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0

    if(heads!=0 and legs==2*heads):
        rabbit_count=heads
        chicken_count=0
        print(chicken_count,rabbit_count)
    elif(2*heads==legs//2):
        rabbit_count =0
        chicken_count=heads
        print(chicken_count,rabbit_count)
    
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count = (legs//2) - heads
        chicken_count = heads - rabbit_count
    print(chicken_count,rabbit_count)
        
        
    #Start writing your code here
    #Populate the variables: chicken_count and rabbit_count
    '''if(heads!=0):
        rabbit_count=heads
        chicken_count = (legs-(heads*2))//2
    '''


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print(chicken_count,rabbit_count)
    #print(error_msg)

#Provide different values for heads and legs and test your program
solve(10,20)
