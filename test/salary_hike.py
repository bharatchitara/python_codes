#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    if (job_level==3):
        new_salary= (current_salary*115)/100
    elif(job_level==4):
        new_salary= (current_salary*107)/100
    elif(job_level==5):
        new_salary= (current_salary*105)/100
    else:
        new_salary =current_salary
        
        
    return new_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(10000,5)
print(new_salary)