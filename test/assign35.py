#PF-Assgn-35

#Global variable

def find_more_than_average():
  #  sort_marks()
    list(list_of_marks)
    
    x=len(list_of_marks)
    
    addition = sum(list_of_marks)
    #print(addition)
    average = addition//x
    
    flag=0
    for list2 in list_of_marks:
        if(average<list2):
            flag+=1
    
    percentage= (flag/x)*100
    return (percentage)
    #Remove pass and write your logic here

def sort_marks():
    
    return sorted(list(list_of_marks))
    #Remove pass and write your logic here
 
def generate_frequency():
    
    list(list_of_marks)
    l=[]
    for value in range(0,26):
        l.append(list_of_marks.count(value))
    return l            
    
list_of_marks = (12,18,25,24,2,5,18,20,20,21)
list_of_marks = list(list_of_marks)
    
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())