#PF-Assgn-35

#Global variable

def find_more_than_average(list_of_marks):
  #  sort_marks()
    sum=0
    x=len(list_of_marks)
    sum=sum(list_of_marks)
    average = sum//x
    
    flag=0
    for list2 in list_of_marks:
        if(average>list2):
            flag+=1
    
    percentage= (flag/x)*100
    print(percentage)
    #Remove pass and write your logic here

def sort_marks():
    list_of_marks.sort()
    #Remove pass and write your logic here
 
def generate_frequency():
    find_more_than_average(list_of_marks)
    #Remove pass and write your logic here
    
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

#print(find_more_than_average(list_of_marks))
 
print(generate_frequency())
#print(sort_marks())