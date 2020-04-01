#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    flag=0
    count=0
    for index in range(0,len(match_tuple)):
        
        if(match_tuple[index]=='Team1'):
            flag+=1
        else:
            count+=1
            
    if(flag>count):
        return ("Team1")
    elif(count==flag):
        return ("Tie")
    else:
        return ("Team2")
            
            
    
    #Remove pass and write the logic here
    

#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team1"))
#print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
