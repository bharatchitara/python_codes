#PF-Assgn-32
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    count_p=0
    count_e=0
    count_o=0
    for list in patient_medical_speciality_list:
        #print(list)
        if list=='P':
            count_p+=1
        elif list=='E':
            count_e+=1
        elif list=='O':
            count_o+=1
        
            
        
    if(count_p>count_e and count_p >count_o):
        return "Pediatrics"
    elif(count_e>count_p and count_e>count_o):
        return "ENT"
    else:
        return "Orthopedics"
    #return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'E',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)