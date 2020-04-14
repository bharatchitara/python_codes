#PF-Assgn-44

def find_duplicates(list_of_numbers):
    x=0
    list1=[]
    #list2=[]
    for i in range(0,len(list_of_numbers)):
        for j in range(i+1,len(list_of_numbers)):
            if(list_of_numbers[i]==list_of_numbers[j]):
                list1.append(list_of_numbers[i])
                
    list1= list(set(list1))
    return list1
    

    
    
    #start writing your code here

list_of_numbers=[12,54,68,759,24,15,12,68,987,758,25,69]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)