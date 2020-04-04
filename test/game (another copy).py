#PF-Exer-32

def human_pyramid(no_of_people):
    
    if(no_of_people==1):
        weight+=1*50
        return weight
    else:
        weight = no_of_people*50 + human_pyramid(no_of_people-2)
    return weight    
        #remove pass and place the recursive code the you had written earlier for this function

def find_maximum_people(max_weight):
    
    value= human_pyramid(max_weight//50)
    print(value)
    if(weight>max_weight):
        people=weight//50
    return people
    
        
    #write your logic here. You may invoke recursive function human_pyramid() wherever applicable 
    
#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)