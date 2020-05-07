#PF-Assgn-61
def validate_name(name):
    #Start writing your code here
    if(name is not None and len(name)<=15 and name.isalpha()):
        return True
    return False
    
def validate_phone_no(phno):
    #Start writing your code here
    lst=[]
    if(len(phno)==10):
        if(phno.isdigit()):
            for i in phno:
                lst.append(i)
            
                if(len(set(lst))!=1):
                    return True            
    return False

def validate_email_id(email_id):
    #Start writing your code here
    lst=[]
    if("@" in email_id):
        #if(".com" in email_id):
            
        if("@gmail" in email_id or "@yahoo" in email_id or "@hotmail" in email_id):
            for i in email_id:
                lst.append(i)
                x= "".join(lst[-4:])
                #print(x)
                if(x==".com"):
                    return True
    return False
        
        
        
def validate_all(name,phone_no,email_id):
    #Start writing your code here
    # Use the below given print statements to display appropriate messages
    # Also, do not modify them for verification to work
    if(validate_name(name) and validate_email_id(email_id) and validate_phone_no(phone_no)):
        return True
    else:
        if(validate_name(name)==False):
            print("Invalid Name")
        elif(validate_phone_no(phone_no)==False):
            print("Invalid phone number")
        elif(validate_email_id(email_id)==False):
            print("Invalid email id")
        else:
            print("All the details are valid")
            
            
    #print("Invalid phone number")
    #print("Invalid email id")
    #print("All the details are valid")


#Provide different values for name, phone_no and email_id and test your program
print(validate_all("Harry", "9988776655", "harry@gmail.com"))



